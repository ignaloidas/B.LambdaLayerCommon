from typing import Optional

try:
    from exceptions.http_exception import HttpException
except ImportError as ex:
    from b_lambda_layer_common.source.python.exceptions.http_exception import HttpException


class FailedRollbackError(HttpException):
    def __init__(self, message: Optional[str] = None):
        super().__init__(message)

    @staticmethod
    def http_code() -> int:
        return 500

    @staticmethod
    def identifier() -> str:
        return 'B_FAILED_ROLLBACK'

    @staticmethod
    def description() -> str:
        return (
            'The server tried to satisfy client\'s request and failed to do so. Because of that server tried to '
            'perform a rollback to prevent data leakage and again failed to do so.'
        )
