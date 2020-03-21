# Problem 15
# http://www.pythonchallenge.com/pc/return/italy.html

from pathlib import Path

from PIL import Image

import utils


def pixel_border_outside_to_in(side_len=100) -> (int, int):
    '''
    Generator function that will give the next pixel dimension to place at, working in a spiral outside in.
    Assumes that the image is square.
    :param side_len: Length of the side of image.
    :return: Tuple of (x,y) that represents the next pixel
    '''
    class BorderTracker:
        def __init__(self, x: int, y: int):
            self.left_bound = 0
            self.right_bound = x
            self.top_bound = 0
            self.bottom_bound = y
    bt = BorderTracker(side_len, side_len)
    x, y = 0, 0

    # While we aren't at the center pixel
    while (bt.left_bound, bt.top_bound) != (bt.right_bound, bt.bottom_bound):
        list_to_yield = [(x_tmp, y) for x_tmp in range(x, bt.right_bound + 1)]  # traverses across top
        for item in list_to_yield:
            yield item
            x = item[0]  # Get last value of x
        bt.top_bound += 1  # Increment top bound since we have just laid another top layer on

        list_to_yield = [(x, y_tmp) for y_tmp in range(bt.top_bound, bt.bottom_bound + 1)]  # traverses across right side
        for item in list_to_yield:
            yield item
            y = item[1]  # Get last value of y
        bt.right_bound -= 1  # Decrement right bound since we have just laid another right layer on

        list_to_yield = [(x_tmp, y) for x_tmp in range(x - 1, bt.left_bound - 1, -1)]  # traverses across bottom side
        for item in list_to_yield:
            yield item
            x = item[0]  # Get last value of x
        bt.bottom_bound -= 1  # Decrement bottom bound since we have just laid another bottom layer on

        list_to_yield = [(x, y_tmp) for y_tmp in range(y - 1, bt.top_bound, -1)]  # traverses across left side
        for item in list_to_yield:
            yield item
            y = item[1] - 1  # Get last value of x
        bt.left_bound += 1  # Increment left bound since we have just laid another left layer on


script_data_dir = Path.joinpath(utils.base_data_dir_path, '14')
wire_image_path = Path.joinpath(script_data_dir, 'wire.png')
new_image_path = Path.joinpath(script_data_dir, 'out.png')
wire_im = Image.open(fp=wire_image_path, mode='r')
new_im = Image.new(color=0, size=(101, 101), mode='RGB')

s = set()

# results = [tup for tup in pixel_border_outside_to_in(99)]
# [s.add(elem) if elem not in s else print(f'{elem} already in set at {index}') for index, elem in enumerate(results)]
# rep = '\n'.join([str(item) for item in results])
# pyperclip.copy(rep)
#
# for item in itertools.product(range(0,100), range(0,100)):
#     assert (item[0], item[1]) in results, f'{(item[0], item[1])} not in results'
old_pixel_gen = (wire_im.getpixel(xy=(x_val, 0)) for x_val in range(0, wire_im.size[0]))

try:
    [new_im.putpixel(xy=coord, value=next(old_pixel_gen)) for coord in pixel_border_outside_to_in(99)]
except StopIteration:
    pass
finally:
    new_im.save(fp=new_image_path)

print(f' check {new_image_path}')
# cat
