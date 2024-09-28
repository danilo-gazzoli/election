from abc import ABC, abstractmethod;
from src.core.entities.adm import Adm;
from typing import Optional, List;


class IAdmRepository(ABC):
    
    # create adm
    @abstractmethod
    def CreateAdm(self, adm: 'Adm'):
        pass
    
    # read/get adm
    @abstractmethod
    def GetAdmbyID(self, adm_id: int) -> Optional['Adm']:
        pass;
    
    @abstractmethod
    def GetAdmbyFilter(self, **filter) -> List['Adm']:
        pass;
    
    @abstractmethod
    def GetAllAdms(self) -> List['Adm']:
        pass;
    
    # update adm
    @abstractmethod
    def UpdateAdm(self, adm: 'Adm') -> None:
        pass;
    
    # delete adm
    @abstractmethod
    def DeleteAdm(self, adm: 'Adm') -> None:
        pass;
    