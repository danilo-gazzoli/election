from core.interfaces.repositories.user_repository import IUserRepository;
from core.entities.user import User;

class CreateUser:
    def __init__(self, UserRepository: IUserRepository):
        self._user_repository = UserRepository;
        
    def execute(self, user_data: dict) -> None:
        user = User(
            name = user_data['name'],
            email = user_data['email'],
            password = user_data['password'],
            isLogged = user_data['isLogged']
        )

        self._user_repository.CreateUser(user);