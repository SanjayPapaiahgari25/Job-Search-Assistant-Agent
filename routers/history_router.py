from fastapi import APIRouter, Depends
from core.database import Database, get_database
from services.history import HistoryService
from services.matching import MatchingService


router = APIRouter(tags=["History"])


def get_history_service(db: Database = Depends(get_database)):
    return HistoryService(db)

def get_matching_service(db):
    return MatchingService(db)

@router.get("/history/{email}")
async def get_search_history(email: str, history_service: HistoryService = Depends(get_history_service)):
    return history_service.get_user_all_history(email)

@router.post("/history/{email}/{job_id}")
async def register_interaction(email: str, job_id: str, history_service: HistoryService = Depends(get_history_service)):
    return history_service.register_interaction(email, job_id)