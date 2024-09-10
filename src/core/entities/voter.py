from core.entities.data_classes import DataVoter, DataVote
from dataclasses import dataclass;

class Voter:
    def __init__(self, voter_data: DataVoter, vote_data: DataVote):
        self._cardNumber = voter_data.cardNumber;
        self._name = voter_data.name;
        self._voteNumber = vote_data.voteNumber;
        self._votePermission = vote_data.votePermission;
        self._votePosition = vote_data.votePosition;
        self._voteNone = vote_data.voteNone;
        self._voteNull = vote_data.voteNull;
        
    # Voter card number getter and setter
    @property
    def VoterCardNumber(self):
        return self._cardNumber;
    
    @VoterCardNumber.setter
    def set_card_number(self, value: int):
        self._cardNumber = value;
        
    # voter name getter and setter
    @property
    def VoterName(self):
        return self._name;
    
    @VoterName.setter
    def set_name(self, value: str):
        self._name = value;
        
    # vote number getter and setter
    @property
    def VoterVoteNumber(self):
        return self._voteNumber
    
    @VoterVoteNumber.setter
    def set_vote_number(self, value: int):
        self._voteNumber = value;
        
    # vote permission getter and setter
    @property
    def VoterVotePermission(self):
        return self._votePermission
    
    @VoterVotePermission.setter
    def set_vote_permission(self, value: bool):
        self._votePermission = value;
        
    # vote position getter and setter
    @property
    def VoterVotePosition(self):
        return self._voteNumber
    
    @VoterVotePosition.setter
    def set_vote_position(self, value: str):
        self._votePosition = value;
    