from core.entities.data_classes import DataUser;
from verify_email import verify_email;

class User:
    def __init__(self, user_data: DataUser):
        self._id = user_data.id;
        self._name = user_data.name;
        self._email = user_data.email;
        self._password = user_data.password;
    
    # user id getter 
    @property
    def UserId(self):
        return self._id;
    
    # user name getter and setter
    @property
    def UserName(self):
        return self._name;
    
    @UserName.setter
    def set_name(self, value: str):
        if not value:
            raise ValueError("Name can't be empty");
        self._name = value;
    
    # user email getter and setter 
    @property
    def UserEmail(self):
        return self._email;
    
    @UserEmail.setter
    def set_email(self, value):
        
        if verify_email(value) is False:
            raise ValueError("This email address is not valid");
        
        self._email = value;
    
    # user password getter and setter
    @property
    def UserPassword(self):
        return self._password;
    
    @UserPassword.setter
    def set_password(self, value: str):
        self._password = value;