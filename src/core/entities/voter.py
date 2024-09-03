from core.entities.data_classes import VoterData, VoteData
from dataclasses import dataclass;

class Voter:
    def __init__(self, voter_data: VoterData, vote_data: VoteData):
        self.cardNumber = voter_data.cardNumber;
        self.name = voter_data.name;
        self.voteNumber = vote_data.voteNumber;
        self.votePermission = vote_data.votePermission;
        self.votePosition = vote_data.votePosition;
        self.voteType = vote_data.voteType;