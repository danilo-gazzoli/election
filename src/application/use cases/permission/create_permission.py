from core.interfaces.repositories.permission_repository import IPermissionRepository;
from core.entities.permission import Permission;

class CreatePermission:
    def __init__(self, PermissionRepository: IPermissionRepository):
        self._permission_repository = PermissionRepository;
        
    def execute(self, permission_data: dict) -> None:
        self.verify_required_fields(permission_data);
        self.verify_strings_length(permission_data);
        self.verify_bool_type(permission_data);
        
        permission = Permission(
            name = permission_data['name'],
            description = permission_data['description'],
            accessLevels = permission_data['accessLevels'],
            isActive = permission_data['isActive']
        );

        self._permission_repository.CreatePermission(permission);
        
    def verify_required_fields(permission_data: dict) -> None:
        required_fields = ['name', 'description', 'accessLevels', 'isActive'];
        
        for field in required_fields:
            if field not in permission_data or not permission_data[field]:
                raise ValueError(f"The {field} data can't be empty");
            
    def verify_strings_length(permission_data: dict):
        
        if len(permission_data['name']) > 45:
            raise ValueError("This permission name is too long.");
        
        if len(permission_data['description']) > 250:
            raise ValueError("This description is too long.");
        
    def verify_bool_type(permission_data: dict):
        
        if isinstance(permission_data['isActive'], bool):
                raise ValueError("This perm isn't a bool data");