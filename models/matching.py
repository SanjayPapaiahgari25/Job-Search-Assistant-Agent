from pydantic import BaseModel, Field

from models.job import JobSummary
from models.profiles import UserProfile

class MatchContext(BaseModel):
    match_score: int = Field(..., ge=0, le=100)

class JobMatch(JobSummary, MatchContext):
    description: str

class ProfileMatch(BaseModel):
    profile: UserProfile
    match_score: float = Field(..., description="Match score for this profile", ge=0, le=100)
