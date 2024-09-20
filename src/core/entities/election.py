from dataclasses import dataclass;
from political_position import PoliticalPosition;
from political_party import PoliticalParty;
from candidate import Candidate;
from voter import Voter;
from typing import List;

@dataclass
class Election:
    _id: int;
    _name: str;
    _politicalPositions: List['PoliticalPosition'];
    _politicalCandidates: List['Candidate'];
    _politicalPartys: List['PoliticalParty'];
    _voters: List['Voter'];
        
    # election id getter
    @property
    def id(self):
        return self._id;
    
    # election name gatter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        
        if value is None:
            raise ValueError("The name can't be empty");
        
        self._name = value;
    
    # election political positions gatter and setter
    @property
    def politicalPositions(self):
        return self._politicalPositions;
    
    @politicalPositions.setter
    def set_political_positions(self, political_positions: List['PoliticalPosition']):
        
        if not all(isinstance(politicalPosition, PoliticalPosition) for politicalPosition in political_positions):
            raise ValueError("All items must be instances of PoliticalPosition");
        
        self._politicalPositions = political_positions;
    
    # election political partys gatter and setter
    @property
    def politicalPartys(self):
        return self._politicalPartys;
    
    @politicalPartys.setter
    def set_political_partys(self, political_partys: List['PoliticalParty']):
        
        if not all(isinstance(politicalParty, PoliticalParty) for politicalParty in political_partys):
            raise ValueError("All items must be instances of PoliticalParty");
        
        self._politicalPartys = political_partys;
    
    # election candidates gatter and setter
    @property
    def candidates(self) -> List['Candidate']:
        return self._politicalCandidates;
    
    @candidates.setter
    def set_candidates(self, political_candidates: List['Candidate']):
        
        if not all(isinstance(candidate, Candidate) for candidate in political_candidates):
            raise ValueError("All items must be instances of Candidate");
        
        self._politicalCandidates = political_candidates;
    
    # election voters gatter and setter
    @property
    def voters(self):
        return self._voters;
    
    @voters.setter
    def set_voters(self, political_voters: List['Voter']):
        
        if not all(isinstance(voter, Voter) for voter in political_voters):
            raise ValueError("All items must be instances of Voter");
        
        self._voters = political_voters;