# DetectorGroup

**Properties**

| Name                             | Type                  | Required | Description                                                                                          |
| :------------------------------- | :-------------------- | :------- | :--------------------------------------------------------------------------------------------------- |
| name                             | str                   | ❌       |                                                                                                      |
| display_name                     | str                   | ❌       |                                                                                                      |
| type\_                           | DetectorGroupTypeEnum | ❌       |                                                                                                      |
| category                         | str                   | ❌       |                                                                                                      |
| is_active                        | bool                  | ❌       | Whether the detector is currently enabled on the workspace                                           |
| scans_code_only                  | bool                  | ❌       | Whether the detector can scan other kinds of resources than VCS ones                                 |
| checkable                        | bool                  | ❌       | Indicates whether this detector has a validity checker                                               |
| use_with_validity_check_disabled | bool                  | ❌       | If false, this detector will not be used if secret validity check is disabled on the workspace       |
| frequency                        | float                 | ❌       | Number of secrets found per million of commits from GitGuardian experience of open-source monitoring |
| removed_at                       | str                   | ❌       | Date at which this detector was disabled by GitGuardian                                              |
| open_incidents_count             | int                   | ❌       | Number of open secret incidents on the workspace associated to this detector                         |
| ignored_incidents_count          | int                   | ❌       | Number of ignored secret incidents on the workspace associated to this detector                      |
| resolved_incidents_count         | int                   | ❌       | Number of resolved secret incidents on the workspace associated to this detector                     |

<!-- This file was generated by liblab | https://liblab.com/ -->