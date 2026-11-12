from fastapi import FastAPI
from .main import health_check

app = FastAPI(
    title="AI Engineering Foundation API",
    description="Core API for the AI Engineering projects",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Engineering Foundation is running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return health_check()

@app.get("/api/v1/status")
def status():
    return {
        "status": "operational",
        "version": "1.0.0"
    }
