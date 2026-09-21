from datetime import date
from typing import Protocol

from application_process_coding_task.domain.entity.settlement_record import (
    SettlementRecord,
)


class SettlementRepository(Protocol):
    def find_by_date(
        self,
        trade_date: date,
        ric: str | None = None,
    ) -> list[SettlementRecord]:
        """Return settlement records for a date, optionally filtered by RIC."""
