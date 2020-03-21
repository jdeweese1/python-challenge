# Problem 13
# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpc.client
from pathlib import Path

import utils

xml_url = 'http://www.pythonchallenge.com/pc/phonebook.php'
script_data_dir = Path.joinpath(utils.base_data_dir_path, '13')
file_download_path = Path.joinpath(script_data_dir, 'error.xml')

conn = xmlrpc.client.ServerProxy(xml_url)
print(f'possible methods are {conn.system.listMethods()}')

print('phoning bert...')
print(conn.phone('Bert'))
# italy
