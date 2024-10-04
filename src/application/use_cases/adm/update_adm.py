import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from typing import Dict
from core.entities.adm import Adm
from core.interfaces.repositories.adm_repository import IAdmRepository
from core.interfaces.repositories.permission_repository import IPermissionRepository
from core.entities.permission import Permission
from src.core.entities.election import Election

class UpdateAdmUseCase:
    def __init__(self, adm_repository: IAdmRepository, permission_repository: IPermissionRepository):
        self.adm_repository = adm_repository;
        self.permission_repository = permission_repository;

    def execute(self, adm_id: int, adm_data: Dict, current_user: 'Adm') -> 'Adm':
        if not self._user_has_permission(current_user, 'update_adm'):
            raise PermissionError("You don't have permission to update administrators.");
        
        existing_adm = self.adm_repository.GetAdmbyID(adm_id);
        
        if not existing_adm:
            raise ValueError("Adm can't be finded.");
        
        self._update_adm_attributes(existing_adm, adm_data);
        self.adm_repository.UpdateAdm(existing_adm);
        
        return existing_adm;

    def _user_has_permission(self, user: 'Adm', permission_name: str) -> bool:
        return any(permission.name == permission_name for permission in user.permitionList);
    
    def _update_adm_attributes(self, adm: 'Adm', adm_data: Dict):
        
        if 'name' in adm_data:
            adm.set_name(adm_data['name']);
            
        if 'email' in adm_data:
            adm.set_email(adm_data['email']);
            
        if 'password' in adm_data:
            adm.set_password(adm_data['password']);
            
        if 'adminRole' in adm_data:
            adm.set_role(adm_data['adminRole']);
            
        if 'permitionList' in adm_data:
            perm_list = adm_data['permitionList'];
            
            if not all(isinstance(permission, Permission) for permission in perm_list):
                raise ValueError("Todos os itens em permitionList devem ser instâncias de Permission.");
            
            adm.set_permition_list(perm_list);
            
        if 'electionList' in adm_data:
            election_list = adm_data['electionList'];
            
            if not all(isinstance(election, Election) for election in election_list):
                raise ValueError("Todos os itens em electionList devem ser instâncias de Election.");
            
            adm.set_election_list(election_list);
            
        if 'lastLogin' in adm_data:
            adm.set_last_login(adm_data['lastLogin']);