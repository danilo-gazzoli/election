from abc import ABC, abstractmethod;
from core.entities.candidate import Candidate;
from typing import Optional, List;

class ICandidateRepository(ABC):
    @abstractmethod
    def GetCandidatebyCardNumber(self, voter_cardNumber: int) -> Optional[Candidate]:
        pass
    
    @abstractmethod
    def GetCandidatebyName(self, user_name: str) -> Optional[Candidate]:
        pass
    
    @abstractmethod
    def GetCandidatebyCandidateNumber(self, candidate_number: int) -> Optional[Candidate]:
        pass
    
    @abstractmethod
    def GetCandidatebyPoliticalParty(self, political_party: str) -> List[Candidate]:
        pass
    
    @abstractmethod
    def GetCandidatebyPoliticalPosition(self, political_position: str) -> List[Candidate]:
        pass