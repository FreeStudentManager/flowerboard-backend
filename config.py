import os

import dotenv

dotenv.load_dotenv()

SECRET_KEY = os.environ['SECRET_KEY']
DATABASE_URL = os.environ['DATABASE_URL']
DEBUG = bool(os.environ.get('DEBUG', 'False'))
