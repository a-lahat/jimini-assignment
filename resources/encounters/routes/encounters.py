from fastapi import APIRouter
from resources.encounters.models.encounters import EncounterCreate
from resources.encounters.models.encounters import Encounter
from resources.encounters.controllers.encounters import encounter_controller

router = APIRouter(prefix="/encounters")


@router.get("/{encounter_id}", response_model=Encounter)
def get_encounter(encounter_id: int, user_id: int):
    encounter = encounter_controller.get_encounter(encounter_id, user_id)
    return encounter


@router.post("/")
def create_encounter(encounter_data: EncounterCreate, user_id: int):
    encounter = encounter_controller.create_encounter(encounter_data, user_id)
    return encounter.id
