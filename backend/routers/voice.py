from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from services.stt import STTService
from services.llm import LLMService
from services.tts import TTSService

router = APIRouter()

# Instâncias únicas (singleton por processo)
stt = STTService()
llm = LLMService()
tts = TTSService()


# ── Schemas ──────────────────────────────────────────
class ChatRequest(BaseModel):
    message: str

class SpeakRequest(BaseModel):
    text: str


# ── Endpoints ────────────────────────────────────────

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    """
    Recebe arquivo de áudio (.wav ou .webm),
    retorna o texto transcrito pelo Whisper.
    """
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Envie um arquivo de áudio.")

    audio_bytes = await file.read()

    if not audio_bytes:
        raise HTTPException(status_code=400, detail="Arquivo de áudio vazio.")

    text = stt.transcribe(audio_bytes, filename=file.filename or "audio.wav")

    if not text:
        raise HTTPException(status_code=422, detail="Não foi possível transcrever o áudio.")

    return {"text": text}


@router.post("/chat")
async def chat(body: ChatRequest):
    """
    Recebe mensagem de texto,
    retorna resposta da Sofia (LLaMA via Groq).
    """
    if not body.message.strip():
        raise HTTPException(status_code=400, detail="Mensagem não pode ser vazia.")

    response = llm.chat(body.message)
    return {"response": response}


@router.post("/speak")
async def speak(body: SpeakRequest):
    """
    Recebe texto,
    retorna áudio mp3 em base64 para o frontend tocar.
    """
    if not body.text.strip():
        raise HTTPException(status_code=400, detail="Texto não pode ser vazio.")

    audio_b64 = tts.synthesize(body.text)

    if not audio_b64:
        raise HTTPException(status_code=500, detail="Erro ao sintetizar voz.")

    return {"audio_base64": audio_b64, "format": "mp3"}


@router.post("/voice")
async def voice_pipeline(file: UploadFile = File(...)):
    """
    Pipeline completo em uma chamada só:
    áudio → transcrição → resposta → voz
    Atalho para o frontend chamar tudo de uma vez.
    """
    audio_bytes = await file.read()
    
    # 1. Transcreve
    user_text = stt.transcribe(audio_bytes, filename=file.filename or "audio.wav")
    if not user_text:
        raise HTTPException(status_code=422, detail="Não entendi o áudio.")

    # 2. Resposta da IA
    ai_response = llm.chat(user_text)

    # 3. Voz
    audio_b64 = tts.synthesize(ai_response)

    return {
        "user_text":    user_text,
        "ai_response":  ai_response,
        "audio_base64": audio_b64,
        "format":       "mp3",
    }