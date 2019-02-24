import os
import json
import glob
import subprocess
from subprocess import run
from multiprocessing import Pool, current_process

api_prefix = 'https://apiv2.webdamdb.com'
refresh_token = 'dbc1ec23adcc50dd55138b2dd89e73db88e1e119'
access_token = '38b03c5dd04aa51204fbceb645c56dc86936e3e4'

folder_mapping = {
    'acquia-cloud': '3814907',
    'dam': '3814908',
    'site-factory': '3814916',
    'journey': '3814912',
    'lift': '3814911',
    'content-hub': '3836128',
    'acquia-search': '3814923',
    'lightning': '3814918',
    'resource': '3814929',
    'shield': '3814919',
    'edge': '3814920',
    'dev-desktop': '3814924',
    'commerce': '3814921',
    'support': '3814927',
    'ra': '3814928',
    'release-note': '3814930',
    'product-guide': '3814922',
    'devtools': '4044003',
    'mollom': '4044013',
    'profile-mgr': '4044014',
    'exp-builder': '4044015',
    'uncategorized': '4044008'
}

DEFAULT_IMAGE_LIMIT = 100
DEFAULT_IMAGE_OFFSET = 0


def get_refresh_token():

    url = '{}/oauth2/token'.format(api_prefix)
    data = 'grant_type=refresh_token&refresh_token=c07118aba47f408a15cf57f8d63cedffee19c4ac&client_id=7a7c50690d8979d003bfc3acbd6dc08498588861&client_secret=e18148df1c234cd2f1b599a72ce48bc2150d29a5&redirect_uri=www.kleva.co.ke'

    args = [
        'curl',
        '--silent',
        '--header', 'Authorization: Bearer {}'.format(refresh_token),
        '--request', 'POST',
        '--data', data,
        '--url', url
    ]

    print('Refreshing token')
    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('Refreshed token')

        response = str(completed_process.stdout, 'utf-8')
        payload = json.loads(response)
        print(payload)

        assert 'access_token' in payload, 'access_token not found'

        return payload['access_token']
    else:
        print('Refreshing token failed')


def generate_upload(file_size, folder_id, file_name, content_type):
    url = '{}/awss3/generateupload?filesize={}&folderid={}&filename={}&contenttype={}'\
        .format(api_prefix, file_size, folder_id, file_name, content_type)

    args = [
        'curl',
        '--silent',
        '--header', 'Authorization: Bearer {}'.format(access_token),
        '--url', url
    ]

    print('{} Generating upload for image "{}"'.format(current_process().name, file_name))
    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('{} Generated upload for image "{}"'.format(current_process().name, file_name))

        response = str(completed_process.stdout, 'utf-8')
        payload = json.loads(response)

        assert ('message' not in payload), \
            '{} Access token "{}" has expired'.format(current_process().name, access_token)
        assert 'presignedUrl' in payload, \
            '{} presignedUrl not found'.format(current_process().name)
        assert 'processId' in payload, \
            '{} processId not found'.format(current_process().name)

        return [payload['presignedUrl'], payload['processId']]
    else:
        print('{} Generating upload failed for image "{}"'.format(current_process().name, file_name))


def upload_file(image_name, image_path, content_type, predesigned_url):
    args = [
        'curl',
        '--silent',
        '-H', 'Content-Type: {}'.format(content_type),
        '-T', image_path,
        predesigned_url
    ]

    print('{} Uploading image "{}"'.format(current_process().name, image_name))
    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('{} Uploaded image "{}"'.format(current_process().name, image_name))

        # No need to process response as nothing is returned
    else:
        print('{} Uploading image "{}" failed'.format(current_process().name, image_name))


def finish_upload(image_name, process_id):
    url = '{}/ws/awss3/finishupload/{}'.format(api_prefix, process_id)

    args = [
        'curl',
        '--silent',
        '--request', 'PUT',
        '--header', 'Authorization: Bearer {}'.format(access_token),
        '--url', url
    ]

    print('{} Finish uploading image "{}"...'.format(current_process().name, image_name))
    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('{} Finished uploading image "{}"'.format(current_process().name, image_name))

        response = str(completed_process.stdout, 'utf-8')
        payload = json.loads(response)

        assert ('message' not in payload), \
            '{} Access token "{}" has expired'.format(current_process().name, access_token)
        assert 'id' in payload, \
            '{} id not found'.format(current_process().name)

        return payload['id']
    else:
        print('{} Finish uploading image "{}" failed'.format(current_process().name, image_name))


def get_dam_image_url(image_name, asset_id):
    url = '{}/assets/{}'.format(api_prefix, asset_id)
    args = [
        'curl',
        '--silent',
        '--header', 'Authorization: Bearer {}'.format(access_token),
        url
    ]

    print('{} Retrieving image [Asset ID={}, Image Name={}] url...'.format(current_process().name, asset_id , image_name))
    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('{} Retrieved image [Asset ID={}, Image Name={}] url'.format(current_process().name, asset_id, image_name))

        response = str(completed_process.stdout, 'utf-8')
        payload = json.loads(response)

        assert ('message' not in payload), \
            '{} Access token "{}" has expired'.format(current_process().name, access_token)
        assert len(payload['thumbnailurls']) != 0, \
            '{} Unsupported format in image {}'.format(current_process().name, image_name)

        return payload['thumbnailurls'][5]['url']
    else:
        print('{} Retrieving image [Asset ID={}, Image Name={}] url failed'.format(current_process().name, asset_id, image_name))


def upload_images():
    image_paths = glob.glob('images/*')

    with Pool(20) as p:
        p.map(upload_image, image_paths)


def upload_image(image_path):
    image_size = os.path.getsize(image_path)
    file_name = image_path.split('/')[-1].strip()

    folder_id = file_name.split('__')[0]
    image_name = file_name.split('__')[1]
    image_format = image_name.split('.')[-1]
    content_type = 'image/{}'.format(image_format)

    try:
        predesigned_url, process_id = generate_upload(image_size, folder_id, image_name, content_type)

        upload_file(image_name, image_path, content_type, predesigned_url)

        asset_id = finish_upload(image_name, process_id)

        dam_image_url = get_dam_image_url(image_name, asset_id)

        with open('imagemapping.txt', 'a') as file:
            mapping = '{} -> {} -> {}\n'.format(asset_id, image_name, dam_image_url)
            file.write(mapping)
    except AssertionError as ae:
        print(str(ae))


def find_images():
    image_paths = glob.glob('images/*')

    for image_path in image_paths:
        os.remove(image_path)
        print('Deleted image "{}"'.format(image_path))

    print('Deleted all images in images directory')

    doc_paths = glob.glob('docs/*/*.rst')

    with Pool(20) as p:
        p.map(find_image, doc_paths)


def find_image(doc_path):
    with open(doc_path) as file:
        for line in file:
            if 'image::' in line:
                url = line.split(' ')[-1].strip()
                if not url.startswith('https://'):
                    url = 'https://kbv2-dev.acquia.com{}'.format(url)

                print('{} Found image [{}] in file {}'.format(current_process().name, url, doc_path))

                # For some reason urls that start with network are timing out
                if 'network' in url:
                    print('{} Aborting download of image [{}]'.format(current_process().name, url))
                    break

                # Check if image exists
                folder = doc_path.split('/')[1]
                folder_id = folder_mapping[folder]

                image_name = url.split('/')[-1]
                image_path = 'images/{}__{}'.format(folder_id, image_name)

                if not os.path.isfile(image_path):
                    print('{} Downloading image [{}]'.format(current_process().name, url))
                    download_image(url, folder_id)
                else:
                    print('{} Image [{}] already exists!'.format(current_process().name, image_path))


def download_image(url, folder_id):
    image_name = url.split('/')[-1]
    args = [
        'curl',
        '--silent',
        '--location',
        '--output', 'images/{}__{}'.format(folder_id, image_name),
        url
    ]

    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('{} File download succeeded'.format(current_process().name))

        # No need to process response as nothing is returned
    else:
        print('{} File download failed'.format(current_process().name))


# This method deletes all assets including in sub folders
def delete_images(folder_id='3764481', folder_name='test', offset=DEFAULT_IMAGE_OFFSET, limit=DEFAULT_IMAGE_LIMIT):
    url = '{}/folders/{}/assets?offset={}&limit={}'.format(api_prefix, folder_id, offset, limit)
    args = [
        'curl',
        '--silent',
        '--header', 'Authorization: Bearer {}'.format(access_token),
        url
    ]

    print('Listing folder "{}" images...'.format(folder_name))
    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('Listed folder "{}" images'.format(folder_name))

        response = str(completed_process.stdout, 'utf-8')
        payload = json.loads(response)

        assert ('message' not in payload), \
            '{} Access token "{}" has expired'.format(current_process().name, access_token)

        # Delete all images in folder
        if 'facets' in payload:
            images = payload['items']
            image_count = len(images)
            total_image_count = int(payload['facets']['types']['image'])

            print('Found total {} images in "{}" folder'.format(total_image_count, folder_name))
            print('Deleting {} images in "{}" folder'.format(image_count, folder_name))

            with Pool(20) as p:
                p.map(delete_asset, images)

            if total_image_count > limit:
                print('Paging "{}" folder'.format(folder_name))

                # Check if next page is the last page
                if (total_image_count - limit) < limit:
                    # Next page is the last page i.e. resize limit
                    new_limit = total_image_count - limit
                else:
                    new_limit = limit

                    delete_images(folder_id, folder_name, offset, new_limit)
        else:
            print('Folder "{}" has 0 images'.format(folder_name))

        if offset == 0:
            # Iterate through sub folders
            if 'folders' in payload:
                folders = payload['folders']
                print('Found total "{}" folders'.format(len(folders)))

                for folder in folders:
                    delete_images(folder['id'], folder['name'], DEFAULT_IMAGE_OFFSET, DEFAULT_IMAGE_LIMIT)
            else:
                print('Folder "{}" has no sub folders'.format(folder_name))
    else:
        print('Listing folder images failed')


def delete_asset(asset):
    url = '{}/assets/{}'.format(api_prefix, asset['id'])
    args = [
        'curl',
        '--silent',
        '--request', 'DELETE',
        '--header', 'Authorization: Bearer {}'.format(access_token),
        url
    ]

    print('{} Deleting asset "{}"...'.format(current_process().name, asset['name']))
    completed_process = run(args, stdout=subprocess.PIPE)

    if completed_process.returncode == 0:
        print('{} Deleting asset "{}" succeeded'.format(current_process().name, asset['name']))
    else:
        print('{} Deleting asset "{}" failed'.format(current_process().name, asset['name']))


if __name__ == '__main__':
    #access_token = get_refresh_token()
    #print('Refreshed token "{}"'.format(access_token))

    delete_images()
    find_images()
    upload_images()



