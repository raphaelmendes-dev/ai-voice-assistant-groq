"""
Voice Assistant - Interface Web com Streamlit
==============================================
Interface gráfica interativa para o Voice Assistant.

Execute com: streamlit run app_streamlit.py
"""

import os
import sys
import tempfile
from pathlib import Path
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from speech_to_text import WhisperTranscriber
from llm_response import ChatGPTAssistant
from text_to_speech import TTSEngine

# Carregar variáveis de ambiente
load_dotenv()


# Configuração da página
st.set_page_config(
    page_title="Voice Assistant Multilíngue",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1E88E5;
        margin-bottom: 1rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #E3F2FD;
        border-left: 4px solid #1E88E5;
    }
    .assistant-message {
        background-color: #F5F5F5;
        border-left: 4px solid #43A047;
    }
</style>
""", unsafe_allow_html=True)


# Inicializar session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "assistant" not in st.session_state:
    try:
        st.session_state.assistant = ChatGPTAssistant()
        st.session_state.transcriber = WhisperTranscriber()
        st.session_state.tts = TTSEngine()
    except Exception as e:
        st.error(f"❌ Erro ao inicializar: {e}")
        st.stop()


# Header
st.markdown('<h1 class="main-header">🎙️ Voice Assistant Multilíngue</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Powered by Whisper, GPT-4o-mini & Google TTS</p>', unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.header("⚙️ Configurações")
    
    # Informações da API
    api_key_status = "✅ Configurada" if os.getenv("OPENAI_API_KEY") else "❌ Não configurada"
    st.metric("API Key OpenAI", api_key_status)
    
    st.divider()
    
    # Configurações de conversa
    st.subheader("💬 Conversa")
    
    temperature = st.slider(
        "Criatividade",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Quão criativa será a resposta (0 = precisa, 2 = muito criativa)"
    )
    
    max_tokens = st.slider(
        "Tamanho da resposta",
        min_value=50,
        max_value=500,
        value=300,
        step=50,
        help="Máximo de tokens na resposta"
    )
    
    st.divider()
    
    # Configurações de TTS
    st.subheader("🔊 Text-to-Speech")
    
    tts_slow = st.checkbox(
        "Velocidade reduzida",
        value=False,
        help="Útil para aprendizado de idiomas"
    )
    
    st.divider()
    
    # Estatísticas
    st.subheader("📊 Estatísticas")
    st.metric("Total de mensagens", len(st.session_state.messages))
    st.metric("Turnos", len(st.session_state.messages) // 2)
    
    if st.button("🗑️ Limpar conversa"):
        st.session_state.messages = []
        st.session_state.assistant.reset_conversation()
        st.rerun()
    
    st.divider()
    
    # Informações
    st.markdown("### ℹ️ Como usar")
    st.markdown("""
    1. **Upload de áudio**: Envie arquivo de áudio
    2. **Ou grave**: Use o gravador de voz
    3. **Aguarde**: Processamento automático
    4. **Ouça**: Resposta em áudio
    """)


# Área principal
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 Conversa")
    
    # Container para mensagens
    chat_container = st.container(height=400)
    
    with chat_container:
        for msg in st.session_state.messages:
            role = msg["role"]
            content = msg["content"]
            language = msg.get("language", "unknown")
            
            if role == "user":
                st.markdown(f"""
                <div class="chat-message user-message">
                    <strong>👤 Você</strong> ({language})<br>
                    {content}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message assistant-message">
                    <strong>🤖 Assistente</strong><br>
                    {content}
                </div>
                """, unsafe_allow_html=True)

with col2:
    st.subheader("🎤 Input de Áudio")
    
    # Upload de arquivo de áudio
    audio_file = st.file_uploader(
        "Upload de áudio (WAV, MP3, M4A)",
        type=["wav", "mp3", "m4a", "ogg"],
        help="Envie um arquivo de áudio para transcrição"
    )
    
    st.markdown("**Ou**")
    
    # Gravador de voz (requer streamlit-mic-recorder)
    st.info("📝 Gravador de voz em desenvolvimento. Use upload por enquanto.")


# Processamento de áudio
if audio_file is not None:
    with st.spinner("🎙️ Processando áudio..."):
        try:
            # Salvar arquivo temporário
            temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            temp_audio.write(audio_file.read())
            temp_audio.close()
            
            # Transcrever
            with st.spinner("📝 Transcrevendo..."):
                transcription = st.session_state.transcriber.transcribe(temp_audio.name)
                user_text = transcription["text"]
                detected_language = transcription["language"]
            
            if user_text:
                # Adicionar mensagem do usuário
                st.session_state.messages.append({
                    "role": "user",
                    "content": user_text,
                    "language": detected_language
                })
                
                # Obter resposta
                with st.spinner("🤔 Gerando resposta..."):
                    response = st.session_state.assistant.get_response(
                        user_text,
                        language=detected_language
                    )
                
                # Adicionar resposta do assistente
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "language": detected_language
                })
                
                # Sintetizar voz
                with st.spinner("🔊 Sintetizando voz..."):
                    audio_response = st.session_state.tts.synthesize(
                        response,
                        language=detected_language,
                        slow=tts_slow
                    )
                
                if audio_response:
                    # Reproduzir áudio
                    with open(audio_response, "rb") as f:
                        st.audio(f.read(), format="audio/mp3")
                
                # Limpar arquivo temporário
                os.unlink(temp_audio.name)
                
                st.rerun()
            else:
                st.warning("⚠️ Não consegui entender o áudio. Tente novamente.")
        
        except Exception as e:
            st.error(f"❌ Erro: {e}")


# Input de texto (alternativo)
st.divider()
st.subheader("⌨️ Ou digite sua mensagem")

text_input = st.text_input(
    "Digite aqui",
    placeholder="Ex: Qual é a capital da França?",
    label_visibility="collapsed"
)

if st.button("📤 Enviar") and text_input:
    with st.spinner("🤔 Processando..."):
        try:
            # Adicionar mensagem do usuário
            st.session_state.messages.append({
                "role": "user",
                "content": text_input,
                "language": "text"
            })
            
            # Obter resposta
            response = st.session_state.assistant.get_response(text_input)
            
            # Adicionar resposta
            st.session_state.messages.append({
                "role": "assistant",
                "content": response,
                "language": "text"
            })
            
            st.rerun()
        
        except Exception as e:
            st.error(f"❌ Erro: {e}")


# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    Desenvolvido com ❤️ usando Streamlit, OpenAI Whisper, GPT-4o-mini e gTTS<br>
    <a href="https://github.com/seu-usuario/voice-assistant" target="_blank">GitHub</a> | 
    <a href="https://linkedin.com/in/seu-perfil" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)
