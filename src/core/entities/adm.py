from core.entities.user import User;

class Adm(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password);