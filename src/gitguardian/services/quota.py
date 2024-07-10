# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.quota import Quota


class QuotaService(BaseService):

    @cast_models
    def quotas(self) -> Quota:
        """Check available scanning calls for this token. Quota is shared between all tokens of a workspace

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Quota Overview
        :rtype: Quota
        """

        serialized_request = (
            Serializer(f"{self.base_url}/v1/quotas", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Quota._unmap(response)