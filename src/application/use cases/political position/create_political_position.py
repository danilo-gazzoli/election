from core.interfaces.repositories.political_position_repository import IPoliticalPositionRepository;
from core.entities.political_position import PoliticalPosition;

class CreateUser:
    def __init__(self, PoliticalPositionRepository: IPoliticalPositionRepository):
        self._political_position_repository = PoliticalPositionRepository;
        
    def execute(self, political_position_data: dict) -> None:
        political_position = PoliticalPosition(
            name = political_position_data['name'],
            vacancies = political_position_data['vacancies'],
            candidatesCompeting = political_position_data['candidatesCompeting']
        )

        self._political_position_repository.CreateUser(political_position);