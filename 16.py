# http://www.pythonchallenge.com/pc/return/mozart.html
from pathlib import Path
import utils

script_data_dir = Path.joinpath(utils.base_data_dir_path, '16/')
gif_download_path = Path.joinpath(script_data_dir, 'mozart.gif')

gif_url = 'http://www.pythonchallenge.com/pc/return/mozart.gif'

utils.download_file(gif_url, gif_download_path)
