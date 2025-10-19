from fastapi import APIRouter, Depends
from models.profiles import UserProfile
from services.profile import ProfileService
from core.database import Database, get_database

router = APIRouter(tags=["Profiles"])


def get_profile_service(db: Database = Depends(get_database)):
    return ProfileService(db)


@router.get("/profiles")
async def get_profiles(profile_service: ProfileService = Depends(get_profile_service)):
    # This function would typically return a list of user profiles.
    return profile_service.get_profiles()


@router.post("/profile")
async def create_profile(profile: UserProfile, profile_service: ProfileService = Depends(get_profile_service)):
    # This function would typically add a new profile to the list.
    return profile_service.add_profile(profile)