from core.entities.political_position import PoliticalPosition;
from abc import ABC, abstractmethod;
from typing import Optional, List;

class IPoliticalPositionRepository(ABC):
    
    # create political party
    @abstractmethod
    def CreatePoliticalPosition(self, politicalPosition: 'PoliticalPosition'):
        pass;
    
    # read/get political party
    @abstractmethod
    def GetPoliticalPositionbyID(self, politicalPosition_id: int) -> Optional['PoliticalPosition']:
        pass;
    
    @abstractmethod
    def GetPoliticalPositionbyFilter(self, **filter) -> List['PoliticalPosition']:
        pass;
    
    @abstractmethod
    def GetAllPoliticalPositions(self) -> List['PoliticalPosition']:
        pass;
    
    # update political party
    @abstractmethod
    def UpdatePoliticalPosition(self, politicalPosition: 'PoliticalPosition') -> None:
        pass;
    
    # delete political party
    @abstractmethod
    def DeletePoliticalPosition(self, politicalPosition_id: int) -> None:
        pass;