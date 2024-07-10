# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ListHoneytokenType(Enum):
    """An enumeration representing different categories.

    :cvar AWS: "AWS"
    :vartype AWS: str
    """

    AWS = "AWS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ListHoneytokenType._member_map_.values()))
