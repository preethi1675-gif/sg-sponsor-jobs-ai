from fastapi import FastAPI

app = FastAPI(
    title="SG Sponsor Jobs AI",
    version="1.0.0"
)

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
