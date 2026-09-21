from datetime import date
from decimal import Decimal

import pytest

from application_process_coding_task.infrastructure.mapper.eod_mapper import (
    infer_asset_subtype,
    to_eod_record,
)


def test_maps_duckdb_row_to_eod_record() -> None:
    record = to_eod_record(("SETH27", "2026-09-04T23:03:19.356147683Z", None, None, "121.05"))

    assert record.ric == "SETH27"
    assert record.trade_date == date(2026, 9, 4)
    assert record.settlement_price == Decimal("121.05")


def test_infers_futures_asset_subtype_from_ric() -> None:
    assert infer_asset_subtype("SETH27") == "FUT"


def test_rejects_row_with_wrong_column_count() -> None:
    with pytest.raises(ValueError, match="must contain"):
        to_eod_record(("SETH27", "2026-09-04"))
