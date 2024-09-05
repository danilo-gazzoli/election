from core.entities.data_classes import UserData

class User:
    def __init__(self, user_data: UserData):
        self.id = user_data.id;
        self.name = user_data.name;
        self.email = user_data.email;
        self.password = user_data.password;