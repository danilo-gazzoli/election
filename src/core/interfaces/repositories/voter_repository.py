from abc import ABC, abstractmethod;
from core.entities.voter import Voter;
from typing import Optional, List;


class IVoterRepository(ABC):
    
    # get voter
    @abstractmethod
    def GetVoterbyCardNumber(self, voter_cardNumber: int) -> Optional[Voter]:
        pass;
    
    @abstractmethod
    def GetVoterbyName(self, user_name: str) -> Optional[Voter]:
        pass;
    
    