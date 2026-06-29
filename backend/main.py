from fastapi import FastAPI

app = FastAPI(title="SG Sponsor Jobs AI")

@app.get("/")
def home():
    return {
        "status": "running",
        "app": "SG Sponsor Jobs AI",
        "message": "Welcome to the API!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/jobs")
def jobs():
    return {
        "count": 0,
        "jobs": []
    }
