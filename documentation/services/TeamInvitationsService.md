# TeamInvitationsService

A list of all methods in the `TeamInvitationsService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                                                                                                                                                                                       |
| :-------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_team_invitation](#list_team_invitation)       | List all existing team invitations. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.                                                        |
| [create_team_invitations](#create_team_invitations) | This endpoint allows you to create a team invitation from an existing team and invitation. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager. |
| [update_team_invitation](#update_team_invitation)   | Update permissions of a team invitation. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.                                                   |
| [delete_team_invitation](#delete_team_invitation)   | Delete an existing team invitation. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.                                                        |

## list_team_invitation

List all existing team invitations. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `GET`
- Endpoint: `/v1/teams/{team_id}/team_invitations`

**Parameters**

| Name                | Type                                                          | Required | Description                          |
| :------------------ | :------------------------------------------------------------ | :------- | :----------------------------------- |
| team_id             | int                                                           | ✅       | The id of the team                   |
| cursor              | str                                                           | ❌       | Pagination cursor.                   |
| per_page            | int                                                           | ❌       | Number of items to list per page.    |
| invitation_id       | int                                                           | ❌       | The id of an invitation to filter on |
| team_permission     | [TeamPermissionEnum](../models/TeamPermissionEnum.md)         | ❌       |                                      |
| incident_permission | [IncidentPermissionEnum](../models/IncidentPermissionEnum.md) | ❌       |                                      |

**Return Type**

`List[TeamInvitation]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import TeamPermissionEnum, IncidentPermissionEnum

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_invitations.list_team_invitation(
    team_id=10,
    cursor="cursor",
    per_page=20,
    invitation_id=10,
    team_permission="can_manage",
    incident_permission="can_view"
)

print(result)
```

## create_team_invitations

This endpoint allows you to create a team invitation from an existing team and invitation. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `POST`
- Endpoint: `/v1/teams/{team_id}/team_invitations`

**Parameters**

| Name         | Type                                                                      | Required | Description        |
| :----------- | :------------------------------------------------------------------------ | :------- | :----------------- |
| request_body | [CreateTeamInvitationsRequest](../models/CreateTeamInvitationsRequest.md) | ❌       | The request body.  |
| team_id      | int                                                                       | ✅       | The id of the team |

**Return Type**

`TeamInvitation`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateTeamInvitationsRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateTeamInvitationsRequest(
    id_=3252,
    invitation_id=4851,
    team_id=991,
    team_permission="can_manage",
    incident_permission="can_view"
)

result = sdk.team_invitations.create_team_invitations(
    request_body=request_body,
    team_id=5
)

print(result)
```

## update_team_invitation

Update permissions of a team invitation. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `PATCH`
- Endpoint: `/v1/teams/{team_id}/team_invitations/{team_invitation_id}`

**Parameters**

| Name               | Type                                                                    | Required | Description                   |
| :----------------- | :---------------------------------------------------------------------- | :------- | :---------------------------- |
| request_body       | [UpdateTeamInvitationRequest](../models/UpdateTeamInvitationRequest.md) | ❌       | The request body.             |
| team_id            | int                                                                     | ✅       | The id of the team            |
| team_invitation_id | int                                                                     | ✅       | The id of the team invitation |

**Return Type**

`TeamInvitation`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import UpdateTeamInvitationRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateTeamInvitationRequest(
    team_permission="can_manage",
    incident_permission="can_view"
)

result = sdk.team_invitations.update_team_invitation(
    request_body=request_body,
    team_id=4,
    team_invitation_id=8
)

print(result)
```

## delete_team_invitation

Delete an existing team invitation. If you are using a personal access token, you must have "can manage" permission on the team or be a workspace manager.

- HTTP Method: `DELETE`
- Endpoint: `/v1/teams/{team_id}/team_invitations/{team_invitation_id}`

**Parameters**

| Name               | Type | Required | Description                   |
| :----------------- | :--- | :------- | :---------------------------- |
| team_id            | int  | ✅       | The id of the team            |
| team_invitation_id | int  | ✅       | The id of the team invitation |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.team_invitations.delete_team_invitation(
    team_id=7,
    team_invitation_id=0
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
