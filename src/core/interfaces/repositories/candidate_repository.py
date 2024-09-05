from abc import ABC, abstractmethod;
from core.entities.candidate import Candidate;
from typing import Optional, List;

class ICandidateRepository(ABC):
    
    # create candidates
    @abstractmethod
    def AddCandidate(self, candidate: Candidate) -> None:
        pass;
    
    # update candidates
    @abstractmethod
    def UpdateCandidate(self, candidate: Candidate) -> None:
        pass;
    
    @abstractmethod
    def UpdateCandidateCardNumber(self, candidate_cardNumber: int) -> None:
        pass;
    
    @abstractmethod
    def UpdateCandidateName(self, candidate_name: str) -> None:
        pass;
    
    @abstractmethod
    def UpdateCandidateNumber(self, candidate_number: int) -> None:
        pass;
    
    @abstractmethod
    def UpdateCandidatePoliticalParty(self, political_party: str) -> None:
        pass;
    
    @abstractmethod
    def UpdateCandidatePoliticalPosition(self, political_position: str) -> None:
        pass;
    
    # read/get candidates
    @abstractmethod
    def GetCandidatebyCardNumber(self, candidate_cardNumber: int) -> Optional[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatebyName(self, candidate_name: str) -> Optional[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatebyCandidateNumber(self, candidate_number: int) -> Optional[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatesbyPoliticalParty(self, political_party: str) -> List[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatesbyPoliticalPosition(self, political_position: str) -> List[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatesbyAmountVotes(self, amount_votes: int) -> List[Candidate]:
        pass;
    
    @abstractmethod
    def GetListCandidates(self) -> List[Candidate]:
        pass;
    
    # Delete/remove candidate
    @abstractmethod
    def RemoveCandidate(self, candidate: Candidate) -> None:
        pass;
    