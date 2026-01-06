from resources.encounters.models.encounters import EncounterCreate
from resources.encounters.models.encounters import Encounter
from resources.encounters.repositories.encounters import EncounterRepository
from resources.user.models.user import User
from resources.audit.controllers.audit import audit_controller


class EncounterController:
    @classmethod
    def create_encounter(cls, data: EncounterCreate, user: User) -> Encounter:
        encounter = Encounter.create(data, user)
        EncounterRepository.create(encounter)
        audit_controller.create(user, "create_encounter", str(encounter.id))
        return encounter

    @classmethod
    def get_encounter(cls, encounter_id: int, user: User) -> Encounter:
        encounter = EncounterRepository.get_encounter_by_encounter_id(encounter_id)
        audit_controller.create(user, "get_encounter", str(encounter.id))
        return encounter


encounter_controller = EncounterController()
