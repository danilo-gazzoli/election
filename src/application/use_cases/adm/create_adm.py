import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from typing import List
from core.entities.permission import Permission;
from core.entities.election import Election;
from core.interfaces.repositories.adm_repository import IAdmRepository;
from datetime import datetime
from core.entities.adm import Adm;

class CreateAdm:
    def __init__(self, AdmRepository: IAdmRepository):
        self._adm_repository = AdmRepository;
        
    def execute(self, adm_data: dict) -> None:
        self.verify_required_fields(adm_data);
        self.verify_strings_length(adm_data);
        self.verify_object_types(adm_data);
        self.verify_data_type(adm_data);
        
        adm = Adm(
            name = adm_data['name'],
            email = adm_data['email'],
            password = adm_data['password'],
            isLogged = adm_data['isLogged'],
            adminRole = adm_data['adminRole'],
            permitionList = adm_data['permitionList'],
            electionList = adm_data['electionList'],
            lastLogin = adm_data['lastLogin']
        );

        self._adm_repository.CreateAdm(adm);

    def verify_required_fields(user_data: dict) -> None:
        required_fields = ['name', 'email', 'password', 'isLogged', 'adminRole', 'permitionList', 'electionList', 'lastLogin'];
        
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                raise ValueError(f"The {field} data can't be empty"); 
            
    def verify_strings_length(adm_data: dict):
        
        if len(adm_data['name']) > 60:
            raise ValueError("This user name is too long.");
        
        if len(adm_data['email']) > 255:
            raise ValueError("This email is too long.");
        
        if len(adm_data['password']) > 60:
            raise ValueError("This password is too long.");
        
    def verify_object_types(adm_data: dict):
        
        new_adm_perms = adm_data['permitionList'];
        new_adm_elections = adm_data['electionList'];
        
        for perm in new_adm_elections:
            if not isinstance(perm, Permission):
                raise ValueError("This perm isn't a permission object");
        
        for election in new_adm_perms:
            if not isinstance(election, Election):
                raise ValueError("This perm isn't a election object");
            
    def verify_data_type(adm_data: dict):
        if not isinstance(adm_data['lastLogin'], datetime):
                raise ValueError("This data isn't a valid date");