from core.entities.data_classes import DataPermission;
from typing import List;

class Permission:
    def __init__(self, permission_data: DataPermission):
        self.id = permission_data.id;
        self.name = permission_data.name;
        self.description = permission_data.description;
        self.accessLevels: List[str] = permission_data.accessLevels;
        self.isActive = permission_data.isActive;