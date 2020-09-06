from .api_error import APIError
from fastapi import status


class ObjectAlreadyExistsError(APIError):

    def __init__(self, err_object: str):
        super(ObjectAlreadyExistsError, self).__init__(f"{err_object} object Already Exists", status.HTTP_409_CONFLICT)
