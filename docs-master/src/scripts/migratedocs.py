import re
import os
import json
import shutil
import requests

from subprocess import run
from tempfile import mkstemp
from requests.exceptions import RequestException

session_cookie = '4rbdoAmkqn5rZCA4pQot3DJsg2BVLlE2E5eplRHB1t8'

# TODO: Rename to sections
folders = [
    'acquia-cloud',
    'acquia-search',
    'api',
    'commerce',
    'content-hub',
    'dam',
    'dev-desktop',
    'devtools',
    'edge',
    'journey',
    'lift',
    'lightning',
    'ra',
    'resource',
    'shield',
    'site-factory',
    'support',
    'tutorials',
    'guide'
]

# index file - section folder mapping used by 'insert_toc'
# method to insert toc only in product index docs
index_file_names = {
    'acquia-cloud.rst': 'acquia-cloud',
    'acquia-search.rst': 'drupal-8',
    'edge.rst': 'edge',
    'shield.rst': 'shield',
    'api.rst': 'api',
    'lift.rst': 'lift',
    'journey.rst': 'journey',
    'commerce.rst': 'commerce',
    'dam.rst': 'dam',
    'dev-desktop.rst': 'dev-desktop',
    'devtools.rst': 'devtools',
    'content-hub.rst': 'content-hub',
    'lightning.rst': 'lightning',
    'site-factory.rst': 'site-factory',
    'ra.rst': 'ra',
    'resource.rst': 'resource',
    'support.rst': 'support',
    'tutorials.rst': 'tutorials'
}


def convert_content(num, id, token_title, body, doc_name, folder_path):
    rst_file_path = 'docs/{}/{}.rst'.format(folder_path, doc_name)
    html_file_path = 'docs/{}/{}.html'.format(folder_path, doc_name)

    os.makedirs(os.path.dirname(rst_file_path), exist_ok=True)
    os.makedirs(os.path.dirname(html_file_path), exist_ok=True)

    with open(html_file_path, 'w') as f:
        # Add document title
        f.write('<h1>{}</h1>\n'.format(token_title))
        # Add document body
        f.write(body)

    completed_process = run(['pandoc',
                             html_file_path,
                             '-f', 'html',
                             '-t', 'rst',
                             '-o', rst_file_path])

    if completed_process.returncode == 0:
        print('{:3}. Converted content for node id "{}"'.format(num, id))
    else:
        print('{:3}. Converting content for node id "{}" failed'.format(num, id))

    os.remove(html_file_path)
    
    modify_doc(rst_file_path)


def extract_content(num, node, aliases):
    id = node['id']
    type = node['type']

    if 'attributes' in node and node['attributes']['status']:
        token_title = node['attributes']['token_title']
        body = node['attributes']['body']['value']
        node_id = str(node['attributes']['nid'])

        if node_id in aliases:
            # Split the alias value on underscore to get product
            # i.e. key is node_id, value format is doc-name_folder_path
            doc_name = aliases[node_id].split('__')[0]
            folder_path = aliases[node_id].split('__')[1]

            if type.split('--')[1] == 'product_documentation' or type.split('--')[1] == 'product_guide':
                # The second token in 'folder_path' is the main folder
                # Check if the main folder or doc_name is in the export list
                # i.e. if not in export list, it should not be imported
                # If folder_path is empty, then doc_name is an index doc
                if doc_name in folders or (len(folder_path) and folder_path.split('/')[1] in folders):
                    convert_content(num, id, token_title, body, doc_name, folder_path)
        else:
            print('{:3}. Node id {} not found in aliases'.format(num, id))
    else:
        print('{:3}. Node id "{}" type "{}" could not be processed. Missing attributes or status property is false'.format(num, id, type))


def modify_doc(file_path):
    line_num = 0
    file_name = os.path.basename(file_path)

    fh, abs_path = mkstemp()
    with os.fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                line_num += 1

                # Insert include
                if line_num == 1:
                    new_file.write('.. include:: /common/global.rst\n\n')

                # Modify replace tokens i.e. from using square brackets to pipes
                line = re.sub(r'\[(acquia-product:[a-z]+)\]', r'|\1|', line)
                new_file.write(line)

    # Remove original file
    os.remove(file_path)
    # Move new file
    shutil.move(abs_path, file_path)


def fetch_aliases():
    # In the format node_id -> product_doc-name
    aliases = {}

    with open('aliases.txt', 'r+') as file:
        for line in file:
            # Split the line on tab char i.e. line separator
            tokens = line.split('\t')

            key = tokens[0].strip().split('/')[-1]

            doc_name = tokens[1].strip().split('/')[-1]
            folder_path = '/'.join(tokens[1].strip().split('/')[:-1])
            value = '{}__{}'.format(doc_name, folder_path)

            aliases[key] = value

    return aliases


def fetch_product_documentation():
    try:
        url = 'https://kbv2-dev.acquia.com/jsonapi/node/product_documentation'
        headers = {
            'Accept': 'application/vnd.api+json'
        }

        cookies = {
            'SSESS74e6c0f04daf8f9b7fac0eecbe819871': session_cookie,
            'path': '/',
            'domain': '.kbv2-dev.acquia.com'
        }

        num = 0
        aliases = fetch_aliases()

        while True:
            res = requests.get(url, headers=headers, cookies=cookies)
            collection = json.loads(res.text)

            if not collection['data']:
                print('Data has no body')
                return

            for node in collection['data']:
                num += 1
                extract_content(num, node, aliases)

            if 'next' in collection['links']:
                url = collection['links']['next']
            else:
                break

    except RequestException as re:
        print(re)


def fetch_product_guide():
    try:
        url = 'https://kbv2-dev.acquia.com/jsonapi/node/product_guide'
        headers = {
            'Accept': 'application/vnd.api+json'
        }

        cookies = {
            'SSESS74e6c0f04daf8f9b7fac0eecbe819871': session_cookie,
            'path': '/',
            'domain': '.kbv2-dev.acquia.com'
        }

        num = 0
        aliases = fetch_aliases()

        while True:
            res = requests.get(url, headers=headers, cookies=cookies)
            collection = json.loads(res.text)

            if not collection['data']:
                print('Data has no body')
                return

            for node in collection['data']:
                num += 1
                extract_content(num, node, aliases)

            if 'next' in collection['links']:
                url = collection['links']['next']
            else:
                break

    except RequestException as re:
        print(re)


def purge_docs():
    if os.path.exists('docs'):
        shutil.rmtree('docs')
        os.makedirs('docs')
    else:
        os.makedirs('docs')


def move_docs():
    # These products have index docs but no folders
    # Therefore, no folder operations can be done on them
    excluded_products = ['api', 'shield']

    # Delete product folders from docs
    for product in folders:
        # Except 'api' and 'shield' products i.e. because they do not exist
        if product not in excluded_products:
            shutil.rmtree('../../docs/{}'.format(product), ignore_errors=True)
            print('Deleted folder "{}" in docs folder'.format(product))

    # Delete product index docs in docs folder
    for product in folders:
        os.remove('../../docs/{}.rst'.format(product))
        print('Deleted index doc "{}.rst" in docs folder'.format(product))

    # Copy product folders to docs folder
    for folder in folders:
        # Except 'api' and 'shield' products i.e. because they do not exist
        if folder not in excluded_products:
            shutil.copytree('docs/{}'.format(folder), '../../docs/{0}'.format(folder))
            print('Copied directory "{}" to docs folder'.format(folder))

    # Copy product index docs to docs folder
    for section in folders:
        shutil.copyfile('docs/{}.rst'.format(section), '../../docs/{}.rst'.format(section))
        print('Copied index doc "{}.rst" to docs folder')


if __name__ == '__main__':
    purge_docs()
    fetch_product_guide()
    fetch_product_documentation()
    #move_docs()