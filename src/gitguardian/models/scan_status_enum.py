# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ScanStatusEnum(Enum):
    """An enumeration representing different categories.

    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar RUNNING: "running"
    :vartype RUNNING: str
    :cvar CANCELED: "canceled"
    :vartype CANCELED: str
    :cvar FAILED: "failed"
    :vartype FAILED: str
    :cvar TOO_LARGE: "too_large"
    :vartype TOO_LARGE: str
    :cvar TIMEOUT: "timeout"
    :vartype TIMEOUT: str
    :cvar FINISHED: "finished"
    :vartype FINISHED: str
    """

    PENDING = "pending"
    RUNNING = "running"
    CANCELED = "canceled"
    FAILED = "failed"
    TOO_LARGE = "too_large"
    TIMEOUT = "timeout"
    FINISHED = "finished"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ScanStatusEnum._member_map_.values()))
