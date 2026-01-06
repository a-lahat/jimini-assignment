from resources.encounters.models.encounters import EncounterCreate
from resources.encounters.models.encounters import Encounter
from resources.encounters.repositories.encounters import EncounterRepository
from resources.user.models.user import User


class EncounterController:
    def create_encounter(self, data: EncounterCreate, user: User) -> Encounter:
        encounter = Encounter.create(data, user)
        EncounterRepository.create(encounter)
        # TODO add audit
        return encounter

    def get_encounter(self, encounter_id: int, user: User) -> Encounter:
        encounter = EncounterRepository.get_encounter_by_encounter_id(encounter_id)
        # TODO add audit
        return encounter


encounter_controller = EncounterController()
