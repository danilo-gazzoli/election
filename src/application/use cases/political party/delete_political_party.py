from src.core.interfaces.repositories.political_party_repository import IPoliticalPartyRepository;

class DeletePoliticalParty:
    def __init__(self, party_repository: IPoliticalPartyRepository, current_user):
        self._party_repository = party_repository
        self._current_user = current_user

    def execute(self, party_id: int) -> None:
        self.verify_user_permissions(self._current_user)
        political_party = self._party_repository.GetPoliticalPartyById(party_id);
        
        if not political_party:
            raise ValueError(f"Political Party with ID {party_id} does not exist.");
        
        self._party_repository.DeletePoliticalParty(party_id);

    def verify_user_permissions(self, user):
        if not user.is_admin():
            raise PermissionError("User does not have permission to delete a political party.");