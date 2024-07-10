# This file was generated by liblab | https://liblab.com/

from enum import Enum


class HmslSourceTypeEnum(Enum):
    """An enumeration representing different categories.

    :cvar GITHUB: "github"
    :vartype GITHUB: str
    :cvar GITHUB_ISSUE: "github_issue"
    :vartype GITHUB_ISSUE: str
    :cvar GITHUB_GIST: "github_gist"
    :vartype GITHUB_GIST: str
    :cvar UNKNOWN: "unknown"
    :vartype UNKNOWN: str
    """

    GITHUB = "github"
    GITHUB_ISSUE = "github_issue"
    GITHUB_GIST = "github_gist"
    UNKNOWN = "unknown"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HmslSourceTypeEnum._member_map_.values()))
