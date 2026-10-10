import csv
from io import StringIO
from typing import Annotated, Iterator

from fastapi import APIRouter, Depends
from starlette.responses import StreamingResponse

from application_process_coding_task.application.dto.query.eod_query import EodQuery
from application_process_coding_task.application.dto.helper.output_format import OutputFormat
from application_process_coding_task.application.service.eod_lookup_service import (
    EodLookupService,
)

from ..dependency import get_eod_service
from application_process_coding_task.presentation.dto.request.multiple_eod_request import MultipleEodRequest
from application_process_coding_task.presentation.dto.request.eod_request import EodRequest
from application_process_coding_task.presentation.dto.response.eod_response import EodResponse
from ..mapper.eod_mapper import (
    to_multiple_eod_query,
    to_eod_query,
    to_eod_response,
)

router = APIRouter(prefix="/eod", tags=["eod"])


@router.get("", response_class=StreamingResponse)
def get_eod(
    request: Annotated[EodRequest, Depends()],
    service: Annotated[EodLookupService, Depends(get_eod_service)],
) -> StreamingResponse:
    query: EodQuery = to_eod_query(request)
    results = service.find(query)
    return _format_response(
        request.output_type,
        (to_eod_response(result) for result in results),
    )

@router.post("", response_class=StreamingResponse)
def post_eod(
    batch_request: MultipleEodRequest,
    service: Annotated[EodLookupService, Depends(get_eod_service)],
) -> StreamingResponse:
    query = to_multiple_eod_query(batch_request)
    results = service.find(query)
    return _format_response(
        batch_request.output_type,
        (to_eod_response(result) for result in results),
    )



def _format_response(
        output_type: OutputFormat,
        responses: Iterator[EodResponse]
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
