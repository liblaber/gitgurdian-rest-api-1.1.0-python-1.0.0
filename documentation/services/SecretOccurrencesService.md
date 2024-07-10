# SecretOccurrencesService

A list of all methods in the `SecretOccurrencesService` service. Click on the method name to view detailed information about that method.

| Methods                 | Description                                             |
| :---------------------- | :------------------------------------------------------ |
| [list_occs](#list_occs) | List occurrences of secrets in the monitored perimeter. |

## list_occs

List occurrences of secrets in the monitored perimeter.

- HTTP Method: `GET`
- Endpoint: `/v1/occurrences/secrets`

**Parameters**

| Name        | Type                                                                | Required | Description                                                                                             |
| :---------- | :------------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------ |
| cursor      | str                                                                 | ❌       | Pagination cursor.                                                                                      |
| page        | int                                                                 | ❌       | Page number.                                                                                            |
| per_page    | int                                                                 | ❌       | Number of items to list per page.                                                                       |
| date_before | str                                                                 | ❌       | Entries found before this date.                                                                         |
| date_after  | str                                                                 | ❌       | Entries found after this date.                                                                          |
| source_id   | int                                                                 | ❌       | Filter on the source ID.                                                                                |
| source_name | str                                                                 | ❌       | Entries matching this source name search.                                                               |
| source_type | [SourceTypeQueryParamsEnum](../models/SourceTypeQueryParamsEnum.md) | ❌       |                                                                                                         |
| incident_id | int                                                                 | ❌       | Filter by incident ID.                                                                                  |
| presence    | [PresenceEnum](../models/PresenceEnum.md)                           | ❌       |                                                                                                         |
| author_name | str                                                                 | ❌       | Entries matching this author name search.                                                               |
| author_info | str                                                                 | ❌       | Entries matching this author email search.                                                              |
| sha         | str                                                                 | ❌       | Entries starting with the commit sha search string.                                                     |
| filepath    | str                                                                 | ❌       | Entries matching this filepath search.                                                                  |
| tags        | any                                                                 | ❌       |                                                                                                         |
| ordering    | [ListOccsOrdering](../models/ListOccsOrdering.md)                   | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |

**Return Type**

`List[VcsOccurrence]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import SourceTypeQueryParamsEnum, PresenceEnum, any, ListOccsOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tags=any(
    ""
)

result = sdk.secret_occurrences.list_occs(
    cursor="cursor",
    per_page=20,
    date_before="2019-08-30T14:15:22Z",
    date_after="2019-08-22T14:15:22Z",
    source_id=5523,
    source_name="gitguardian/test-repository",
    source_type="bitbucket",
    incident_id=2,
    presence="present",
    author_name="John Doe",
    author_info="john.doe@gitguardian.com",
    sha="fccebf0562698ab99dc10dcb2e864fc563b25ac4",
    filepath="myfile.txt",
    tags=tags,
    ordering="date"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
