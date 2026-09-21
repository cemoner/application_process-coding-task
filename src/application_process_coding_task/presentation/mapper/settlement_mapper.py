from application_process_coding_task.application.dto.settlement_query import (
    SettlementQuery,
)
from application_process_coding_task.application.dto.settlement_result import (
    SettlementResult,
)

from ..dto.settlement_request import SettlementRequest
from ..dto.settlement_response import SettlementResponse


def to_settlement_query(request: SettlementRequest) -> SettlementQuery:
    return SettlementQuery(
        ric=request.ric,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_settlement_response(result: SettlementResult) -> SettlementResponse:
    return SettlementResponse(
        **{
            "Asset SubType": result.asset_subtype,
            "RIC": result.ric,
            "Trade Date": result.trade_date,
            "Ask": str(result.ask) if result.ask is not None else None,
            "Bid": str(result.bid) if result.bid is not None else None,
            "Settlement Price": str(result.settlement_price),
        }
    )
