import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from typing import Dict
from core.entities.permission import Permission
from core.interfaces.repositories.permission_repository import IPermissionRepository
from core.interfaces.repositories.adm_repository import IAdmRepository
from src.core.entities.adm import Adm

class UpdatePermissionUseCase:
    def __init__(self, permission_repository: IPermissionRepository, adm_repository: IAdmRepository):
        self.permission_repository = permission_repository;
        self.adm_repository = adm_repository;

    def execute(self, permission_id: int, permission_data: Dict, current_user: 'Adm') -> 'Permission':
        if not self._user_has_permission(current_user, 'update_permission'):
            raise PermissionError("You do not have permission to update permissions.");
        
        existing_permission = self.permission_repository.GetPermissionByID(permission_id);
        
        if not existing_permission:
            raise ValueError("Permission don't finded.");
        
        self._update_permission_attributes(existing_permission, permission_data);
        self.permission_repository.UpdatePermission(existing_permission);
        
        return existing_permission;

    def _user_has_permission(self, user: 'Adm', permission_name: str) -> bool:
        return any(permission.name == permission_name for permission in user.permitionList);
    
    def _update_permission_attributes(self, permission: 'Permission', permission_data: Dict):
        if 'name' in permission_data:
            permission.set_name(permission_data['name']);
        
        if 'description' in permission_data:
            permission.set_description(permission_data['description']);
        
        if 'accessLevels' in permission_data:
            permission.set_access_levels(permission_data['accessLevels']);
        
        if 'isActive' in permission_data:
            permission.set_is_active(permission_data['isActive']);