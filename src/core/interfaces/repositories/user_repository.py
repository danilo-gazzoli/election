from abc import ABC, abstractmethod;
from src.core.entities.user import User;
from typing import Optional, List;


class IUserRepository(ABC):
    
    # create users
    @abstractmethod
    def CreateUser(self, user: 'User'):
        pass
    
    # read/get users
    @abstractmethod
    def GetUserbyID(self, user_id: int) -> Optional['User']:
        pass;
    
    @abstractmethod
    def GetUserbyFilter(self, **filter) -> Optional['User'] | List['User']:
        pass;
    
    @abstractmethod
    def GetAllUsers(self) -> List['User']:
        pass;
    
    # update users
    @abstractmethod
    def UpdateUser(self, user: 'User') -> None:
        pass;
    
    # delete users
    @abstractmethod
    def DeleteUser(self, user: 'User') -> None:
        pass;