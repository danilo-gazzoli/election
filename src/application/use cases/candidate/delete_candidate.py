from src.core.entities.candidate import Candidate;
from src.core.interfaces.repositories.candidate_repository import ICandidateRepository;

class DeleteCandidate:
    def __init__(self, candidate_repository: ICandidateRepository, current_user):
        self._candidate_repository = candidate_repository;
        self._current_user = current_user;

    def execute(self, candidate_id: int) -> None:
        self.verify_user_permissions(self._current_user);

        candidate = self.verify_candidate_exists(candidate_id);

        self.verify_candidate_status(candidate);

        self._candidate_repository.DeleteCandidate(candidate_id);

    def verify_user_permissions(self, user) -> None:
        if not user.is_admin():
            raise PermissionError("User does not have permission to delete a candidate.");
    
    def verify_candidate_exists(self, candidate_id: int) -> Candidate:
        candidate = self._candidate_repository.GetCandidateById(candidate_id);
        if not candidate:
            raise ValueError(f"Candidate with ID {candidate_id} does not exist.");
        return candidate

    def verify_candidate_status(self, candidate: Candidate) -> None:
        if candidate.is_in_election_process():
            raise ValueError("Cannot delete a candidate who is currently participating in an election process.");