import os

import dotenv

dotenv.load_dotenv()

AUTHING_USERPOOL_ID = os.environ['AUTHING_USERPOOL_ID']
AUTHING_USERPOOL_SECRET = os.environ['AUTHING_USERPOOL_SECRET']
AUTHING_APP_ID = os.environ['AUTHING_APP_ID']
AUTHING_APP_HOST = os.environ['AUTHING_APP_HOST']
DATABASE_URL = os.environ['DATABASE_URL']
DEBUG = bool(os.environ.get('DEBUG', 'False'))
