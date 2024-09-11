from core.entities.data_classes import DataPoliticalParty;
from core.entities.candidate import Candidate;
from core.entities.election import Election;
from typing import List;
from PIL import Image;

class PoliticalParty:
    def __init__(self, politicalParty_data: DataPoliticalParty):
        self._id = politicalParty_data.id;
        self._name = politicalParty_data.name;
        self._partyPicture = politicalParty_data.partyPicture;
        self._candidateList: List[Candidate] = politicalParty_data.candidateList;
        
    # id getter
    @property
    def id(self) -> int:
        return self._id;
    
    # political party name getter and setter
    @property
    def name(self) -> str:
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        
        if value is None:
            raise ValueError("Name can't be empty");
        
        self._name = value
        
    # political party picture getter and setter
    @property
    def picture(self) -> Image:
        return self._partyPicture;
    
    @picture.setter
    def set_picture(self, value: Image, election: Election):
        
        if value is None:
            raise ValueError("The picture can't be empty");
        
        for politicalParty in election.politicalPartys:
            if value == PoliticalParty.picture():
                raise ValueError(f"The {value} must be used bt another political party");
            
        self._partyPicture = value;
    
    # political party candidate list getter and setter    
    @property
    def candidatesList(self) -> List[Candidate]:
        return self._candidateList;
    
    def set_candidate_list(self, candidates: List[Candidate]):
        
        if not all(isinstance(candidate, Candidate) for candidate in candidates):
            raise ValueError("All candidates must be instances of Candidate");
        
        self._candidateList = candidates;