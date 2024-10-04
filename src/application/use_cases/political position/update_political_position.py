from typing import Dict
from core.entities.political_position import PoliticalPosition
from core.interfaces.repositories.political_position_repository import IPoliticalPositionRepository
from core.interfaces.repositories.adm_repository import IAdmRepository
from src.core.entities.adm import Adm

class UpdatePoliticalPositionUseCase:
    def __init__(self, political_position_repository: IPoliticalPositionRepository, adm_repository: IAdmRepository):
        self.political_position_repository = political_position_repository;
        self.adm_repository = adm_repository;

    def execute(self, position_id: int, position_data: Dict, current_user: 'Adm') -> 'PoliticalPosition':
        if not self._user_has_permission(current_user, 'update_political_position'):
            raise PermissionError("You don't have permission to update political positions.");
        
        existing_position = self.political_position_repository.GetPoliticalPositionByID(position_id);
        
        if not existing_position:
            raise ValueError("Political position don't finded.");
        
        self._update_position_attributes(existing_position, position_data);
        self.political_position_repository.UpdatePoliticalPosition(existing_position);
        
        return existing_position;

    def _user_has_permission(self, user: 'Adm', permission_name: str) -> bool:
        return any(permission.name == permission_name for permission in user.permitionList);
    
    def _update_position_attributes(self, position: 'PoliticalPosition', position_data: Dict):
        if 'name' in position_data:
            position.set_name(position_data['name']);
        
        if 'vacancies' in position_data:
            position.set_vacancies(position_data['vacancies']);
        
        if 'candidatesCompeting' in position_data:
            position.set_candidates_competing(position_data['candidatesCompeting']);