from core.entities.data_classes import DataPoliticalParty;
from core.entities.candidate import Candidate;
from typing import List;

class PoliticalParty:
    def __init__(self, politicalParty_data: DataPoliticalParty):
        self.id = politicalParty_data.id;
        self.name = politicalParty_data.name;
        self.partyPicture = politicalParty_data.partyPicture;
        self.candidateList: List[Candidate] = politicalParty_data.candidateList;