import logging
import os

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.INFO,
		format = '[{levelname}]: {message}',
		style = '{'
	)

	directory_name: str = './Development/Before_Edit_Picture'
	for image_file in os.listdir(path = directory_name):
		if os.path.isfile(path = f"{directory_name}/{image_file}"):
			logging.info(msg = image_file)

	logging.info(msg = '処理が正常に終了しました。')