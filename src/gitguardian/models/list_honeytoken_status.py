# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ListHoneytokenStatus(Enum):
    """An enumeration representing different categories.

    :cvar TRIGGERED: "triggered"
    :vartype TRIGGERED: str
    :cvar ACTIVE: "active"
    :vartype ACTIVE: str
    :cvar REVOKED: "revoked"
    :vartype REVOKED: str
    """

    TRIGGERED = "triggered"
    ACTIVE = "active"
    REVOKED = "revoked"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ListHoneytokenStatus._member_map_.values()))