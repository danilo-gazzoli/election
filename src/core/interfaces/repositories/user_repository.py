from abc import ABC, abstractmethod;
from core.entities.user import User;
from typing import Optional;


class IUserRepository(ABC):
    @abstractmethod
    def GetUserbyID(self, user_id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def GetUserbyName(self, user_name: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def GetUserbyEmail(self, user_email: str) -> Optional[User]:
        pass