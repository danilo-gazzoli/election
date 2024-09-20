from dataclasses import dataclass;

@dataclass
class Voter:
    _name: str;
    _cardNumber: int;
    _voteNumber: int;
    _voteNull: int;
    _voteNone: int;
    _votePosition: str;
    _votePermission: bool;
    
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