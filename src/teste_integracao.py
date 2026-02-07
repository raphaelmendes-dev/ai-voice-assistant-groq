import os
from dotenv import load_dotenv
from audio_utils import gravar_audio, tocar_audio
from speech_to_text import WhisperTranscriber
from llm_response import ChatGPTAssistant 
from text_to_speech import TTSEngine

load_dotenv()

def rodar_assistente_completo():
    # 1. Inicializa tudo
    transcritor = WhisperTranscriber()
    cerebro = ChatGPTAssistant()
    motor_voz = TTSEngine()

    print("\n--- 🎤 FALE COM O ASSISTENTE ---")
    arquivo_gravado = gravar_audio(segundos=5)

    # 2. Transcrição
    print("\n--- 📝 PROCESSANDO SUA FALA ---")
    resultado = transcritor.transcribe(arquivo_gravado)
    texto_usuario = resultado['text']
    print(f"Você: {texto_usuario}")

    if not texto_usuario.strip():
        print("Não entendi nada...")
        return

    # 3. Inteligência Artificial (O Cérebro responde)
    print("\n--- 🧠 PENSANDO NA RESPOSTA ---")
    resposta_ia = cerebro.get_response(texto_usuario)
    print(f"Assistente: {resposta_ia}")

    # 4. Transforma a resposta em voz
    print("\n--- 🔊 GERANDO ÁUDIO ---")
    arquivo_resposta = motor_voz.synthesize(resposta_ia)

    # 5. Toca a voz da IA
    if arquivo_resposta:
        tocar_audio(arquivo_resposta)

if __name__ == "__main__":
    rodar_assistente_completo()