# LabelsService

A list of all methods in the `LabelsService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                              |
| :---------------------------------------------------------- | :----------------------------------------------------------------------- |
| [list_honeytoken_labels](#list_honeytoken_labels)           | List labels created for honeytokens in chronological order.              |
| [create_honeytoken_label](#create_honeytoken_label)         | Create a label for honeytokens.                                          |
| [patch_honeytoken_label_key](#patch_honeytoken_label_key)   | Rename a label key. It will be renamed in all the labels using this key. |
| [delete_honeytoken_label_key](#delete_honeytoken_label_key) | Delete a key. All the labels using this key will be deleted.             |
| [patch_honeytoken_label](#patch_honeytoken_label)           | Rename the value of a label.                                             |
| [delete_honeytoken_label](#delete_honeytoken_label)         | Delete a label for honeytokens.                                          |

## list_honeytoken_labels

List labels created for honeytokens in chronological order.

- HTTP Method: `GET`
- Endpoint: `/v1/honeytokens/labels`

**Parameters**

| Name     | Type | Required | Description                                                                                                                                             |
| :------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cursor   | str  | ❌       | Pagination cursor.                                                                                                                                      |
| per_page | int  | ❌       | Number of items to list per page.                                                                                                                       |
| search   | str  | ❌       | Search string to filter only labels which contains the search string in either its key or value. The search string can also be in the key:value format. |
| key      | str  | ❌       | Filter only labels which have the given key.                                                                                                            |

**Return Type**

`List[HoneyTokenLabel]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.labels.list_honeytoken_labels(
    cursor="cursor",
    per_page=20,
    search="env:production",
    key="env"
)

print(result)
```

## create_honeytoken_label

Create a label for honeytokens.

- HTTP Method: `POST`
- Endpoint: `/v1/honeytokens/labels`

**Parameters**

| Name         | Type                                                                      | Required | Description       |
| :----------- | :------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [CreateHoneytokenLabelRequest](../models/CreateHoneytokenLabelRequest.md) | ❌       | The request body. |

**Return Type**

`HoneyTokenLabel`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateHoneytokenLabelRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateHoneytokenLabelRequest(
    key="env",
    value="production"
)

result = sdk.labels.create_honeytoken_label(request_body=request_body)

print(result)
```

## patch_honeytoken_label_key

Rename a label key. It will be renamed in all the labels using this key.

- HTTP Method: `PATCH`
- Endpoint: `/v1/honeytokens/labels`

**Parameters**

| Name    | Type | Required | Description                            |
| :------ | :--- | :------- | :------------------------------------- |
| old_key | str  | ✅       | an existing key that we want to rename |
| new_key | str  | ✅       | a new name of the key                  |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.labels.patch_honeytoken_label_key(
    old_key="env",
    new_key="env prod"
)

print(result)
```

## delete_honeytoken_label_key

Delete a key. All the labels using this key will be deleted.

- HTTP Method: `DELETE`
- Endpoint: `/v1/honeytokens/labels`

**Parameters**

| Name | Type | Required | Description                                                             |
| :--- | :--- | :------- | :---------------------------------------------------------------------- |
| key  | str  | ❌       | A specified key to use to delete all labels which have the key matched. |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.labels.delete_honeytoken_label_key(key="env")

print(result)
```

## patch_honeytoken_label

Rename the value of a label.

- HTTP Method: `PATCH`
- Endpoint: `/v1/honeytokens/labels/{label_id}`

**Parameters**

| Name         | Type                                                                    | Required | Description       |
| :----------- | :---------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [PatchHoneytokenLabelRequest](../models/PatchHoneytokenLabelRequest.md) | ❌       | The request body. |
| label_id     | str                                                                     | ✅       | Id of the label.  |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import PatchHoneytokenLabelRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PatchHoneytokenLabelRequest(
    value="production"
)

result = sdk.labels.patch_honeytoken_label(
    request_body=request_body,
    label_id="5ddaad0c-5a0c-4674-beb5-1cd198d13360"
)

print(result)
```

## delete_honeytoken_label

Delete a label for honeytokens.

- HTTP Method: `DELETE`
- Endpoint: `/v1/honeytokens/labels/{label_id}`

**Parameters**

| Name     | Type | Required | Description      |
| :------- | :--- | :------- | :--------------- |
| label_id | str  | ✅       | Id of the label. |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.labels.delete_honeytoken_label(label_id="5ddaad0c-5a0c-4674-beb5-1cd198d13360")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
