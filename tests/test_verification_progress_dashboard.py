import pytest

from factory.verification_progress_dashboard import validate_preparation_status


def valid_status():
    return {
        "version": 1,
        "state": "NOT_VERIFIED",
        "promotion_eligible": 0,
        "queue_total": 1000,
        "queued_records": 800,
        "prepared_review_records": 600,
        "reviewed_records": 120,
        "verified_records": 20,
        "packet_qc_checked_items": 600,
        "queue_qc_error_count": 0,
        "registry_qc_error_count": 0,
        "promotion_qc_error_count": 0,
        "prepared_percent": 60.0,
        "verified_percent_of_queue": 2.0,
    }


def test_valid_preparation_status_returns_prepared_count():
    assert validate_preparation_status(valid_status(), 1000) == 600


@pytest.mark.parametrize(
    "field,value,error",
    [
        ("state", "VERIFIED", "PREPARATION_STATUS_STATE_MUST_REMAIN_NOT_VERIFIED"),
        ("promotion_eligible", 1, "PREPARATION_STATUS_PROMOTION_ELIGIBLE_MUST_BE_ZERO"),
        ("queue_total", True, "PREPARATION_STATUS_INVALID_QUEUE_TOTAL"),
        ("prepared_review_records", -1, "PREPARATION_STATUS_INVALID_PREPARED_REVIEW_RECORDS"),
    ],
)
def test_status_rejects_unsafe_control_values(field, value, error):
    data = valid_status()
    data[field] = value
    with pytest.raises(SystemExit, match=error):
        validate_preparation_status(data, 1000)


def test_status_rejects_prepared_above_queue():
    data = valid_status()
    data["prepared_review_records"] = 801
    data["prepared_percent"] = 80.1
    with pytest.raises(SystemExit, match="PREPARATION_STATUS_QUEUE_INVARIANT_FAILED"):
        validate_preparation_status(data, 1000)


def test_status_rejects_reviewed_above_prepared():
    data = valid_status()
    data["reviewed_records"] = 601
    with pytest.raises(SystemExit, match="PREPARATION_STATUS_REVIEW_INVARIANT_FAILED"):
        validate_preparation_status(data, 1000)


def test_status_rejects_percent_mismatch():
    data = valid_status()
    data["prepared_percent"] = 59.999
    with pytest.raises(SystemExit, match="PREPARATION_STATUS_PREPARED_PERCENT_MISMATCH"):
        validate_preparation_status(data, 1000)


def test_status_rejects_verified_percent_mismatch():
    data = valid_status()
    data["verified_percent_of_queue"] = 99.0
    with pytest.raises(SystemExit, match="PREPARATION_STATUS_VERIFIED_PERCENT_MISMATCH"):
        validate_preparation_status(data, 1000)
