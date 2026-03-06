[![Status](https://img.shields.io/badge/Status-MVP%20Concluído-brightgreen)](https://github.com/raphaelmendes-dev/ai-voice-assistant-groq)
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-Ultra%20Low%20Latency-00A86B?logo=groq&logoColor=white)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="center">
  <h1>AI Voice Assistant Groq</h1>
  <p><strong>Assistente de Voz Inteligente com Latência Ultra-Baixa</strong></p>
  <p>Ouça, entenda, responda e fale – tudo em tempo real usando Groq + Llama 3.3.</p>

  <p>
    <a href="https://github.com/raphaelmendes-dev"><strong>Meu GitHub</strong></a> •
    <a href="https://www.linkedin.com/in/raphaelmendes-dev/">LinkedIn</a> •
    <a href="mailto:python.dev.raphael@gmail.com">Contato</a>
  </p>

  <p><em>README em <a href="README.en.md">English</a></em></p>
</div>

## 🎯 Visão Geral

Assistente de voz conversacional multilíngue que:
- Captura áudio (upload ou gravação)
- Transcreve com Whisper
- Processa com Groq (Llama 3.3) para respostas ultra-rápidas
- Sintetiza voz natural (gTTS)

Foco em **baixa latência** (Groq LPU™) e **validação determinística** no fluxo de áudio/texto, ideal para aplicações reais como atendimento, educação ou automação.

Persona customizável (ex.: Jarvis elegante ou agente financeira).

## ✨ Funcionalidades

- Gravação e upload de áudio (WAV/MP3/M4A)
- Transcrição automática multilíngue (Whisper)
- Respostas inteligentes com Groq + Llama 3.3 (latência < 500ms)
- Síntese de voz natural em PT-BR (gTTS)
- Interface Streamlit interativa (chat + configurações)
- Histórico de conversa persistente + logs
- Suporte a temperatura, max tokens e velocidade de fala

Fluxo: Áudio → Transcrição determinística → LLM rápida → Voz natural.

## 🛠️ Stack Técnica

- IA / LLM → Groq Cloud (Llama 3.3)
- STT → OpenAI Whisper (local ou API)
- TTS → gTTS (Google Text-to-Speech)
- UI → Streamlit (web interativa)
- Áudio → sounddevice, scipy, playsound
- Env → python-dotenv

## 🚀 Como Rodar

- Clone o repositórioBashgit clone https://github.com/raphaelmendes-dev/ai-voice-assistant-groq.git
- cd ai-voice-assistant-groq
- Ambiente virtualBashpython -m venv venv
- venv\Scripts\activate  # Windows
- ou source venv/bin/activate  # Linux/Mac
- Instale dependênciasBashpip install -r requirements.txt
- Configure chaves no .envtextGROQ_API_KEY=sua-chave-groq-aqui
- Execute interface webBashstreamlit run src/app_streamlit.py

Acesse: http://localhost:8501

(Para CLI: python src/main.py)

## 📊 Diferenciais

- Latência ultra-baixa graças à Groq LPU™
- 100% determinístico no fluxo de áudio (STT/TTS)
- Persona customizável via prompt system
- Multilíngue (detecção automática + resposta adaptada)
- Logs de conversa para depuração

## 🤝 Contribua ou Freelance
- Contribuições bem-vindas! Fork → branch → PR.
- Assistentes de voz/voz-texto, arquiteturas híbridas (determinístico + LLM), Groq, FastAPI, Azure AI, Redis, baixa latência.
- Projetos funcionais entregues.


Contato: raphaelmendes-dev | python.dev.raphael@gmail.com | LinkedIn


# ⭐ Dê uma estrela se o projeto te impressionou!


Última atualização: Março 2026

