from datetime import date
from typing import Protocol

from application_process_coding_task.domain.entity.settlement_record import (
    SettlementRecord,
)


class SettlementRepository(Protocol):
    def find_by_ric_and_date(
        self,
        ric: str,
        trade_date: date,
    ) -> SettlementRecord | None:
        """Return the settlement record for one instrument and date."""
