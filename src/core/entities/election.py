from core.entities.data_classes import DataElection;

class Election:
    def __init__(self, election_data: DataElection):
        self.id = election_data.id;
        self.name = election_data.name;
        self.politicalPosition = election_data.politicalPosition;
        self.politicalPartys = election_data.politicalPartys;
        self.politicalCandidates = election_data.politicalCandidates;
        self.voters = election_data.voters;