from collections.abc import Iterator

from application_process_coding_task.application.dto.query.eod_query import (
    MultipleEodQuery,
    SingleEodQuery,
)
from application_process_coding_task.application.dto.result.eod_result import EodResult
from application_process_coding_task.application.mapper.eod_mapper import to_eod_result
from application_process_coding_task.domain.interface.eod_repository import EodRepository


class EodLookupService:
    def __init__(self, repository: EodRepository) -> None:
        self.repository = repository

    def find_single(self, query: SingleEodQuery) -> Iterator[EodResult]:
        for record in self.repository.find_single(query):
            yield to_eod_result(record)

    def find_multiple(self, query: MultipleEodQuery) -> Iterator[EodResult]:
        for record in self.repository.find_multiple(query):
            yield to_eod_result(record)
