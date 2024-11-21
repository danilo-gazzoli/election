import sys;

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')));

from src.core.interfaces.repositories.user_repository import IUserRepository;
from src.core.entities.user import User;
from sqlalchemy.orm import Session;
from src.infrastructure.db.db_config import get_db_session;
from typing import Optional, List;
from src.infrastructure.db.models.user_model import UserModel;

class UserRepository(IUserRepository):
    
    def __init__(self) -> None:
        self._db_session = lambda: next(get_db_session());
        
    # create
    def CreateUser(self, user: 'User'):
        session: Session = self._db_session();
        user_model = UserModel(
            name=user.name(),
            email=user.email(),
            password=user.password(),
            is_logged=user.is_logged()
        )
        session.add(user_model);
        session.commit();
    
    # read
    def GetUserbyID(self, user_id: int) -> Optional['User']:
        session: Session = self._db_session();
        user_model = session.query(UserModel).filter(UserModel.Id() == user_id).first();
        session.close();
        
        if not user_model:
            raise ValueError("This user can't be found.");
        
        return User(
                _id = user_model.user_id,
                _name = user_model.user_name,
                _email = user_model.user_email,
                _password = user_model.user_password,
                _is_logged = user_model.user_is_logged
            );
    
    def GetUserbyFilter(self, **filter) -> List['User']:
        session: Session = self._db_session();
        user_models = session.query(UserModel).filter_by(**filter).all();
        session.close();
        users = [
            User(
                _id = user_model.user_id,
                _name = user_model.user_name,
                _email = user_model.user_email,
                _password = user_model.user_password,
                _is_logged = user_model.user_is_logged
            ) for user_model in user_models
        ]
        return users;
    
    def GetAllUsers(self) -> List['User']:
        session: Session = self._db_session();
        user_models = session.query(UserModel).all();
        session.close();
        users = [
            User(
                _id = user_model.user_id,
                _name = user_model.user_name,
                _email = user_model.user_email,
                _password = user_model.user_password,
                _is_logged = user_model.user_is_logged
            ) for user_model in user_models
        ]
        return users;
    
    # update
    def UpdateUser(self, user: 'User'):
        
        session: Session = self._db_session();
        existing_user = session.query(UserModel).filter(UserModel.user_id() == user.Id()).first();
        
        if not existing_user:
            raise ValueError("This adm can't be found");
        
        existing_user.set_name(user.name());
        existing_user.set_email(user.email());
        existing_user.set_password(user.password());
        existing_user.set_is_logged(user.isLogged());
        session.commit();
        session.close();
        
    # delete
    def DeleteUser(self, user_id: int) -> None:
        session: Session = self._db_session();
        existing_user = session.query(UserModel).filter(UserModel.user_id() == user_id).first();
        
        if not existing_user:
            raise ValueError("This user can't be finded");
        
        session.delete(existing_user);
        session.commit();
        session.close();