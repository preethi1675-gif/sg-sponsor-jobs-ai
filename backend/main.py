from fastapi import FastAPI

app = FastAPI(title="SG Sponsor Jobs AI")

sample_jobs = [
    {
        "title": "Tax Operations Analyst",
        "company": "Global Bank",
        "location": "Singapore",
        "visa": "EP Possible",
        "link": "https://example.com/job1"
    },
    {
        "title": "KYC Analyst",
        "company": "ABC Financial",
        "location": "Singapore",
        "visa": "S Pass Possible",
        "link": "https://example.com/job2"
    },
    {
        "title": "AML Operations Specialist",
        "company": "XYZ Services",
        "location": "Singapore",
        "visa": "Not Mentioned",
        "link": "https://example.com/job3"
    }
]

@app.get("/")
def home():
    return {
        "status": "running",
        "app": "SG Sponsor Jobs AI"
    }

@app.get("/jobs")
def jobs():
    return {
        "count": len(sample_jobs),
        "jobs": sample_jobs
    }
