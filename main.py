from fastapi import FastAPI

from routers.profiles_router import router as profiles_router
from routers.jobs_router import router as jobs_router
from routers.matching_router import router as matching_router
from routers.history_router import router as history_router

app = FastAPI(
    title="AI Job Search Agent",
    description="A service for managing profiles, jobs, and job matching",
    version="1.0.0"
)

for router in [profiles_router, jobs_router, matching_router, history_router]:
    if not hasattr(router, 'tags'):
        router.tags = []
    app.include_router(router, tags=router.tags)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "AI Job Search Agent is running"}
