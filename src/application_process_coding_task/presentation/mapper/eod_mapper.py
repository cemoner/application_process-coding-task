from application_process_coding_task.application.dto.eod_query import (
    EodQuery,
)
from application_process_coding_task.application.dto.eod_result import (
    EodResult,
)

from ..dto.eod_batch_request import EodBatchRequest
from ..dto.eod_request import EodRequest
from ..dto.eod_response import EodResponse


def to_eod_query(request: EodRequest) -> EodQuery:
    return EodQuery(
        ric=request.ric,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_batch_eod_query(
    request: EodRequest,
    batch_request: EodBatchRequest,
) -> EodQuery:
    return EodQuery(
        rics=batch_request.rics,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_eod_response(result: EodResult) -> EodResponse:
    return EodResponse(
        **{
            "Asset SubType": result.asset_subtype,
            "RIC": result.ric,
            "Trade Date": result.trade_date,
            "Ask": str(result.ask) if result.ask is not None else None,
            "Bid": str(result.bid) if result.bid is not None else None,
            "Settlement Price": str(result.settlement_price),
        }
    )
