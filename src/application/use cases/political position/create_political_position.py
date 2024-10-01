from core.interfaces.repositories.political_position_repository import IPoliticalPositionRepository;
from core.entities.political_position import PoliticalPosition;

class CreateUser:
    def __init__(self, PoliticalPositionRepository: IPoliticalPositionRepository):
        self._political_position_repository = PoliticalPositionRepository;
        
    def execute(self, political_position_data: dict) -> None:
        self.verify_required_fields(political_position_data);
        
        political_position = PoliticalPosition(
            name = political_position_data['name'],
            vacancies = political_position_data['vacancies'],
            candidatesCompeting = political_position_data['candidatesCompeting']
        )

        self._political_position_repository.CreateUser(political_position);
        
    def verify_required_fields(self, political_position_data: dict) -> None:
        required_fields = ['name', 'vacancies', 'candidatesCompeting'];
        
        for field in required_fields:
            if field not in political_position_data or not political_position_data[field]:
                raise ValueError(f"The {field} data can't be empty");