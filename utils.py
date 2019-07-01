import requests
import os
from bs4 import Comment, BeautifulSoup as BS

base_url = "http://www.pythonchallenge.com/pc/def/"
base_data_dir_path = './data/'


def get_status_and_html_content(url: str):
    resp = requests.get(url)
    status_code = resp.status_code
    html_content = resp.content
    searchable_text = html_content.decode('utf-8')
    return status_code, searchable_text


def grab_html_comments(html_content: str):
    document = BS(html_content, 'html.parser')
    comments = document.find_all(string=lambda text: isinstance(text, Comment))
    return comments


def download_file(file_url: str, write_path_w_ext: str):
    dir_name = os.path.dirname(write_path_w_ext)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    with open(write_path_w_ext, 'wb') as file_writer:
        resp = requests.get(file_url)
        file_writer.write(resp.content)
