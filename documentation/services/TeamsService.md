# TeamsService

A list of all methods in the `TeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                                                                           |
| :-------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_teams](#list_teams)                                             | This endpoint allows you to list all the teams of your workspace. The response contains the list of teams and a pagination cursor to retrieve the next page. The teams are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `member`.    |
| [create_teams](#create_teams)                                         | This endpoint allows you to create a team. If you are using a personal access token, you need to have an access level superior or equal to `manager`. If a personal access token is being used, the member is automatically added to the created team with permissions `can_manage` and `full_access` |
| [retrieve_team](#retrieve_team)                                       | Retrieve an existing team. If you are using a personal access token, you need to have an access level greater or equal to `member`.                                                                                                                                                                   |
| [update_team](#update_team)                                           | Update a team's name and/or its description. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager. The "All-incidents" team (is_global=true) cannot be updated.                                                                      |
| [delete_team](#delete_team)                                           | Delete an existing team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager. The "All-incidents" team (is_global=true) cannot be deleted.                                                                                          |
| [get_team_resource_access](#get_team_resource_access)                 | Return the permission a team has on a resource. For the global team, it will always be the highest possible permission.                                                                                                                                                                               |
| [set_team_resource_access](#set_team_resource_access)                 | This will create or update a direct access for the team on the resource. If the access to the resource is already given by the team's perimeter, an error is raised. This endpoint is not allowed for the global team.                                                                                |
| [revoke_team_resource_access](#revoke_team_resource_access)           | Revoke the access a team has to a resource. This only works for direct accesses. If the access to the resource is given by the team's perimeter, an error is raised. This endpoint is not allowed for the global team.                                                                                |
| [list_team_secret_incident_access](#list_team_secret_incident_access) | List secret incidents that a team has access to.                                                                                                                                                                                                                                                      |

## list_teams

This endpoint allows you to list all the teams of your workspace. The response contains the list of teams and a pagination cursor to retrieve the next page. The teams are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `member`.

- HTTP Method: `GET`
- Endpoint: `/v1/teams`

**Parameters**

| Name      | Type | Required | Description                                          |
| :-------- | :--- | :------- | :--------------------------------------------------- |
| cursor    | str  | ❌       | Pagination cursor.                                   |
| per_page  | int  | ❌       | Number of items to list per page.                    |
| is_global | bool | ❌       | Filter on/exclude the "All-incidents" team.          |
| search    | str  | ❌       | Search teams based on their name and/or description. |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.list_teams(
    cursor="cursor",
    per_page=20,
    is_global=True,
    search="search"
)

print(result)
```

## create_teams

This endpoint allows you to create a team. If you are using a personal access token, you need to have an access level superior or equal to `manager`. If a personal access token is being used, the member is automatically added to the created team with permissions `can_manage` and `full_access`

- HTTP Method: `POST`
- Endpoint: `/v1/teams`

**Parameters**

| Name         | Type                                                  | Required | Description       |
| :----------- | :---------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateTeamsRequest](../models/CreateTeamsRequest.md) | ❌       | The request body. |

**Return Type**

`Team`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateTeamsRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateTeamsRequest(
    id_=3252,
    name="feature team A",
    description="Description of my team",
    is_global=False,
    gitguardian_url="https://dashboard.gitguardian.com/workspace/1/settings/workspace/teams/1"
)

result = sdk.teams.create_teams(request_body=request_body)

print(result)
```

## retrieve_team

Retrieve an existing team. If you are using a personal access token, you need to have an access level greater or equal to `member`.

- HTTP Method: `GET`
- Endpoint: `/v1/teams/{team_id}`

**Parameters**

| Name    | Type | Required | Description        |
| :------ | :--- | :------- | :----------------- |
| team_id | int  | ✅       | The id of the team |

**Return Type**

`Team`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.retrieve_team(team_id=6)

print(result)
```

## update_team

Update a team's name and/or its description. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager. The "All-incidents" team (is_global=true) cannot be updated.

- HTTP Method: `PATCH`
- Endpoint: `/v1/teams/{team_id}`

**Parameters**

| Name         | Type                      | Required | Description        |
| :----------- | :------------------------ | :------- | :----------------- |
| request_body | [Team](../models/Team.md) | ❌       | The request body.  |
| team_id      | int                       | ✅       | The id of the team |

**Return Type**

`Team`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import Team

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = Team(
    id_=3252,
    name="feature team A",
    description="Description of my team",
    is_global=False,
    gitguardian_url="https://dashboard.gitguardian.com/workspace/1/settings/workspace/teams/1"
)

result = sdk.teams.update_team(
    request_body=request_body,
    team_id=5
)

print(result)
```

## delete_team

Delete an existing team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager. The "All-incidents" team (is_global=true) cannot be deleted.

- HTTP Method: `DELETE`
- Endpoint: `/v1/teams/{team_id}`

**Parameters**

| Name    | Type | Required | Description        |
| :------ | :--- | :------- | :----------------- |
| team_id | int  | ✅       | The id of the team |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.delete_team(team_id=8)

print(result)
```

## get_team_resource_access

Return the permission a team has on a resource. For the global team, it will always be the highest possible permission.

- HTTP Method: `GET`
- Endpoint: `/v1/teams/{team_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                      | Required | Description                          |
| :------------ | :---------------------------------------- | :------- | :----------------------------------- |
| team_id       | int                                       | ✅       | The id of the team                   |
| resource_type | [ResourceType](../models/ResourceType.md) | ✅       | The kind of resource of the access   |
| resource_id   | int                                       | ✅       | The id of the resource of the access |

**Return Type**

`ResourceTeamAccess`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.get_team_resource_access(
    team_id=6,
    resource_type="secret-incidents",
    resource_id=4
)

print(result)
```

## set_team_resource_access

This will create or update a direct access for the team on the resource. If the access to the resource is already given by the team's perimeter, an error is raised. This endpoint is not allowed for the global team.

- HTTP Method: `PUT`
- Endpoint: `/v1/teams/{team_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                                  | Required | Description                          |
| :------------ | :---------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [ResourceTeamAccess](../models/ResourceTeamAccess.md) | ✅       | The request body.                    |
| team_id       | int                                                   | ✅       | The id of the team                   |
| resource_type | [ResourceType](../models/ResourceType.md)             | ✅       | The kind of resource of the access   |
| resource_id   | int                                                   | ✅       | The id of the resource of the access |

**Return Type**

`ResourceTeamAccess`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceTeamAccess, ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ResourceTeamAccess(
    team_id=1345,
    resource_id=3252,
    resource_type="secret-incidents",
    permission="can_view"
)

result = sdk.teams.set_team_resource_access(
    request_body=request_body,
    team_id=9,
    resource_type="secret-incidents",
    resource_id=9
)

print(result)
```

## revoke_team_resource_access

Revoke the access a team has to a resource. This only works for direct accesses. If the access to the resource is given by the team's perimeter, an error is raised. This endpoint is not allowed for the global team.

- HTTP Method: `DELETE`
- Endpoint: `/v1/teams/{team_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                                  | Required | Description                          |
| :------------ | :---------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [ResourceTeamAccess](../models/ResourceTeamAccess.md) | ✅       | The request body.                    |
| team_id       | int                                                   | ✅       | The id of the team                   |
| resource_type | [ResourceType](../models/ResourceType.md)             | ✅       | The kind of resource of the access   |
| resource_id   | int                                                   | ✅       | The id of the resource of the access |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceTeamAccess, ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ResourceTeamAccess(
    team_id=1345,
    resource_id=3252,
    resource_type="secret-incidents",
    permission="can_view"
)

result = sdk.teams.revoke_team_resource_access(
    request_body=request_body,
    team_id=10,
    resource_type="secret-incidents",
    resource_id=0
)

print(result)
```

## list_team_secret_incident_access

List secret incidents that a team has access to.

- HTTP Method: `GET`
- Endpoint: `/v1/teams/{team_id}/secret-incidents`

**Parameters**

| Name                  | Type                                                                                      | Required | Description                                                                                             |
| :-------------------- | :---------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| team_id               | int                                                                                       | ✅       | The id of the team                                                                                      |
| cursor                | str                                                                                       | ❌       | Pagination cursor.                                                                                      |
| page                  | int                                                                                       | ❌       | Page number.                                                                                            |
| per_page              | int                                                                                       | ❌       | Number of items to list per page.                                                                       |
| date_before           | str                                                                                       | ❌       | Entries found before this date.                                                                         |
| date_after            | str                                                                                       | ❌       | Entries found after this date.                                                                          |
| assignee_email        | str                                                                                       | ❌       | Incidents assigned to this email.                                                                       |
| assignee_id           | int                                                                                       | ❌       | Incidents assigned to this user id.                                                                     |
| status                | [StatusEnum](../models/StatusEnum.md)                                                     | ❌       |                                                                                                         |
| severity              | [SeverityEnum](../models/SeverityEnum.md)                                                 | ❌       |                                                                                                         |
| validity              | [ValidityEnum](../models/ValidityEnum.md)                                                 | ❌       |                                                                                                         |
| tags                  | any                                                                                       | ❌       |                                                                                                         |
| ordering              | [ListTeamSecretIncidentAccessOrdering](../models/ListTeamSecretIncidentAccessOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| detector_group_name   | str                                                                                       | ❌       | Incidents belonging to the specified detector group.                                                    |
| ignorer_id            | int                                                                                       | ❌       | Incidents ignored by this user id.                                                                      |
| ignorer_api_token_id  | str                                                                                       | ❌       | Incidents ignored by this API token id.                                                                 |
| resolver_id           | int                                                                                       | ❌       | Incidents resolved by this user id.                                                                     |
| resolver_api_token_id | str                                                                                       | ❌       | Incidents resolved by this API token id.                                                                |

**Return Type**

`List[IncidentWithoutOccurrences]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import StatusEnum, SeverityEnum, ValidityEnum, any, ListTeamSecretIncidentAccessOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tags=any(
    ""
)

result = sdk.teams.list_team_secret_incident_access(
    team_id=1,
    cursor="cursor",
    per_page=20,
    date_before="2019-08-30T14:15:22Z",
    date_after="2019-08-22T14:15:22Z",
    assignee_email="eric@gitguardian.com",
    assignee_id=4932,
    status="IGNORED",
    severity="critical",
    validity="valid",
    tags=tags,
    ordering="date",
    detector_group_name="slackbot_token",
    ignorer_id=4932,
    ignorer_api_token_id="fdf075f9-1662-4cf1-9171-af50568158a8",
    resolver_id=4932,
    resolver_api_token_id="fdf075f9-1662-4cf1-9171-af50568158a8"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
