from src.core.entities.political_position import PoliticalPosition
from src.core.interfaces.repositories.political_position_repository import IPoliticalPositionRepository

class GetPoliticalPosition:
    def __init__(self, political_position_repository: IPoliticalPositionRepository):
        self._political_position_repository = political_position_repository;

    def execute(self, position_id: int) -> PoliticalPosition:
        position = self._political_position_repository.GetPoliticalPositionById(position_id);
        if not position:
            raise ValueError(f"Political Position with ID {position_id} does not exist.");
        return position;