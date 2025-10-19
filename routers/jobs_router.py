from fastapi import APIRouter, Depends

from models.job import Job
from services.jobs import JobService
from core.database import Database, get_database

router = APIRouter(tags=["Jobs"])


def get_job_service(db: Database = Depends(get_database)):
    return JobService(db)


@router.get("/jobs")
async def get_jobs(job_service: JobService = Depends(get_job_service)):
    # This function would typically return a list of jobs.
    return job_service.get_jobs()


@router.post("/job")
async def create_job(job: Job, job_service: JobService = Depends(get_job_service)):
    # This function would typically add a new job to the list.
    return job_service.add_job(job)
