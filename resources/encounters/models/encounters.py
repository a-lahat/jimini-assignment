from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any, Literal


EncounterType = Literal[
    "initial_assessment",
    "follow_up",
    "treatment_session"
]


class EncounterCreate(BaseModel):
    patientId: int
    providerId: int
    encounterDate: datetime
    encounterType: EncounterType
    clinicalData: Dict[str, Any]


class Encounter(BaseModel):
    id: int
    patientId: int
    providerId: int
    encounterDate: datetime
    encounterType: EncounterType
    clinicalData: Dict[str, Any]
    metadata: Dict[str, Any]

    @classmethod
    def create(cls, data: EncounterCreate, user_id: int) -> 'Encounter':
        now = datetime.utcnow()
        return Encounter(
            patientId=data.patientId,
            providerId=data.providerId,
            encounterDate=data.encounterDate,
            encounterType=data.encounterType,
            clinicalData=data.clinicalData,
            metadata={
                "created_at": now,
                "updated_at": now,
                "created_by": user_id,
            },
        )
