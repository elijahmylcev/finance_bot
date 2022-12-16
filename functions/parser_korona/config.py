import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

executable_path = str(os.getenv('EXECUTABLE_PATH'))
url=str(os.getenv('KORONA_URL'))