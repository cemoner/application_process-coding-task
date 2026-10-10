from application_process_coding_task.application.dto.query.orderbook_query import (
    MultipleOrderBookQuery,
    SingleOrderBookQuery,
)
from application_process_coding_task.application.dto.result.orderbook_result import OrderBookResult
from application_process_coding_task.presentation.dto.request.multiple_orderbook_request import (
    MultipleOrderbookRequest,
)
from application_process_coding_task.presentation.dto.request.orderbook_request import (
    OrderBookRequest,
)
from application_process_coding_task.presentation.dto.response.orderbook_response import (
    OrderBookResponse,
)


def to_orderbook_query(request: OrderBookRequest) -> SingleOrderBookQuery:
    return SingleOrderBookQuery(
        ric=request.ric,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_multiple_orderbook_query(
    request: MultipleOrderbookRequest,
) -> MultipleOrderBookQuery:
    return MultipleOrderBookQuery(
        rics=request.rics,
        trade_date=request.trade_date,
        output_type=request.output_type,
    )


def to_orderbook_response(result: OrderBookResult) -> OrderBookResponse:
    return OrderBookResponse.model_validate(
        {
            "ric": result.ric,
            "alias_underlying_ric": result.alias_underlying_ric,
            "domain": result.domain,
            "date_time": result.date_time_text,
            "gmt_offset": result.gmt_offset,
            "event_type": result.event_type,
            "bid_price": result.bid_price,
            "bid_size": result.bid_size,
            "ask_price": result.ask_price,
            "ask_size": result.ask_size,
        }
    )
