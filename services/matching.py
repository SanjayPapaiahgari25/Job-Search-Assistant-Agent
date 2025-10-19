from fastapi import HTTPException

from models.profiles import UserProfile
from models.job import Job
from models.matching import JobMatch, ProfileMatch
from services.profile import ProfileService
from services.jobs import JobService


def get_profile_service(db):
    return ProfileService(db)

def get_job_service(db):
    return JobService(db)

class MatchingService:

    def __init__(self, db):
        self.db = db
        self.profile_service = get_profile_service(db)
        self.job_service = get_job_service(db)
        self.profiles = self.profile_service.get_profiles()
        self.jobs = self.job_service.get_jobs()

    def get_match_score(self, profile: UserProfile, job: Job) -> int:
        score = 0
        for skill in profile.skills:
            if skill in job.skills_required:
                score += 1
        score = (score * 100)//(len(job.skills_required))
        return score

    def get_matching_jobs(self, email) -> list[JobMatch]:
        profile = self.profile_service.get_profile(email)

        if profile is None:
            raise HTTPException(status_code=404, detail="Profile not found")
        
        matched_jobs = [
            JobMatch(**job.model_dump(), match_score=score)
            for job in self.jobs
            if (score := self.get_match_score(profile, job)) > 0
        ]
        matched_jobs.sort(key=lambda x: x.match_score, reverse=True)
        return matched_jobs
    
    def get_matching_profiles(self, job_id) -> list[ProfileMatch]:
        job = self.job_service.get_job(job_id)

        if job is None:
            raise HTTPException(status_code=404, detail="Job not found")
        
        matched_profiles = [
            ProfileMatch(profile=profile, match_score=self.get_match_score(profile, job))
            for profile in self.profiles
            if self.get_match_score(profile, job) > 0
        ]

        matched_profiles.sort(key=lambda x: x.match_score, reverse=True)
        return matched_profiles
