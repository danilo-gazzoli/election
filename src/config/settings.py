from dotenv import load_dotenv;
import os;

load_dotenv();

DB_CONNECTION = os.getenv('DB_CONNECTION');
DB_HOST = os.getenv('DB_HOST');
DB_PORT = os.getenv('DB_PORT');
DB_NAME = os.getenv('DB_NAME');
DB_USER = os.getenv('DB_USER');
DB_PASSWORD = os.getenv('DB_PASSWORD');

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID');
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET');
SECRET_KEY = os.getenv('SECRET_KEY');