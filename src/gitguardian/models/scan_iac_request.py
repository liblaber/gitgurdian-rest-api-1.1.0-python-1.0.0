# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .iac_scan_tar_parameters import IacScanTarParameters


@JsonMap({})
class ScanIacRequest(BaseModel):
    """ScanIacRequest

    :param directory: Tar file containing the folder to be scanned.
    :type directory: dict
    :param scan_parameters: scan_parameters, defaults to None
    :type scan_parameters: IacScanTarParameters, optional
    """

    def __init__(self, directory: dict, scan_parameters: IacScanTarParameters = None):
        self.directory = directory
        if scan_parameters is not None:
            self.scan_parameters = self._define_object(
                scan_parameters, IacScanTarParameters
            )
