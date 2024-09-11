from dataclasses import DataPermission;
from typing import List;

class Permission:
    def __init__(self, permission_data: 'DataPermission'):
        self._id = permission_data.id;
        self._name = permission_data.name;
        self._description = permission_data.description;
        self._accessLevels: List[str] = permission_data.accessLevels;
        self._isActive = permission_data.isActive;
        
    # id getter
    @property
    def id(self):
        return self._id;
    
    # name getter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        
        if value is None:
            raise ValueError("Name can't be empty");
        
        self._name = value;
        
    # description getter and setter
    @property
    def description(self):
        return self._name;
    
    @description.setter
    def set_description(self, value: str):
        
        if value is None:
            raise ValueError("Description can't be empty");
        
        self._description = value;
        
    # access level getter and setter
    @property
    def accessLevel(self):
        return self._name;
    
    @accessLevel.setter
    def set_accessLevel(self, access_list: List[str]):
        
        if access_list is None:
            raise ValueError("Access level can't be empty");
        
        if len(access_list) != len(set(access_list)):
            raise ValueError("The level access can't be duplicated");
        
        self._accessLevels = access_list;
        
    @property
    def isActive(self):
        return self._isActive;
    
    @isActive.setter
    def set_isActive(self, value: bool):
        
        if value is None:
            raise ValueError("This atribute can't be empty");
        
        self._isActive = value;