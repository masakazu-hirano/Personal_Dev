import logging
import os

from datetime import datetime
from PIL import Image

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.INFO,
		format = '[{levelname}]: {message}',
		style = '{'
	)

	directory_name: str = './Development/Before_Edit_Picture'
	for in_directory_file in os.listdir(path = directory_name):
		if os.path.isfile(path = f"{directory_name}/{in_directory_file}"):
			with Image.open(
				fp = f"{directory_name}/{in_directory_file}",
				mode = 'r',
				formats = ('BMP', 'GIF', 'JPEG', 'PNG', 'WEBP')
			) as image_file:
				photography_datetime: datetime = datetime.strptime(image_file.getexif().get(key = 306), '%Y:%m:%d %H:%M:%S')
				maker: str = image_file.getexif().get(key = 271)
				model_name: str = image_file.getexif().get(key = 272)

				logging.info(msg = f"{datetime.strftime(photography_datetime, '%Y-%m-%d %H:%M:%S')}_{maker}_{model_name}")

		break
	logging.info(msg = '処理が正常に終了しました。')