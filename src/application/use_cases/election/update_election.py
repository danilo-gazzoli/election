from typing import Dict
from core.entities.election import Election
from core.interfaces.repositories.election_repository import IElectionRepository
from core.interfaces.repositories.adm_repository import IAdmRepository
from src.core.entities.adm import Adm

class UpdateElectionUseCase:
    def __init__(self, election_repository: IElectionRepository, adm_repository: IAdmRepository):
        self.election_repository = election_repository;
        self.adm_repository = adm_repository;

    def execute(self, election_id: int, election_data: Dict, current_user: 'Adm') -> 'Election':
        if not self._user_has_permission(current_user, 'update_election'):
            raise PermissionError("You don't have permission to update election.");
        
        existing_election = self.election_repository.GetElectionByID(election_id);
        if not existing_election:
            raise ValueError("Election don't finded.");
        
        self._update_election_attributes(existing_election, election_data);
        self.election_repository.UpdateElection(existing_election);
        
        return existing_election;

    def _user_has_permission(self, user: 'Adm', permission_name: str) -> bool:
        return any(permission.name == permission_name for permission in user.permitionList);
    
    def _update_election_attributes(self, election: 'Election', election_data: Dict):
        if 'name' in election_data:
            election.set_name(election_data['name']);
            
        if 'usersRegistered' in election_data:
            election.set_users_registered(election_data['usersRegistered']);
        
        if 'politicalPositions' in election_data:
            election.set_political_positions(election_data['politicalPositions']);
        
        if 'politicalCandidates' in election_data:
            election.set_political_candidates(election_data['politicalCandidates']);
        
        if 'politicalParties' in election_data:
            election.set_political_parties(election_data['politicalParties']);