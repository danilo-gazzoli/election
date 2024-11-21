from flask_login import UserMixin;

class UserAdapter(UserMixin):
    def __init__(self, user_entity):
        self.user = user_entity

    def get_id(self):
        return str(self.user.id)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False