import os
from groq import Groq

class WhisperTranscriber:
    def __init__(self, api_key=None):
        # Puxa a chave GROQ do seu .env
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY não encontrada no .env")
        
        self.client = Groq(api_key=self.api_key)
        self.model = "whisper-large-v3" # Modelo top e grátis do Groq

    def transcribe(self, audio_file):
        if not os.path.exists(audio_file):
            raise FileNotFoundError(f"Arquivo não encontrado: {audio_file}")

        try:
            with open(audio_file, "rb") as file:
                transcription = self.client.audio.transcriptions.create(
                    file=(audio_file, file.read()),
                    model=self.model,
                    response_format="verbose_json",
                )
                return {
                    "text": transcription.text,
                    "language": getattr(transcription, "language", "pt")
                }
        except Exception as e:
            print(f"❌ Erro no Whisper (Groq): {e}")
            return {"text": "", "language": "pt"}