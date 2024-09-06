from core.entities.data_classes import DataPoliticalPosition;
from core.entities.candidate import Candidate;
from typing import List;
class PoliticalPosition:
    def __init__(self, politicalPosition_data: DataPoliticalPosition):
        self.id = politicalPosition_data.id;
        self.name = politicalPosition_data.name;
        self.candidatesCompeting: List[Candidate] = politicalPosition_data.candidatesCompeting;