from typing import Dict
from core.entities.political_party import PoliticalParty
from core.interfaces.repositories.political_party_repository import IPoliticalPartyRepository
from core.interfaces.repositories.adm_repository import IAdmRepository
from src.core.entities.adm import Adm

class UpdatePoliticalPartyUseCase:
    def __init__(self, political_party_repository: IPoliticalPartyRepository, adm_repository: IAdmRepository):
        self.political_party_repository = political_party_repository;
        self.adm_repository = adm_repository;

    def execute(self, party_id: int, party_data: Dict, current_user: 'Adm') -> 'PoliticalParty':
        if not self._user_has_permission(current_user, 'update_political_party'):
            raise PermissionError("You are not allowed to update political parties.");
        
        existing_party = self.political_party_repository.GetPoliticalPartyByID(party_id);
        
        if not existing_party:
            raise ValueError("Political party don't finded.");
        
        self._update_party_attributes(existing_party, party_data);
        self.political_party_repository.UpdatePoliticalParty(existing_party);
        
        return existing_party;

    def _user_has_permission(self, user: 'Adm', permission_name: str) -> bool:
        return any(permission.name == permission_name for permission in user.permitionList);
    
    def _update_party_attributes(self, party: 'PoliticalParty', party_data: Dict):
        if 'name' in party_data:
            party.set_name(party_data['name']);
        
        if 'partyPicture' in party_data:
            party.set_party_picture(party_data['partyPicture']);
        
        if 'candidateList' in party_data:
            party.set_candidate_list(party_data['candidateList']);