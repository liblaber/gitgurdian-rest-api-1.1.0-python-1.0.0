# This file was generated by liblab | https://liblab.com/

from enum import Enum


class OccurrenceKindEnum(Enum):
    """An enumeration representing different categories.

    :cvar REALTIME: "Realtime"
    :vartype REALTIME: str
    :cvar HISTORICAL: "Historical"
    :vartype HISTORICAL: str
    """

    REALTIME = "Realtime"
    HISTORICAL = "Historical"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OccurrenceKindEnum._member_map_.values()))
