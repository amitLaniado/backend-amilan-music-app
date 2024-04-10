from fastapi import FastAPI
from routers import song_router

app = FastAPI()

app.include_router(song_router.router)

@app.get("/")
def root():
    return {"message": "Hello world"}