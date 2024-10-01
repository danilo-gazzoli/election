import unittest;
from unittest.mock import MagicMock;
from src.core.entities.political_party import PoliticalParty;
from src.core.interfaces.repositories.election_repository import IElectionRepository;
from src.application.use_cases.political_party.create_political_party import CreatePoliticalParty;