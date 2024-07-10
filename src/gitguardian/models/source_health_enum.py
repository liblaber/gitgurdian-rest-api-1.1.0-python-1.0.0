# This file was generated by liblab | https://liblab.com/

from enum import Enum


class SourceHealthEnum(Enum):
    """An enumeration representing different categories.

    :cvar SAFE: "safe"
    :vartype SAFE: str
    :cvar UNKNOWN: "unknown"
    :vartype UNKNOWN: str
    :cvar AT_RISK: "at_risk"
    :vartype AT_RISK: str
    """

    SAFE = "safe"
    UNKNOWN = "unknown"
    AT_RISK = "at_risk"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SourceHealthEnum._member_map_.values()))