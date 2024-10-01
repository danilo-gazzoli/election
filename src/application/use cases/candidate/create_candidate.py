from core.interfaces.repositories.candidate_repository import ICandidateRepository;
from core.entities.candidate import Candidate;

class CreateUser:
    def __init__(self, CandidateRepository: ICandidateRepository):
        self._candidate_repository = CandidateRepository;  
    
    def execute(self, candidate_data: dict) -> None:
        self.verify_required_fields(candidate_data);
        self.verify_existing_candidate_name(candidate_data);
        self.verify_existing_candidate_number(candidate_data);
        
        candidate = Candidate(
            name = candidate_data['name'],
            cardNumber = candidate_data['cardNumber'],
            candidateNumber = candidate_data['candidateNumber'],
            politicalParty = candidate_data['politicalParty'],
            politicalPosition = candidate_data['politicalPosition'],
            amountVotes= candidate_data['amountVotes']
        )

        self._candidate_repository.CreateUser(candidate);
        
    def verify_existing_candidate_number(self, candidate_data: dict):
        existing_candidates = self._candidate_repository.GetAllCandidate();
        
        for Candidate in existing_candidates:
            if Candidate.candidateNumber() == candidate_data['candidateNumber']:
                raise ValueError("This number was used by another candidate");
            
    def verify_existing_candidate_name(self, candidate_data: dict):
        existing_candidates = self._candidate_repository.GetAllCandidate();
        
        for Candidate in existing_candidates:
            if Candidate.name() == candidate_data['name']:
                raise ValueError("This name was used by another candidate");
    
    def verify_required_fields(self, candidate_data: dict) -> None:
        required_fields = ['name', 'cardNumber', 'candidateNumber', 'politicalParty', 'politicalPosition', 'amountVotes'];
        
        for field in required_fields:
            if field not in candidate_data or not candidate_data[field]:
                raise ValueError(f"The {field} data can't be empty");  