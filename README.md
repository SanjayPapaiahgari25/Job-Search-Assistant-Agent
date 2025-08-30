# AIJob-Search-Agent
This is a Job Search Agent that scrapes the job boards to get the relevant job postings based on user profile. This is currently WIP and is no where close to completion. I will try to complete this to the best of what i can so that I can get to implement an end to end system and also learn about Agents.

The following is how the project structure will eventually look like:-

# Project Structure
app/
│── main.py                 # Entry point, includes routers
│── core/                   # Shared infra & config
│   ├── database.py          # Singleton DB
│   └── utils.py             # (optional) common helpers
│
│── models/                 # Pydantic models (data contracts)
│   ├── user_profile.py
│   ├── job.py
│   └── matching.py          # e.g. JobMatch, ProfileMatch, JobHistory
│
│── services/               # Business logic (domain services)
│   ├── profiles_service.py  # CRUD for profiles
│   ├── jobs_service.py      # CRUD for jobs
│   └── matching_service.py  # Matching logic
│
│── routers/                # API layer
│   ├── profiles_router.py   # /profiles endpoints
│   ├── jobs_router.py       # /jobs endpoints
│   └── matching_router.py   # /match, /candidates, /history endpoints
│
└── tests/                  # Tests for each module
    ├── test_profiles.py
    ├── test_jobs.py
    └── test_matching.py
