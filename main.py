from fastapi import FastAPI

from app.routers import auth

app = FastAPI(title="Vicadem API")

app.include_router(auth.router)


@app.get("/")
def home():
    return {"message": "Vicadem API Running"}
