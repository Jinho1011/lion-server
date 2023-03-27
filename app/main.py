from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.idiom.router import idiom_router
from app.lib.matcher import Matcher

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(idiom_router)

matcher = Matcher()
