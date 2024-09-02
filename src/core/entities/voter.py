from dataclasses import dataclass;

class VoterData:
    name: str;
    cardNumber: int;

class VoteData:
    voteNumber: int;
    votePermission: bool;

class Voter:
    def __init__(self, voter_data: VoterData, vote_data: VoteData):
        self.cardNumber = voter_data.cardNumber;
        self.name = voter_data.name;
        self.voteNumber = vote_data.voteNumber;
        self.votePermission = vote_data.votePermission;