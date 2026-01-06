from resources.audit.models.audit import AuditEvents, AuditEvent
from resources.user.models.user import User
from datetime import datetime
from typing import Optional
from resources.audit.repositories.audit import AuditRepository


class AuditController:
    def __init__(self):
        pass

    @classmethod
    def create(cls, user: User, action: str, resource_id: str) -> AuditEvent:
        encounter = AuditEvent.create(user, action, resource_id)
        AuditRepository.create(encounter)
        return encounter

    @classmethod
    def get_audit(cls, user: User,
                  start_date: Optional[datetime] = None,
                  end_date: Optional[datetime] = None) -> AuditEvents:
        audit_events = AuditRepository.get_audit_in_date_range(user, start_date, end_date)
        return AuditEvents(events=audit_events, total=len(audit_events))


audit_controller = AuditController()
