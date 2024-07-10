# TeamRequestsService

A list of all methods in the `TeamRequestsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                                                                                                                                                                                                              |
| :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_team_requests](#list_team_requests)               | List pending requests of a team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.                                                                                  |
| [create_team_request](#create_team_request)             | Create an access request to a team. You must be authenticated via a Personal Access Token. You must not already have a pending request on the team, be a member of the team, be a workspace manager or have the restricted access level. |
| [delete_team_request](#delete_team_request)             | Cancel or decline a team request. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager, or be the member who created the request being cancelled.                       |
| [accept_team_request](#accept_team_request)             | Accept a team request by adding the member to the team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.                                                           |
| [list_member_team_requests](#list_member_team_requests) | List pending team requests of a member. If you are using a personal access token, you need to be either a workspace manager or the member being queried.                                                                                 |

## list_team_requests

List pending requests of a team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `GET`
- Endpoint: `/v1/teams/{team_id}/team_requests`

**Parameters**

| Name      | Type  | Required | Description                                   |
| :-------- | :---- | :------- | :-------------------------------------------- |
| team_id   | int   | ✅       | The id of the team                            |
| cursor    | str   | ❌       | Pagination cursor.                            |
| per_page  | int   | ❌       | Number of items to list per page.             |
| member_id | float | ❌       | Filter requests coming from a specific member |

**Return Type**

`List[TeamRequest]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_requests.list_team_requests(
    team_id=0,
    cursor="cursor",
    per_page=20,
    member_id=1234
)

print(result)
```

## create_team_request

Create an access request to a team. You must be authenticated via a Personal Access Token. You must not already have a pending request on the team, be a member of the team, be a workspace manager or have the restricted access level.

- HTTP Method: `POST`
- Endpoint: `/v1/teams/{team_id}/team_requests`

**Parameters**

| Name    | Type | Required | Description        |
| :------ | :--- | :------- | :----------------- |
| team_id | int  | ✅       | The id of the team |

**Return Type**

`TeamRequest`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_requests.create_team_request(team_id=9)

print(result)
```

## delete_team_request

Cancel or decline a team request. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager, or be the member who created the request being cancelled.

- HTTP Method: `DELETE`
- Endpoint: `/v1/teams/{team_id}/team_requests/{team_request_id}`

**Parameters**

| Name            | Type | Required | Description                |
| :-------------- | :--- | :------- | :------------------------- |
| team_id         | int  | ✅       | The id of the team         |
| team_request_id | int  | ✅       | The id of the team request |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_requests.delete_team_request(
    team_id=7,
    team_request_id=1
)

print(result)
```

## accept_team_request

Accept a team request by adding the member to the team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `POST`
- Endpoint: `/v1/teams/{team_id}/team_requests/{team_request_id}/accept`

**Parameters**

| Name            | Type                                                              | Required | Description                |
| :-------------- | :---------------------------------------------------------------- | :------- | :------------------------- |
| request_body    | [AcceptTeamRequestRequest](../models/AcceptTeamRequestRequest.md) | ❌       | The request body.          |
| team_id         | int                                                               | ✅       | The id of the team         |
| team_request_id | int                                                               | ✅       | The id of the team request |

**Return Type**

`TeamMembership`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import AcceptTeamRequestRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AcceptTeamRequestRequest(
    team_permission="can_manage",
    incident_permission="can_view"
)

result = sdk.team_requests.accept_team_request(
    request_body=request_body,
    team_id=10,
    team_request_id=1
)

print(result)
```

## list_member_team_requests

List pending team requests of a member. If you are using a personal access token, you need to be either a workspace manager or the member being queried.

- HTTP Method: `GET`
- Endpoint: `/v1/members/{member_id}/team_requests`

**Parameters**

| Name      | Type  | Required | Description                        |
| :-------- | :---- | :------- | :--------------------------------- |
| member_id | int   | ✅       | The id of the workspace member     |
| cursor    | str   | ❌       | Pagination cursor.                 |
| per_page  | int   | ❌       | Number of items to list per page.  |
| team_id   | float | ❌       | Filter requests to a specific team |

**Return Type**

`List[TeamRequest]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_requests.list_member_team_requests(
    member_id=7,
    cursor="cursor",
    per_page=20,
    team_id=1234
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
