from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.voice import router as voice_router

app = FastAPI(
    title="SofiaVoice API",
    description="Rs4Machine · Assistente de Voz · Backend",
    version="2.0.0",
)

# Libera o frontend Next.js (local e Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://*.vercel.app",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice_router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok", "project": "SofiaVoice", "version": "2.0.0"}