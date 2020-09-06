from fastapi import FastAPI
from src.error.api_error import APIError
from src.error.error_handler import api_errors, general_errors

app = FastAPI()


@app.exception_handler(APIError)
def deal_with_api_errors(request, error: APIError):
    return api_errors(error)


@app.exception_handler(Exception)
def deal_with_general_errors(request, error: Exception):
    return general_errors(error)
