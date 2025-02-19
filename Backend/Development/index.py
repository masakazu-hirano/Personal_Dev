import logging
import os
import shortuuid

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

				width, height = image_file.size
				aspect_ratio: float = height / width

				if width < 1920:
					new_width: int = width
				elif 1920 <= width < 2560:
					new_width: int = 1920
				elif 2560 <= width < 3840:
					new_width: int = 2560
				else:
					new_width: int = 3840

				new_height: int = int(new_width * aspect_ratio)
				resize_image: Image = image_file.resize(
					size = (new_width, new_height),
				)

				resize_image.save(
					fp = f"./Development/After_Edit_Picture/{datetime.strftime(photography_datetime, '%Y-%m-%d %H:%M:%S')}_{maker}_{model_name}_{shortuuid.uuid()}.png",
					format = 'PNG',
					compress_level = 0
				)

		break
	logging.info(msg = '処理が正常に終了しました。')