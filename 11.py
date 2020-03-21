# Problem 11
# http://www.pythonchallenge.com/pc/return/5808.html
import itertools
from pathlib import Path

from PIL import Image

import utils

script_data_dir = Path.joinpath(utils.base_data_dir_path, '11/')
original_image_download_path = Path.joinpath(script_data_dir, 'cave.jpg')

first_output_path = Path.joinpath(script_data_dir, 'first.png')

original_image = Image.open(original_image_download_path)
original_size = original_image.size
new_size = (original_size[0] // 2, original_size[1] // 2)

first_image = Image.new(size=new_size, mode=original_image.mode, color=0)

tf_repeater = itertools.repeat([True, False])
for y_pixel_index in range(original_size[1]):
    for x_pixel_index in range(original_size[0]):
        new_pixel_position = (x_pixel_index // 2, y_pixel_index // 2)
        original_pixel_value = original_image.getpixel(
            xy=(x_pixel_index, y_pixel_index))
        if next(tf_repeater):
            first_image.putpixel(xy=new_pixel_position,
                                 value=original_pixel_value)


first_image.save(first_output_path)

# evil

print(f'check {first_output_path}')
