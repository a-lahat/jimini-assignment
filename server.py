from fastapi import FastAPI
from resources.encounters.routes.encounters import router as encounter_router
from resources.audit.routes.audit import router as audit_router

app = FastAPI(title="Patient Encounter API")

app.include_router(encounter_router, tags=["Encounters"])
app.include_router(audit_router, tags=["Audit"])
