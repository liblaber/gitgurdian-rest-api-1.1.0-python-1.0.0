# HoneytokenNotesService

A list of all methods in the `HoneytokenNotesService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                      |
| :------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------- |
| [list_honeytoken_notes](#list_honeytoken_notes)   | List notes left on a honeytoken in chronological order.                                                          |
| [create_honeytoken_note](#create_honeytoken_note) | Add a note on a honeytoken.                                                                                      |
| [update_honeytoken_note](#update_honeytoken_note) | Update an existing comment on a honeytoken. Only honeytoken notes created by the current API key can be updated. |
| [delete_honeytoken_note](#delete_honeytoken_note) | Delete an existing comment on a honeytoken. Only honeytoken notes created by the current API key can be deleted. |

## list_honeytoken_notes

List notes left on a honeytoken in chronological order.

- HTTP Method: `GET`
- Endpoint: `/v1/honeytokens/{honeytoken_id}/notes`

**Parameters**

| Name          | Type                                                                    | Required | Description                                                                                             |
| :------------ | :---------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| honeytoken_id | str                                                                     | ✅       | The id of the honeytoken to retrieve                                                                    |
| cursor        | str                                                                     | ❌       | Pagination cursor.                                                                                      |
| per_page      | int                                                                     | ❌       | Number of items to list per page.                                                                       |
| ordering      | [ListHoneytokenNotesOrdering](../models/ListHoneytokenNotesOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| member_id     | int                                                                     | ❌       | Filter by member id.                                                                                    |
| api_token_id  | str                                                                     | ❌       | Entries matching this API token id.                                                                     |
| search        | str                                                                     | ❌       | Search notes based on the comment field content.                                                        |

**Return Type**

`List[HoneyTokenNote]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ListHoneytokenNotesOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.honeytoken_notes.list_honeytoken_notes(
    honeytoken_id="honeytoken_id",
    cursor="cursor",
    per_page=20,
    ordering="created_at",
    member_id=1,
    api_token_id="fdf075f9-1662-4cf1-9171-af50568158a8",
    search="I revoked this"
)

print(result)
```

## create_honeytoken_note

Add a note on a honeytoken.

- HTTP Method: `POST`
- Endpoint: `/v1/honeytokens/{honeytoken_id}/notes`

**Parameters**

| Name          | Type                                                                    | Required | Description                          |
| :------------ | :---------------------------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [CreateHoneytokenNoteRequest](../models/CreateHoneytokenNoteRequest.md) | ❌       | The request body.                    |
| honeytoken_id | str                                                                     | ✅       | The id of the honeytoken to retrieve |

**Return Type**

`HoneyTokenNote`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateHoneytokenNoteRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateHoneytokenNoteRequest(
    comment="I revoked this honeytoken"
)

result = sdk.honeytoken_notes.create_honeytoken_note(
    request_body=request_body,
    honeytoken_id="honeytoken_id"
)

print(result)
```

## update_honeytoken_note

Update an existing comment on a honeytoken. Only honeytoken notes created by the current API key can be updated.

- HTTP Method: `PATCH`
- Endpoint: `/v1/honeytokens/{honeytoken_id}/notes/{note_id}`

**Parameters**

| Name          | Type                                                                    | Required | Description                             |
| :------------ | :---------------------------------------------------------------------- | :------- | :-------------------------------------- |
| request_body  | [UpdateHoneytokenNoteRequest](../models/UpdateHoneytokenNoteRequest.md) | ❌       | The request body.                       |
| honeytoken_id | str                                                                     | ✅       | The id of the honeytoken to retrieve    |
| note_id       | str                                                                     | ✅       | The id of the honeytoken note to update |

**Return Type**

`HoneyTokenNote`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import UpdateHoneytokenNoteRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateHoneytokenNoteRequest(
    comment="I revoked this"
)

result = sdk.honeytoken_notes.update_honeytoken_note(
    request_body=request_body,
    honeytoken_id="honeytoken_id",
    note_id="note_id"
)

print(result)
```

## delete_honeytoken_note

Delete an existing comment on a honeytoken. Only honeytoken notes created by the current API key can be deleted.

- HTTP Method: `DELETE`
- Endpoint: `/v1/honeytokens/{honeytoken_id}/notes/{note_id}`

**Parameters**

| Name          | Type | Required | Description                             |
| :------------ | :--- | :------- | :-------------------------------------- |
| honeytoken_id | str  | ✅       | The id of the honeytoken to retrieve    |
| note_id       | str  | ✅       | The id of the honeytoken note to update |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.honeytoken_notes.delete_honeytoken_note(
    honeytoken_id="honeytoken_id",
    note_id="note_id"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
