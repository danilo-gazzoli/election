import unittest;
from unittest.mock import MagicMock;
from src.core.entities.candidate import Candidate;
from src.core.interfaces.repositories.candidate_repository import ICandidateRepository;
from src.application.use_cases.candidate.create_candidate import CreateCandidate;