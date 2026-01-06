from datetime import datetime
from resources.user.models.user import User
from resources.audit.models.audit import AuditEvent


class AuditRepository:
    _db = {}

    @classmethod
    def get_audit_in_date_range(cls, user: User, start_time: datetime, end_time: datetime) -> list[AuditEvent]:
        user_events = cls._db.get(user.id)
        # TODO filter for events in the date range
        return user_events

    @classmethod
    def create(cls, audit: AuditEvent):
        cls._db[str(audit.user_id)].append(audit)
