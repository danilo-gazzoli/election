import unittest;
from unittest.mock import MagicMock;
from src.core.entities.adm import Adm;
from src.core.interfaces.repositories.adm_repository import IAdmRepository;
from src.application.use_cases.adm.create_adm import CreateAdm;