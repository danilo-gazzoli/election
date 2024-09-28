from core.entities.political_party import PoliticalParty;
from abc import ABC, abstractmethod;
from typing import Optional, List;

class IPoliticalPartyRepository(ABC):
    
    # create political party
    @abstractmethod
    def CreatePoliticalParty(self, politicalParty: 'PoliticalParty'):
        pass;
    
    # read/get political party
    @abstractmethod
    def GetPoliticalPartybyID(self, politicalParty_id: int) -> Optional['PoliticalParty']:
        pass;
    
    @abstractmethod
    def GetPoliticalPartybyFilter(self, **filter) -> List['PoliticalParty']:
        pass;
    
    @abstractmethod
    def GetAllPoliticalPartys(self) -> List['PoliticalParty']:
        pass;
    
    # update political party
    @abstractmethod
    def UpdatePoliticalParty(self, politicalParty: 'PoliticalParty') -> None:
        pass;
    
    # delete political party
    @abstractmethod
    def DeletePoliticalParty(self, politicalParty_id: int) -> None:
        pass;