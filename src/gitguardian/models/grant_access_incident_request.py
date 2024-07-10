# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .incident_permission_enum import IncidentPermissionEnum


@JsonMap({})
class GrantAccessIncidentRequest(BaseModel):
    """GrantAccessIncidentRequest

    :param email: Email address of a user or invitee. This parameter is mutually exclusive with `member_id`, `invitation_id` and `team_id`. , defaults to None
    :type email: str, optional
    :param member_id: Id of a member. This parameter is mutually exclusive with `email`, `invitation_id` and `team_id`. , defaults to None
    :type member_id: float, optional
    :param invitation_id: Id of an invitation. This parameter is mutually exclusive with `email`, `member_id` and `team_id`. , defaults to None
    :type invitation_id: float, optional
    :param team_id: Id of a team, except for the global team. This parameter is mutually exclusive with `email`, `member_id` and `invitation_id`. , defaults to None
    :type team_id: float, optional
    :param incident_permission: incident_permission, defaults to None
    :type incident_permission: IncidentPermissionEnum, optional
    """

    def __init__(
        self,
        email: str = None,
        member_id: float = None,
        invitation_id: float = None,
        team_id: float = None,
        incident_permission: IncidentPermissionEnum = None,
    ):
        if email is not None:
            self.email = email
        if member_id is not None:
            self.member_id = member_id
        if invitation_id is not None:
            self.invitation_id = invitation_id
        if team_id is not None:
            self.team_id = team_id
        if incident_permission is not None:
            self.incident_permission = self._enum_matching(
                incident_permission,
                IncidentPermissionEnum.list(),
                "incident_permission",
            )
