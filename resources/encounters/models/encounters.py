from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any, Literal
from resources.user.models.user import User


EncounterType = Literal[
    "initial_assessment",
    "follow_up",
    "treatment_session"
]


class EncounterCreate(BaseModel):
    patient_id: int
    provider_id: int
    encounter_date: datetime
    encounter_type: EncounterType
    data: Dict[str, Any]


class Encounter(BaseModel):
    id: int
    patient_id: int
    provider_id: int
    encounter_date: datetime
    encounter_type: EncounterType
    data: Dict[str, Any]
    metadata: Dict[str, Any]

    @classmethod
    def create(cls, encounter_create_data: EncounterCreate, user: User) -> 'Encounter':
        now = datetime.utcnow()
        return Encounter(
            patientId=encounter_create_data.patient_id,
            providerId=encounter_create_data.provider_id,
            encounterDate=encounter_create_data.encounter_date,
            encounterType=encounter_create_data.encounter_type,
            clinicalData=encounter_create_data.data,
            metadata={
                "created_at": now,
                "updated_at": now,
                "created_by": user.id,
            },
        )
