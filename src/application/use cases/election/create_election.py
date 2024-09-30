from core.interfaces.repositories.election_repository import IElectionRepository;
from core.entities.election import Election;

class CreateUser:
    def __init__(self, ElectionRepository: IElectionRepository):
        self._election_repository = ElectionRepository;
        
    def execute(self, election_data: dict) -> None:
        election = Election(
            name = election_data['name'],
            usersRegistered = election_data['usersRegistered'],
            politicalPositions = election_data['politicalPositions'],
            politicalCandidates = election_data['politicalCandidates'],
            politicalPartys = election_data['politicalPartys']
        )

        self._election_repository.CreateUser(election);