# Problem 6
# http://www.pythonchallenge.com/pc/def/channel.html

import requests
import os
import zipfile
import re
import itertools
import utils
from collections import Counter
file_url = "http://www.pythonchallenge.com/pc/def/channel.zip"
unzip_to_path = f'{utils.base_data_dir_path}06/'
zip_path = f'{unzip_to_path}/channel.zip'
resp = requests.get(file_url)

visited_ids = set()  # Set of strings
pattern = re.compile('[0-9]{2,7}')
matching_files: [str] = []


def get_id_from_file(file_path: str):
    with open(file_path, 'r') as f:
        contents = f.read()
    assert type(contents) == str
    print(f'\t{contents}')
    matches = pattern.findall(contents)
    if len(matches) == 1:
        assert matches[0] not in visited_ids
        return matches[0]
    return None



utils.download_file(file_url, zip_path)

with zipfile.ZipFile(zip_path, 'r') as zf:
    zf.extractall(unzip_to_path)

unzip_to_path_format = unzip_to_path + '{file_name}.txt'
file_name_sans_ext = 'readme'
index_iterator = itertools.count(0)
should_loop = True

while should_loop:
    matching_files.append(file_name_sans_ext + '.txt')
    file_name_sans_ext = get_id_from_file(
        unzip_to_path_format.format(file_name=file_name_sans_ext)) or ''
    should_loop = file_name_sans_ext != ''
    print(f'{next(index_iterator)} {file_name_sans_ext}')

# Collect the comments

with zipfile.ZipFile(zip_path, 'r') as zip:
    decoded_contents = []
    for file_w_path in matching_files:
        info = zip.getinfo(file_w_path)
        comment = str(info.comment.decode())
        decoded_contents.append(comment)
        print(comment)

[print(f'{key} {value}') for key, value in Counter(decoded_contents).items()]
