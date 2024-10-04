from core.interfaces.repositories.election_repository import IElectionRepository;
from core.entities.election import Election
from src.core.entities.candidate import Candidate
from src.core.entities.political_party import PoliticalParty
from src.core.entities.political_position import PoliticalPosition
from src.core.entities.user import User;

class CreateElection:
    def __init__(self, ElectionRepository: IElectionRepository):
        self._election_repository = ElectionRepository;
        
    def execute(self, election_data: dict) -> None:
        self.verify_required_fields(election_data);
        self.verify_strings_length(election_data);
        self.verify_object_types(election_data);
        
        election = Election(
            name = election_data['name'],
            usersRegistered = election_data['usersRegistered'],
            politicalPositions = election_data['politicalPositions'],
            politicalCandidates = election_data['politicalCandidates'],
            politicalPartys = election_data['politicalPartys']
        );

        self._election_repository.CreateElection(election);
        
    def verify_required_fields(election_data: dict) -> None:
        required_fields = ['name', 'usersRegistered', 'politicalPositions', 'politicalCandidates', 'politicalPartys'];
        
        for field in required_fields:
            if field not in election_data or not election_data[field]:
                raise ValueError(f"The {field} data can't be empty"); 
            
    def verify_strings_length(election_data: dict):
        
        if len(election_data['name']) > 45:
            raise ValueError("This election name is too long.");
        
    def verify_object_types(election_data: dict):
        
        new_adm_political_users = election_data['usersRegistered'];
        new_adm_political_positions = election_data['politicalPositions'];
        new_adm_political_candidates = election_data['politicalCandidates'];
        new_adm_political_partys = election_data['politicalPartys'];
        
        for user in new_adm_political_users:
            if not isinstance(user, User):
                raise ValueError("This perm isn't a user object");
            
        for political_candidate in new_adm_political_candidates:
            if not isinstance(political_candidate, Candidate):
                raise ValueError("This perm isn't a candidate object");
            
        for political_position in new_adm_political_positions:
            if not isinstance(political_position, PoliticalPosition):
                raise ValueError("This perm isn't a political position object");
            
        for political_party in new_adm_political_partys:
            
            if not isinstance(political_party, PoliticalParty):
                raise ValueError("This perm isn't a political party object");
            
    