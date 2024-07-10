# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .incident_permission_enum import IncidentPermissionEnum


@JsonMap({})
class ResourceMemberAccess(BaseModel):
    """ResourceMemberAccess

    :param member_id: member_id, defaults to None
    :type member_id: int, optional
    :param resource_id: resource_id, defaults to None
    :type resource_id: int, optional
    :param resource_type: resource_type, defaults to None
    :type resource_type: str, optional
    :param permission: permission, defaults to None
    :type permission: IncidentPermissionEnum, optional
    """

    def __init__(
        self,
        member_id: int = None,
        resource_id: int = None,
        resource_type: str = None,
        permission: IncidentPermissionEnum = None,
    ):
        if member_id is not None:
            self.member_id = member_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if permission is not None:
            self.permission = self._enum_matching(
                permission, IncidentPermissionEnum.list(), "permission"
            )
