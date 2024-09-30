from core.interfaces.repositories.political_party_repository import IPoliticalPartyRepository;
from core.entities.political_party import PoliticalParty;

class CreateUser:
    def __init__(self, PoliticalPartyRepository: IPoliticalPartyRepository):
        self._political_party_repository = PoliticalPartyRepository;
        
    def execute(self, political_party_data: dict) -> None:
        political_party = PoliticalParty(
            name = political_party_data['name'],
            partyPicture = political_party_data['partyPicture'],
            candidateList = political_party_data['candidateList']
        )

        self._political_party_repository.CreateUser(political_party);