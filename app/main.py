
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, web, auth
from pathlib import Path
from .oauth2 import oauth2_scheme




models.Base.metadata.create_all(bind=engine)
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Sets Access-Control-Allow-Origin: *
    allow_credentials=True,    # Must be False if allow_origins is "*"
    allow_methods=["*"],        # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],        # Allows all headers
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(post.router)
app.include_router(user.router)
app.include_router(web.router)
app.include_router(auth.router)
