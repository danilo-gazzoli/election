from core.interfaces.repositories.candidate_repository import ICandidateRepository;
from core.entities.candidate import Candidate;

class CreateUser:
    def __init__(self, CandidateRepository: ICandidateRepository):
        self._candidate_repository = CandidateRepository;
        
    def execute(self, candidate_data: dict) -> None:
        candidate = Candidate(
            name = candidate_data['name'],
            cardNumber = candidate_data['cardNumber'],
            candidateNumber = candidate_data['candidateNumber'],
            politicalParty = candidate_data['politicalParty'],
            politicalPosition = candidate_data['politicalPosition'],
            amountVotes= candidate_data['amountVotes']
        )

        self._candidate_repository.CreateUser(candidate);