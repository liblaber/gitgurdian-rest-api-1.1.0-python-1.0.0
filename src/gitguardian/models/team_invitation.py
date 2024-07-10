# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .team_permission_enum import TeamPermissionEnum
from .incident_permission_enum import IncidentPermissionEnum


@JsonMap({"id_": "id"})
class TeamInvitation(BaseModel):
    """TeamInvitation

    :param id_: id_, defaults to None
    :type id_: int, optional
    :param invitation_id: invitation_id, defaults to None
    :type invitation_id: int, optional
    :param team_id: team_id, defaults to None
    :type team_id: int, optional
    :param team_permission: team_permission, defaults to None
    :type team_permission: TeamPermissionEnum, optional
    :param incident_permission: incident_permission, defaults to None
    :type incident_permission: IncidentPermissionEnum, optional
    """

    def __init__(
        self,
        id_: int = None,
        invitation_id: int = None,
        team_id: int = None,
        team_permission: TeamPermissionEnum = None,
        incident_permission: IncidentPermissionEnum = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if invitation_id is not None:
            self.invitation_id = invitation_id
        if team_id is not None:
            self.team_id = team_id
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
