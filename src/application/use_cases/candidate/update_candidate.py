from typing import Dict
from core.entities.candidate import Candidate
from core.interfaces.repositories.candidate_repository import ICandidateRepository
from core.interfaces.repositories.adm_repository import IAdmRepository
from core.entities.permission import Permission
from src.core.entities.adm import Adm

class UpdateCandidateUseCase:
    def __init__(self, candidate_repository: ICandidateRepository, adm_repository: IAdmRepository):
        self.candidate_repository = candidate_repository;
        self.adm_repository = adm_repository;

    def execute(self, candidate_id: int, candidate_data: Dict, current_user: 'Adm') -> 'Candidate':
        if not self._user_has_permission(current_user, 'update_candidate'):
            raise PermissionError("You are not allowed to update candidates.");
        
        existing_candidate = self.candidate_repository.GetCandidateByID(candidate_id);
        
        if not existing_candidate:
            raise ValueError("Candidate can't finded.");
        
        self._update_candidate_attributes(existing_candidate, candidate_data);
        self.candidate_repository.UpdateCandidate(existing_candidate);
        
        return existing_candidate;

    def _user_has_permission(self, user: 'Adm', permission_name: str) -> bool:
        return any(permission.name == permission_name for permission in user.permitionList);
    
    def _update_candidate_attributes(self, candidate: 'Candidate', candidate_data: Dict):
        if 'name' in candidate_data:
            candidate.set_name(candidate_data['name']);
        
        if 'cardNumber' in candidate_data:
            candidate.set_card_number(candidate_data['cardNumber']);
        
        if 'candidateNumber' in candidate_data:
            candidate.set_candidate_number(candidate_data['candidateNumber']);
        
        if 'politicalParty' in candidate_data:
            candidate.set_political_party(candidate_data['politicalParty']);
        
        if 'politicalPosition' in candidate_data:
            candidate.set_political_position(candidate_data['politicalPosition']);
        
        if 'profilePicture' in candidate_data:
            candidate.set_profile_picture(candidate_data['profilePicture']);