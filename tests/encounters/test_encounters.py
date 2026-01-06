from datetime import datetime

from resources.encounters.controllers.encounters import encounter_controller
from resources.encounters.models.encounters import EncounterCreate
from resources.user.models.user import User


def test_create_and_get_encounter_data_matches():
    user = User(id=1, name="My User", is_admin=True)
    data = EncounterCreate(
        patient_id=123,
        provider_id=456,
        encounter_date=datetime(2026, 1, 6, 12, 0),
        encounter_type="initial_assessment",
        data={"notes": "Test notes"},
    )

    # Create encounter
    created = encounter_controller.create_encounter(data, user)

    # Retrieve encounter
    retrieved = encounter_controller.get_encounter(created.id, user)

    # Compare input data vs retrieved
    assert retrieved.patient_id == data.patient_id
    assert retrieved.provider_id == data.provider_id
    assert retrieved.encounter_date == data.encounter_date
    assert retrieved.encounter_type == data.encounter_type
    assert retrieved.data == data.data
