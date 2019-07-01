
# Problem 2
# http://www.pythonchallenge.com/pc/def/ocr.html
from collections import Counter
import requests
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

html_content = requests.get(url).content
begin_comment_index = html_content.find(bytes('-->\n\n<!--', 'utf-8'))
randoms = html_content[begin_comment_index:].decode('utf-8')
c = Counter(randoms)
[print(f'{key}: {value}') for key, value in c.items()]
