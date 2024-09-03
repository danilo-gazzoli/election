from abc import ABC, abstractmethod;
from core.entities.candidate import Candidate;
from typing import Optional, List;

class ICandidateRepository(ABC):
    
    # get candidates
    @abstractmethod
    def GetCandidatebyCardNumber(self, voter_cardNumber: int) -> Optional[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatebyName(self, candidate_name: str) -> Optional[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatebyCandidateNumber(self, candidate_number: int) -> Optional[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatebyPoliticalParty(self, political_party: str) -> List[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatebyPoliticalPosition(self, political_position: str) -> List[Candidate]:
        pass;
    
    @abstractmethod
    def GetCandidatebyAmountVotes(self, amount_votes: int) -> List[Candidate]:
        pass;
    
    @abstractmethod
    def GetListCandidates(self) -> List[Candidate]:
        pass;
    
    # add candidates
    @abstractmethod
    def AddCandidate(self, candidate: Candidate) -> None:
        pass;
    
    # remove candidate
    @abstractmethod
    def RemoveCandidate(self, candidate: Candidate) -> None:
        pass;
    
    # update candidates
    @abstractmethod
    def UpdateCandidate(self, candidate: Candidate) -> None:
        pass;