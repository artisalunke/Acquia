import os
import shutil

from tempfile import mkstemp

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


def process_product_folders():
    for folder in folders:
        target_folder = 'docs/{}'.format(folder)
        for curr_folder, subfolders, file_names in os.walk(target_folder):
            # Strip the path from the folder path
            curr_folder_name = os.path.split(curr_folder)[1]
            for file_name in file_names:
                # Get the file name without the extension
                file_name_without_ext = os.path.splitext(file_name)[0]
                # If the file name has a corresponding folder name,
                # then it means it is an index file and should have a toc
                if file_name_without_ext in subfolders:
                    # Compose the file path
                    file_path = '{}/{}'.format(curr_folder, file_name)
                    # Create a temp file
                    fh, abs_path = mkstemp()
                    # Open temporary file
                    with os.fdopen(fh, 'w') as temp_file:
                        # Line number counter
                        line_num = 0
                        # Open the file
                        with open(file_path, 'r') as file:
                            # Iterate through the lines
                            for line in file:
                                line_num += 1
                                # Line no 5 is the line below the doc title
                                if line_num == 5:
                                    # Insert the toc
                                    temp_file.write('\n')
                                    temp_file.write('.. toctree::\n')
                                    temp_file.write('   :hidden:\n')
                                    temp_file.write('   :glob:\n\n')
                                    # Strip preceding '../../docs'
                                    # Then remove the file extension
                                    # '../../docs/acquia-cloud/ready.rst' becomes '/docs/acquia-cloud/ready'
                                    temp_file.write('   {}/*'.format(file_path[10:][:-4]))
                                    temp_file.write('\n\n')
                                else:
                                    temp_file.write(line)


                    # Remove file
                    os.remove(file_path)
                    # Move temp file
                    shutil.move(abs_path, file_path)

                    print('Inserted toc in "{}"'.format(file_path))


def process_product_indexes():
    # Index docs without corresponding product folders
    excluded_products = ['acquia-search']

    for product in folders:
        if product not in excluded_products:
            # Compose the file path
            file_path = 'docs/{}.rst'.format(product)
            # Create a temp file
            fh, abs_path = mkstemp()
            # Open temporary file
            with os.fdopen(fh, 'w') as temp_file:
                # Line number counter
                line_num = 0
                # Open the file
                with open(file_path, 'r') as file:
                    # Iterate through the lines
                    for line in file:
                        line_num += 1
                        # Line no 5 is the line below the doc title
                        if line_num == 5:
                            # Insert the toc
                            temp_file.write('\n')
                            temp_file.write('.. toctree::\n')
                            temp_file.write('   :hidden:\n')
                            temp_file.write('   :glob:\n\n')
                            temp_file.write('   /{}/*'.format(product))
                            temp_file.write('\n\n')
                        else:
                            temp_file.write(line)

            # Remove file
            os.remove(file_path)
            # Move temp file
            shutil.move(abs_path, file_path)

            print('Inserted toc in "{}"'.format(file_path))


if __name__ == '__main__':
    process_product_indexes()
    #process_product_folders()











