from fastapi import FastAPI
from app.slack_handler import router

app = FastAPI(title="Slack AI Data Bot")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Slack AI Data Bot running"}

@app.get("/health")
def health():
    return {"status": "healthy"}
