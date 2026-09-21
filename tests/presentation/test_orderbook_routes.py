from fastapi.testclient import TestClient

from application_process_coding_task.main import api

client = TestClient(api)


def test_get_orderbook_returns_quote_events() -> None:
    response = client.get(
        "/orderbook",
        params={"ric": "SETU26", "date": "2026-09-04", "type": "json"},
    )

    assert response.status_code == 200
    records = response.json()
    assert records
    assert records[0]["#RIC"] == "SETU26"
    assert records[0]["Type"] == "Quote"


def test_get_orderbook_excludes_empty_quote_events() -> None:
    response = client.get(
        "/orderbook",
        params={"date": "2026-09-04", "type": "json"},
    )

    assert response.status_code == 200
    records = response.json()
    assert records
    assert all(
        record["Bid Price"] is not None or record["Ask Price"] is not None for record in records
    )


def test_post_orderbook_filters_multiple_rics() -> None:
    response = client.post(
        "/orderbook",
        params={"date": "2026-09-04", "type": "json"},
        json={"rics": ["SETU26", "SETZ26"]},
    )

    assert response.status_code == 200
    assert {record["#RIC"] for record in response.json()} == {"SETU26", "SETZ26"}
