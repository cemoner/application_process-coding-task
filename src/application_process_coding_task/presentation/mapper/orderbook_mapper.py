from application_process_coding_task.application.dto.orderbook_query import OrderBookQuery
from application_process_coding_task.application.dto.orderbook_result import OrderBookResult

from ..dto.orderbook_batch_request import OrderBookBatchRequest
from ..dto.orderbook_request import OrderBookRequest
from ..dto.orderbook_response import OrderBookResponse


def to_orderbook_query(request: OrderBookRequest) -> OrderBookQuery:
    return OrderBookQuery(
        ric=request.ric,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_batch_orderbook_query(
    request: OrderBookRequest,
    batch_request: OrderBookBatchRequest,
) -> OrderBookQuery:
    return OrderBookQuery(
        rics=batch_request.rics,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_orderbook_response(result: OrderBookResult) -> OrderBookResponse:
    return OrderBookResponse.model_validate(
        {
            "ric": result.ric,
            "alias_underlying_ric": result.alias_underlying_ric,
            "domain": result.domain,
            "date_time": result.date_time,
            "gmt_offset": result.gmt_offset,
            "event_type": result.event_type,
            "bid_price": result.bid_price,
            "bid_size": result.bid_size,
            "ask_price": result.ask_price,
            "ask_size": result.ask_size,
        }
    )
