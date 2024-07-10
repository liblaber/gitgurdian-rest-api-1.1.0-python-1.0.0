# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .team_permission_enum import TeamPermissionEnum
from .incident_permission_enum import IncidentPermissionEnum


@JsonMap({})
class AcceptTeamRequestRequest(BaseModel):
    """AcceptTeamRequestRequest

    :param team_permission: team_permission, defaults to None
    :type team_permission: TeamPermissionEnum, optional
    :param incident_permission: incident_permission, defaults to None
    :type incident_permission: IncidentPermissionEnum, optional
    """

    def __init__(
        self,
        team_permission: TeamPermissionEnum = None,
        incident_permission: IncidentPermissionEnum = None,
    ):
        if team_permission is not None:
            self.team_permission = self._enum_matching(
                team_permission, TeamPermissionEnum.list(), "team_permission"
            )
        if incident_permission is not None:
            self.incident_permission = self._enum_matching(
                incident_permission,
                IncidentPermissionEnum.list(),
                "incident_permission",
            )
