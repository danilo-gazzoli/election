import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from src.core.entities.political_party import PoliticalParty
from src.core.interfaces.repositories.political_party_repository import IPoliticalPartyRepository

class GetPoliticalParty:
    def __init__(self, political_party_repository: IPoliticalPartyRepository):
        self._political_party_repository = political_party_repository;

    def execute(self, party_id: int) -> PoliticalParty:
        political_party = self._political_party_repository.GetPoliticalPartyById(party_id);
        if not political_party:
            raise ValueError(f"Political Party with ID {party_id} does not exist.");
        return political_party;