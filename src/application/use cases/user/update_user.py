from typing import Dict
from core.entities.user import User
from core.interfaces.repositories.user_repository import IUserRepository

class UpdateUserUseCase:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository;

    def execute(self, user_id: int, user_data: Dict, current_user: 'User') -> 'User':
        existing_user = self.user_repository.GetUserbyID(user_id);
        
        if not existing_user:
            raise ValueError("User don't finded.");
        
        if current_user.id != user_id:
            raise PermissionError("You can only update your own profile.");
        
        self._update_user_attributes(existing_user, user_data);
        self.user_repository.UpdateUser(existing_user);
        
        return existing_user;
    
    def _update_user_attributes(self, user: 'User', user_data: Dict):
        if 'name' in user_data:
            user.set_name(user_data['name']);
        
        if 'email' in user_data:
            user.set_email(user_data['email']);
        
        if 'password' in user_data:
            user.set_password(user_data['password']);