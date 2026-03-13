import os
import tempfile
import time
from pathlib import Path
from typing import Optional
from gtts import gTTS

class TTSEngine:
    """
    Engine de text-to-speech otimizada para o MVP.
    """
    
    def __init__(self):
        # Cria pasta temporária única para evitar conflitos de permissão
        self.temp_dir = Path(tempfile.gettempdir()) / "voice_assistant"
        self.temp_dir.mkdir(exist_ok=True)
    
    def _get_temp_audio_file(self) -> str:
        """Gera nome único usando milissegundos para evitar Erro de Permissão"""
        timestamp = int(time.time() * 1000)
        return str(self.temp_dir / f"output_{timestamp}.mp3")
    
    def synthesize(self, text: str) -> Optional[str]:
        """Sintetiza texto em áudio PT-BR de forma rápida"""
        if not text or not text.strip():
            return None
        
        try:
            # Configurado fixo para Português para ser mais leve
            tts = gTTS(text=text, lang="pt", slow=False)
            
            output_file = self._get_temp_audio_file()
            tts.save(output_file)
            
            return output_file
            
        except Exception as e:
            print(f"❌ Erro na síntese de voz: {e}")
            return None

    def cleanup_temp_files(self) -> None:
        """Limpa os áudios antigos para não entulhar o PC"""
        try:
            for file in self.temp_dir.glob("output_*.mp3"):
                try:
                    file.unlink()
                except:
                    pass # Se o arquivo estiver em uso, ignora
        except Exception as e:
            print(f"⚠️ Erro ao limpar temporários: {e}")