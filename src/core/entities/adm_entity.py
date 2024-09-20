from dataclasses import dataclass;
from permission import Permission;
from verify_email import verify_email;
from user import User;
from datetime import datetime
from typing import List;

@dataclass
class Adm(User):
    _adminRole: str;
    _permitionList: List['Permission'];
    _lastLogin: datetime;
        
    # adm role getter and setter
    @property
    def role(self):
        return self._adminRole;
    
    @role.setter
    def set_role(self, value: str):
        self._adminRole = value;
        
    # adm last login getter and setter 
    @property
    def lastLogin(self):
        return self._lastLogin;
    
    @lastLogin.setter
    def set_last_login(self, value: datetime):
        self._lastLogin = value;
        
    # adm permition list getter and setter
    @property
    def permitionList(self):
        return self._permissionsList;
    
    @permitionList.setter
    def set_permition_list(self, perm_list: List['Permission']):
        
        if not all(isinstance(permission, Permission) for permission in perm_list):
            raise ValueError("All items must be instances of Permission")
        
        self._permissionsList = perm_list;