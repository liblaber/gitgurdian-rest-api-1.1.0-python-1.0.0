# This file was generated by liblab | https://liblab.com/

from enum import Enum


class MemberAccessLevelEnum(Enum):
    """An enumeration representing different categories.

    :cvar OWNER: "owner"
    :vartype OWNER: str
    :cvar MANAGER: "manager"
    :vartype MANAGER: str
    :cvar MEMBER: "member"
    :vartype MEMBER: str
    :cvar RESTRICTED: "restricted"
    :vartype RESTRICTED: str
    """

    OWNER = "owner"
    MANAGER = "manager"
    MEMBER = "member"
    RESTRICTED = "restricted"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MemberAccessLevelEnum._member_map_.values()))