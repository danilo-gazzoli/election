from dataclasses import dataclass;
from permission import Permission;
from verify_email import verify_email;
from user import User;
from election import Election;
from datetime import datetime
from typing import List;

@dataclass
class Adm(User):
    _adminRole: str;
    _permitionList: List['Permission'];
    _electionList: List['Election'];
    _lastLogin: datetime;
        
    # adm role getter and setter
    @property
    def role(self):
        return self._adminRole;
    
    @role.setter
    def set_role(self, value: str):
        self._adminRole = value;
        
        
    # adm permition list getter and setter
    @property
    def permitionList(self):
        return self._permissionsList;
    
    @permitionList.setter
    def set_permition_list(self, perm_list: List['Permission']):
        
        if not all(isinstance(permission, Permission) for permission in perm_list):
            raise ValueError("All items must be instances of Permission");
        
        self._permissionsList = perm_list;
        
    # adm last login getter and setter 
    @property
    def electionList(self):
        return self._electionList;
    
    @electionList.setter
    def set_election_list(self, election_list: List['Election']):
        
        if not all(isinstance(election, Election) for election in election_list):
            raise ValueError("All items must be instances of Election");
        
        self._electionList = election_list;
        
    # adm last login getter and setter 
    @property
    def lastLogin(self):
        return self._lastLogin;
    
    @lastLogin.setter
    def set_last_login(self, value: datetime):
        self._lastLogin = value;