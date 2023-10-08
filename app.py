import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"api_version": "1.0"}


uvicorn.run(app, host="0.0.0.0", port=8000)
