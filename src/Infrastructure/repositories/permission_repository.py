from core.interfaces.repositories.permission_repository import IPermissionRepository;
from core.entities.permission import Permission;
from sqlalchemy.orm import Session;
from Infrastructure.db.db import get_db_session;
from typing import Optional, List;

class PermissionRepository(IPermissionRepository):
    
    def __init__(self):
        self._db_session = get_db_session;
        
    # create
    def CreatePermission(self, permission: 'Permission') -> None:
        session: Session = self._db_session();
        session.add(permission);
        session.commit();
        
    # read
    def GetPermissionbyID(self, permission_id: int) -> 'Permission' | None:
        session: Session = self._db_session();
        return session.query(Permission).filter(Permission.Id() == permission_id).first();
    
    def GetAllPermissions(self) -> List['Permission']:
        session: Session = self._db_session();
        return session.query(Permission).all();
    
    def GetPermissionbyFilter(self, **filter) -> List['Permission']:
        session: Session = self._db_session();
        return session.query(Permission).filter_by(**filter).all();
    
    # update
    def UpdatePermission(self, permission: 'Permission'):
        session: Session = self._db_session();
        existing_permission = session.query(Permission).filter(Permission.Id() == permission.Id()).first();
        
        if not existing_permission:
            raise ValueError("This permission can't be finded");
        
        existing_permission._name = permission.name();
        existing_permission._description = permission.description();
        existing_permission._accessLevels = permission.accessLevel();
        existing_permission._isActive = permission.isActive();
        session.commit();
    
    # delete
    def DeletePermission(self, permission_id: int) -> None:
        session: Session = self._db_session();
        permission = session.query(Permission).filter(Permission.Id() == permission_id).first();
        
        if not permission:
            raise ValueError("This permission can't be finded");
        
        session.delete(permission);
        session.commit();