from rest_framework import status

# pylint: disable=unused-import
from rest_framework.exceptions import (
    APIException,
    AuthenticationFailed,
    ErrorDetail,
    NotAuthenticated,
    NotFound,
    PermissionDenied,
    ValidationError,
)
# pylint: enable=unused-import


class ConflictError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_code = 'conflict_error'


class SystemError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = 'system_error'


class UserDoesNotExistError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = 'system_error'


class BadRequestError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'bad_request'
