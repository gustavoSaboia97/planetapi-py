from .api_error import APIError
from src.util.logger import get_logger
from fastapi.responses import JSONResponse
from fastapi import Response, status


logger = get_logger()


def api_errors(exception: APIError) -> Response:
    logger.error(f"[API ERRORS] An error occurred during api processing {exception.message}")
    return JSONResponse(content=exception.to_dict(), status_code=exception.status_code)


def general_errors(exception: Exception) -> Response:
    logger.error(f"[GENERAL ERRORS] An error was found on API {str(exception)}")
    return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
