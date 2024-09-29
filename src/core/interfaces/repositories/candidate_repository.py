from abc import ABC, abstractmethod;
from core.entities.candidate import Candidate;
from typing import Optional, List;

class ICandidateRepository(ABC):
    
    # create candidates
    @abstractmethod
    def CreateCandidate(self, candidate: 'Candidate') -> None:
        pass;
    
    # read/get candidates
    @abstractmethod
    def GetCandidatebyID(self, candidate_id: int) -> Optional['Candidate']:
        pass;
    
    @abstractmethod
    def GetCandidatebyFilter(self, **filter) -> List['Candidate']:
        pass;
    
    @abstractmethod
    def GetAllCandidate(self) -> List['Candidate']:
        pass;
    
    #  update candidate
    @abstractmethod
    def UpdateCandidate(self, candidate: 'Candidate'):
        pass;
    
    # Delete/remove candidate
    @abstractmethod
    def DeleteCandidate(self, candidate: 'Candidate') -> None:
        pass;