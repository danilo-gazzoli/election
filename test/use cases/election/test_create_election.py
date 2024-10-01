import unittest;
from unittest.mock import MagicMock;
from src.core.entities.election import Election;
from src.core.interfaces.repositories.election_repository import IElectionRepository;
from src.application.use_cases.election.create_election import CreateElection;