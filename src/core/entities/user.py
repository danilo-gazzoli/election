from classes_data import DataUser;
from verify_email import verify_email;

class User:
    def __init__(self, user_data: 'DataUser'):
        self._id = user_data.id;
        self._name = user_data.name;
        self._email = user_data.email;
        self._password = user_data.password;
    
    # user id getter 
    @property
    def id(self):
        return self._id;
    
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
        
        if value is "":
            raise ValueError("This password is not valid");
        
        self._password = value;