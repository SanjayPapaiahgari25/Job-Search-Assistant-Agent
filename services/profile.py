from fastapi import HTTPException

class ProfileService:
    def __init__(self, db):
        self.db = db
    
    def get_profiles(self):
        if not self.db.profiles:
            return []
        return self.db.get_profiles()
    
    def get_profile(self, email):
        if not self.db.get_profile(email):
            raise HTTPException(status_code=404, detail="Profile not found")
        
        return self.db.get_profile(email)
    
    def add_profile(self, profile):

        if self.db.get_profile(profile.email):
            raise HTTPException(status_code=400, detail="Profile already exists")

        self.db.add_profile(profile)
        return {"message": "Profile created successfully", "profile": profile}
    
    def delete_profile(self, email):
        if not self.db.get_profile(email):
            raise HTTPException(status_code=404, detail="Profile not found")
        
        self.db.delete_profile(email)
        return {"message": "Profile deleted successfully"}
    
    def update_profile(self, email, updated_profile):
        if not self.db.get_profile(email):
            self.db.add_profile(updated_profile)
            return {"message": "Profile created successfully", "profile": updated_profile}

        self.db.update_profile(email, updated_profile)
        return {"message": "Profile updated successfully", "profile": updated_profile}
