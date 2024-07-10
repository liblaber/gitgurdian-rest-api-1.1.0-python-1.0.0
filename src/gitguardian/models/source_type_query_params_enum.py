# This file was generated by liblab | https://liblab.com/

from enum import Enum


class SourceTypeQueryParamsEnum(Enum):
    """An enumeration representing different categories.

    :cvar BITBUCKET: "bitbucket"
    :vartype BITBUCKET: str
    :cvar GITHUB: "github"
    :vartype GITHUB: str
    :cvar GITLAB: "gitlab"
    :vartype GITLAB: str
    :cvar AZURE_DEVOPS: "azure_devops"
    :vartype AZURE_DEVOPS: str
    :cvar SLACK: "slack"
    :vartype SLACK: str
    :cvar JIRA_CLOUD: "jira_cloud"
    :vartype JIRA_CLOUD: str
    :cvar CONFLUENCE_CLOUD: "confluence_cloud"
    :vartype CONFLUENCE_CLOUD: str
    :cvar MICROSOFT_TEAMS: "microsoft_teams"
    :vartype MICROSOFT_TEAMS: str
    :cvar CONFLUENCE_DATA_CENTER: "confluence_data_center"
    :vartype CONFLUENCE_DATA_CENTER: str
    """

    BITBUCKET = "bitbucket"
    GITHUB = "github"
    GITLAB = "gitlab"
    AZURE_DEVOPS = "azure_devops"
    SLACK = "slack"
    JIRA_CLOUD = "jira_cloud"
    CONFLUENCE_CLOUD = "confluence_cloud"
    MICROSOFT_TEAMS = "microsoft_teams"
    CONFLUENCE_DATA_CENTER = "confluence_data_center"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SourceTypeQueryParamsEnum._member_map_.values())
        )
