from datetime import datetime
from core.interfaces.repositories.user_repository import IUserRepository;
from core.entities.user import User;

class CreateUser:
    def __init__(self, UserRepository: IUserRepository):
        self._user_repository = UserRepository;
        
    def execute(self, user_data: dict) -> None:
        self.verify_required_fields(user_data);
        self.verify_strings_length(user_data);
        self.verify_data_type(user_data);
        
        user = User(
            name = user_data['name'],
            email = user_data['email'],
            password = user_data['password'],
            isLogged = user_data['isLogged']
        );

        self._user_repository.CreateUser(user);
        
    def verify_required_fields(self, user_data: dict) -> None:
        required_fields = ['name', 'email', 'password', 'isLogged'];
        
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                raise ValueError(f"The {field} data can't be empty"); 
            
    def verify_strings_length(self, user_data: dict):
        
        if len(user_data['name']) > 60:
            raise ValueError("This user name is too long.");
        
        if len(user_data['email']) > 255:
            raise ValueError("This email is too long.");
        
        if len(user_data['password']) > 60:
            raise ValueError("This password is too long.");
        
    def verify_data_type(self, adm_data: dict):
        if not isinstance(adm_data['lastLogin'], datetime):
                raise ValueError("This data isn't a valid date");