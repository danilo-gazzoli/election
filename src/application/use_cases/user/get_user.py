import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from src.core.entities.user import User;
from src.core.interfaces.repositories.user_repository import IUserRepository;

class GetUser:
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository;

    def execute(self, user_id: int) -> User:
        user = self._user_repository.GetUserById(user_id);
        if not user:
            raise ValueError(f"User with ID {user_id} does not exist.");
        return user;