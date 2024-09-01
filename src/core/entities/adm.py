from core.entities.user import User

class Adm(User):
    def __init__(self, email, password):
        super().__init__(email, password);