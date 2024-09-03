from abc import ABC, abstractmethod;
from core.entities.user import User;
from typing import Optional, List;

class IElectionRepository(ABC):
    
    @abstractmethod
    def StartElection(election_id: int) -> None:
        pass
    
    @abstractmethod
    def EndElection(election_id: int) -> None:
        pass
    
    @abstractmethod
    def GetElectionStatus(election_id: int) -> str:
        pass