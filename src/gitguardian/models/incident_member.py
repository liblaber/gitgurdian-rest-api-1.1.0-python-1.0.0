# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .incident_permission_enum import IncidentPermissionEnum
from .member_access_level_enum import MemberAccessLevelEnum


@JsonMap({"id_": "id"})
class IncidentMember(BaseModel):
    """IncidentMember

    :param member_id: The id of the Member object (replaces the id field) , defaults to None
    :type member_id: int, optional
    :param incident_id: The id of the Incident object , defaults to None
    :type incident_id: int, optional
    :param incident_permission: incident_permission, defaults to None
    :type incident_permission: IncidentPermissionEnum, optional
    :param id_: id_, defaults to None
    :type id_: int, optional
    :param name: name, defaults to None
    :type name: str, optional
    :param email: email, defaults to None
    :type email: str, optional
    :param role: role, defaults to None
    :type role: MemberAccessLevelEnum, optional
    """

    def __init__(
        self,
        member_id: int = None,
        incident_id: int = None,
        incident_permission: IncidentPermissionEnum = None,
        id_: int = None,
        name: str = None,
        email: str = None,
        role: MemberAccessLevelEnum = None,
    ):
        if member_id is not None:
            self.member_id = member_id
        if incident_id is not None:
            self.incident_id = incident_id
        if incident_permission is not None:
            self.incident_permission = self._enum_matching(
                incident_permission,
                IncidentPermissionEnum.list(),
                "incident_permission",
            )
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if role is not None:
            self.role = self._enum_matching(role, MemberAccessLevelEnum.list(), "role")
