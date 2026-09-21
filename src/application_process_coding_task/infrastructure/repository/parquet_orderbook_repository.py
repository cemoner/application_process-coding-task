from datetime import date
from pathlib import Path

from application_process_coding_task.domain.entity.orderbook_record import (
    OrderBookRecord,
)
from application_process_coding_task.infrastructure.database.duckdb_connection import (
    get_duckdb_connection,
)
from application_process_coding_task.infrastructure.mapper.orderbook_mapper import (
    to_orderbook_record,
)


class ParquetOrderBookRepository:
    def __init__(self, source_path: Path) -> None:
        self.source_path = source_path

    def find_quotes_by_date(
        self,
        trade_date: date,
        ric: str | None = None,
        rics: list[str] | None = None,
    ) -> list[OrderBookRecord]:
        query = """
            SELECT "#RIC", NULL AS "Alias Underlying RIC", "Domain", "Date-Time",
                   "GMT Offset", "Type", "Bid Price", "Bid Size",
                   "Ask Price", "Ask Size"
            FROM read_parquet(?)
            WHERE "Domain" = 'Market Price'
              AND "Type" = 'Quote'
              AND CAST(
                  CAST("Date-Time" AS TIMESTAMPTZ)
                  + ("GMT Offset" || ' hours')::INTERVAL
                  AS DATE
              ) = ?
              AND ("Bid Price" IS NOT NULL OR "Ask Price" IS NOT NULL)
        """
        parameters: list[object] = [str(self.source_path), trade_date]
        if ric is not None:
            query += ' AND "#RIC" = ?'
            parameters.append(ric)
        elif rics:
            placeholders = ", ".join("?" for _ in rics)
            query += f' AND "#RIC" IN ({placeholders})'
            parameters.extend(rics)
        query += ' ORDER BY "#RIC", "Date-Time"'

        with get_duckdb_connection(self.source_path) as connection:
            rows = connection.execute(query, parameters).fetchall()

        return [to_orderbook_record(row) for row in rows]
