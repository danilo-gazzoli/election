from core.interfaces.repositories.permission_repository import IPermissionRepository;
from core.entities.permission import Permission;

class CreateUser:
    def __init__(self, PermissionRepository: IPermissionRepository):
        self._permission_repository = PermissionRepository;
        
    def execute(self, permission_data: dict) -> None:
        self.verify_required_fields(permission_data);
        
        permission = Permission(
            name = permission_data['name'],
            description = permission_data['description'],
            accessLevels = permission_data['accessLevels'],
            isActive = permission_data['isActive']
        )

        self._permission_repository.CreateUser(permission);
        
    def verify_required_fields(self, permission_data: dict) -> None:
        required_fields = ['name', 'description', 'accessLevels', 'isActive'];
        
        for field in required_fields:
            if field not in permission_data or not permission_data[field]:
                raise ValueError(f"The {field} data can't be empty"); 