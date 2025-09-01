from pydantic import BaseModel

class JobSummary(BaseModel):
    job_id: str
    title: str
    company: str

class Job(JobSummary):
    description: str
    skills_required: list[str]
