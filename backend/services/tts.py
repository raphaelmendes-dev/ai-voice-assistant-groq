import base64
import tempfile
from pathlib import Path
from gtts import gTTS


class TTSService:
    def synthesize(self, text: str) -> str | None:
        """
        Recebe texto, retorna string base64 do mp3.
        O frontend toca o áudio diretamente no browser.
        """
        if not text or not text.strip():
            return None

        try:
            tts = gTTS(text=text, lang="pt", slow=False)

            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                tts.save(tmp.name)
                tmp_path = Path(tmp.name)

            audio_bytes = tmp_path.read_bytes()
            tmp_path.unlink(missing_ok=True)

            return base64.b64encode(audio_bytes).decode("utf-8")

        except Exception as e:
            print(f"❌ Erro no TTS: {e}")
            return None