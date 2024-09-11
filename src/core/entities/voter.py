from classes_data import DataVoter, DataVote;

class Voter:
    def __init__(self, voter_data: 'DataVoter', vote_data: 'DataVote'):
        self._cardNumber = voter_data.cardNumber;
        self._name = voter_data.name;
        self._voteNumber = vote_data.voteNumber;
        self._votePermission = vote_data.votePermission;
        self._votePosition = vote_data.votePosition;
        self._voteNone = vote_data.voteNone;
        self._voteNull = vote_data.voteNull;
        
    # Voter card number getter and setter
    @property
    def cardNumber(self):
        return self._cardNumber;
    
    @cardNumber.setter
    def set_card_number(self, value: int):
        self._cardNumber = value;
        
    # voter name getter and setter
    @property
    def name(self):
        return self._name;
    
    @name.setter
    def set_name(self, value: str):
        self._name = value;
        
    # vote number getter and setter
    @property
    def voteNumber(self):
        return self._voteNumber
    
    @voteNumber.setter
    def set_vote_number(self, value):
        self._voteNumber = value;
        
    # vote permission getter and setter
    @property
    def votePermission(self):
        return self._votePermission
    
    @votePermission.setter
    def set_vote_permission(self, value: bool):
        self._votePermission = value;
        
    # vote position getter and setter
    @property
    def votePosition(self):
        return self._voteNumber
    
    @votePosition.setter
    def set_vote_position(self, value: str):
        self._votePosition = value;
    
    # vote none getter and setter
    @property
    def voteNone(self):
        return self._voteNone;
    
    @voteNone.setter
    def set_voteNone(self, value):
        self._voteNone = value;
    
    # vote null getter and setter
    @property
    def voteNull(self):
        return self._voteNone;
    
    @voteNull.setter
    def set_voteNull(self, value):
        self._voteNull = value;