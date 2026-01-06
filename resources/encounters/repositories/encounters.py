from resources.encounters.models.encounters import Encounter


class EncounterRepository:
    _db = {}

    @classmethod
    def get_encounter_by_encounter_id(cls, encounter_id: int):
        return cls._db.get(encounter_id)

    @classmethod
    def create(cls, encounter: Encounter):
        # would actually save to a real DB here and then return the new record with unique id
        cls._db[str(encounter.id)] = encounter
