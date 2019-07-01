
# Problem 1
key_dict = {
    'k': 'm',
    'o': 'q',
    'e': 'g',
}

url = "http://www.pythonchallenge.com/pc/def/map.html"
cipher = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""


def subtract(a: str, b: str):
    return ord(a) - ord(b)


[print(f'ord of {tmp} is {ord(tmp)}') for tmp in 'az']

[print(f'diff of {k} and {v} is {subtract(k, v)}')
 for k, v in key_dict.items()]


def shift_alpha(txt: str) -> str:
    if txt in [' ', ',', '"', ",", '.', '(', ')', '/', ':']:
        return txt
    tmp = chr(ord(txt) + 2)
    if ord(tmp) < ord('z'):
        return tmp
    return chr(ord(tmp) - 26)


new_str = ''.join([*map(shift_alpha, cipher)])
decrypted_url = ''.join([*map(shift_alpha, url)])

print(f'{new_str}')
print(f'{decrypted_url}')
