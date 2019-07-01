# Problem 7
# http://www.pythonchallenge.com/pc/def/oxygen.html
import utils
import os
import statistics
from PIL import Image
import re


def is_grey(pixel: tuple):
    average = statistics.mean(pixel[:2]) # get average of rgb colors, do not include alpha
    is_close = lambda x, y: y > .95 * x and y < 1.05 * x
    return all([is_close(average, channel_value) for channel_value in pixel[:3]])


image_url = utils.base_url + 'oxygen.png'
script_data_dir = utils.base_data_dir_path + '07/'
image_path = script_data_dir + 'oxygen.png'
grey_pixel_coords = []


utils.download_file(image_url, image_path)

with Image.open(image_path) as im:
    print(f'w:{im.width} h:{im.height}')

    # Begin traversing down to find grey
    for y_pixel in range(0, im.height, 5):
        coords = (0, y_pixel)
        pixel = im.getpixel(coords)
        print(f'{coords} {pixel}')

        if is_grey(pixel):
            print('found grey pixel, now traversing horizontally')
            break

    # Begin traversing across to find grey vals
    for x_pixel in range(0, im.width, 5):
        coords = (x_pixel, y_pixel)
        pixel = im.getpixel(coords)
        print(f'x:{x_pixel}, y:{y_pixel} {pixel}')
        if not is_grey(pixel):
            print('end of grey pixels horizontally, starting next step of analyzing...')
            break
        if len(grey_pixel_coords) == 0 or grey_pixel_coords[-1] != pixel: # Make sure we aren't sampling same square twice.
            grey_pixel_coords.append(pixel)

# take out of with later
message = ''.join(''.join([chr(item[0]) for item in grey_pixel_coords]))
print(message)
pattern = re.compile('[0-9]+')

matches = [int(item) for item in pattern.findall(message)]
next_puzzle = ''.join([chr(item) for item in matches])
next_puzzle = next_puzzle.replace('\n', 'n')
next_puzzle = next_puzzle.replace('\t', 't')
next_puzzle = next_puzzle.replace('\r', 'r')
print(next_puzzle)
#integrity