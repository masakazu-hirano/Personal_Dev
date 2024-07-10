import logging
import os

from dotenv import load_dotenv

def Read_Environment_File() -> bool:
	directory: str = f"{os.environ['HOME']}/Documents/Projects/Personal_Dev"
	return load_dotenv(
		dotenv_path = f"{directory}/Backend/Development/.env",
		encoding = 'utf-8',
		override = True,
		verbose = True
	)

if __name__ == '__main__':
	logging.basicConfig(
		level = logging.INFO,
		format = '[{levelname}]: {message}',
		style = '{'
	)

	if Read_Environment_File() == True:
		logging.info(msg = '処理が正常に終了しました。')
	else:
		logging.error(msg = '環境変数（.env）ファイルの読み込みに失敗しました。')