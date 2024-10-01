import unittest;
from unittest.mock import MagicMock;
from src.core.entities.user import User;
from src.core.interfaces.repositories.user_repository import IUserRepository;
from src.application.use_cases.user.create_user import CreateUser;