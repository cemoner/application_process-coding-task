import csv
from collections.abc import Iterator
from io import StringIO

from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from application_process_coding_task.application.dto.helper.output_format import OutputFormat


def format_streaming_response[T: BaseModel](
    output_type: OutputFormat, responses: Iterator[T]
) -> StreamingResponse:
    match output_type:
        case OutputFormat.JSON:

            def generate_json() -> Iterator[str]:
                for response in responses:
                    yield response.model_dump_json() + "\n"

            return StreamingResponse(generate_json(), media_type="application/x-ndjson")

        case OutputFormat.CSV:

            def generate_csv() -> Iterator[str]:
                buffer = StringIO()
                writer = csv.writer(buffer, delimiter=";", lineterminator="\n")
                is_first_row = True

                for response in responses:
                    data_dict = response.model_dump(by_alias=True)

                    if is_first_row:
                        writer.writerow(data_dict)
                        is_first_row = False

                    writer.writerow(data_dict.values())

                    yield buffer.getvalue()
                    buffer.seek(0)
                    buffer.truncate(0)

            return StreamingResponse(generate_csv(), media_type="text/csv")

        case _:
            raise ValueError(f"Unsupported output format: {output_type}")
