# SecretIncidentNotesService

A list of all methods in the `SecretIncidentNotesService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                         |
| :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| [list_incident_notes](#list_incident_notes)   | List notes left on a secret incident in chronological order.                                                        |
| [create_incident_note](#create_incident_note) | Add a note on a secret incident.                                                                                    |
| [update_incident_note](#update_incident_note) | Update an existing comment on a secret incident. Only incident notes created by the current API key can be updated. |
| [delete_incident_note](#delete_incident_note) | Delete an existing comment on a secret incident. Only incident notes created by the current API key can be deleted. |

## list_incident_notes

List notes left on a secret incident in chronological order.

- HTTP Method: `GET`
- Endpoint: `/v1/incidents/secrets/{incident_id}/notes`

**Parameters**

| Name        | Type                                                                | Required | Description                                                                                             |
| :---------- | :------------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------ |
| incident_id | int                                                                 | ✅       | The id of the incident to retrieve                                                                      |
| cursor      | str                                                                 | ❌       | Pagination cursor.                                                                                      |
| page        | int                                                                 | ❌       | Page number.                                                                                            |
| per_page    | int                                                                 | ❌       | Number of items to list per page.                                                                       |
| ordering    | [ListIncidentNotesOrdering](../models/ListIncidentNotesOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| member_id   | int                                                                 | ❌       | Filter by member id.                                                                                    |
| search      | str                                                                 | ❌       | Search notes based on the comment field content.                                                        |

**Return Type**

`List[IncidentNote]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ListIncidentNotesOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incident_notes.list_incident_notes(
    incident_id=5,
    cursor="cursor",
    per_page=20,
    ordering="created_at",
    member_id=1,
    search="I revoked this"
)

print(result)
```

## create_incident_note

Add a note on a secret incident.

- HTTP Method: `POST`
- Endpoint: `/v1/incidents/secrets/{incident_id}/notes`

**Parameters**

| Name         | Type                                                                | Required | Description                        |
| :----------- | :------------------------------------------------------------------ | :------- | :--------------------------------- |
| request_body | [CreateIncidentNoteRequest](../models/CreateIncidentNoteRequest.md) | ❌       | The request body.                  |
| incident_id  | int                                                                 | ✅       | The id of the incident to retrieve |

**Return Type**

`IncidentNote`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateIncidentNoteRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateIncidentNoteRequest(
    comment="I revoked this secret"
)

result = sdk.secret_incident_notes.create_incident_note(
    request_body=request_body,
    incident_id=2
)

print(result)
```

## update_incident_note

Update an existing comment on a secret incident. Only incident notes created by the current API key can be updated.

- HTTP Method: `PATCH`
- Endpoint: `/v1/incidents/secrets/{incident_id}/notes/{note_id}`

**Parameters**

| Name         | Type                                                                | Required | Description                           |
| :----------- | :------------------------------------------------------------------ | :------- | :------------------------------------ |
| request_body | [UpdateIncidentNoteRequest](../models/UpdateIncidentNoteRequest.md) | ❌       | The request body.                     |
| incident_id  | int                                                                 | ✅       | The id of the incident to retrieve    |
| note_id      | int                                                                 | ✅       | The id of the incident note to update |

**Return Type**

`IncidentNote`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import UpdateIncidentNoteRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateIncidentNoteRequest(
    comment="I revoked this secret"
)

result = sdk.secret_incident_notes.update_incident_note(
    request_body=request_body,
    incident_id=1,
    note_id=6
)

print(result)
```

## delete_incident_note

Delete an existing comment on a secret incident. Only incident notes created by the current API key can be deleted.

- HTTP Method: `DELETE`
- Endpoint: `/v1/incidents/secrets/{incident_id}/notes/{note_id}`

**Parameters**

| Name        | Type | Required | Description                           |
| :---------- | :--- | :------- | :------------------------------------ |
| incident_id | int  | ✅       | The id of the incident to retrieve    |
| note_id     | int  | ✅       | The id of the incident note to delete |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_incident_notes.delete_incident_note(
    incident_id=10,
    note_id=5
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
