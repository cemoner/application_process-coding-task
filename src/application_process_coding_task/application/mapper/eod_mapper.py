from application_process_coding_task.application.dto.result.eod_result import EodResult
from application_process_coding_task.domain.entity.eod_record import EodRecord


def to_eod_result(record: EodRecord) -> EodResult:
    return EodResult(
        asset_subtype=record.asset_subtype,
        ric=record.ric,
        trade_date=record.trade_date,
        ask=record.ask,
        bid=record.bid,
        settlement_price=record.settlement_price,
    )
