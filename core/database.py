from collections import defaultdict

class Database:
    _instance = None   # class-level storage for singleton
    matches = {}
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.profiles = {}
            cls._instance.jobs = {}
            cls._instance.history = defaultdict(dict)
        return cls._instance
    
    def add_profile(self, profile):
        self.profiles[profile.email] = profile
    
    def get_profiles(self):
        return list(self.profiles.values())
    
    def get_profile(self, email):
        return self.profiles.get(email)
    
    def add_job(self, job):
        self.jobs[job.job_id] = job
    
    def get_jobs(self):
        return list(self.jobs.values())
    
    def get_job(self, job_id):
        return self.jobs.get(job_id)
    
    def delete_job(self, job_id):
        if job_id in self.jobs:
            del self.jobs[job_id]
        
    def update_job(self, job_id, updated_job):
        self.jobs[job_id] = updated_job

    def register_interaction(self, email: str, entry: dict):
        self.history.setdefault(email, {})[entry["job_id"]] = entry

    def update_interaction(self, email: str, job_id: str, entry: dict):
        if email in self.history and job_id in self.history[email]:
            self.history[email][job_id] = entry

    def get_history(self, email: str = None, job_id: str = None):
        if job_id:
            return self.history.get(email, {}).get(job_id)
        return list(self.history.get(email, {}).values())
    
def get_database():
    return Database()
