from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.analysis import router as analysis_router
from app.websocket.socket import router as websocket_router

app = FastAPI(
    title="AI Financial Intelligence Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    analysis_router
)

app.include_router(
    websocket_router
)

@app.get("/")

async def home():

    return {
        "message":
        "AI Financial Intelligence Backend Running"
    }