import re
import glob

from shutil import move
from tempfile import mkstemp
from os import fdopen, remove
from multiprocessing import Pool, current_process


def get_dam_url(image_name):
    with open('imagemapping.txt', 'r') as file:
        for line in file:
            if image_name == line.split('->')[1].strip():
                return line.split('->')[2].strip()
                break
        else:
            print('{} Could not find mapping for image "{}"'.format(current_process().name, image_name))
            return ''


def modify_directive(file_path):
    # Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                m = re.search('\A(.. [-:\|\w. ]+image:: )(/[/\w.]+/([\w-]+.\w{3}))\Z', line.strip())
                if m:
                    directive = m.group(1)
                    site_url = m.group(2)
                    image_name = m.group(3)

                    dam_url = get_dam_url(image_name)

                    new_line = '{}{}\n'.format(directive, dam_url)
                    new_file.write(new_line)

                    print('{} - Modified image path from "{}" to "{}"'
                          .format(current_process().name, site_url, dam_url))
                else:
                    new_file.write(line)

    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


if __name__ == '__main__':
    doc_paths = glob.glob('docs/*.rst') + glob.glob('docs/*/*.rst')

    with Pool(20) as p:
        p.map(modify_directive, doc_paths)
