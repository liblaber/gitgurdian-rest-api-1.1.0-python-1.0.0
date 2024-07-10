# SecretDetectorsService

A list of all methods in the `SecretDetectorsService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description            |
| :---------------------------------------------- | :--------------------- |
| [list_secret_detectors](#list_secret_detectors) | List secret detectors. |
| [get_secret_detector](#get_secret_detector)     | Get a secret detector. |

## list_secret_detectors

List secret detectors.

- HTTP Method: `GET`
- Endpoint: `/v1/secret_detectors`

**Parameters**

| Name      | Type                                                                    | Required | Description                                                                                             |
| :-------- | :---------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| cursor    | str                                                                     | ❌       | Pagination cursor.                                                                                      |
| per_page  | int                                                                     | ❌       | Number of items to list per page.                                                                       |
| is_active | bool                                                                    | ❌       | Filter only active or inactive detectors.                                                               |
| type\_    | [DetectorGroupTypeEnum](../models/DetectorGroupTypeEnum.md)             | ❌       |                                                                                                         |
| search    | str                                                                     | ❌       |                                                                                                         |
| ordering  | [ListSecretDetectorsOrdering](../models/ListSecretDetectorsOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |

**Return Type**

`List[DetectorGroup]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import DetectorGroupTypeEnum, ListSecretDetectorsOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_detectors.list_secret_detectors(
    cursor="cursor",
    per_page=20,
    is_active=True,
    type_="specific",
    search="aws",
    ordering="name"
)

print(result)
```

## get_secret_detector

Get a secret detector.

- HTTP Method: `GET`
- Endpoint: `/v1/secret_detectors/{detector_name}`

**Parameters**

| Name          | Type | Required | Description                      |
| :------------ | :--- | :------- | :------------------------------- |
| detector_name | str  | ✅       | Name of the detector to retrieve |

**Return Type**

`DetectorGroup`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_detectors.get_secret_detector(detector_name="aws_iam")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->