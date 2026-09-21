import csv
from io import StringIO

from fastapi.testclient import TestClient

from application_process_coding_task.main import api

client = TestClient(api)


def test_get_settlements_returns_all_records_for_date() -> None:
    response = client.get("/settlements", params={"date": "2026-09-04", "type": "json"})

    assert response.status_code == 200
    records = response.json()
    assert len(records) == 21
    assert records[0] == {
        "Asset SubType": "FUT",
        "RIC": "SETH27",
        "Trade Date": "2026-09-04",
        "Ask": None,
        "Bid": None,
        "Settlement Price": "118.6",
    }


def test_get_settlements_filters_by_ric() -> None:
    response = client.get(
        "/settlements",
        params={"ric": "SETH27", "date": "2026-09-04", "type": "json"},
    )

    assert response.status_code == 200
    assert response.json() == [
        {
            "Asset SubType": "FUT",
            "RIC": "SETH27",
            "Trade Date": "2026-09-04",
            "Ask": None,
            "Bid": None,
            "Settlement Price": "118.6",
        }
    ]


def test_get_settlements_returns_csv() -> None:
    response = client.get(
        "/settlements",
        params={"ric": "SETH27", "date": "2026-09-04", "type": "csv"},
    )

    rows = list(csv.DictReader(StringIO(response.text), delimiter=";"))

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    assert response.headers["content-disposition"] == "attachment; filename=settlements.csv"
    assert rows[0]["RIC"] == "SETH27"
    assert rows[0]["Settlement Price"] == "118.6"


def test_get_settlements_rejects_unsupported_output_type() -> None:
    response = client.get(
        "/settlements",
        params={"date": "2026-09-04", "type": "xml"},
    )

    assert response.status_code == 422
