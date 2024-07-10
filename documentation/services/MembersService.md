# MembersService

A list of all methods in the `MembersService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_members](#list_members)                                             | List members of the workspace.                                                                                                                                                                                                                                                                                                                  |
| [retrieve_member](#retrieve_member)                                       | Retrieve an existing workspace member. If you are using a personal access token, you need to have an access level greater or equal to `member`.                                                                                                                                                                                                 |
| [update_member](#update_member)                                           | Update an existing workspace member. If you are using a personal access token, you need to have an access level greater or equal to `manager`.                                                                                                                                                                                                  |
| [delete_member](#delete_member)                                           | Delete an existing workspace member. If you are using a personal access token, you need to have an access level greater or equal to `manager`.                                                                                                                                                                                                  |
| [list_member_teams](#list_member_teams)                                   | List teams of a workspace member. The response contains the list of teams and a pagination cursor to retrieve the next page. The teams are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `manager` except if the requested member is yourself.                                  |
| [get_member_resource_access](#get_member_resource_access)                 | Return the permission a member has on a resource. The permission is the higher value between the different accesses the member can have (direct access, member's teams accesses, and administrator access).                                                                                                                                     |
| [set_member_resource_access](#set_member_resource_access)                 | This will create or update a direct access for the member on the resource. If the member has higher permission from another source, they will take precedence over those you have given.                                                                                                                                                        |
| [revoke_member_resource_access](#revoke_member_resource_access)           | Revoke a member access to a resource. This only works for direct accesses. If the member has only indirect access, a 404 is returned.                                                                                                                                                                                                           |
| [list_member_secret_incident_access](#list_member_secret_incident_access) | List secret incidents that a member has access to.                                                                                                                                                                                                                                                                                              |
| [list_member_team_memberships](#list_member_team_memberships)             | List team memberships of a workspace member. The response contains the list of team memberships and a pagination cursor to retrieve the next page. The team memberships are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `manager` except if the requested member is yourself. |

## list_members

List members of the workspace.

- HTTP Method: `GET`
- Endpoint: `/v1/members`

**Parameters**

| Name         | Type                                                        | Required | Description                                                                                             |
| :----------- | :---------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| cursor       | str                                                         | ❌       | Pagination cursor.                                                                                      |
| page         | int                                                         | ❌       | Page number.                                                                                            |
| per_page     | int                                                         | ❌       | Number of items to list per page.                                                                       |
| role         | [MemberAccessLevelEnum](../models/MemberAccessLevelEnum.md) | ❌       |                                                                                                         |
| access_level | [MemberAccessLevelEnum](../models/MemberAccessLevelEnum.md) | ❌       |                                                                                                         |
| search       | str                                                         | ❌       | Search members based on their name or email.                                                            |
| ordering     | [ListMembersOrdering](../models/ListMembersOrdering.md)     | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |

**Return Type**

`List[Member]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import MemberAccessLevelEnum, ListMembersOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.members.list_members(
    cursor="cursor",
    per_page=20,
    access_level="owner",
    search="search",
    ordering="created_at"
)

print(result)
```

## retrieve_member

Retrieve an existing workspace member. If you are using a personal access token, you need to have an access level greater or equal to `member`.

- HTTP Method: `GET`
- Endpoint: `/v1/members/{member_id}`

**Parameters**

| Name      | Type | Required | Description                    |
| :-------- | :--- | :------- | :----------------------------- |
| member_id | int  | ✅       | The id of the workspace member |

**Return Type**

`Member`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.members.retrieve_member(member_id=6)

print(result)
```

## update_member

Update an existing workspace member. If you are using a personal access token, you need to have an access level greater or equal to `manager`.

- HTTP Method: `PATCH`
- Endpoint: `/v1/members/{member_id}`

**Parameters**

| Name         | Type                          | Required | Description                    |
| :----------- | :---------------------------- | :------- | :----------------------------- |
| request_body | [Member](../models/Member.md) | ❌       | The request body.              |
| member_id    | int                           | ✅       | The id of the workspace member |

**Return Type**

`Member`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import Member

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = Member(
    id_=3252,
    name="John Smith",
    email="john.smith@example.org",
    role="owner",
    access_level="owner",
    created_at="2023-06-28T16:40:26.897Z",
    last_login="2023-06-28T16:40:26.897Z"
)

result = sdk.members.update_member(
    request_body=request_body,
    member_id=2
)

print(result)
```

## delete_member

Delete an existing workspace member. If you are using a personal access token, you need to have an access level greater or equal to `manager`.

- HTTP Method: `DELETE`
- Endpoint: `/v1/members/{member_id}`

**Parameters**

| Name      | Type | Required | Description                    |
| :-------- | :--- | :------- | :----------------------------- |
| member_id | int  | ✅       | The id of the workspace member |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.members.delete_member(member_id=7)

print(result)
```

## list_member_teams

List teams of a workspace member. The response contains the list of teams and a pagination cursor to retrieve the next page. The teams are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `manager` except if the requested member is yourself.

- HTTP Method: `GET`
- Endpoint: `/v1/members/{member_id}/teams`

**Parameters**

| Name      | Type | Required | Description                                          |
| :-------- | :--- | :------- | :--------------------------------------------------- |
| member_id | int  | ✅       | The id of the workspace member                       |
| cursor    | str  | ❌       | Pagination cursor.                                   |
| per_page  | int  | ❌       | Number of items to list per page.                    |
| search    | str  | ❌       | Search teams based on their name and/or description. |
| is_global | bool | ❌       | Filter on/exclude the "All-incidents" team.          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.members.list_member_teams(
    member_id=4,
    cursor="cursor",
    per_page=20,
    search="search",
    is_global=True
)

print(result)
```

## get_member_resource_access

Return the permission a member has on a resource. The permission is the higher value between the different accesses the member can have (direct access, member's teams accesses, and administrator access).

- HTTP Method: `GET`
- Endpoint: `/v1/members/{member_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                      | Required | Description                          |
| :------------ | :---------------------------------------- | :------- | :----------------------------------- |
| member_id     | int                                       | ✅       | The id of the workspace member       |
| resource_type | [ResourceType](../models/ResourceType.md) | ✅       | The kind of resource of the access   |
| resource_id   | int                                       | ✅       | The id of the resource of the access |

**Return Type**

`ResourceMemberAccess`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.members.get_member_resource_access(
    member_id=6,
    resource_type="secret-incidents",
    resource_id=0
)

print(result)
```

## set_member_resource_access

This will create or update a direct access for the member on the resource. If the member has higher permission from another source, they will take precedence over those you have given.

- HTTP Method: `PUT`
- Endpoint: `/v1/members/{member_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                                      | Required | Description                          |
| :------------ | :-------------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [ResourceMemberAccess](../models/ResourceMemberAccess.md) | ✅       | The request body.                    |
| member_id     | int                                                       | ✅       | The id of the workspace member       |
| resource_type | [ResourceType](../models/ResourceType.md)                 | ✅       | The kind of resource of the access   |
| resource_id   | int                                                       | ✅       | The id of the resource of the access |

**Return Type**

`ResourceMemberAccess`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceMemberAccess, ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ResourceMemberAccess(
    member_id=1345,
    resource_id=3252,
    resource_type="secret-incidents",
    permission="can_view"
)

result = sdk.members.set_member_resource_access(
    request_body=request_body,
    member_id=10,
    resource_type="secret-incidents",
    resource_id=3
)

print(result)
```

## revoke_member_resource_access

Revoke a member access to a resource. This only works for direct accesses. If the member has only indirect access, a 404 is returned.

- HTTP Method: `DELETE`
- Endpoint: `/v1/members/{member_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                                      | Required | Description                          |
| :------------ | :-------------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [ResourceMemberAccess](../models/ResourceMemberAccess.md) | ✅       | The request body.                    |
| member_id     | int                                                       | ✅       | The id of the workspace member       |
| resource_type | [ResourceType](../models/ResourceType.md)                 | ✅       | The kind of resource of the access   |
| resource_id   | int                                                       | ✅       | The id of the resource of the access |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceMemberAccess, ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ResourceMemberAccess(
    member_id=1345,
    resource_id=3252,
    resource_type="secret-incidents",
    permission="can_view"
)

result = sdk.members.revoke_member_resource_access(
    request_body=request_body,
    member_id=1,
    resource_type="secret-incidents",
    resource_id=4
)

print(result)
```

## list_member_secret_incident_access

List secret incidents that a member has access to.

- HTTP Method: `GET`
- Endpoint: `/v1/members/{member_id}/secret-incidents`

**Parameters**

| Name                  | Type                                                                                          | Required | Description                                                                                             |
| :-------------------- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| member_id             | int                                                                                           | ✅       | The id of the workspace member                                                                          |
| cursor                | str                                                                                           | ❌       | Pagination cursor.                                                                                      |
| page                  | int                                                                                           | ❌       | Page number.                                                                                            |
| per_page              | int                                                                                           | ❌       | Number of items to list per page.                                                                       |
| date_before           | str                                                                                           | ❌       | Entries found before this date.                                                                         |
| date_after            | str                                                                                           | ❌       | Entries found after this date.                                                                          |
| assignee_email        | str                                                                                           | ❌       | Incidents assigned to this email.                                                                       |
| assignee_id           | int                                                                                           | ❌       | Incidents assigned to this user id.                                                                     |
| status                | [StatusEnum](../models/StatusEnum.md)                                                         | ❌       |                                                                                                         |
| severity              | [SeverityEnum](../models/SeverityEnum.md)                                                     | ❌       |                                                                                                         |
| validity              | [ValidityEnum](../models/ValidityEnum.md)                                                     | ❌       |                                                                                                         |
| tags                  | any                                                                                           | ❌       |                                                                                                         |
| ordering              | [ListMemberSecretIncidentAccessOrdering](../models/ListMemberSecretIncidentAccessOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| detector_group_name   | str                                                                                           | ❌       | Incidents belonging to the specified detector group.                                                    |
| ignorer_id            | int                                                                                           | ❌       | Incidents ignored by this user id.                                                                      |
| ignorer_api_token_id  | str                                                                                           | ❌       | Incidents ignored by this API token id.                                                                 |
| resolver_id           | int                                                                                           | ❌       | Incidents resolved by this user id.                                                                     |
| resolver_api_token_id | str                                                                                           | ❌       | Incidents resolved by this API token id.                                                                |

**Return Type**

`List[IncidentWithoutOccurrences]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import StatusEnum, SeverityEnum, ValidityEnum, any, ListMemberSecretIncidentAccessOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tags=any(
    ""
)

result = sdk.members.list_member_secret_incident_access(
    member_id=1,
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

## list_member_team_memberships

List team memberships of a workspace member. The response contains the list of team memberships and a pagination cursor to retrieve the next page. The team memberships are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `manager` except if the requested member is yourself.

- HTTP Method: `GET`
- Endpoint: `/v1/members/{member_id}/team_memberships`

**Parameters**

| Name      | Type | Required | Description                       |
| :-------- | :--- | :------- | :-------------------------------- |
| member_id | int  | ✅       | The id of the workspace member    |
| cursor    | str  | ❌       | Pagination cursor.                |
| per_page  | int  | ❌       | Number of items to list per page. |
| team_id   | int  | ❌       | The id of a team to filter on     |

**Return Type**

`List[TeamMembership]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.members.list_member_team_memberships(
    member_id=2,
    cursor="cursor",
    per_page=20,
    team_id=9
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
