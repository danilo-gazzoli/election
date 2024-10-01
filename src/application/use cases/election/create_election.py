from core.interfaces.repositories.election_repository import IElectionRepository;
from core.entities.election import Election;

class CreateElection:
    def __init__(self, ElectionRepository: IElectionRepository):
        self._election_repository = ElectionRepository;
        
    def execute(self, election_data: dict) -> None:
        self.verify_required_fields(election_data);
        self.verify_strings_length(election_data);
        
        election = Election(
            name = election_data['name'],
            usersRegistered = election_data['usersRegistered'],
            politicalPositions = election_data['politicalPositions'],
            politicalCandidates = election_data['politicalCandidates'],
            politicalPartys = election_data['politicalPartys']
        );

        self._election_repository.CreateElection(election);
        
    def verify_required_fields(self, election_data: dict) -> None:
        required_fields = ['name', 'usersRegistered', 'politicalPositions', 'politicalCandidates', 'politicalPartys'];
        
        for field in required_fields:
            if field not in election_data or not election_data[field]:
                raise ValueError(f"The {field} data can't be empty"); 
            
    def verify_strings_length(self, election_data: dict):
        
        if len(election_data['name']) > 45:
            raise ValueError("This election name is too long.");