# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class IncidentNote(BaseModel):
    """IncidentNote

    :param id_: id_, defaults to None
    :type id_: int, optional
    :param incident_id: Id of the related Incident, defaults to None
    :type incident_id: int, optional
    :param member_id: Id of the member who created this note. Can be null if the note was not created by a member or if the member was deleted. , defaults to None
    :type member_id: int, optional
    :param api_token: Name of the API key which created this note. Can be null if the note was not created via the API. Use `api_token_id` instead. , defaults to None
    :type api_token: str, optional
    :param api_token_id: ID of the API key which created this note. Can be null if the note was not created via the API. , defaults to None
    :type api_token_id: str, optional
    :param created_at: Creation date of the note, defaults to None
    :type created_at: str, optional
    :param updated_at: Last time the content of the note was updated. Null if the comment was never modified. , defaults to None
    :type updated_at: str, optional
    :param comment: comment, defaults to None
    :type comment: str, optional
    :param issue_id: Id of the related Incident. Use `incident_id` instead., defaults to None
    :type issue_id: int, optional
    :param user_id: Id of the user who created this note. Can be null if the note was not created by a user or if the user was deleted. Use `member_id` instead. , defaults to None
    :type user_id: int, optional
    """

    def __init__(
        self,
        id_: int = None,
        incident_id: int = None,
        member_id: int = None,
        api_token: str = None,
        api_token_id: str = None,
        created_at: str = None,
        updated_at: str = None,
        comment: str = None,
        issue_id: int = None,
        user_id: int = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if incident_id is not None:
            self.incident_id = incident_id
        if member_id is not None:
            self.member_id = member_id
        if api_token is not None:
            self.api_token = api_token
        if api_token_id is not None:
            self.api_token_id = api_token_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if comment is not None:
            self.comment = comment
        if issue_id is not None:
            self.issue_id = issue_id
        if user_id is not None:
            self.user_id = user_id