# Problem 08
# http://www.pythonchallenge.com/pc/def/integrity.html

import bz2
import os

import utils

page_url = utils.base_url + 'integrity.html'
image_url = utils.base_url + 'integrity.jpg'
script_data_dir = os.path.join(utils.base_data_dir_path, '08/')
image_download_path = os.path.join(script_data_dir, 'integrity.jpg')
form_url = 'http://www.pythonchallenge.com/pc/return/good_data.py'

utils.download_file(image_url, image_download_path)
html_content = utils.get_html_content(page_url)

'''
parsing the html has proven to be too finicky, here are the compressed values
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->'''
compressed_un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressed_pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

uncompressed_un = bz2.decompress(compressed_un)
uncompressed_pw = bz2.decompress(compressed_pw)

print(uncompressed_un)
print(uncompressed_pw)
print(f'now go to {form_url}')
