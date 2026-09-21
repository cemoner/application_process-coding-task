import csv
from io import StringIO
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import Response

from application_process_coding_task.application.dto.eod_query import EodQuery
from application_process_coding_task.application.dto.output_format import OutputFormat
from application_process_coding_task.application.service.eod_lookup_service import (
    EodLookupService,
)

from ..dependency import get_eod_service
from ..dto.eod_batch_request import EodBatchRequest
from ..dto.eod_request import EodRequest
from ..dto.eod_response import EodResponse
from ..mapper import (
    to_batch_eod_query,
    to_eod_query,
    to_eod_response,
)

router = APIRouter(prefix="/eod", tags=["eod"])


@router.get("", response_model=list[EodResponse])
def get_eod(
    request: Annotated[EodRequest, Depends()],
    service: Annotated[EodLookupService, Depends(get_eod_service)],
) -> list[EodResponse] | Response:
    query: EodQuery = to_eod_query(request)
    results = service.find(query)
    responses = [to_eod_response(result) for result in results]

    match request.output_type:
        case OutputFormat.JSON:
            return responses
        case OutputFormat.CSV:
            return _to_csv_response(responses)


@router.post("", response_model=list[EodResponse])
def post_eod(
    request: Annotated[EodRequest, Depends()],
    batch_request: EodBatchRequest,
    service: Annotated[EodLookupService, Depends(get_eod_service)],
) -> list[EodResponse] | Response:
    query = to_batch_eod_query(request, batch_request)
    results = service.find(query)
    responses = [to_eod_response(result) for result in results]

    match request.output_type:
        case OutputFormat.JSON:
            return responses
        case OutputFormat.CSV:
            return _to_csv_response(responses)


def _to_csv_response(responses: list[EodResponse]) -> Response:
    buffer = StringIO()
    writer = csv.writer(buffer, delimiter=";")
    writer.writerow(["Asset SubType", "RIC", "Trade Date", "Ask", "Bid", "Settlement Price"])
    for response in responses:
        writer.writerow(response.model_dump(by_alias=True).values())

    return Response(
        content=buffer.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=eod.csv"},
    )
