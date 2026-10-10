import csv
from io import StringIO
from typing import Annotated, Iterator

from fastapi import APIRouter, Depends
from starlette.responses import StreamingResponse

from application_process_coding_task.application.service.orderbook_lookup_service import (
    OrderBookLookupService,
)

from ..dependency import get_orderbook_service
from application_process_coding_task.presentation.dto.request.multiple_orderbook_request import MultipleOrderbookRequest
from application_process_coding_task.presentation.dto.request.orderbook_request import OrderBookRequest
from application_process_coding_task.presentation.dto.response.orderbook_response import OrderBookResponse
from ..mapper.format_response import format_streaming_response
from ..mapper.orderbook_mapper import (
    to_multiple_orderbook_query,
    to_orderbook_query,
    to_orderbook_response,
)

router = APIRouter(prefix="/orderbook", tags=["orderbook"])


@router.get("", response_class=StreamingResponse)
def get_orderbook(
    request: Annotated[OrderBookRequest, Depends()],
    service: Annotated[OrderBookLookupService, Depends(get_orderbook_service)],
) -> StreamingResponse:
    results = service.find(to_orderbook_query(request))
    return format_streaming_response(
        request.output_type,
        (to_orderbook_response(result) for result in results)
    )


@router.post("", response_class=StreamingResponse)
def post_orderbook(
    batch_request: MultipleOrderbookRequest,
    service: Annotated[OrderBookLookupService, Depends(get_orderbook_service)],
) -> StreamingResponse:
    results = service.find(to_multiple_orderbook_query(batch_request))
    return format_streaming_response(
        batch_request.output_type,
        (to_orderbook_response(result) for result in results),
    )
