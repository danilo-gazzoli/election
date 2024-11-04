from sqlalchemy import Column, Integer, String, Boolean
from src.infrastructure.db.base import Base

class UserModel(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, index=True);
    name = Column(String, index=True);
    email = Column(String, unique=True, index=True);
    password = Column(String);
    is_logged = Column(Boolean, default=False);
