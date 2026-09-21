from application_process_coding_task.application.dto.eod_query import EodQuery
from application_process_coding_task.application.dto.eod_result import EodResult
from application_process_coding_task.domain.interface.eod_repository import (
    EodRepository,
)


class EodLookupService:
    def __init__(self, repository: EodRepository) -> None:
        self.repository = repository

    def find(self, query: EodQuery) -> list[EodResult]:
        records = self.repository.find_by_date(query.trade_date, query.ric, query.rics)
        return [
            EodResult(
                asset_subtype=record.asset_subtype,
                ric=record.ric,
                trade_date=record.trade_date,
                ask=record.ask,
                bid=record.bid,
                settlement_price=record.settlement_price,
            )
            for record in records
        ]
