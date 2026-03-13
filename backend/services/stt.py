from groq import Groq
from config import GROQ_API_KEY


class STTService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = "whisper-large-v3"

    def transcribe(self, audio_bytes: bytes, filename: str = "audio.wav") -> str:
        """
        Recebe bytes de áudio, retorna texto transcrito.
        """
        try:
            transcription = self.client.audio.transcriptions.create(
                file=(filename, audio_bytes),
                model=self.model,
                response_format="verbose_json",
                language="pt",
            )
            return transcription.text or ""
        except Exception as e:
            print(f"❌ Erro no Whisper: {e}")
            return ""