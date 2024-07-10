# This file was generated by liblab | https://liblab.com/

from enum import Enum


class SeverityEnumIac(Enum):
    """An enumeration representing different categories.

    :cvar CRITICAL: "critical"
    :vartype CRITICAL: str
    :cvar HIGH: "high"
    :vartype HIGH: str
    :cvar MEDIUM: "medium"
    :vartype MEDIUM: str
    :cvar LOW: "low"
    :vartype LOW: str
    """

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SeverityEnumIac._member_map_.values()))