# Problem 5
# http://www.pythonchallenge.com/pc/def/peak.html
import utils
import re
from collections import Counter
import os
import pickle


def expand_row(row: [tuple]):
    return ''.join([item[0] * item[1] for item in row])


url = "http://www.pythonchallenge.com/pc/def/peak.html"
_, html_content = utils.get_status_and_html_content(url)
pattern = re.compile('peakhell src="([a-z\.]+)')
next_url = utils.base_url + pattern.findall(html_content)[0]

_, html_content = utils.get_status_and_html_content(next_url)
# print(html_content)

obj = pickle.loads(bytes(html_content, encoding='utf-8'))
[print(expand_row(item)) for item in obj]

# channel
