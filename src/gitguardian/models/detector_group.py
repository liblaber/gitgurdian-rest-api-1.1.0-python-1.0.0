# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .detector_group_type_enum import DetectorGroupTypeEnum


@JsonMap({"type_": "type"})
class DetectorGroup(BaseModel):
    """DetectorGroup

    :param name: name, defaults to None
    :type name: str, optional
    :param display_name: display_name, defaults to None
    :type display_name: str, optional
    :param type_: type_, defaults to None
    :type type_: DetectorGroupTypeEnum, optional
    :param category: category, defaults to None
    :type category: str, optional
    :param is_active: Whether the detector is currently enabled on the workspace, defaults to None
    :type is_active: bool, optional
    :param scans_code_only: Whether the detector can scan other kinds of resources than VCS ones, defaults to None
    :type scans_code_only: bool, optional
    :param checkable: Indicates whether this detector has a validity checker, defaults to None
    :type checkable: bool, optional
    :param use_with_validity_check_disabled: If false, this detector will not be used if secret validity check is disabled on the workspace, defaults to None
    :type use_with_validity_check_disabled: bool, optional
    :param frequency: Number of secrets found per million of commits from GitGuardian experience of open-source monitoring, defaults to None
    :type frequency: float, optional
    :param removed_at: Date at which this detector was disabled by GitGuardian, defaults to None
    :type removed_at: str, optional
    :param open_incidents_count: Number of open secret incidents on the workspace associated to this detector, defaults to None
    :type open_incidents_count: int, optional
    :param ignored_incidents_count: Number of ignored secret incidents on the workspace associated to this detector, defaults to None
    :type ignored_incidents_count: int, optional
    :param resolved_incidents_count: Number of resolved secret incidents on the workspace associated to this detector, defaults to None
    :type resolved_incidents_count: int, optional
    """

    def __init__(
        self,
        name: str = None,
        display_name: str = None,
        type_: DetectorGroupTypeEnum = None,
        category: str = None,
        is_active: bool = None,
        scans_code_only: bool = None,
        checkable: bool = None,
        use_with_validity_check_disabled: bool = None,
        frequency: float = None,
        removed_at: str = None,
        open_incidents_count: int = None,
        ignored_incidents_count: int = None,
        resolved_incidents_count: int = None,
    ):
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, DetectorGroupTypeEnum.list(), "type_"
            )
        if category is not None:
            self.category = category
        if is_active is not None:
            self.is_active = is_active
        if scans_code_only is not None:
            self.scans_code_only = scans_code_only
        if checkable is not None:
            self.checkable = checkable
        if use_with_validity_check_disabled is not None:
            self.use_with_validity_check_disabled = use_with_validity_check_disabled
        if frequency is not None:
            self.frequency = frequency
        if removed_at is not None:
            self.removed_at = removed_at
        if open_incidents_count is not None:
            self.open_incidents_count = open_incidents_count
        if ignored_incidents_count is not None:
            self.ignored_incidents_count = ignored_incidents_count
        if resolved_incidents_count is not None:
            self.resolved_incidents_count = resolved_incidents_count
