import csv
from io import StringIO
from typing import Annotated, Iterator

from fastapi import APIRouter, Depends
from starlette.responses import StreamingResponse

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
from ..mapper.format_response import format_streaming_response

router = APIRouter(prefix="/eod", tags=["eod"])


@router.get("", response_class=StreamingResponse)
def get_eod(
    request: Annotated[EodRequest, Depends()],
    service: Annotated[EodLookupService, Depends(get_eod_service)],
) -> StreamingResponse:
    query = to_eod_query(request)
    results = service.find(query)
    return format_streaming_response(
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
    return format_streaming_response(
        batch_request.output_type,
        (to_eod_response(result) for result in results),
    )

