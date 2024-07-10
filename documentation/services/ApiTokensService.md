# ApiTokensService

A list of all methods in the `ApiTokensService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                                                                                |
| :-------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| [self_retrieve_api_token](#self_retrieve_api_token) |                                                                                                            |
| [self_delete_api_token](#self_delete_api_token)     |                                                                                                            |
| [list_api_tokens](#list_api_tokens)                 | List all the tokens in the workspace, some filters are available and described below.                      |
| [retrieve_api_token](#retrieve_api_token)           |                                                                                                            |
| [delete_api_token](#delete_api_token)               |                                                                                                            |
| [public_jwt_create](#public_jwt_create)             | Create a short lived JWT for authentication to specific GitGuardian services, including HasMySecretLeaked. |

## self_retrieve_api_token

- HTTP Method: `GET`
- Endpoint: `/v1/api_tokens/self`

**Return Type**

`ApiTokenDetails`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.api_tokens.self_retrieve_api_token()

print(result)
```

## self_delete_api_token

- HTTP Method: `DELETE`
- Endpoint: `/v1/api_tokens/self`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.api_tokens.self_delete_api_token()

print(result)
```

## list_api_tokens

List all the tokens in the workspace, some filters are available and described below.

- HTTP Method: `GET`
- Endpoint: `/v1/api_tokens`

**Parameters**

| Name       | Type                                                        | Required | Description                                                                                             |
| :--------- | :---------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------ |
| cursor     | str                                                         | ❌       | Pagination cursor.                                                                                      |
| per_page   | int                                                         | ❌       | Number of items to list per page.                                                                       |
| status     | [ApiTokenStatusEnum](../models/ApiTokenStatusEnum.md)       | ❌       |                                                                                                         |
| member_id  | int                                                         | ❌       | Filter by member id.                                                                                    |
| creator_id | int                                                         | ❌       | Filter by creator id.                                                                                   |
| scopes     | [ApiTokenScopeEnum](../models/ApiTokenScopeEnum.md)         | ❌       |                                                                                                         |
| search     | str                                                         | ❌       | Search tokens based on their name.                                                                      |
| ordering   | [ListApiTokensOrdering](../models/ListApiTokensOrdering.md) | ❌       | Sort the results by their field value. The default sort is ASC, DESC if the field is preceded by a '-'. |

**Return Type**

`List[ApiTokenDetails]`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import ApiTokenStatusEnum, ApiTokenScopeEnum, ListApiTokensOrdering

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.api_tokens.list_api_tokens(
    cursor="cursor",
    per_page=20,
    status="active",
    member_id=1,
    creator_id=1,
    scopes="scan",
    search="search",
    ordering="created_at"
)

print(result)
```

## retrieve_api_token

- HTTP Method: `GET`
- Endpoint: `/v1/api_tokens/{token_id}`

**Parameters**

| Name     | Type | Required | Description      |
| :------- | :--- | :------- | :--------------- |
| token_id | str  | ✅       | Id of the token. |

**Return Type**

`ApiTokenDetails`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.api_tokens.retrieve_api_token(token_id="5ddaad0c-5a0c-4674-beb5-1cd198d13360")

print(result)
```

## delete_api_token

- HTTP Method: `DELETE`
- Endpoint: `/v1/api_tokens/{token_id}`

**Parameters**

| Name     | Type | Required | Description      |
| :------- | :--- | :------- | :--------------- |
| token_id | str  | ✅       | Id of the token. |

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.api_tokens.delete_api_token(token_id="5ddaad0c-5a0c-4674-beb5-1cd198d13360")

print(result)
```

## public_jwt_create

Create a short lived JWT for authentication to specific GitGuardian services, including HasMySecretLeaked.

- HTTP Method: `POST`
- Endpoint: `/v1/auth/jwt`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [PublicJwtCreateRequest](../models/PublicJwtCreateRequest.md) | ❌       | The request body. |

**Return Type**

`PublicJwtCreateOkResponse`

**Example Usage Code Snippet**

```python
from gitguardian import Gitguardian, Environment
from gitguardian.models import PublicJwtCreateRequest

sdk = Gitguardian(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PublicJwtCreateRequest(
    audience="https://api.hasmysecretleaked.com",
    audience_type="hmsl"
)

result = sdk.api_tokens.public_jwt_create(request_body=request_body)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
