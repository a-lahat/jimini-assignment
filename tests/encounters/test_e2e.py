import pytest
from fastapi.testclient import TestClient
from server import app


@pytest.fixture
def client():
    """
    Returns a TestClient instance to make requests against the FastAPI app.
    """
    with TestClient(app) as c:
        yield c


@pytest.mark.parametrize(
    "payload, expected_error_field",
    [
        (
                {
                    "patient_id": 1,
                    "encounter_date": "2024-01-01T10:00:00Z",
                    "encounter_type": "initial_assessment",
                    "data": {"notes": "secret"},
                },
                "provider_id",
        )
    ],
)
def test_create_encounter_validation_errors(
        client,
        payload,
        expected_error_field,
):
    response = client.post(
        "/encounters/",
        headers={"X-User-Id": "123"},
        json=payload,
    )

    assert response.status_code == 422

    body = response.json()

    # Validation error references the correct field
    assert any(
        expected_error_field in error["loc"]
        for error in body["detail"]
    )

    # PHI must not leak
    assert "patient_id" not in str(body)
    assert "secret" not in str(body)
