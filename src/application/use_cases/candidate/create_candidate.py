import sys;
import os;

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'));
sys.path.append(src_path);

from PIL import Image
from core.interfaces.repositories.candidate_repository import ICandidateRepository;
from core.entities.candidate import Candidate;
from core.entities.political_party import PoliticalParty;

class CreateCandidate:
    def __init__(self, CandidateRepository: ICandidateRepository):
        self._candidate_repository = CandidateRepository;  
    
    def execute(self, candidate_data: dict) -> None:
        self.verify_required_fields(candidate_data);
        self.verify_using_name_and_number(candidate_data);
        self.verify_amount_votes_value(candidate_data);
        self.verify_strings_length(candidate_data);
        self.verify_image_type(candidate_data);
        self.verify_object_types(candidate_data);
        
        candidate = Candidate(
            name = candidate_data['name'],
            cardNumber = candidate_data['cardNumber'],
            candidateNumber = candidate_data['candidateNumber'],
            politicalParty = candidate_data['politicalParty'],
            amountVotes= candidate_data['amountVotes'],
            profilePicture = candidate_data['profilePicture']
        );

        self._candidate_repository.CreateCandidate(candidate);
        
    def verify_using_name_and_number(self, candidate_data: dict):
        existing_candidates = self._candidate_repository.GetAllCandidate();
        
        for Candidate in existing_candidates:
            
            if Candidate.candidateNumber() == candidate_data['candidateNumber']:
                raise ValueError("This number was used by another candidate.");
            
            if Candidate.name() == candidate_data['name']:
                raise ValueError("This name was used by another candidate.");
            
            if Candidate.candidateNumber() == candidate_data['candidateNumber']:
                raise ValueError("This candidate number was used by another candidate.");
        
    def verify_required_fields(candidate_data: dict) -> None:
        required_fields = ['name', 'cardNumber', 'candidateNumber', 'politicalParty', 'politicalPosition', 'amountVotes', 'profilePicture'];
        
        for field in required_fields:
            if field not in candidate_data or not candidate_data[field]:
                raise ValueError(f"The {field} data can't be empty.");  
            
    def verify_amount_votes_value(candidate_data: dict):

        if candidate_data['amountVotes'] > 0:
            raise ValueError("The value of amount votes need be start in 0.");
        
    def verify_strings_length(candidate_data: dict):
        
        if len(candidate_data['name']) > 60:
            raise ValueError("This candidate name is too long.");
        
        if len(candidate_data['politicalParty']) > 100:
            raise ValueError("This political party name is too long.");
        
        if len(candidate_data['politicalPosition']) > 50:
            raise ValueError("This political party name is too long.");
        
    def verify_image_type(candidate_data: dict):
        
        if isinstance(candidate_data['profilePicture'], Image):
                raise ValueError("This perm isn't a image object");
        
    def verify_object_types(candidate_data: dict):
        
        new_adm_political_partys = candidate_data['politicalParty'];
        new_adm_political_positions = candidate_data['politicalPosition'];
        
        for political_party in new_adm_political_partys:
            if not isinstance(political_party, PoliticalParty):
                raise ValueError("This perm isn't a political party object");
        