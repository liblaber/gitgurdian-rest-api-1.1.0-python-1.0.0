# This file was generated by liblab | https://liblab.com/

from enum import Enum


class ListTeamSourcesType(Enum):
    """An enumeration representing different categories.

    :cvar BITBUCKET: "bitbucket"
    :vartype BITBUCKET: str
    :cvar GITHUB: "github"
    :vartype GITHUB: str
    :cvar GITLAB: "gitlab"
    :vartype GITLAB: str
    :cvar AZURE_DEVOPS: "azure_devops"
    :vartype AZURE_DEVOPS: str
    """

    BITBUCKET = "bitbucket"
    GITHUB = "github"
    GITLAB = "gitlab"
    AZURE_DEVOPS = "azure_devops"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ListTeamSourcesType._member_map_.values()))
