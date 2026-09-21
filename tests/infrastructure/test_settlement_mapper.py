from datetime import date
from decimal import Decimal

import pytest

from application_process_coding_task.infrastructure.mapper.settlement_mapper import (
    to_settlement_record,
)


def test_maps_duckdb_row_to_settlement_record() -> None:
    record = to_settlement_record(("FUT", "SETH27", "2026-09-04T23:03:19.356147683Z", "121.05"))

    assert record.asset_subtype == "FUT"
    assert record.ric == "SETH27"
    assert record.trade_date == date(2026, 9, 4)
    assert record.settlement_price == Decimal("121.05")


def test_rejects_row_with_wrong_column_count() -> None:
    with pytest.raises(ValueError, match="must contain"):
        to_settlement_record(("SETH27", "2026-09-04"))
