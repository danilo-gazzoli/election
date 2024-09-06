from core.entities.data_classes import DataAdm, DataUser;
from core.entities.permission import Permission;
from core.entities.user import User;
from typing import List;

class Adm(User):
    def __init__(self, adm_data: DataAdm, user_data: DataUser):
        super().__init__(user_data);
        self.adminRole = adm_data.adminRole;
        self.permissionsList: List[Permission] = adm_data.permissions;
        self.lastLogin = adm_data.lastLogin;