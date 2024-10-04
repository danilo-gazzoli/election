from src.core.interfaces.repositories.political_position_repository import IPoliticalPositionRepository;

class DeletePoliticalPosition:
    def __init__(self, position_repository: IPoliticalPositionRepository, current_user):
        self._position_repository = position_repository;
        self._current_user = current_user;

    def execute(self, position_id: int) -> None:
        self.verify_user_permissions(self._current_user);
        position = self._position_repository.GetPoliticalPositionById(position_id);
        
        if not position:
            raise ValueError(f"Political Position with ID {position_id} does not exist.");
        
        self._position_repository.DeletePoliticalPosition(position_id);

    def verify_user_permissions(self, user):
        if not user.is_admin():
            raise PermissionError("User does not have permission to delete a political position.");