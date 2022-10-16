import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ID=os.getenv('ID')

admins = [
  ID
]