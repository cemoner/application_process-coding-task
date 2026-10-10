import csv
import json
from io import StringIO

from fastapi.testclient import TestClient

from application_process_coding_task.main import api

client = TestClient(api)


def test_get_settlements_requires_ric() -> None:
    response = client.get("/eod", params={"date": "2026-09-04", "type": "json"})

    assert response.status_code == 422


def test_get_settlements_filters_by_ric() -> None:
    response = client.get(
        "/eod",
        params={"ric": "SETH27", "date": "2026-09-04", "type": "json"},
    )

    assert response.status_code == 200
    assert response.text.splitlines() == [
        '{"asset_subtype":"FUT","ric":"SETH27","trade_date":"2026-09-04","ask":null,"bid":null,"settlement_price":"118.6"}'
    ]


def test_get_settlements_returns_csv() -> None:
    response = client.get(
        "/eod",
        params={"ric": "SETH27", "date": "2026-09-04", "type": "csv"},
    )

    rows = list(csv.DictReader(StringIO(response.text), delimiter=";"))

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    assert rows[0]["RIC"] == "SETH27"
    assert rows[0]["Settlement Price"] == "118.6"


def test_get_settlements_rejects_unsupported_output_type() -> None:
    response = client.get(
        "/eod",
        params={"date": "2026-09-04", "type": "xml"},
    )

    assert response.status_code == 422


def test_post_settlements_filters_by_multiple_rics() -> None:
    response = client.post(
        "/eod",
        json={
            "date": "2026-09-04",
            "type": "json",
            "rics": ["SETH27", "SETH28"],
        },
    )

    assert response.status_code == 200
    assert [record["ric"] for record in map(json.loads, response.text.splitlines())] == [
        "SETH27",
        "SETH28",
    ]
