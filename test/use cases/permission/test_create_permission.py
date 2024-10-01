import unittest;
from unittest.mock import MagicMock;
from src.core.entities.permission import Permission;
from src.core.interfaces.repositories.permission_repository import IPermissionRepository;
from src.application.use_cases.permission.create_permission import CreatePermission;