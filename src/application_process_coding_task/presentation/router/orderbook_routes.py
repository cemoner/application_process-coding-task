import csv
from io import StringIO
from typing import Annotated, Iterator

from fastapi import APIRouter, Depends
from starlette.responses import StreamingResponse

from application_process_coding_task.application.dto.helper.output_format import OutputFormat
from application_process_coding_task.application.service.orderbook_lookup_service import (
    OrderBookLookupService,
)

from ..dependency import get_orderbook_service
from application_process_coding_task.presentation.dto.request.multiple_orderbook_request import MultipleOrderbookRequest
from application_process_coding_task.presentation.dto.request.orderbook_request import OrderBookRequest
from application_process_coding_task.presentation.dto.response.orderbook_response import OrderBookResponse
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
    return _format_response(request.output_type, (to_orderbook_response(result) for result in results))


@router.post("", response_class=StreamingResponse)
def post_orderbook(
    batch_request: MultipleOrderbookRequest,
    service: Annotated[OrderBookLookupService, Depends(get_orderbook_service)],
) -> StreamingResponse:
    results = service.find(to_multiple_orderbook_query(batch_request))
    return _format_response(
        batch_request.output_type,
        (to_orderbook_response(result) for result in results),
    )


def _format_response(
    output_type: OutputFormat,
    responses: Iterator[OrderBookResponse],
) -> StreamingResponse:
    match output_type:
        case OutputFormat.JSON:
            def generate_json() -> Iterator[str]:
                for response in responses:
                    # model_dump() converts the Pydantic model to a dict
                    yield response.model_dump_json() + "\n"
            return StreamingResponse(
                generate_json(),
                media_type="application/x-ndjson"
            )

        case OutputFormat.CSV:
            def generate_csv() -> Iterator[str]:
                # Use StringIO as an in-memory text buffer for the csv writer
                buffer = StringIO()
                writer = csv.writer(buffer)
                is_first_row = True

                for response in responses:
                    data_dict = response.model_dump()

                    if is_first_row:
                        writer.writerow(data_dict.keys())
                        is_first_row = False

                    writer.writerow(data_dict.values())

                    # Yield the buffered string and clear it for the next row
                    yield buffer.getvalue()
                    buffer.seek(0)
                    buffer.truncate(0)

            return StreamingResponse(
                generate_csv(),
                media_type="text/csv"
            )

        case _:
            raise ValueError(f"Unsupported output format: {output_type}")
