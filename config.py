import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
URI_INFO = f'https://api.telegram.org/bot{API_TOKEN}/getFile?file_id='
URI = f'https://api.telegram.org/file/bot{API_TOKEN}/'


