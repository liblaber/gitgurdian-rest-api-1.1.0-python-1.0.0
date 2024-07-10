# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ListMembersOrdering(Enum):
    """An enumeration representing different categories.

    :cvar CREATED_AT: "created_at"
    :vartype CREATED_AT: str
    :cvar _CREATED_AT: "-created_at"
    :vartype _CREATED_AT: str
    :cvar LAST_LOGIN: "last_login"
    :vartype LAST_LOGIN: str
    :cvar _LAST_LOGIN: "-last_login"
    :vartype _LAST_LOGIN: str
    """

    CREATED_AT = "created_at"
    _CREATED_AT = "-created_at"
    LAST_LOGIN = "last_login"
    _LAST_LOGIN = "-last_login"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ListMembersOrdering._member_map_.values()))