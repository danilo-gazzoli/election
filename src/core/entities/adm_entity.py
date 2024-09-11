from classes_data import DataAdm, DataUser;
from permission import Permission;
from verify_email import verify_email;
from user import User;
from datetime import datetime
from typing import List;

class Adm(User):
    def __init__(self, id: int, name: str, email: str, password: str, adminRole: str, permitionList: List['Permission'], lastLogin: datetime):
        super().__init__(id, name, email, password);
        self._adminRole = adminRole;
        self._permissionsList = permitionList;
        self._lastLogin = lastLogin;
    
    # adm id getter
    @property
    def id(self):
        return self._id;
    
    # adm name getter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        if not value:
            raise ValueError("Name can't be empty");
        self._name = value;
    
    # adm email getter and setter
    @property
    def email(self):
        return self._email;
    
    @email.setter
    def set_email(self, value):
        
        if verify_email(value) is False:
            raise ValueError("This email address is not valid");
        
        self._email = value;
    
    # password getter and setter
    @property
    def password(self):
        return self._password;
    
    @password.setter
    def set_password(self, value: str):
        self._password = value;
        
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