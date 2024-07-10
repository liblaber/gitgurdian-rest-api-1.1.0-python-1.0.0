# ScanMethodsService

A list of all methods in the `ScanMethodsService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [content_scan](#content_scan)   | Scan provided document content for policy breaks. Request body shouldn't exceed 1MB. This endpoint is stateless and as such will not store in our servers neither the documents nor the secrets found.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [multiple_scan](#multiple_scan) | Scan provided document contents for policy breaks. Multiple documents are returned by the same index order. There should not be more than 20 documents in the payload. Individual documents should not exceed 1MB. Quota usage is based on requests and not on the content size. One request to this endpoint will consume 1 API call. Also note that the quota is set on a rolling month and not on a calendar month. See [this documentation](https://docs.gitguardian.com/api-docs/usage-and-quotas) for more details. This endpoint is stateless and as such will not store in our servers neither the documents nor the secrets found. |

## content_scan

Scan provided document content for policy breaks. Request body shouldn't exceed 1MB. This endpoint is stateless and as such will not store in our servers neither the documents nor the secrets found.

- HTTP Method: `POST`
- Endpoint: `/v1/scan`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [Document](../models/Document.md) | ❌       | The request body. |

**Return Type**

`ScanResult`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import Document

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = Document(
    filename=".env",
    document="\nimport urllib.request\nurl = 'http://jen_barber:correcthorsebatterystaple@cake.gitguardian.com/isreal.json'\nresponse = urllib.request.urlopen(url)\nconsume(response.read())\n"
)

result = sdk.scan_methods.content_scan(request_body=request_body)

print(result)
```

## multiple_scan

Scan provided document contents for policy breaks. Multiple documents are returned by the same index order. There should not be more than 20 documents in the payload. Individual documents should not exceed 1MB. Quota usage is based on requests and not on the content size. One request to this endpoint will consume 1 API call. Also note that the quota is set on a rolling month and not on a calendar month. See [this documentation](https://docs.gitguardian.com/api-docs/usage-and-quotas) for more details. This endpoint is stateless and as such will not store in our servers neither the documents nor the secrets found.

- HTTP Method: `POST`
- Endpoint: `/v1/multiscan`

**Parameters**

| Name         | Type                                    | Required | Description       |
| :----------- | :-------------------------------------- | :------- | :---------------- |
| request_body | [List[Document]](../models/Document.md) | ❌       | The request body. |

**Return Type**

`List[ScanResult]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    {
        "filename": ".env",
        "document": "\nimport urllib.request\nurl = 'http://jen_barber:correcthorsebatterystaple@cake.gitguardian.com/isreal.json'\nresponse = urllib.request.urlopen(url)\nconsume(response.read())\n"
    }
]

result = sdk.scan_methods.multiple_scan(request_body=request_body)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
