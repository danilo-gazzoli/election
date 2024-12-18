from dataclasses import dataclass;
from verify_email import verify_email;
from typing import List;

@dataclass
class User():
    _id: int;
    _name: str;
    _email: str;
    _google_id: str = None;
    _password: str = None;
    _isLogged: bool = False;
    

    # user id getter 
    @property
    def Id(self):
        return self._id;
    
    # google id getter and setter
    @property
    def google_id(self):
        return self._google_id;
    
    @google_id.setter
    def set_google_id(self, value):
        self._google_id = value;
    
    # user name getter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        if not value:
            raise ValueError("Name can't be empty");
        self._name = value;
    
    # user email getter and setter 
    @property
    def email(self):
        return self._email;
    
    @email.setter
    def set_email(self, value):
        
        if verify_email(value) is False:
            raise ValueError("This email address is not valid");
        
        self._email = value;
    
    # user password getter and setter
    @property
    def password(self):
        return self._password;
    
    @password.setter
    def set_password(self, value: str):
        
        if value == "":
            raise ValueError("This password is not valid");
        
        self._password = value;
        
    # user is logged getter and setter
    @property
    def isLogged(self):
        return self._isLogged;
    
    @isLogged.setter
    def set_is_logged(self, value: bool):
        
        if value is None:
            raise ValueError("This value can't be empty");
        
        self._isLogged = value;
        