from datetime import date
from typing import Protocol

from application_process_coding_task.domain.entity.eod_record import (
    EodRecord,
)


class EodRepository(Protocol):
    def find_by_date(
        self,
        trade_date: date,
        ric: str | None = None,
        rics: list[str] | None = None,
    ) -> list[EodRecord]:
        """Return EOD records for a date, optionally filtered by RICs."""
