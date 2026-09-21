from application_process_coding_task.application.dto.settlement_query import SettlementQuery
from application_process_coding_task.application.dto.settlement_result import SettlementResult
from application_process_coding_task.domain.interface.settlement_repository import (
    SettlementRepository,
)


class SettlementLookupService:
    def __init__(self, repository: SettlementRepository) -> None:
        self.repository = repository

    def find(self, query: SettlementQuery) -> list[SettlementResult]:
        records = self.repository.find_by_date(query.trade_date, query.ric, query.rics)
        return [
            SettlementResult(
                asset_subtype=record.asset_subtype,
                ric=record.ric,
                trade_date=record.trade_date,
                ask=record.ask,
                bid=record.bid,
                settlement_price=record.settlement_price,
            )
            for record in records
        ]
