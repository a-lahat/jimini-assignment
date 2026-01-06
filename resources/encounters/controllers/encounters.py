from resources.encounters.models.encounters import EncounterCreate
from resources.encounters.models.encounters import Encounter
from resources.encounters.repositories.encounters import EncounterRepository


class EncounterController:
    def create_encounter(self, data: EncounterCreate, user_id: int) -> Encounter:
        encounter = Encounter.create(data, user_id)
        EncounterRepository.create(encounter)
        # TODO add audit
        return encounter

    def get_encounter(self, encounter_id: int, user_id: int) -> Encounter:
        encounter = EncounterRepository.get_encounter_by_encounter_id(encounter_id)
        # TODO add audit
        return encounter


encounter_controller = EncounterController()
