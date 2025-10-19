from pydantic import BaseModel

class JobInteractionHistory(BaseModel):
    job_id: str
    title: str
    company: str
    match_score: int
    timestamp: str

class UserSearchHistory(BaseModel):
    profile: str
    history: list[JobInteractionHistory]

class InteractionResponse(BaseModel):
    message: str = "History recorded successfully"
    email: str
    job_id: str
    timestamp: str
