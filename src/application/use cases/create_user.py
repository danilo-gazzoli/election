from core.interfaces.repositories import user_repository
from core.entities import user

class CreateUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository;