import unittest;
from unittest.mock import MagicMock;
from src.core.entities.political_position import PoliticalPosition;
from src.core.interfaces.repositories.political_position_repository import IPoliticalPositionRepository;
from src.application.use_cases.political_position.create_political_position import CreatePoliticalPosition;