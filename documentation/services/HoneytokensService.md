# HoneytokensService

A list of all methods in the `HoneytokensService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                                                                                                                                                                                                                                                                           |
| :---------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [list_honeytoken](#list_honeytoken)                               | This endpoint allows you to list all the honeytokens of your workspace. The response contains the list of honeytokens and a pagination cursor to retrieve the next page. The honeytokens are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `manager`. |
| [create_honeytoken](#create_honeytoken)                           | This endpoint allows you to create a honeytoken of a type. If you are using a personal access token, you need to have an access level superior or equal to `manager`.                                                                                                                                                 |
| [create_honeytoken_with_context](#create_honeytoken_with_context) | This endpoint allows you to create a honeytoken of a given type within a context. The context is a realistic file in which your honeytoken is inserted. If `language`, `project_extensions` and `filename` are not provided, a random context will be generated.                                                      |
| [retrieve_honeytoken](#retrieve_honeytoken)                       | Retrieve an existing honeytoken. If you are using a personal access token, you need to have an access level greater or equal to `manager`.                                                                                                                                                                            |
| [update_honeytoken](#update_honeytoken)                           | Update a name or descriptions of an existing honeytoken.                                                                                                                                                                                                                                                              |
| [reset_honeytoken](#reset_honeytoken)                             | Resets a triggered honeytoken. All the associated events will be closed.                                                                                                                                                                                                                                              |
| [revoke_honeytoken](#revoke_honeytoken)                           | Revokes an active or triggered honeytoken. All the associated events will be closed.                                                                                                                                                                                                                                  |

## list_honeytoken

This endpoint allows you to list all the honeytokens of your workspace. The response contains the list of honeytokens and a pagination cursor to retrieve the next page. The honeytokens are sorted by id. If you are using a personal access token, you need to have an access level superior or equal to `manager`.

- HTTP Method: `GET`
- Endpoint: `/v1/honeytokens`

**Parameters**

| Name                 | Type                                                          | Required | Description                                                                                             |
| :------------------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------ |
| cursor               | str                                                           | ❌       | Pagination cursor.                                                                                      |
| per_page             | int                                                           | ❌       | Number of items to list per page.                                                                       |
| status               | [ListHoneytokenStatus](../models/ListHoneytokenStatus.md)     | ❌       |                                                                                                         |
| type\_               | [ListHoneytokenType](../models/ListHoneytokenType.md)         | ❌       |                                                                                                         |
| search               | str                                                           | ❌       | Search honeytokens based on their name and/or description.                                              |
| creator_id           | float                                                         | ❌       | Member id of the honeytoken creator.                                                                    |
| revoker_id           | float                                                         | ❌       | Member id of the honeytoken revoker.                                                                    |
| creator_api_token_id | str                                                           | ❌       | Token id of the honeytoken creator.                                                                     |
| revoker_api_token_id | str                                                           | ❌       | Token id of the honeytoken creator.                                                                     |
| tags                 | str                                                           | ❌       | Comma-separated list of tags to filter on.                                                              |
| ordering             | [ListHoneytokenOrdering](../models/ListHoneytokenOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |
| show_token           | bool                                                          | ❌       | Show token details (`access_token_id` and `secret_key`).                                                |

**Return Type**

`List[Honeytoken]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ListHoneytokenStatus, ListHoneytokenType, ListHoneytokenOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.honeytokens.list_honeytoken(
    cursor="cursor",
    per_page=20,
    status="triggered",
    type_="AWS",
    search="search",
    creator_id=5.74,
    revoker_id=4.44,
    creator_api_token_id="creator_api_token_id",
    revoker_api_token_id="revoker_api_token_id",
    tags="tags",
    ordering="created_at",
    show_token=True
)

print(result)
```

## create_honeytoken

This endpoint allows you to create a honeytoken of a type. If you are using a personal access token, you need to have an access level superior or equal to `manager`.

- HTTP Method: `POST`
- Endpoint: `/v1/honeytokens`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateHoneytokenRequest](../models/CreateHoneytokenRequest.md) | ❌       | The request body. |

**Return Type**

`Honeytoken`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateHoneytokenRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateHoneytokenRequest(
    name="honeytoken name",
    description="This honeytoken was placed in the repository test",
    type_="AWS",
    labels=[
        {
            "id_": "0cad1887-d616-4a46-8b5e-4c7b3a70dbaf",
            "key": "env",
            "value": "production"
        }
    ]
)

result = sdk.honeytokens.create_honeytoken(request_body=request_body)

print(result)
```

## create_honeytoken_with_context

This endpoint allows you to create a honeytoken of a given type within a context. The context is a realistic file in which your honeytoken is inserted. If `language`, `project_extensions` and `filename` are not provided, a random context will be generated.

- HTTP Method: `POST`
- Endpoint: `/v1/honeytokens/with-context`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [CreateHoneytokenWithContextRequest](../models/CreateHoneytokenWithContextRequest.md) | ❌       | The request body. |

**Return Type**

`HoneyTokenWithContext`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import CreateHoneytokenWithContextRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CreateHoneytokenWithContextRequest(
    name="honeytoken name",
    description="This honeytoken was placed in the repository test",
    type_="AWS",
    labels=[
        {
            "id_": "0cad1887-d616-4a46-8b5e-4c7b3a70dbaf",
            "key": "env",
            "value": "production"
        }
    ],
    language="python",
    filename="test_config.py",
    project_extensions=[
        "project_extensions"
    ]
)

result = sdk.honeytokens.create_honeytoken_with_context(request_body=request_body)

print(result)
```

## retrieve_honeytoken

Retrieve an existing honeytoken. If you are using a personal access token, you need to have an access level greater or equal to `manager`.

- HTTP Method: `GET`
- Endpoint: `/v1/honeytokens/{honeytoken_id}`

**Parameters**

| Name          | Type | Required | Description                                              |
| :------------ | :--- | :------- | :------------------------------------------------------- |
| honeytoken_id | str  | ✅       | The id of the honeytoken to retrieve                     |
| show_token    | bool | ❌       | Show token details (`access_token_id` and `secret_key`). |

**Return Type**

`Honeytoken`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.honeytokens.retrieve_honeytoken(
    honeytoken_id="honeytoken_id",
    show_token=False
)

print(result)
```

## update_honeytoken

Update a name or descriptions of an existing honeytoken.

- HTTP Method: `PATCH`
- Endpoint: `/v1/honeytokens/{honeytoken_id}`

**Parameters**

| Name          | Type                                                            | Required | Description                          |
| :------------ | :-------------------------------------------------------------- | :------- | :----------------------------------- |
| request_body  | [UpdateHoneytokenRequest](../models/UpdateHoneytokenRequest.md) | ❌       | The request body.                    |
| honeytoken_id | str                                                             | ✅       | The id of the honeytoken to retrieve |

**Return Type**

`Honeytoken`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import UpdateHoneytokenRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateHoneytokenRequest(
    name="test-honeytoken",
    description="honeytoken in repository test",
    labels=[
        {
            "id_": "0cad1887-d616-4a46-8b5e-4c7b3a70dbaf",
            "key": "env",
            "value": "production"
        }
    ]
)

result = sdk.honeytokens.update_honeytoken(
    request_body=request_body,
    honeytoken_id="honeytoken_id"
)

print(result)
```

## reset_honeytoken

Resets a triggered honeytoken. All the associated events will be closed.

- HTTP Method: `POST`
- Endpoint: `/v1/honeytokens/{honeytoken_id}/reset`

**Parameters**

| Name          | Type | Required | Description                          |
| :------------ | :--- | :------- | :----------------------------------- |
| honeytoken_id | str  | ✅       | The id of the honeytoken to retrieve |

**Return Type**

`Honeytoken`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.honeytokens.reset_honeytoken(honeytoken_id="honeytoken_id")

print(result)
```

## revoke_honeytoken

Revokes an active or triggered honeytoken. All the associated events will be closed.

- HTTP Method: `POST`
- Endpoint: `/v1/honeytokens/{honeytoken_id}/revoke`

**Parameters**

| Name          | Type | Required | Description                          |
| :------------ | :--- | :------- | :----------------------------------- |
| honeytoken_id | str  | ✅       | The id of the honeytoken to retrieve |

**Return Type**

`Honeytoken`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.honeytokens.revoke_honeytoken(honeytoken_id="honeytoken_id")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
