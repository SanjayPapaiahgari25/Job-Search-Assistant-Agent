from fastapi import APIRouter, Depends
from core.database import Database, get_database
from services.matching import MatchingService

router = APIRouter(tags=["Matching"])

def get_matching_service(db: Database = Depends(get_database)):
    return MatchingService(db)

@router.get("/match/{email}")
async def match_jobs(email: str, matching_service: MatchingService = Depends(get_matching_service)):
    # This function would typically match jobs based on the user's profile.
    return matching_service.get_matching_jobs(email)


@router.get("/candidates/{job_id}")
async def match_profiles(job_id: str, matching_service: MatchingService = Depends(get_matching_service)):
    # This function would typically match profiles based on the job requirements.
    return matching_service.get_matching_profiles(job_id)