from datetime import date
from typing import Protocol

from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
)


class OrderBookRepository(Protocol):
    def find_quotes_by_date(
        self,
        trade_date: date,
        ric: str | None = None,
        rics: list[str] | None = None,
    ) -> list[OrderBookRecord]:
        """Return quote events for a date, optionally filtered by RIC."""
