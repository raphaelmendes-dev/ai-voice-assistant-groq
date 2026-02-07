import sys
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from audio_utils import gravar_audio, tocar_audio
from speech_to_text import WhisperTranscriber
from llm_response import ChatGPTAssistant
from text_to_speech import TTSEngine

def start_assistant():
    stt = WhisperTranscriber()
    llm = ChatGPTAssistant()
    tts = TTSEngine()

    print("=== ASSISTENTE DE VOZ v1.0 ===")
    print("Pressione Ctrl+C para sair.")

    try:
        while True:
            input("\n[Pressione Enter para falar...]")
            audio = gravar_audio(segundos=5)
            
            # 1. Transcreve
            print("🤔 Entendendo...")
            texto = stt.transcribe(audio)["text"]
            if not texto: continue
            print(f"Você: {texto}")

            # 2. Responde
            print("🧠 Pensando...")
            resposta = llm.get_response(texto)
            print(f"IA: {resposta}")

            # 3. Fala
            audio_resp = tts.synthesize(resposta)
            if audio_resp:
                tocar_audio(audio_resp)
                
    except KeyboardInterrupt:
        print("\nAté logo!")
        sys.exit()

if __name__ == "__main__":
    start_assistant()