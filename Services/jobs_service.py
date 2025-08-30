from fastapi import HTTPException

class JobService:

    def __init__(self, db):
        self.db = db
    
    def get_jobs(self):
        return self.db.get_jobs()
    
    def get_job(self, job_id):
        job = self.db.get_job(job_id)

        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        
        return job

    def add_job(self, job):
        if self.db.get_job(job.id):
            raise HTTPException(status_code=400, detail="Job already exists")
        
        self.db.add_job(job)
        return {"message": "Job created successfully", "job": job}
    
    def delete_job(self, job_id):
        if not self.db.get_job(job_id):
            raise HTTPException(status_code=404, detail="Job not found")
        
        self.db.delete_job(job_id)
        return {"message": "Job deleted successfully"}
    
    def update_job(self, job_id, updated_job):
        if not self.db.get_job(job_id):
            self.db.add_job(updated_job)
            return {"message": "Job created successfully", "job": updated_job}

        self.db.update_job(job_id, updated_job)
        return {"message": "Job updated successfully", "job": updated_job}
