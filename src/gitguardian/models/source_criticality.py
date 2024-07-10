# This file was generated by liblab | https://liblab.com/

from enum import Enum


class SourceCriticality(Enum):
    """An enumeration representing different categories.

    :cvar CRITICAL: "critical"
    :vartype CRITICAL: str
    :cvar HIGH: "high"
    :vartype HIGH: str
    :cvar MEDIUM: "medium"
    :vartype MEDIUM: str
    :cvar LOW: "low"
    :vartype LOW: str
    :cvar UNKNOWN: "unknown"
    :vartype UNKNOWN: str
    """

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SourceCriticality._member_map_.values()))
