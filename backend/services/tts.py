import base64
import os
import requests

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "")
VOICE_ID = "HOfBIVLhom4mc9WvXfyH"  # LavenderLessons — PT-BR
MODEL_ID = "eleven_multilingual_v2"


class TTSService:
    def synthesize(self, text: str) -> str | None:
        """
        Recebe texto, retorna string base64 do mp3.
        Usa ElevenLabs — voz LavenderLessons PT-BR.
        """
        if not text or not text.strip():
            return None

        try:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

            headers = {
                "xi-api-key": ELEVENLABS_API_KEY,
                "Content-Type": "application/json",
            }

            payload = {
                "text": text,
                "model_id": MODEL_ID,
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "speed": 1.0,
                },
            }

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code != 200:
                print(f"❌ Erro ElevenLabs: {response.status_code} — {response.text}")
                return None

            return base64.b64encode(response.content).decode("utf-8")

        except Exception as e:
            print(f"❌ Erro no TTS: {e}")
            return None