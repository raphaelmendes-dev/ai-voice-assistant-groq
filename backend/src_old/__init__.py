"""
Voice Assistant Package
=======================
Assistente de voz multilíngue com Whisper, ChatGPT e gTTS.

Módulos:
    - audio_utils: Captura e reprodução de áudio
    - speech_to_text: Transcrição com Whisper
    - llm_response: Respostas com ChatGPT
    - text_to_speech: Síntese de voz com gTTS
    - main: Orquestrador principal
"""

__version__ = "1.0.0"
__author__ = "Seu Nome"
__email__ = "seu.email@example.com"

from .audio_utils import AudioRecorder, AudioPlayer
from .speech_to_text import WhisperTranscriber
from .llm_response import ChatGPTAssistant
from .text_to_speech import TTSEngine

__all__ = [
    "AudioRecorder",
    "AudioPlayer",
    "WhisperTranscriber",
    "ChatGPTAssistant",
    "TTSEngine",
]
