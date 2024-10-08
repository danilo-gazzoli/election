import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from src.core.entities.candidate import Candidate;
from src.core.interfaces.repositories.candidate_repository import ICandidateRepository;


class GetCandidate:
    def __init__(self, candidate_repository: ICandidateRepository):
        self._candidate_repository = candidate_repository;

    def execute(self, candidate_id: int) -> Candidate:
        candidate = self._candidate_repository.GetCandidateById(candidate_id);
        if not candidate:
            raise ValueError(f"Candidate with ID {candidate_id} does not exist.");
        return candidate;
