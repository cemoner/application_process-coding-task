from typing import Iterator

from application_process_coding_task.application.dto.query.eod_query import EodQuery, SingleEodQuery, MultipleEodQuery
from application_process_coding_task.application.dto.result.eod_result import EodResult
from application_process_coding_task.domain.interface.eod_repository import (
    EodRepository,
)


class EodLookupService:
    def __init__(self, repository: EodRepository) -> None:
        self.repository = repository

    def find(self,query: SingleEodQuery | MultipleEodQuery) -> Iterator[EodResult]:
        """Return EOD events for a date, optionally filtered by RICs."""
