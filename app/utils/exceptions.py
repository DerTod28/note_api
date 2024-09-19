from typing import Any, Union

from fastapi import HTTPException, status


class ApiExceptionsError(Exception):
    @staticmethod
    def not_found_404(detail: str = 'Not found', as_dict: bool = False) -> Union[HTTPException, dict[str, Any]]:
        if as_dict:
            return {'detail': detail}
        return HTTPException(detail=detail, status_code=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def bad_request_400(detail: str = 'Bad Request', as_dict: bool = False) -> Union[HTTPException, dict[str, Any]]:
        if as_dict:
            return {'detail': detail}
        return HTTPException(detail=detail, status_code=status.HTTP_400_BAD_REQUEST)
