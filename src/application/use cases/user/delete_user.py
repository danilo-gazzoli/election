from src.core.interfaces.repositories.user_repository import IUserRepository;


class DeleteUser:
    def __init__(self, user_repository: IUserRepository, current_user):
        self._user_repository = user_repository;
        self._current_user = current_user;

    def execute(self, user_id: int) -> None:
        self.verify_user_permissions(self._current_user);
        
        user = self._user_repository.GetUserById(user_id);
        
        if not user:
            raise ValueError(f"User with ID {user_id} does not exist.");
        
        self._user_repository.DeleteUser(user_id);

    def verify_user_permissions(self, user):
        if not user.is_admin():
            raise PermissionError("User does not have permission to delete other users.");