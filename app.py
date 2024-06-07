from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import song_controller

# to run the server enter to cmd: "uvicorn app:app --reload"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

app.include_router(song_controller.router)

@app.get("/")
def root():
    return {"message": "Hello world"}