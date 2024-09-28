from core.entities.election import Election;
from abc import ABC, abstractmethod;
from typing import Optional, List;

class IElectionRepository(ABC):
    
    # create election
    @abstractmethod
    def CreateElection(self, electtion: 'Election') -> None:
        pass;
    
    # read/ get election
    @abstractmethod
    def GetElectionbyID(self, election_id: int) -> Optional['Election']:
        pass;
    
    @abstractmethod
    def GetElectionbyFilter(self, **filter) -> List['Election']:
        pass;
    
    @abstractmethod
    def GetAllElections(self) -> List['Election']:
        pass;
    
    # update election
    @abstractmethod
    def UpdateElection(election: 'Election'):
        pass
    
    # delete election
    @abstractmethod
    def DeleteElection(self, election: 'Election') -> None:
        pass;