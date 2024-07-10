# InvitationsService

A list of all methods in the `InvitationsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                                                                                                                                                                                                                                                                            |
| :-------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_invitations](#list_invitations)                                             | This endpoint allows you to list all pending invitations. The response contains the list of invitations and a pagination cursor to retrieve the next page. The invitations are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `member`. |
| [create_invitations](#create_invitations)                                         | This endpoint allows you to send an invitation to a user. If you are using a personal access token, you need to have an access level superior or equal to `member`.                                                                                                                                    |
| [delete_invitation](#delete_invitation)                                           | Delete an existing invitation. If you are using a personal access token, you need to have an access level superior or equal to `manager`.                                                                                                                                                              |
| [resend_invitation](#resend_invitation)                                           | Resend an existing invitation. If you are using a personal access token, you need to have an access level superior or equal to `manager`.                                                                                                                                                              |
| [get_invitation_resource_access](#get_invitation_resource_access)                 | Return the permission an invitation has on a resource. If the invitation has an admin access level, it will be the highest possible value.                                                                                                                                                             |
| [set_invitation_resource_access](#set_invitation_resource_access)                 | This will create or update a direct access for the invitation on the resource. If the invitation has an administrator access level, it will take precedence over the permission you have given.                                                                                                        |
| [revoke_invitation_resource_access](#revoke_invitation_resource_access)           | Revoke an invitation access to a resource. This only works for direct accesses. If the access is from the administrator access level of the invitation, a 404 is returned.                                                                                                                             |
| [list_invitation_secret_incident_access](#list_invitation_secret_incident_access) | List secret incidents that an invitation has access to.                                                                                                                                                                                                                                                |

## list_invitations

This endpoint allows you to list all pending invitations. The response contains the list of invitations and a pagination cursor to retrieve the next page. The invitations are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `member`.

- HTTP Method: `GET`
- Endpoint: `/v1/invitations`

**Parameters**

| Name     | Type                                                            | Required | Description                                                                                             |
| :------- | :-------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| cursor   | str                                                             | ❌       | Pagination cursor.                                                                                      |
| per_page | int                                                             | ❌       | Number of items to list per page.                                                                       |
| search   | str                                                             | ❌       | Search invitations based on the email field.                                                            |
| ordering | [ListInvitationsOrdering](../models/ListInvitationsOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |

**Return Type**

`List[Invitation]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ListInvitationsOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invitations.list_invitations(
    cursor="cursor",
    per_page=20,
    search="search",
    ordering="date"
)

print(result)
```

## create_invitations

This endpoint allows you to send an invitation to a user. If you are using a personal access token, you need to have an access level superior or equal to `member`.

- HTTP Method: `POST`
- Endpoint: `/v1/invitations`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateInvitationsRequest](../models/CreateInvitationsRequest.md) | ❌       | The request body. |

**Return Type**

`Invitation`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateInvitationsRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateInvitationsRequest(
    email="eric@gitguardian.com",
    role="manager",
    access_level="manager"
)

result = sdk.invitations.create_invitations(request_body=request_body)

print(result)
```

## delete_invitation

Delete an existing invitation. If you are using a personal access token, you need to have an access level superior or equal to `manager`.

- HTTP Method: `DELETE`
- Endpoint: `/v1/invitations/{invitation_id}`

**Parameters**

| Name          | Type | Required | Description                          |
| :------------ | :--- | :------- | :----------------------------------- |
| invitation_id | int  | ✅       | The id of the invitation to retrieve |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invitations.delete_invitation(invitation_id=0)

print(result)
```

## resend_invitation

Resend an existing invitation. If you are using a personal access token, you need to have an access level superior or equal to `manager`.

- HTTP Method: `POST`
- Endpoint: `/v1/invitations/{invitation_id}/resend`

**Parameters**

| Name          | Type | Required | Description                          |
| :------------ | :--- | :------- | :----------------------------------- |
| request_body  | dict | ❌       | The request body.                    |
| invitation_id | int  | ✅       | The id of the invitation to retrieve |

**Return Type**

`ResendInvitationOkResponse`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import dict

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = {}

result = sdk.invitations.resend_invitation(
    request_body=request_body,
    invitation_id=7
)

print(result)
```

## get_invitation_resource_access

Return the permission an invitation has on a resource. If the invitation has an admin access level, it will be the highest possible value.

- HTTP Method: `GET`
- Endpoint: `/v1/invitations/{invitation_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                      | Required | Description                          |
| :------------ | :---------------------------------------- | :------- | :----------------------------------- |
| invitation_id | int                                       | ✅       | The id of the invitation to retrieve |
| resource_type | [ResourceType](../models/ResourceType.md) | ✅       | The kind of resource of the access   |
| resource_id   | int                                       | ✅       | The id of the resource of the access |

**Return Type**

`ResourceInvitationAccess`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.invitations.get_invitation_resource_access(
    invitation_id=1,
    resource_type="secret-incidents",
    resource_id=8
)

print(result)
```

## set_invitation_resource_access

This will create or update a direct access for the invitation on the resource. If the invitation has an administrator access level, it will take precedence over the permission you have given.

- HTTP Method: `PUT`
- Endpoint: `/v1/invitations/{invitation_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                                              | Required | Description                          |
| :------------ | :---------------------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [ResourceInvitationAccess](../models/ResourceInvitationAccess.md) | ✅       | The request body.                    |
| invitation_id | int                                                               | ✅       | The id of the invitation to retrieve |
| resource_type | [ResourceType](../models/ResourceType.md)                         | ✅       | The kind of resource of the access   |
| resource_id   | int                                                               | ✅       | The id of the resource of the access |

**Return Type**

`ResourceInvitationAccess`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceInvitationAccess, ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ResourceInvitationAccess(
    invitation_id=1345,
    resource_id=3252,
    resource_type="secret-incidents",
    permission="can_view"
)

result = sdk.invitations.set_invitation_resource_access(
    request_body=request_body,
    invitation_id=5,
    resource_type="secret-incidents",
    resource_id=5
)

print(result)
```

## revoke_invitation_resource_access

Revoke an invitation access to a resource. This only works for direct accesses. If the access is from the administrator access level of the invitation, a 404 is returned.

- HTTP Method: `DELETE`
- Endpoint: `/v1/invitations/{invitation_id}/{resource_type}/{resource_id}`

**Parameters**

| Name          | Type                                                              | Required | Description                          |
| :------------ | :---------------------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [ResourceInvitationAccess](../models/ResourceInvitationAccess.md) | ✅       | The request body.                    |
| invitation_id | int                                                               | ✅       | The id of the invitation to retrieve |
| resource_type | [ResourceType](../models/ResourceType.md)                         | ✅       | The kind of resource of the access   |
| resource_id   | int                                                               | ✅       | The id of the resource of the access |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResourceInvitationAccess, ResourceType

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ResourceInvitationAccess(
    invitation_id=1345,
    resource_id=3252,
    resource_type="secret-incidents",
    permission="can_view"
)

result = sdk.invitations.revoke_invitation_resource_access(
    request_body=request_body,
    invitation_id=5,
    resource_type="secret-incidents",
    resource_id=8
)

print(result)
```

## list_invitation_secret_incident_access

List secret incidents that an invitation has access to.

- HTTP Method: `GET`
- Endpoint: `/v1/invitations/{invitation_id}/secret-incidents`

**Parameters**

| Name                  | Type                                                                                                  | Required | Description                                                                                             |
| :-------------------- | :---------------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| invitation_id         | int                                                                                                   | ✅       | The id of the invitation to retrieve                                                                    |
| cursor                | str                                                                                                   | ❌       | Pagination cursor.                                                                                      |
| page                  | int                                                                                                   | ❌       | Page number.                                                                                            |
| per_page              | int                                                                                                   | ❌       | Number of items to list per page.                                                                       |
| date_before           | str                                                                                                   | ❌       | Entries found before this date.                                                                         |
| date_after            | str                                                                                                   | ❌       | Entries found after this date.                                                                          |
| assignee_email        | str                                                                                                   | ❌       | Incidents assigned to this email.                                                                       |
| assignee_id           | int                                                                                                   | ❌       | Incidents assigned to this user id.                                                                     |
| status                | [StatusEnum](../models/StatusEnum.md)                                                                 | ❌       |                                                                                                         |
| severity              | [SeverityEnum](../models/SeverityEnum.md)                                                             | ❌       |                                                                                                         |
| validity              | [ValidityEnum](../models/ValidityEnum.md)                                                             | ❌       |                                                                                                         |
| tags                  | any                                                                                                   | ❌       |                                                                                                         |
| ordering              | [ListInvitationSecretIncidentAccessOrdering](../models/ListInvitationSecretIncidentAccessOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| detector_group_name   | str                                                                                                   | ❌       | Incidents belonging to the specified detector group.                                                    |
| ignorer_id            | int                                                                                                   | ❌       | Incidents ignored by this user id.                                                                      |
| ignorer_api_token_id  | str                                                                                                   | ❌       | Incidents ignored by this API token id.                                                                 |
| resolver_id           | int                                                                                                   | ❌       | Incidents resolved by this user id.                                                                     |
| resolver_api_token_id | str                                                                                                   | ❌       | Incidents resolved by this API token id.                                                                |

**Return Type**

`List[IncidentWithoutOccurrences]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import StatusEnum, SeverityEnum, ValidityEnum, any, ListInvitationSecretIncidentAccessOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tags=any(
    ""
)

result = sdk.invitations.list_invitation_secret_incident_access(
    invitation_id=0,
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
