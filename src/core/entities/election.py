from core.entities.political_position import PoliticalPosition;
from core.entities.political_party import PoliticalParty;
from core.entities.data_classes import DataElection;
from core.entities.candidate import Candidate;
from core.entities.voter import Voter;
from typing import List;

class Election:
    def __init__(self, election_data: DataElection):
        self._id = election_data.id;
        self._name = election_data.name;
        self._politicalPositions: List[PoliticalPosition] = election_data.politicalPositions;
        self._politicalPartys: List[PoliticalParty] = election_data.politicalPartys;
        self._politicalCandidates: List[Candidate] = election_data.politicalCandidates;
        self._voters: List[Voter] = election_data.voters;
        
        # election id getter
        @property
        def ElectionID(self):
            return self._id;
        
        # election name gatter and setter
        @property
        def ElectionName(self):
            return self._name;
        
        @ElectionName.setter
        def set_election_name(self, value: str):
            
            if value is None:
                raise ValueError("The name can't be empty");
            
            self._name = value;
        
        # election political positions gatter and setter
        @property
        def ElectionPoliticalPositions(self):
            return self._politicalPositions;
        
        @ElectionPoliticalPositions.setter
        def set_political_positions(self, political_positions: List[PoliticalPosition]):
            
            if not all(isinstance(politicalPosition, PoliticalPosition) for politicalPosition in political_positions):
                raise ValueError("All items must be instances of PoliticalPosition");
            
            self._politicalPositions = political_positions;
        
        # election political partys gatter and setter
        @property
        def ElectionPoliticalPartys(self):
            return self._politicalPartys;
        
        @ElectionPoliticalPartys.setter
        def set_political_partys(self, political_partys: List[PoliticalParty]):
            
            if not all(isinstance(politicalParty, PoliticalParty) for politicalParty in political_partys):
                raise ValueError("All items must be instances of PoliticalParty");
            
            self._politicalPartys = political_partys;
        
        # election candidates gatter and setter
        @property
        def ElectionCandidates(self):
            return self._politicalCandidates;
        
        @ElectionCandidates.setter
        def set_political_candidates(self, political_candidates: List[Candidate]):
            
            if not all(isinstance(candidate, Candidate) for candidate in political_candidates):
                raise ValueError("All items must be instances of Candidate");
            
            self._politicalCandidates = political_candidates;
        
        # election voters gatter and setter
        @property
        def ElectionVoters(self):
            return self._voters;
        
        @ElectionVoters.setter
        def set_voters(self, political_voters: List[Voter]):
            
            if not all(isinstance(voter, Voter) for voter in political_voters):
                raise ValueError("All items must be instances of Voter");
            
            self._voters = political_voters;