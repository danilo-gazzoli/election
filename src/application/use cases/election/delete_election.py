from src.core.interfaces.repositories.election_repository import IElectionRepository

class DeleteElection:
    def __init__(self, election_repository: IElectionRepository, current_user):
        self._election_repository = election_repository;
        self._current_user = current_user;

    def execute(self, election_id: int) -> None:
        self.verify_user_permissions(self._current_user)
        
        election = self._election_repository.GetElectionById(election_id);
        
        if not election:
            raise ValueError(f"Election with ID {election_id} does not exist.");
        
        self.verify_election_status(election);
        self._election_repository.DeleteElection(election_id);

    def verify_user_permissions(self, user):
        if not user.is_admin():
            raise PermissionError("User does not have permission to delete an election.");

    def verify_election_status(self, election):
        if election.is_active():
            raise ValueError("Cannot delete an active election.");