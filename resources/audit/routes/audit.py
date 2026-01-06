from fastapi import APIRouter
from fastapi import Depends
from datetime import datetime
from typing import Optional
from resources.audit.models.audit import AuditEvents
from resources.audit.controllers.audit import audit_controller
from resources.auth.common import get_current_user
from resources.user.models.user import User

router = APIRouter(prefix="/audit")


@router.get("/audit/encounters", response_model=AuditEvents)
def get_audit(start_date: Optional[datetime] = None,
              end_date: Optional[datetime] = None,
              user: User = Depends(get_current_user)):
    audit = audit_controller.get_audit(user, start_date, end_date)
    return audit
