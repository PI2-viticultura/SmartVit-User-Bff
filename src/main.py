from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import asyncio

from settings import load_configuration
from views import (
    support_view,
    feedback_view,
    indicator_view,
    notification_view,
    pest_view
)

app = FastAPI()

origins = [
    'http://localhost',
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(support_view.router)
app.include_router(feedback_view.router)
app.include_router(indicator_view.router)
app.include_router(notification_view.router)
app.include_router(pest_view.router)

if __name__ == "__main__":
    server_config = load_configuration()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(uvicorn.run('main:app', **server_config))
