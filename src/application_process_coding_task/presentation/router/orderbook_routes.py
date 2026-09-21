import csv
from io import StringIO
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import Response

from application_process_coding_task.application.dto.output_format import OutputFormat
from application_process_coding_task.application.service.orderbook_lookup_service import (
    OrderBookLookupService,
)

from ..dependency import get_orderbook_service
from ..dto.orderbook_batch_request import OrderBookBatchRequest
from ..dto.orderbook_request import OrderBookRequest
from ..dto.orderbook_response import OrderBookResponse
from ..mapper.orderbook_mapper import (
    to_batch_orderbook_query,
    to_orderbook_query,
    to_orderbook_response,
)

router = APIRouter(prefix="/orderbook", tags=["orderbook"])


@router.get("", response_model=list[OrderBookResponse])
def get_orderbook(
    request: Annotated[OrderBookRequest, Depends()],
    service: Annotated[OrderBookLookupService, Depends(get_orderbook_service)],
) -> list[OrderBookResponse] | Response:
    results = service.find(to_orderbook_query(request))
    return _format_response(
        request.output_type, [to_orderbook_response(result) for result in results]
    )


@router.post("", response_model=list[OrderBookResponse])
def post_orderbook(
    request: Annotated[OrderBookRequest, Depends()],
    batch_request: OrderBookBatchRequest,
    service: Annotated[OrderBookLookupService, Depends(get_orderbook_service)],
) -> list[OrderBookResponse] | Response:
    results = service.find(to_batch_orderbook_query(request, batch_request))
    return _format_response(
        request.output_type, [to_orderbook_response(result) for result in results]
    )


def _format_response(
    output_type: OutputFormat,
    responses: list[OrderBookResponse],
) -> list[OrderBookResponse] | Response:
    match output_type:
        case OutputFormat.JSON:
            return responses
        case OutputFormat.CSV:
            buffer = StringIO()
            writer = csv.writer(buffer, delimiter=";")
            writer.writerow(
                [
                    "#RIC",
                    "Alias Underlying RIC",
                    "Domain",
                    "Date-Time",
                    "GMT Offset",
                    "Type",
                    "Bid Price",
                    "Bid Size",
                    "Ask Price",
                    "Ask Size",
                ]
            )
            for response in responses:
                writer.writerow(response.model_dump(by_alias=True).values())
            return Response(
                content=buffer.getvalue(),
                media_type="text/csv",
                headers={"Content-Disposition": "attachment; filename=orderbook.csv"},
            )
