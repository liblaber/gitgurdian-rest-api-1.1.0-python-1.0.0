# TeamMembershipsService

A list of all methods in the `TeamMembershipsService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                                                                                         |
| :------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_team_memberships](#list_team_memberships)   | List all the memberships of a team. If you are using a personal access token, you need to be a workspace manager or be part of the team.                                            |
| [create_team_membership](#create_team_membership) | Add a member to a team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.                                      |
| [update_team_membership](#update_team_membership) | Update permissions of a team membership. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.                     |
| [delete_team_membership](#delete_team_membership) | Remove a member from a team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager, or be the member being removed. |

## list_team_memberships

List all the memberships of a team. If you are using a personal access token, you need to be a workspace manager or be part of the team.

- HTTP Method: `GET`
- Endpoint: `/v1/teams/{team_id}/team_memberships`

**Parameters**

| Name                | Type                                                          | Required | Description                                  |
| :------------------ | :------------------------------------------------------------ | :------- | :------------------------------------------- |
| team_id             | int                                                           | ✅       | The id of the team                           |
| cursor              | str                                                           | ❌       | Pagination cursor.                           |
| per_page            | int                                                           | ❌       | Number of items to list per page.            |
| team_permission     | [TeamPermissionEnum](../models/TeamPermissionEnum.md)         | ❌       |                                              |
| incident_permission | [IncidentPermissionEnum](../models/IncidentPermissionEnum.md) | ❌       |                                              |
| member_id           | float                                                         | ❌       | Filter team memberships on a specific member |

**Return Type**

`List[TeamMembership]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import TeamPermissionEnum, IncidentPermissionEnum

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_memberships.list_team_memberships(
    team_id=1,
    cursor="cursor",
    per_page=20,
    team_permission="can_manage",
    incident_permission="can_view",
    member_id=1234
)

print(result)
```

## create_team_membership

Add a member to a team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `POST`
- Endpoint: `/v1/teams/{team_id}/team_memberships`

**Parameters**

| Name         | Type                                          | Required | Description        |
| :----------- | :-------------------------------------------- | :------- | :----------------- |
| request_body | [TeamMembership](../models/TeamMembership.md) | ❌       | The request body.  |
| team_id      | int                                           | ✅       | The id of the team |

**Return Type**

`TeamMembership`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import TeamMembership

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = TeamMembership(
    id_=1234,
    member_id=2489,
    team_id=4285,
    team_permission="can_manage",
    incident_permission="can_view"
)

result = sdk.team_memberships.create_team_membership(
    request_body=request_body,
    team_id=2
)

print(result)
```

## update_team_membership

Update permissions of a team membership. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `PATCH`
- Endpoint: `/v1/teams/{team_id}/team_memberships/{team_membership_id}`

**Parameters**

| Name               | Type                                                                    | Required | Description                   |
| :----------------- | :---------------------------------------------------------------------- | :------- | :---------------------------- |
| request_body       | [UpdateTeamMembershipRequest](../models/UpdateTeamMembershipRequest.md) | ❌       | The request body.             |
| team_id            | int                                                                     | ✅       | The id of the team            |
| team_membership_id | int                                                                     | ✅       | The id of the team membership |

**Return Type**

`TeamMembership`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import UpdateTeamMembershipRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateTeamMembershipRequest(
    team_permission="can_manage",
    incident_permission="can_view"
)

result = sdk.team_memberships.update_team_membership(
    request_body=request_body,
    team_id=5,
    team_membership_id=2
)

print(result)
```

## delete_team_membership

Remove a member from a team. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager, or be the member being removed.

- HTTP Method: `DELETE`
- Endpoint: `/v1/teams/{team_id}/team_memberships/{team_membership_id}`

**Parameters**

| Name               | Type | Required | Description                   |
| :----------------- | :--- | :------- | :---------------------------- |
| team_id            | int  | ✅       | The id of the team            |
| team_membership_id | int  | ✅       | The id of the team membership |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_memberships.delete_team_membership(
    team_id=10,
    team_membership_id=5
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
