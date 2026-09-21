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
    return OrderBookResponse(
        **{
            "#RIC": result.ric,
            "Alias Underlying RIC": result.alias_underlying_ric,
            "Domain": result.domain,
            "Date-Time": result.date_time,
            "GMT Offset": result.gmt_offset,
            "Type": result.event_type,
            "Bid Price": result.bid_price,
            "Bid Size": result.bid_size,
            "Ask Price": result.ask_price,
            "Ask Size": result.ask_size,
        }
    )
