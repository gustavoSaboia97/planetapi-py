from .api_error import APIError
from fastapi import status


class ObjectNotFoundError(APIError):

    def __init__(self, err_object: str):
        super(ObjectNotFoundError, self).__init__(f"{err_object} object not found", status.HTTP_404_NOT_FOUND)
