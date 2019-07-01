
# Problem 3
# http://www.pythonchallenge.com/pc/def/equality.html
# One small letter surrounded by exactly 3 body guards on either side
import re
import utils
url = "http://www.pythonchallenge.com/pc/def/equality.html"
_, html_content = utils.get_status_and_html_content(url)
searchable_comment = utils.grab_html_comments(html_content)

pattern = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
matches = pattern.findall(searchable_comment)

guesses = '\n'.join([possible_match for possible_match in matches])
print(guesses)