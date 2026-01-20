
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine
from .routers import post, user, web
from pathlib import Path

models.Base.metadata.create_all(bind=engine)
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(post.router)
app.include_router(user.router)
app.include_router(web.router)
