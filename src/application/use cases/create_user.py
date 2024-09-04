from core.interfaces.repositories.user_repository import IUserRepository;
from core.entities.user import User;
from typing import Optional;

class CreateUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository;
        
    def execute(self, name: str, email: str, password: int) -> Optional[User]:
        existing_users = self.user_repository.GetUserbyEmail(email);
        if (existing_users != None):
            print("This email has already been used");
            return None;
        
        new_user = User(id=None, name=name, email=email, password=password);
        
        self.user_repository.AddUser(new_user);
        
        return new_user;