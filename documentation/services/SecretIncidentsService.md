# SecretIncidentsService

A list of all methods in the `SecretIncidentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                                                                              |
| :-------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| [list_incidents](#list_incidents)                                                 | List secret incidents detected by the GitGuardian dashboard. Occurrences are not returned in this route. |
| [retrieve_incidents](#retrieve_incidents)                                         | Retrieve secret incident detected by the GitGuardian dashboard with its occurrences.                     |
| [update_secret_incident](#update_secret_incident)                                 | Update a secret incident                                                                                 |
| [retrieve_incidents_leaks](#retrieve_incidents_leaks)                             | Retrieve where a secret has been publicly leaked.                                                        |
| [assign_incident](#assign_incident)                                               | Assign secret incident detected by the GitGuardian dashboard to a workspace member by email.             |
| [unassign_incident](#unassign_incident)                                           | Unassign secret incident from a workspace member by email.                                               |
| [resolve_incident](#resolve_incident)                                             | Resolve a secret incident detected by the GitGuardian dashboard.                                         |
| [ignore_incident](#ignore_incident)                                               | Ignore a secret incident detected by the GitGuardian dashboard.                                          |
| [reopen_incident](#reopen_incident)                                               | Unresolve or unignore a secret incident detected by the GitGuardian dashboard.                           |
| [share_incident](#share_incident)                                                 | Share a secret incident by creating a public link.                                                       |
| [unshare_incident](#unshare_incident)                                             | Unshare a secret incident by revoking its public link.                                                   |
| [list_secret_incident_member_access](#list_secret_incident_member_access)         | List members that have access to a secret incident.                                                      |
| [list_secret_incident_team_access](#list_secret_incident_team_access)             | List teams that have access to a secret incident.                                                        |
| [list_secret_incident_invitation_access](#list_secret_incident_invitation_access) | List invitations that have access to a secret incident.                                                  |
| [list_sources_incidents](#list_sources_incidents)                                 | List secret incidents linked to a source. Occurrences are not returned in this route.                    |

## list_incidents

List secret incidents detected by the GitGuardian dashboard. Occurrences are not returned in this route.

- HTTP Method: `GET`
- Endpoint: `/v1/incidents/secrets`

**Parameters**

| Name                  | Type                                                        | Required | Description                                                                                             |
| :-------------------- | :---------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| cursor                | str                                                         | ❌       | Pagination cursor.                                                                                      |
| page                  | int                                                         | ❌       | Page number.                                                                                            |
| per_page              | int                                                         | ❌       | Number of items to list per page.                                                                       |
| date_before           | str                                                         | ❌       | Entries found before this date.                                                                         |
| date_after            | str                                                         | ❌       | Entries found after this date.                                                                          |
| assignee_email        | str                                                         | ❌       | Incidents assigned to this email.                                                                       |
| assignee_id           | int                                                         | ❌       | Incidents assigned to this user id.                                                                     |
| status                | [StatusEnum](../models/StatusEnum.md)                       | ❌       |                                                                                                         |
| severity              | [SeverityEnum](../models/SeverityEnum.md)                   | ❌       |                                                                                                         |
| validity              | [ValidityEnum](../models/ValidityEnum.md)                   | ❌       |                                                                                                         |
| tags                  | any                                                         | ❌       |                                                                                                         |
| ordering              | [ListIncidentsOrdering](../models/ListIncidentsOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| detector_group_name   | str                                                         | ❌       | Incidents belonging to the specified detector group.                                                    |
| ignorer_id            | int                                                         | ❌       | Incidents ignored by this user id.                                                                      |
| ignorer_api_token_id  | str                                                         | ❌       | Incidents ignored by this API token id.                                                                 |
| resolver_id           | int                                                         | ❌       | Incidents resolved by this user id.                                                                     |
| resolver_api_token_id | str                                                         | ❌       | Incidents resolved by this API token id.                                                                |

**Return Type**

`List[IncidentWithoutOccurrences]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import StatusEnum, SeverityEnum, ValidityEnum, any, ListIncidentsOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tags=any(
    ""
)

result = sdk.secret_incidents.list_incidents(
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

## retrieve_incidents

Retrieve secret incident detected by the GitGuardian dashboard with its occurrences.

- HTTP Method: `GET`
- Endpoint: `/v1/incidents/secrets/{incident_id}`

**Parameters**

| Name             | Type | Required | Description                                        |
| :--------------- | :--- | :------- | :------------------------------------------------- |
| incident_id      | int  | ✅       | The id of the incident to retrieve                 |
| with_occurrences | int  | ❌       | Retrieve a number of occurrences of this incident. |

**Return Type**

`Incident`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.retrieve_incidents(
    incident_id=1,
    with_occurrences=20
)

print(result)
```

## update_secret_incident

Update a secret incident

- HTTP Method: `PATCH`
- Endpoint: `/v1/incidents/secrets/{incident_id}`

**Parameters**

| Name         | Type                                                                  | Required | Description                        |
| :----------- | :-------------------------------------------------------------------- | :------- | :--------------------------------- |
| request_body | [IncidentWithoutOccurrences](../models/IncidentWithoutOccurrences.md) | ❌       | The request body.                  |
| incident_id  | int                                                                   | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentWithoutOccurrences`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import IncidentWithoutOccurrences

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = IncidentWithoutOccurrences(
    id_=3759,
    date_="2019-08-22T14:15:22Z",
    detector={
        "name": "slack_bot_token",
        "display_name": "Slack Bot Token",
        "nature": "specific",
        "family": "apikey",
        "detector_group_name": "slackbot_token",
        "detector_group_display_name": "Slack Bot Token"
    },
    secret_hash="Ri9FjVgdOlPnBmujoxP4XPJcbe82BhJXB/SAngijw/juCISuOMgPzYhV28m6OG24",
    hmsl_hash="05975add34ddc9a38a0fb57c7d3e676ffed57080516fc16bf8d8f14308fedb86",
    gitguardian_url="https://dashboard.gitguardian.com/workspace/1/incidents/3899",
    regression=True,
    status="IGNORED",
    assignee_id=309,
    assignee_email="eric@gitguardian.com",
    occurrences_count=4,
    ignore_reason="test_credential",
    triggered_at="2019-05-12T09:37:49Z",
    ignored_at="2019-08-24T14:15:22Z",
    ignorer_id=309,
    ignorer_api_token_id="fdf075f9-1662-4cf1-9171-af50568158a8",
    resolver_id=395,
    resolver_api_token_id="fdf075f9-1662-4cf1-9171-af50568158a8",
    secret_revoked=False,
    severity="critical",
    validity="valid",
    resolved_at="resolved_at",
    share_url="https://dashboard.gitguardian.com/share/incidents/11111111-1111-1111-1111-111111111111",
    tags=[
        "DEFAULT_BRANCH"
    ],
    occurrences=[
        {
            "id_": 4421,
            "incident_id": 3759,
            "kind": "Realtime",
            "source": {
                "id_": 6531,
                "url": "https://github.com/GitGuardian/gg-shield",
                "type_": "github",
                "full_name": "gitguardian/gg-shield",
                "health": "safe",
                "default_branch": "main",
                "default_branch_head": "abcd97b4aaf927ea934504263322e75e86c31xyz",
                "open_incidents_count": 3,
                "closed_incidents_count": 2,
                "secret_incidents_breakdown": {
                    "open_secret_incidents": {
                        "total": 9,
                        "severity_breakdown": {
                            "critical": 8,
                            "high": 2,
                            "medium": 3,
                            "low": 6,
                            "info": 7,
                            "unknown": 1
                        }
                    },
                    "closed_secret_incidents": {
                        "total": 9,
                        "severity_breakdown": {
                            "critical": 8,
                            "high": 2,
                            "medium": 3,
                            "low": 6,
                            "info": 7,
                            "unknown": 1
                        }
                    }
                },
                "visibility": "public",
                "external_id": "125",
                "source_criticality": "critical",
                "last_scan": {
                    "date_": "2021-05-20T12:40:55.662949Z",
                    "status": "pending",
                    "failing_reason": "DMCA takedown",
                    "commits_scanned": 123,
                    "branches_scanned": 2,
                    "duration": "1:30.454444"
                },
                "monitored": True
            },
            "author_name": "Eric",
            "author_info": "eric@gitguardian.com",
            "date_": "2021-05-20T12:40:55.662949Z",
            "url": "https://github.com/prm-dev-team/QATest_staging/commit/76dd18a2a8d27eaf00a45851cc7731c53b59ed19#diff-0f372f3171c8f13a15a22a1081487ed54fa70ad088e17c6c6386196a179a04ffR1",
            "matches": [
                {
                    "name": "apikey",
                    "indice_start": 32,
                    "indice_end": 79,
                    "pre_line_start": 2,
                    "pre_line_end": 8,
                    "post_line_start": 1,
                    "post_line_end": 1
                }
            ],
            "tags": [
                "DEFAULT_BRANCH"
            ],
            "sha": "d670460b4b4aece5915caf5c68d12f560a9fe3e4",
            "presence": "present",
            "filepath": "test_data/12123testfile.txt"
        }
    ]
)

result = sdk.secret_incidents.update_secret_incident(
    request_body=request_body,
    incident_id=4
)

print(result)
```

## retrieve_incidents_leaks

Retrieve where a secret has been publicly leaked.

- HTTP Method: `GET`
- Endpoint: `/v1/incidents/secrets/{incident_id}/leaks`

**Parameters**

| Name        | Type | Required | Description                        |
| :---------- | :--- | :------- | :--------------------------------- |
| incident_id | int  | ✅       | The id of the incident to retrieve |

**Return Type**

`List[RetrieveIncidentsLeaksOkResponse]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.retrieve_incidents_leaks(incident_id=7)

print(result)
```

## assign_incident

Assign secret incident detected by the GitGuardian dashboard to a workspace member by email.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/assign`

**Parameters**

| Name         | Type                                                        | Required | Description                        |
| :----------- | :---------------------------------------------------------- | :------- | :--------------------------------- |
| request_body | [AssignIncidentRequest](../models/AssignIncidentRequest.md) | ❌       | The request body.                  |
| incident_id  | int                                                         | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentWithoutOccurrences`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import AssignIncidentRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = AssignIncidentRequest(
    email="eric@gitguardian.com",
    member_id=4295
)

result = sdk.secret_incidents.assign_incident(
    request_body=request_body,
    incident_id=8
)

print(result)
```

## unassign_incident

Unassign secret incident from a workspace member by email.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/unassign`

**Parameters**

| Name        | Type | Required | Description                        |
| :---------- | :--- | :------- | :--------------------------------- |
| incident_id | int  | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentWithoutOccurrences`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.unassign_incident(incident_id=9)

print(result)
```

## resolve_incident

Resolve a secret incident detected by the GitGuardian dashboard.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/resolve`

**Parameters**

| Name         | Type                                                          | Required | Description                        |
| :----------- | :------------------------------------------------------------ | :------- | :--------------------------------- |
| request_body | [ResolveIncidentRequest](../models/ResolveIncidentRequest.md) | ❌       | The request body.                  |
| incident_id  | int                                                           | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentWithoutOccurrences`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ResolveIncidentRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ResolveIncidentRequest(
    secret_revoked=True
)

result = sdk.secret_incidents.resolve_incident(
    request_body=request_body,
    incident_id=5
)

print(result)
```

## ignore_incident

Ignore a secret incident detected by the GitGuardian dashboard.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/ignore`

**Parameters**

| Name         | Type                                                        | Required | Description                        |
| :----------- | :---------------------------------------------------------- | :------- | :--------------------------------- |
| request_body | [IgnoreIncidentRequest](../models/IgnoreIncidentRequest.md) | ❌       | The request body.                  |
| incident_id  | int                                                         | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentWithoutOccurrences`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import IgnoreIncidentRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = IgnoreIncidentRequest(
    ignore_reason="test_credential"
)

result = sdk.secret_incidents.ignore_incident(
    request_body=request_body,
    incident_id=9
)

print(result)
```

## reopen_incident

Unresolve or unignore a secret incident detected by the GitGuardian dashboard.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/reopen`

**Parameters**

| Name        | Type | Required | Description                        |
| :---------- | :--- | :------- | :--------------------------------- |
| incident_id | int  | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentWithoutOccurrences`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.reopen_incident(incident_id=9)

print(result)
```

## share_incident

Share a secret incident by creating a public link.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/share`

**Parameters**

| Name         | Type                                                      | Required | Description                        |
| :----------- | :-------------------------------------------------------- | :------- | :--------------------------------- |
| request_body | [ShareIncidentRequest](../models/ShareIncidentRequest.md) | ❌       | The request body.                  |
| incident_id  | int                                                       | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentToken`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ShareIncidentRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ShareIncidentRequest(
    auto_healing=True,
    feedback_collection=True,
    lifespan=720
)

result = sdk.secret_incidents.share_incident(
    request_body=request_body,
    incident_id=7
)

print(result)
```

## unshare_incident

Unshare a secret incident by revoking its public link.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/unshare`

**Parameters**

| Name        | Type | Required | Description                        |
| :---------- | :--- | :------- | :--------------------------------- |
| incident_id | int  | ✅       | The id of the incident to retrieve |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.unshare_incident(incident_id=8)

print(result)
```

## list_secret_incident_member_access

List members that have access to a secret incident.

- HTTP Method: `GET`
- Endpoint: `/v1/secret-incidents/{incident_id}/members`

**Parameters**

| Name          | Type                                                                                          | Required | Description                                                                                             |
| :------------ | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| incident_id   | int                                                                                           | ✅       | The id of the incident to retrieve                                                                      |
| cursor        | str                                                                                           | ❌       | Pagination cursor.                                                                                      |
| per_page      | int                                                                                           | ❌       | Number of items to list per page.                                                                       |
| role          | [MemberAccessLevelEnum](../models/MemberAccessLevelEnum.md)                                   | ❌       |                                                                                                         |
| access_level  | [MemberAccessLevelEnum](../models/MemberAccessLevelEnum.md)                                   | ❌       |                                                                                                         |
| search        | str                                                                                           | ❌       | Search members based on their name or email.                                                            |
| ordering      | [ListSecretIncidentMemberAccessOrdering](../models/ListSecretIncidentMemberAccessOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| direct_access | bool                                                                                          | ❌       | Filter on direct or indirect accesses.                                                                  |

**Return Type**

`List[Member]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import MemberAccessLevelEnum, ListSecretIncidentMemberAccessOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.list_secret_incident_member_access(
    incident_id=4,
    cursor="cursor",
    per_page=20,
    role="owner",
    access_level="owner",
    search="search",
    ordering="created_at",
    direct_access=False
)

print(result)
```

## list_secret_incident_team_access

List teams that have access to a secret incident.

- HTTP Method: `GET`
- Endpoint: `/v1/secret-incidents/{incident_id}/teams`

**Parameters**

| Name          | Type | Required | Description                                          |
| :------------ | :--- | :------- | :--------------------------------------------------- |
| incident_id   | int  | ✅       | The id of the incident to retrieve                   |
| cursor        | str  | ❌       | Pagination cursor.                                   |
| per_page      | int  | ❌       | Number of items to list per page.                    |
| search        | str  | ❌       | Search teams based on their name and/or description. |
| direct_access | bool | ❌       | Filter on direct or indirect accesses.               |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.list_secret_incident_team_access(
    incident_id=2,
    cursor="cursor",
    per_page=20,
    search="search",
    direct_access=True
)

print(result)
```

## list_secret_incident_invitation_access

List invitations that have access to a secret incident.

- HTTP Method: `GET`
- Endpoint: `/v1/secret-incidents/{incident_id}/invitations`

**Parameters**

| Name          | Type                                                                                                  | Required | Description                                                                                             |
| :------------ | :---------------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| incident_id   | int                                                                                                   | ✅       | The id of the incident to retrieve                                                                      |
| cursor        | str                                                                                                   | ❌       | Pagination cursor.                                                                                      |
| per_page      | int                                                                                                   | ❌       | Number of items to list per page.                                                                       |
| search        | str                                                                                                   | ❌       | Search invitations based on the email field.                                                            |
| ordering      | [ListSecretIncidentInvitationAccessOrdering](../models/ListSecretIncidentInvitationAccessOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| direct_access | bool                                                                                                  | ❌       | Filter on direct or indirect accesses.                                                                  |

**Return Type**

`List[Invitation]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ListSecretIncidentInvitationAccessOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incidents.list_secret_incident_invitation_access(
    incident_id=1,
    cursor="cursor",
    per_page=20,
    search="search",
    ordering="date",
    direct_access=False
)

print(result)
```

## list_sources_incidents

List secret incidents linked to a source. Occurrences are not returned in this route.

- HTTP Method: `GET`
- Endpoint: `/v1/sources/{source_id}/incidents/secrets`

**Parameters**

| Name                  | Type                                                                      | Required | Description                                                                                             |
| :-------------------- | :------------------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------ |
| source_id             | int                                                                       | ✅       | The id of the source to filter on.                                                                      |
| cursor                | str                                                                       | ❌       | Pagination cursor.                                                                                      |
| per_page              | int                                                                       | ❌       | Number of items to list per page.                                                                       |
| date_before           | str                                                                       | ❌       | Entries found before this date.                                                                         |
| date_after            | str                                                                       | ❌       | Entries found after this date.                                                                          |
| assignee_email        | str                                                                       | ❌       | Incidents assigned to this email.                                                                       |
| assignee_id           | int                                                                       | ❌       | Incidents assigned to this user id.                                                                     |
| status                | [StatusEnum](../models/StatusEnum.md)                                     | ❌       |                                                                                                         |
| severity              | [SeverityEnum](../models/SeverityEnum.md)                                 | ❌       |                                                                                                         |
| validity              | [ValidityEnum](../models/ValidityEnum.md)                                 | ❌       |                                                                                                         |
| tags                  | any                                                                       | ❌       |                                                                                                         |
| ordering              | [ListSourcesIncidentsOrdering](../models/ListSourcesIncidentsOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| detector_group_name   | str                                                                       | ❌       | Incidents belonging to the specified detector group.                                                    |
| ignorer_id            | int                                                                       | ❌       | Incidents ignored by this user id.                                                                      |
| ignorer_api_token_id  | str                                                                       | ❌       | Incidents ignored by this API token id.                                                                 |
| resolver_id           | int                                                                       | ❌       | Incidents resolved by this user id.                                                                     |
| resolver_api_token_id | str                                                                       | ❌       | Incidents resolved by this API token id.                                                                |

**Return Type**

`List[IncidentWithoutOccurrences]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import StatusEnum, SeverityEnum, ValidityEnum, any, ListSourcesIncidentsOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tags=any(
    ""
)

result = sdk.secret_incidents.list_sources_incidents(
    source_id=5523,
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
