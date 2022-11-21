import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

page = str(os.getenv('PAGE'))
user_agent = str(os.getenv('USER_AGENT'))
driver_path = str(os.getenv('DRIVER_PATH'))
