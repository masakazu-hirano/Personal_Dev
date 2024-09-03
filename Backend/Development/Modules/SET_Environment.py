import dotenv

def Read_Environment_File() -> bool:
	return dotenv.load_dotenv(
		dotenv_path = './.env',
		encoding = 'utf-8',
		override = True,
		verbose = True
	)