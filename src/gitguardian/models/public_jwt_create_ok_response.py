# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class PublicJwtCreateOkResponse(BaseModel):
    """PublicJwtCreateOkResponse

    :param token: JWT, defaults to None
    :type token: str, optional
    """

    def __init__(self, token: str = None):
        if token is not None:
            self.token = token
