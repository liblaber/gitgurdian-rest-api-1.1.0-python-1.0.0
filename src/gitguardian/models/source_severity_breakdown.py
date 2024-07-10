# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SeverityBreakdown(BaseModel):
    """SeverityBreakdown

    :param critical: critical, defaults to None
    :type critical: int, optional
    :param high: high, defaults to None
    :type high: int, optional
    :param medium: medium, defaults to None
    :type medium: int, optional
    :param low: low, defaults to None
    :type low: int, optional
    :param info: info, defaults to None
    :type info: int, optional
    :param unknown: unknown, defaults to None
    :type unknown: int, optional
    """

    def __init__(
        self,
        critical: int = None,
        high: int = None,
        medium: int = None,
        low: int = None,
        info: int = None,
        unknown: int = None,
    ):
        if critical is not None:
            self.critical = critical
        if high is not None:
            self.high = high
        if medium is not None:
            self.medium = medium
        if low is not None:
            self.low = low
        if info is not None:
            self.info = info
        if unknown is not None:
            self.unknown = unknown


@JsonMap({})
class SourceSeverityBreakdown(BaseModel):
    """SourceSeverityBreakdown

    :param total: total, defaults to None
    :type total: int, optional
    :param severity_breakdown: severity_breakdown, defaults to None
    :type severity_breakdown: SeverityBreakdown, optional
    """

    def __init__(self, total: int = None, severity_breakdown: SeverityBreakdown = None):
        if total is not None:
            self.total = total
        if severity_breakdown is not None:
            self.severity_breakdown = self._define_object(
                severity_breakdown, SeverityBreakdown
            )