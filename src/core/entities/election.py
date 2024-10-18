from dataclasses import dataclass;
from user import User;
from political_party import PoliticalParty;
from candidate import Candidate;
from typing import List;

@dataclass
class Election:
    _id: int;
    _name: str;
    _noneVotes: int;
    _usersRegistered: List['User'];
    _mayorsCandidates: List['Candidate'];
    _councilorsCandidates: List['Candidate'];
    _politicalPartys: List['PoliticalParty'];
        
    # election id getter
    @property
    def Id(self):
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
        
    # election none votes 
    @property
    def noneVotes(self):
        return self._noneVotes;
    
    @noneVotes.setter
    def set_none_votes(self, value: int):
        self._noneVotes = value;
    
    # election users gatter and setter
    @property
    def usersRegistered(self):
        return self._usersRegistered;
    
    @usersRegistered.setter
    def set_users_registered(self, list_users: List['User']):
        
        if not all(isinstance(user, User) for user in list_users):
            raise ValueError("All items must be instances of user");
        
        self._usersRegistered = list_users;
    
    
    
    # election political partys gatter and setter
    @property
    def politicalPartys(self):
        return self._politicalPartys;
    
    @politicalPartys.setter
    def set_political_partys(self, political_partys: List['PoliticalParty']):
        
        if not all(isinstance(politicalParty, PoliticalParty) for politicalParty in political_partys):
            raise ValueError("All items must be instances of PoliticalParty");
        
        self._politicalPartys = political_partys;
    
    # election councilors gatter and setter
    @property
    def councilors(self) -> List['Candidate']:
        return self._politicalCandidates;
    
    @councilors.setter
    def set_councilors(self, candidates: List['Candidate']):
        
        if not all(isinstance(candidate, Candidate) for candidate in candidates):
            raise ValueError("All items must be instances of Candidate");
        
        self._councilorsCandidates = candidates;
        
    # election mayors gatter and setter
    @property
    def mayors(self) -> List['Candidate']:
        return self._politicalCandidates;
    
    @mayors.setter
    def set_mayors(self, candidates: List['Candidate']):
        
        if not all(isinstance(candidate, Candidate) for candidate in candidates):
            raise ValueError("All items must be instances of Candidate");
        
        self._mayorsCandidates = candidates;