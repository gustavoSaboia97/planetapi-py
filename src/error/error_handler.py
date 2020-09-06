from .api_error import APIError
from src.util.logger import get_logger
from fastapi.responses import PlainTextResponse


logger = get_logger()


def api_errors(exception: APIError) -> PlainTextResponse:
    logger.error(f"[API ERRORS] An error occurred during api processing {exception.message}")
    return PlainTextResponse(str(exception), status_code=exception.status_code)


def general_errors(exception: Exception) -> PlainTextResponse:
    logger.error(f"[GENERAL ERRORS] An error was found on API {str(exception)}")
    return PlainTextResponse(str(""), status_code=500)
