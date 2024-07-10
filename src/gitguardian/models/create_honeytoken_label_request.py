# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateHoneytokenLabelRequest(BaseModel):
    """CreateHoneytokenLabelRequest

    :param key: Label's key's content.
    :type key: str
    :param value: Label's value's content.
    :type value: str
    """

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
