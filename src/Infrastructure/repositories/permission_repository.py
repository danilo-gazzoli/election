import sys;
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')));

from core.interfaces.repositories.permission_repository import IPermissionRepository;
from core.entities.permission import Permission;
from sqlalchemy.orm import Session;
from infrastructure.db.db_config import get_db_session;
from typing import Optional, List;

class PermissionRepository(IPermissionRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
        
    # create
    def CreatePermission(self, permission: 'Permission') -> None:
        session: Session = self._db_session();
        session.add(permission);
        session.commit();
        session.close();
        
    # read
    def GetPermissionbyID(self, permission_id: int) -> 'Permission' | None:
        session: Session = self._db_session();
        permission = session.query(Permission).filter(Permission.Id() == permission_id).first();
        session.close();
        return permission;
    
    def GetAllPermissions(self) -> List['Permission']:
        session: Session = self._db_session();
        permission = session.query(Permission).all();
        session.close();
        return permission;
    
    def GetPermissionbyFilter(self, **filter) -> List['Permission']:
        session: Session = self._db_session();
        permission = session.query(Permission).filter_by(**filter).all();
        session.close();
        return permission;
        
    # update
    def UpdatePermission(self, permission: 'Permission'):
        session: Session = self._db_session();
        existing_permission = session.query(Permission).filter(Permission.Id() == permission.Id()).first();
        
        if not existing_permission:
            raise ValueError("This permission can't be finded");
        
        existing_permission.set_name(permission.name());
        existing_permission.set_description(permission.description());
        existing_permission.set_accessLevels(permission.accessLevel());
        existing_permission.set_isActive(permission.isActive());
        session.commit();
        session.close();
    
    # delete
    def DeletePermission(self, permission_id: int) -> None:
        session: Session = self._db_session();
        permission = session.query(Permission).filter(Permission.Id() == permission_id).first();
        
        if not permission:
            raise ValueError("This permission can't be finded");
        
        session.delete(permission);
        session.commit();
        session.close();