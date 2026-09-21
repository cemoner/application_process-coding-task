from datetime import datetime
from decimal import Decimal

from application_process_coding_task.infrastructure.mapper.orderbook_mapper import (
    to_orderbook_record,
)


def test_maps_quote_row_to_orderbook_record() -> None:
    record = to_orderbook_record(
        (
            "SETU26",
            None,
            "Market Price",
            "2026-09-04T11:47:05.376472448Z",
            "-5",
            "Quote",
            None,
            None,
            "7.95",
            "50",
        )
    )

    assert record.ric == "SETU26"
    assert record.date_time == datetime.fromisoformat("2026-09-04T11:47:05.376472448+00:00")
    assert record.ask_price == Decimal("7.95")
    assert record.ask_size == Decimal("50")
