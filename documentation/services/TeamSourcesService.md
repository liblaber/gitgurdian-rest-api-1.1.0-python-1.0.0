# TeamSourcesService

A list of all methods in the `TeamSourcesService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                                                                                                                                    |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_team_sources](#list_team_sources)     | List sources belonging to a team's perimeter.                                                                                                                  |
| [update_team_sources](#update_team_sources) | This endpoint allows you to add and remove sources from the perimeter of a team. If you are using a personal access token, you need to be a workspace manager. |

## list_team_sources

List sources belonging to a team's perimeter.

- HTTP Method: `GET`
- Endpoint: `/v1/teams/{team_id}/sources`

**Parameters**

| Name             | Type                                                                | Required | Description                                                                                             |
| :--------------- | :------------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------ |
| team_id          | int                                                                 | ✅       | The id of the team                                                                                      |
| cursor           | str                                                                 | ❌       | Pagination cursor.                                                                                      |
| per_page         | int                                                                 | ❌       | Number of items to list per page.                                                                       |
| search           | str                                                                 | ❌       | Sources matching this search.                                                                           |
| last_scan_status | [ScanStatusEnum](../models/ScanStatusEnum.md)                       | ❌       |                                                                                                         |
| health           | [SourceHealthEnum](../models/SourceHealthEnum.md)                   | ❌       |                                                                                                         |
| type\_           | [ListTeamSourcesType](../models/ListTeamSourcesType.md)             | ❌       |                                                                                                         |
| ordering         | [ListTeamSourcesOrdering](../models/ListTeamSourcesOrdering.md)     | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| visibility       | [ListTeamSourcesVisibility](../models/ListTeamSourcesVisibility.md) | ❌       |                                                                                                         |
| external_id      | str                                                                 | ❌       | Filter by specific external id.                                                                         |

**Return Type**

`List[Source]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ScanStatusEnum, SourceHealthEnum, ListTeamSourcesType, ListTeamSourcesOrdering, ListTeamSourcesVisibility

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_sources.list_team_sources(
    team_id=8,
    cursor="cursor",
    per_page=20,
    search="test-repository",
    last_scan_status="pending",
    health="safe",
    type_="bitbucket",
    ordering="last_scan_date",
    visibility="public",
    external_id="1"
)

print(result)
```

## update_team_sources

This endpoint allows you to add and remove sources from the perimeter of a team. If you are using a personal access token, you need to be a workspace manager.

- HTTP Method: `POST`
- Endpoint: `/v1/teams/{team_id}/sources`

**Parameters**

| Name         | Type                                                              | Required | Description        |
| :----------- | :---------------------------------------------------------------- | :------- | :----------------- |
| request_body | [UpdateTeamSourcesRequest](../models/UpdateTeamSourcesRequest.md) | ❌       | The request body.  |
| team_id      | int                                                               | ✅       | The id of the team |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import UpdateTeamSourcesRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateTeamSourcesRequest(
    sources_to_add=[
        0
    ],
    sources_to_remove=[
        7
    ]
)

result = sdk.team_sources.update_team_sources(
    request_body=request_body,
    team_id=0
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
