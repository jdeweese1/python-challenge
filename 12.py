# Problem 12
# http://www.pythonchallenge.com/pc/return/evil.html
# http://www.pythonchallenge.com/pc/return/evil1.jpg
# going to # http://www.pythonchallenge.com/pc/return/evil2.jpg yields not jpg - gfx
# going to # http://www.pythonchallenge.com/pc/return/evil3.jpg yields no more evils


from pathlib import Path

import utils

script_data_dir = Path.joinpath(utils.base_data_dir_path, '12')
original_gfx_download_path = Path.joinpath(script_data_dir, 'evil2.gfx')

with open(original_gfx_download_path, mode='rb') as file:
    file_bytes = bytes(file.read())
    bufs = [file_bytes[index::5] for index in [0, 1, 2, 3, 4]]

for index, val in enumerate(bufs):
    output_path = Path.joinpath(script_data_dir, f'{index}.png')
    with open(file=output_path, mode='wb') as f:
        f.write(val)

    print(f'check {output_path}')


# disproportional
