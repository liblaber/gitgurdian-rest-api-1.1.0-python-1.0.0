# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .sca_scan_tar_parameters import ScaScanTarParameters


@JsonMap({})
class ScaScanAllRequest(BaseModel):
    """ScaScanAllRequest

    :param scan_parameters: scan_parameters, defaults to None
    :type scan_parameters: ScaScanTarParameters, optional
    :param directory: directory
    :type directory: str
    """

    def __init__(self, directory: str, scan_parameters: ScaScanTarParameters = None):
        if scan_parameters is not None:
            self.scan_parameters = self._define_object(
                scan_parameters, ScaScanTarParameters
            )
        self.directory = directory