# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.source_type_query_params_enum import SourceTypeQueryParamsEnum
from ..models.source_health_enum import SourceHealthEnum
from ..models.source_criticality import SourceCriticality
from ..models.source import Source
from ..models.scan_status_enum import ScanStatusEnum
from ..models.list_sources_visibility import ListSourcesVisibility
from ..models.list_sources_ordering import ListSourcesOrdering


class SourcesService(BaseService):

    @cast_models
    def list_sources(
        self,
        cursor: str = None,
        page: int = None,
        per_page: int = None,
        search: str = None,
        last_scan_status: ScanStatusEnum = None,
        health: SourceHealthEnum = None,
        type_: SourceTypeQueryParamsEnum = None,
        ordering: ListSourcesOrdering = None,
        visibility: ListSourcesVisibility = None,
        external_id: str = None,
        source_criticality: SourceCriticality = None,
        monitored: bool = None,
    ) -> List[Source]:
        """List sources known by GitGuardian.

        :param cursor: Pagination cursor., defaults to None
        :type cursor: str, optional
        :param page: Page number., defaults to None
        :type page: int, optional
        :param per_page: Number of items to list per page., defaults to None
        :type per_page: int, optional
        :param search: search, defaults to None
        :type search: str, optional
        :param last_scan_status: last_scan_status, defaults to None
        :type last_scan_status: ScanStatusEnum, optional
        :param health: health, defaults to None
        :type health: SourceHealthEnum, optional
        :param type_: type_, defaults to None
        :type type_: SourceTypeQueryParamsEnum, optional
        :param ordering: Sort the results by their field value. The default sort is ASC, DESC if the
        field is preceded by a '-'., defaults to None
        :type ordering: ListSourcesOrdering, optional
        :param visibility: visibility, defaults to None
        :type visibility: ListSourcesVisibility, optional
        :param external_id: external_id, defaults to None
        :type external_id: str, optional
        :param source_criticality: source_criticality, defaults to None
        :type source_criticality: SourceCriticality, optional
        :param monitored: monitored, defaults to None
        :type monitored: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Source List
        :rtype: List[Source]
        """

        Validator(str).is_optional().validate(cursor)
        Validator(int).is_optional().min(0).validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)
        Validator(str).is_optional().validate(search)
        Validator(ScanStatusEnum).is_optional().validate(last_scan_status)
        Validator(SourceHealthEnum).is_optional().validate(health)
        Validator(SourceTypeQueryParamsEnum).is_optional().validate(type_)
        Validator(ListSourcesOrdering).is_optional().validate(ordering)
        Validator(ListSourcesVisibility).is_optional().validate(visibility)
        Validator(str).is_optional().validate(external_id)
        Validator(SourceCriticality).is_optional().validate(source_criticality)
        Validator(bool).is_optional().validate(monitored)

        serialized_request = (
            Serializer(f"{self.base_url}/v1/sources", self.get_default_headers())
            .add_query("cursor", cursor)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .add_query("search", search)
            .add_query("last_scan_status", last_scan_status)
            .add_query("health", health)
            .add_query("type", type_)
            .add_query("ordering", ordering)
            .add_query("visibility", visibility)
            .add_query("external_id", external_id)
            .add_query("source_criticality", source_criticality)
            .add_query("monitored", monitored)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [Source._unmap(item) for item in response]

    @cast_models
    def retrieve_source(self, source_id: int) -> Source:
        """Retrieve a source known by GitGuardian.

        :param source_id: The id of the source to retrieve.
        :type source_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Source List
        :rtype: Source
        """

        Validator(int).validate(source_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/v1/sources/{{source_id}}", self.get_default_headers()
            )
            .add_path("source_id", source_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Source._unmap(response)
