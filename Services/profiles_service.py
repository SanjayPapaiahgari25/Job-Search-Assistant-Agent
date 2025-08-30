from fastapi import HTTPException

class ProfileService:
    
    def __init__(self, db):
        self.db = db
    
    def get_profiles(self):
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
    
