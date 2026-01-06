from pydantic import BaseModel
from datetime import datetime
from typing import Literal, ClassVar
from resources.user.models.user import User


class AuditEvent(BaseModel):
    id: int
    user_id: int
    action: Literal["CREATE", "READ"]
    resource_type: Literal["ENCOUNTER"]
    resource_id: int
    access_date: datetime

    id_counter: ClassVar[int] = 0

    @classmethod
    def create(cls, user: User, action: str, resource_id: str):
        cls.id_counter += 1
        return AuditEvent(
            id=cls.id_counter,
            user_id=user.id,
            action=action,
            resource_type="ENCOUNTER",  # TODO move to consts
            resource_id=resource_id,
            access_date=datetime.utcnow()
        )


class AuditEvents(BaseModel):
    events: list[AuditEvent]
    total: int
