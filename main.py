from fastapi import FastAPI
from app.routers import auth
from app.routers import admin



app = FastAPI(title="Vicadem API")

app.include_router(auth.router)
app.include_router(admin.router)

@app.get("/")
def home():
    return {"message": "Vicadem API Running"}
