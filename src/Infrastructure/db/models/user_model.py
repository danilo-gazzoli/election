from src.infrastructure.db.base import Base;
from sqlalchemy import Column, Integer, String, Boolean;

class UserModel(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True);
    google_id = Column(String(45));
    name = Column(String(60), nullable=True);
    email = Column(String(255), nullable=True);
    password = Column(String(60), nullable=True);
    is_logged = Column(Boolean, nullable=True);
    
    def __init__(self, google_id=None, name=None, email=None, password=None, is_logged=None):
        self.google_id = google_id;
        self.name = name;
        self.email = email;
        self.password = password;
        self.is_logged = is_logged;
