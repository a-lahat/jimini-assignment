from fastapi import APIRouter
from fastapi import Depends
from resources.encounters.models.encounters import EncounterCreate
from resources.encounters.models.encounters import Encounter
from resources.encounters.controllers.encounters import encounter_controller
from resources.auth.common import get_current_user
from resources.user.models.user import User

router = APIRouter(prefix="/encounters")


@router.get("/{encounter_id}", response_model=Encounter)
def get_encounter(encounter_id: int, user: User = Depends(get_current_user)):
    encounter = encounter_controller.get_encounter(encounter_id, user)
    return encounter


@router.post("/")
def create_encounter(encounter_data: EncounterCreate, user: User = Depends(get_current_user)):
    encounter = encounter_controller.create_encounter(encounter_data, user)
    return encounter.id
