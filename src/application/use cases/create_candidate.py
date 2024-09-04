from core.interfaces.repositories.candidate_repository import ICandidateRepository;
from core.entities.candidate import Candidate;
from typing import Optional;

class CreateCandidate:
    def __init__(self, candidate_repository: ICandidateRepository) :
        self.candidate_repository = candidate_repository;
        
    def execute(self, cardNumber: int, name: str, candidateNumber: int, politicalParty: str, politicalPosition: str) -> Optional[Candidate]:
        existing_candidates = self.candidate_repository.GetCandidatebyName(name);
        usings_candidateNumers = self.candidate_repository.GetCandidatebyCardNumber(candidateNumber);
        usings_cardNumbers = self.candidate_repository.GetCandidatebyCardNumber(cardNumber);
        
        if (existing_candidates != None):
            print("This email has already been used");
            return None;
        
        if (usings_candidateNumers != None):
            print("This candidateNumber has already been used");
            return None;
        
        if (usings_candidateNumers != None):
            print("This card number has already been used");
            return None;
        
        new_candidate = Candidate(id=None, cardNumber=cardNumber, name=name, candidateNumber=candidateNumber, politicalParty=politicalParty, politicalPosition=politicalPosition);
        
        self.candidate_repository.AddCandidate(new_candidate);
        
        return new_candidate;
        
        