import json

from fastapi.testclient import TestClient

from application_process_coding_task.main import api

client = TestClient(api)


def test_get_orderbook_returns_quote_events() -> None:
    response = client.get(
        "/orderbook",
        params={"ric": "SETU26", "date": "2026-09-04", "type": "json"},
    )

    assert response.status_code == 200
    records = [json.loads(line) for line in response.text.splitlines()]
    assert records
    assert records[0]["ric"] == "SETU26"
    assert records[0]["event_type"] == "Quote"


def test_get_orderbook_excludes_empty_quote_events() -> None:
    response = client.get(
        "/orderbook",
        params={"ric": "SETU26", "date": "2026-09-04", "type": "json"},
    )

    assert response.status_code == 200
    records = [json.loads(line) for line in response.text.splitlines()]
    assert records
    assert all(
        record["bid_price"] is not None or record["ask_price"] is not None for record in records
    )


def test_post_orderbook_filters_multiple_rics() -> None:
    response = client.post(
        "/orderbook",
        json={
            "date": "2026-09-04",
            "type": "json",
            "rics": ["SETU26", "SETZ26"],
        },
    )

    assert response.status_code == 200
    records = [json.loads(line) for line in response.text.splitlines()]
    assert {record["ric"] for record in records} == {"SETU26", "SETZ26"}
