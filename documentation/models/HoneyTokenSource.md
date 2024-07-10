# HoneyTokenSource

**Properties**

| Name              | Type                 | Required | Description                                                               |
| :---------------- | :------------------- | :------- | :------------------------------------------------------------------------ |
| type\_            | HoneyTokenSourceType | ❌       |                                                                           |
| name              | str                  | ❌       |                                                                           |
| url               | str                  | ❌       |                                                                           |
| open_issues_count | float                | ❌       | Number of open secret issues with at least one occurrence on this source. |
| total_files_count | float                | ❌       | Number of files where the honeytoken appears.                             |
| files             | List[str]            | ❌       | Files where the honeytoken appears.                                       |
| source_id         | float                | ❌       |                                                                           |

# HoneyTokenSourceType

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| GITHUB       | str  | ✅       | "github"       |
| GITLAB       | str  | ✅       | "gitlab"       |
| BITBUCKET    | str  | ✅       | "bitbucket"    |
| AZURE_DEVOPS | str  | ✅       | "azure_devops" |

<!-- This file was generated by liblab | https://liblab.com/ -->