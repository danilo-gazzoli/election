from core.interfaces.repositories.user_repository import IUserRepository;
from core.entities.user import User;
from sqlalchemy.orm import Session;
from Infrastructure.db.db import get_db_session;
from typing import Optional, List;

class UserRepository(IUserRepository):
    
    def __init__(self) -> None:
        self._db_session = get_db_session;
        
    # create
    def CreateUser(self, user: 'User'):
        session: Session = self._db_session();
        session.add(user);
        session.commit();
    
    # read
    def GetUserbyID(self, user_id: int) -> Optional['User']:
        session: Session = self._db_session();
        return session.query(User).filter(User.Id() == user_id).first();
    
    def GetUserbyFilter(self, **filter) -> List['User']:
        session: Session = self._db_session();
        return session.query(User).filter_by(**filter).all();
    
    def GetAllUsers(self) -> List['User']:
        session: Session = self._db_session();
        return session.query(User).all()
    
    # update
    def UpdateUser(self, user: 'User'):
        
        session: Session = self._db_session();
        existing_user = session.query(User).filter(User.Id() == user.Id()).first();
        
        if not existing_user:
            raise ValueError("This adm can't be finded");
        
        existing_user.set_name(user.name());
        existing_user.set_email(user.email());
        existing_user.set_password(user.password());
        existing_user.set_is_logged(user.isLogged());
        
    # delete
    def DeleteUser(self, user_id: int) -> None:
        session: Session = self._db_session();
        existing_user = session.query(User).filter(User.Id() == user_id).first();
        
        if not existing_user:
            raise ValueError("This user can't be finded");
        
        session.delete(existing_user);
        session.commit();