from core.entities.data_classes import DataPoliticalParty;
from core.entities.political_party import PoliticalParty;
from abc import ABC, abstractmethod;
from typing import Optional, List;

class IPoliticalPartyRepository(ABC):
    
    # create political party
    @abstractmethod
    def CreatePoliticalParty(self, politicalParty_data: DataPoliticalParty):
        pass;
    
    # read/get political party
    @abstractmethod
    def GetPoliticalPartys(self) -> List[PoliticalParty]:
        pass;
    
    @abstractmethod
    def GetPoliticalPartybyId(self, politicalParty_id: int) -> Optional[PoliticalParty]:
        pass;
    
    @abstractmethod
    def GetPoliticalPartybyName(self, politicalParty_name: str) -> Optional[PoliticalParty]:
        pass;
    
    # update political party
    @abstractmethod
    def UpdatePoliticalParty(self, politicalParty: PoliticalParty) -> None:
        pass;
    
    # delete political party
    @abstractmethod
    def DeletePoliticalParty(self, politicalParty_id: int) -> None:
        pass;