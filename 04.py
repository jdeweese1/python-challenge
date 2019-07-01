# Problem 4
# http://www.pythonchallenge.com/pc/def/linkedlist.html
# This stil errors out, but is fine, bc it prints solution
import utils
import re
from itertools import product


class DataConverter:
    def __init__(self):
        self.num_map = ('zero', 'one', 'two', 'three', 'four',
                        'five', 'six', 'seven', 'eight', 'nine')
        for index, val in enumerate(self.num_map):
            setattr(self, val, index)

        self.operation_map = {
            'divide': lambda x, y: x/y,
        }


url = "http://www.pythonchallenge.com/pc/def/linkedlist.html"
converter = DataConverter()
final_html_pattern = re.compile('[a-zA-Z]{1,11}.html')


def try_guess_next_number(html_content: str, last_matching_id):
    html_content = html_content.lower()
    match = final_html_pattern.findall(html_content)
    if len(match) > 0:
        print(match)

    tf_map = list(map(lambda num: num in html_content, converter.num_map))
    nums_in_html = [index for index,
                    value in enumerate(tf_map) if value is True]
    print(nums_in_html)

    operation_keys_in_html = list(map(
        lambda operation_key: operation_key if operation_key in html_content else False, converter.operation_map.keys()))
    print(operation_keys_in_html)
    operations_in_html = [converter.operation_map[operation_key]
                          for operation_key in operation_keys_in_html]
    print(f'{nums_in_html}, operations found: {operation_keys_in_html}')
    # for func, num in product(iter1=operations_in_html, iter2=nums_in_html, repeat=1):
    # yield func(last_matching_id, nums_in_html)
    return operations_in_html[0](last_matching_id, nums_in_html[0])


_, searchable_text = utils.get_status_and_html_content(url)
print(searchable_text)

php_url = url.replace("linkedlist.html", 'linkedlist.php')
_, php_text = utils.get_status_and_html_content(php_url)
print(php_url)

page_url = php_url
html_content = php_text
html_content = re.sub("(<!--.*?-->)", "", html_content, flags=re.DOTALL)
pattern = re.compile('g[a-zA-Z\s=]{,7}([0-9]{3,6})')

guessing_pattern = "linkedlist.php?nothing={number}"
last_matching_id = -1
past_guesses = set()

for i in range(600):
    matches = pattern.findall(html_content)
    print(f'{i}: {matches}')
    if len(matches) != 1:
        print(
            f'matches was {matches}, trying another algorithm to get intent...')
        number = try_guess_next_number(html_content, last_matching_id)
        print(number)  # fixme later
    else:
        number = int(matches[-1])
    page_url = f"{utils.base_url}{guessing_pattern.format(number=number)}"
    _, html_content = utils.get_status_and_html_content(page_url)
    last_matching_id = number
    if number in past_guesses:
        break
    past_guesses.add(number)

print(f'{utils.base_url}{guessing_pattern.format(number=number)}')
