# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ValidityEnum(Enum):
    """An enumeration representing different categories.

    :cvar VALID: "valid"
    :vartype VALID: str
    :cvar INVALID: "invalid"
    :vartype INVALID: str
    :cvar FAILED_TO_CHECK: "failed_to_check"
    :vartype FAILED_TO_CHECK: str
    :cvar NO_CHECKER: "no_checker"
    :vartype NO_CHECKER: str
    :cvar UNKNOWN: "unknown"
    :vartype UNKNOWN: str
    """

    VALID = "valid"
    INVALID = "invalid"
    FAILED_TO_CHECK = "failed_to_check"
    NO_CHECKER = "no_checker"
    UNKNOWN = "unknown"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ValidityEnum._member_map_.values()))