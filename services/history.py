from datetime import datetime
from models.history import JobInteractionHistory, InteractionResponse, UserSearchHistory

def get_matching_service(db):
    from services.matching import MatchingService
    return MatchingService(db)

class HistoryService:
    def __init__(self, db):
        self.db = db
    
    def register_interaction(self, email, job_id):
        # Step 1: check if job already in user's history
        existing_entry = self.db.get_history(email=email, job_id=job_id)

        current_time = datetime.now().isoformat()

        if existing_entry:
            # Update timestamp of existing entry
            existing_entry["timestamp"] = current_time
            self.db.update_interaction(email, job_id, existing_entry)
            return InteractionResponse(email=email, job_id=job_id, timestamp=current_time)

        # Step 2: new interaction
        job = self.db.get_job(job_id)
        profile = self.db.get_profile(email)
        if job is None or profile is None:
            raise ValueError("Invalid email or job_id")

        match_score = get_matching_service(self.db).get_match_score(profile, job)

        entry = JobInteractionHistory(
            job_id=job.job_id,
            title=job.title,
            company=job.company,
            match_score=match_score,
            timestamp=current_time,
        )

        self.db.register_interaction(email, entry.model_dump())
        return InteractionResponse(email=email, job_id=job_id, timestamp=current_time)

    def get_user_all_history(self, email):
        # Always hydrate DB dicts back into Pydantic models
        entries = self.db.get_history(email=email) or []
        history = [JobInteractionHistory(**e) for e in entries if isinstance(e, dict)]
        return UserSearchHistory(profile=email, history=history)
