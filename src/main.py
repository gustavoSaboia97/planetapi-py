from fastapi import FastAPI, Response
from src.error.api_error import APIError
from src.error.error_handler import api_errors, general_errors

app = FastAPI()


@app.exception_handler(APIError)
def deal_with_api_errors(request, error: APIError) -> Response:
    return api_errors(error)


@app.exception_handler(Exception)
def deal_with_general_errors(request, error: Exception) -> Response:
    return general_errors(error)
