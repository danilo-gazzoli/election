from core.entities.data_classes import DataElection;
from core.entities.election import Election;
from abc import ABC, abstractmethod;
from typing import Optional, List;

class IElectionRepository(ABC):
    
    # create election
    @abstractmethod
    def CreateElection(self, electtion_data: DataElection) -> None:
        pass;
    
    # read/ get election
    @abstractmethod
    def GetElectionbyId(self, election_id: int) -> Optional[Election]:
        pass;
    
    @abstractmethod
    def GetElectionbyName(self, election_name: str) -> Optional[Election]:
        pass;
    
    @abstractmethod
    def GetListElection(self) -> List[Election]:
        pass;
    
    # update election
    
    # delete/remove election
    @abstractmethod
    def DeleteElection(self, election: Election) -> None:
        pass;
    
    @abstractmethod
    def StartElection(election_id: int) -> None:
        pass
    
    @abstractmethod
    def EndElection(election_id: int) -> None:
        pass
    
    @abstractmethod
    def GetElectionStatus(election_id: int) -> str:
        pass