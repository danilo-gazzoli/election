import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from src.core.entities.election import Election;
from src.core.interfaces.repositories.election_repository import IElectionRepository;

class GetElection:
    def __init__(self, election_repository: IElectionRepository):
        self._election_repository = election_repository;

    def execute(self, election_id: int) -> Election:
        election = self._election_repository.GetElectionById(election_id);
        if not election:
            raise ValueError(f"Election with ID {election_id} does not exist.");
        return election;