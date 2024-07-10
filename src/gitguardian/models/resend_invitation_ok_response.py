# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ResendInvitationOkResponse(BaseModel):
    """ResendInvitationOkResponse

    :param detail: Details on response., defaults to None
    :type detail: str, optional
    """

    def __init__(self, detail: str = None):
        if detail is not None:
            self.detail = detail
