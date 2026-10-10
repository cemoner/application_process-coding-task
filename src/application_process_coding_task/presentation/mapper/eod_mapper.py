from application_process_coding_task.application.dto.query.eod_query import (
    EodQuery,
)
from application_process_coding_task.application.dto.result.eod_result import (
    EodResult,
)

from application_process_coding_task.presentation.dto.request.multiple_eod_request import MultipleEodRequest
from application_process_coding_task.presentation.dto.request.eod_request import EodRequest
from application_process_coding_task.presentation.dto.response.eod_response import EodResponse


def to_eod_query(request: EodRequest) -> EodQuery:
    return EodQuery(
        ric=request.ric,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_multiple_eod_query(
    request: MultipleEodRequest,
) -> EodQuery:
    return EodQuery(
        rics=request.rics,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_eod_response(result: EodResult) -> EodResponse:
    return EodResponse.model_validate(
        {
            "asset_subtype": result.asset_subtype,
            "ric": result.ric,
            "trade_date": result.trade_date,
            "ask": str(result.ask) if result.ask is not None else None,
            "bid": str(result.bid) if result.bid is not None else None,
            "settlement_price": str(result.settlement_price),
        }
    )
