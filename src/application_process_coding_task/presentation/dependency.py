from application_process_coding_task.application.service.eod_lookup_service import (
    EodLookupService,
)
from application_process_coding_task.config import settings

from ..infrastructure.repository.parquet_eod_repository import ParquetEodRepository


def get_eod_repository() -> ParquetEodRepository:
    return ParquetEodRepository(settings.source_path)


def get_eod_service() -> EodLookupService:
    return EodLookupService(get_eod_repository())
