from core.entities.data_classes import DataAdm, DataUser;
from core.entities.permission import Permission;
from verify_email import verify_email;
from core.entities.user import User;
from datetime import datetime
from typing import List;

class Adm(User):
    def __init__(self, adm_data: DataAdm, user_data: DataUser):
        super().__init__(user_data);
        self._adminRole = adm_data.adminRole;
        self._permissionsList: List[Permission] = adm_data.permissions;
        self._lastLogin = adm_data.lastLogin;
    
    # adm id getter
    @property
    def AdmId(self):
        return self._id;
    
    # adm name getter and setter
    @property
    def AdmName(self):
        return self._name;
    
    @AdmName.setter
    def set_name(self, value: str):
        if not value:
            raise ValueError("Name can't be empty");
        self._name = value;
    
    # adm email getter and setter
    @property
    def AdmEmail(self):
        return self._email;
    
    @AdmEmail.setter
    def set_email(self, value):
        
        if verify_email(value) is False:
            raise ValueError("This email address is not valid");
        
        self._email = value;
    
    # password getter and setter
    @property
    def AdmPassword(self):
        return self._password;
    
    @AdmPassword.setter
    def set_password(self, value: str):
        self._password = value;
        
    # adm role getter and setter
    @property
    def AdmRole(self):
        return self._adminRole;
    
    @AdmRole.setter
    def set_role(self, value: str):
        self._adminRole = value;
        
    # adm last login getter and setter 
    @property
    def AdmLastLogin(self):
        return self._lastLogin;
    
    @AdmLastLogin.setter
    def set_last_login(self, value: datetime):
        self._lastLogin = value;
        
    # adm permition list getter and setter
    @property
    def AdmPermitionList(self):
        return self._permissionsList;
    
    @AdmPermitionList.setter
    def set_permition_list(self, perm_list: List[Permission]):
        
        if not all(isinstance(permission, Permission) for permission in perm_list):
            raise ValueError("All items must be instances of Permission")
        
        self._permissionsList = perm_list;