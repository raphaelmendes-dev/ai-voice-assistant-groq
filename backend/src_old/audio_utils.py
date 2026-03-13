import sounddevice as sd
from scipy.io.wavfile import write
import os
from playsound import playsound

def gravar_audio(segundos=5, nome_arquivo="input.wav"):
    """
    Grava áudio do microfone e salva em formato .wav
    """
    fs = 44100  # Taxa de amostragem padrão
    print(f"🎤 [OUVINDO] Fale agora por {segundos} segundos...")
    
    try:
        # Grava os dados
        gravacao = sd.rec(int(segundos * fs), samplerate=fs, channels=1)
        sd.wait()  # Espera finalizar a gravação
        
        # Salva o arquivo no disco
        write(nome_arquivo, fs, gravacao)
        print(f"✅ [OK] Áudio salvo em: {nome_arquivo}")
        return nome_arquivo
    except Exception as e:
        print(f"❌ Erro ao capturar áudio: {e}")
        return None

def tocar_audio(caminho_arquivo):
    """
    Reproduz um arquivo de áudio (.mp3 ou .wav)
    """
    if not caminho_arquivo or not os.path.exists(caminho_arquivo):
        print("⚠️ Arquivo de áudio não encontrado para reprodução.")
        return

    try:
        print(f"🔊 [ASSISTENTE] Reproduzindo resposta...")
        playsound(caminho_arquivo)
    except Exception as e:
        print(f"❌ Erro ao reproduzir áudio: {e}")

if __name__ == "__main__":
    # Teste simples: grava e depois tenta tocar (se você tiver um wave de teste)
    arquivo = gravar_audio(3)
    # tocar_audio(arquivo) # Descomente se quiser testar a volta do som