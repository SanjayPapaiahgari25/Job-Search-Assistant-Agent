from fastapi import FastAPI

from routers.profiles_router import router as profiles_router
from routers.jobs_router import router as jobs_router

app = FastAPI(
    title="AI Job Search Agent",
    description="A service for managing profiles, jobs, and job matching",
    version="1.0.0"
)

app.include_router(profiles_router, tags=["Profiles"])
app.include_router(jobs_router, tags=["Jobs"])

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "AI Job Search Agent is running"}
