from PIL import Image
from core.interfaces.repositories.political_party_repository import IPoliticalPartyRepository;
from core.entities.political_party import PoliticalParty
from src.core.entities.candidate import Candidate;

class CreatePoliticalParty:
    def __init__(self, PoliticalPartyRepository: IPoliticalPartyRepository):
        self._political_party_repository = PoliticalPartyRepository;
        
    def execute(self, political_party_data: dict) -> None:
        self.verify_required_fields(political_party_data);
        self.verify_strings_length(political_party_data);
        self.verify_image_type(political_party_data);
        self.verify_object_types(political_party_data);
        
        political_party = PoliticalParty(
            name = political_party_data['name'],
            partyPicture = political_party_data['partyPicture'],
            candidateList = political_party_data['candidateList']
        );

        self._political_party_repository.CreatePoliticalParty(political_party);
        
    def verify_required_fields(political_party_data: dict) -> None:
        required_fields = ['name', 'partyPicture', 'candidateList'];
        
        for field in required_fields:
            if field not in political_party_data or not political_party_data[field]:
                raise ValueError(f"The {field} data can't be empty"); 
            
    def verify_strings_length(political_party_data: dict):
        
        if len(political_party_data['name']) > 100:
            raise ValueError("This candidate name is too long.");
    
    def verify_image_type(political_party_data: dict):
        
        if isinstance(political_party_data['partyPicture'], Image):
                raise ValueError("This perm isn't a image object");
            
    def verify_object_types(political_party_data: dict):
        
        new_adm_political_candidates = political_party_data['usersRegistered'];
        
        for candidate in new_adm_political_candidates:
            if not isinstance(candidate, Candidate):
                raise ValueError("This perm isn't a candidate object");