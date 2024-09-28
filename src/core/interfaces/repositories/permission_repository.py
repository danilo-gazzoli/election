from core.entities.permission import Permission;
from abc import ABC, abstractmethod;
from typing import Optional, List;

class IPermissionRepository(ABC):
    
    # create permission
    @abstractmethod
    def CreatePermission(self, permission: 'Permission') -> None:
        pass;
    
    # read/ get permission
    @abstractmethod
    def GetPermissionbyID(self, permission_id: int) -> Optional['Permission']:
        pass;
    
    @abstractmethod
    def GetPermissionbyFilter(self, **filter) -> List['Permission']:
        pass;
    
    @abstractmethod
    def GetAllPermissions(self) -> List['Permission']:
        pass;
    
    # update permission
    
    # delete permission
    @abstractmethod
    def DeletePermission(self, Permission: 'Permission') -> None:
        pass;
    