from pydantic import BaseModel, Field


class WorkExperience(BaseModel):
    company: str = Field(..., description="Name of the company")
    role: str = Field(..., description="Position held at the company")
    years_of_experience: int = Field(..., description="Number of years of experience in this role", alias='years')


class UserProfile(BaseModel):
    name: str = Field(..., description="Name of the user")
    email: str = Field(..., description="Email address of the user")
    skills: list[str] = Field(..., description="List of skills the user possesses")
    experience: list[WorkExperience] = Field(..., description="List of work experiences")
