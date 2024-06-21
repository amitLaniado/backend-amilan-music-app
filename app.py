from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers import song_controller, user_controller, playlist_controller

# to run the server enter to cmd: "uvicorn app:app --reload"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(song_controller.router)
app.include_router(user_controller.router)
app.include_router(playlist_controller.router)

@app.get("/")
def root():
    return {"message": "Hello world"}