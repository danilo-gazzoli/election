from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from src.config import settings;

engine = create_engine(settings.DB_CONNECTION);

local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine);

def get_db_session():
    session = local_session();
    
    try:
        yield session;
    finally:
        session.close();
