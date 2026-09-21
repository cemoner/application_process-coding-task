import csv
from io import StringIO
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.responses import Response

from application_process_coding_task.application.dto.output_format import OutputFormat
from application_process_coding_task.application.dto.settlement_query import SettlementQuery
from application_process_coding_task.application.service.settlement_lookup_service import (
    SettlementLookupService,
)

from ..dependency import get_settlement_service
from ..dto.settlement_request import SettlementRequest
from ..dto.settlement_response import SettlementResponse
from ..mapper import to_settlement_query, to_settlement_response

router = APIRouter(prefix="/settlements", tags=["settlements"])


@router.get("", response_model=list[SettlementResponse])
def get_settlement(
    request: Annotated[SettlementRequest, Depends()],
    service: Annotated[SettlementLookupService, Depends(get_settlement_service)],
) -> list[SettlementResponse] | Response:
    query: SettlementQuery = to_settlement_query(request)
    results = service.find(query)
    responses = [to_settlement_response(result) for result in results]

    match request.output_type:
        case OutputFormat.JSON:
            return responses
        case OutputFormat.CSV:
            return _to_csv_response(responses)


def _to_csv_response(responses: list[SettlementResponse]) -> Response:
    buffer = StringIO()
    writer = csv.writer(buffer, delimiter=";")
    writer.writerow(["Asset SubType", "RIC", "Trade Date", "Ask", "Bid", "Settlement Price"])
    for response in responses:
        writer.writerow(response.model_dump(by_alias=True).values())

    return Response(
        content=buffer.getvalue(),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=settlements.csv"},
    )
