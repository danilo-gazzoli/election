import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'));
sys.path.append(src_path);

from core.entities.user import User;
from core.interfaces.repositories.user_repository import IUserRepository;
from typing import Dict;
from datetime import datetime;

class AuthenticateWithGoogle:
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository;
        
    def execute(self, user_info: dict):
        email = user_info.get('email');
        
        if not email:
            raise ValueError("Email can't be finded");
        
        user = self._user_repository.GetUserbyFilter(email);
        
        if user:
            user.set_is_logget(True);
            self._user_repository.UpdateUser(user);
            return user;
        
        user = User(
            User.set_name(user_info.get('name')),
            User.set_email(email),
            User.set_is_logged(True)
        )
            
        self._user_repository.CreateUser(user);
        
        return user;
        
    @property
    def get_user_repository(self):
        return self._user_repository;