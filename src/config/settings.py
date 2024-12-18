from dotenv import load_dotenv;
from pathlib import Path;
import os;

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

DB_CONNECTION = os.getenv('DB_CONNECTION');
DB_HOST = os.getenv('DB_HOST');
DB_PORT = os.getenv('DB_PORT');
DB_NAME = os.getenv('DB_NAME');
DB_USER = os.getenv('DB_USER');
DB_PASSWORD = os.getenv('DB_PASSWORD');

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID');
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET');
SECRET_KEY = os.getenv('SECRET_KEY');