import csv
from io import StringIO
from typing import Annotated, Iterator

from fastapi import APIRouter, Depends
from fastapi.responses import Response
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

