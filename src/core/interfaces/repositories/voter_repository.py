from core.entities.data_classes import VoterData;
from core.entities.voter import Voter;
from abc import ABC, abstractmethod;
from typing import Optional, List;


class IVoterRepository(ABC):
    
    # create voter
    @abstractmethod
    def CreateVoter(self, voter_data: VoterData):
        pass;
    
    # read/get voter
    @abstractmethod
    def GetVoterbyCardNumber(self, voter_cardNumber: int) -> Optional[Voter]:
        pass;
    
    @abstractmethod
    def GetVoterbyName(self, voter_name: str) -> Optional[Voter]:
        pass;
    
    @abstractmethod
    def GetVoters(self) -> List[Voter]:
        pass;
    
    # uptade voter
    @abstractmethod
    def UpdateVoter(self, voter: Voter) -> None:
        pass;
    
    # delete voter
    @abstractmethod
    def DeleteVoter(self, voter: Voter) -> None:
        pass;