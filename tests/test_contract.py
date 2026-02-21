from src.project_profile import CORE_CAPABILITIES, PROJECT_NAME, PROJECT_SUMMARY
from src.service_contract import build_status, status_payload


def test_project_profile_populated():
    assert PROJECT_NAME
    assert PROJECT_SUMMARY
    assert len(CORE_CAPABILITIES) == 4


def test_status_payload_shape():
    status = build_status(PROJECT_NAME)
    payload = status_payload(status)
    assert payload["name"] == PROJECT_NAME
    assert payload["healthy"] is True
    assert "timestamp" in payload
