[![Status](https://img.shields.io/badge/Status-Live%20em%20Produção-brightgreen)](https://ai-voice-assistant-groq.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white)](https://sofia-voice-backend.onrender.com/docs)
[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js&logoColor=white)](https://ai-voice-assistant-groq.vercel.app)
[![Groq](https://img.shields.io/badge/Groq-Ultra%20Low%20Latency-orange?logo=thunderbird&logoColor=white)](https://groq.com)
[![Vercel](https://img.shields.io/badge/Vercel-Frontend-black?logo=vercel&logoColor=white)](https://ai-voice-assistant-groq.vercel.app)
[![Render](https://img.shields.io/badge/Render-Backend-46E3B7?logo=render&logoColor=white)](https://sofia-voice-backend.onrender.com/docs)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="center">
<img src="assets/Rs4Machine.png" alt="Rs4Machine Logo" width="380" />
  <h1>🎙️ SofiaVoice — Rs4Machine</h1>
  <img src="sofia-voice.gif" alt="SofiaVoice Demo" width="100%" />
  <p><strong>Voice Intelligence System v2.0</strong></p>
  <p>Assistente de voz com IA — fala, entende e responde em português em tempo real.</p>
  <p>
    <a href="https://ai-voice-assistant-groq.vercel.app" target="_blank"><strong>🚀 App Online</strong></a> •
    <a href="https://sofia-voice-backend.onrender.com/docs" target="_blank"><strong>📡 API Docs</strong></a> •
    <a href="https://github.com/raphaelmendes-dev"><strong>GitHub</strong></a> •
    <a href="mailto:python.dev.raphael@gmail.com">Contato</a>
  </p>
  <p><em>README in <a href="README.en.md">English</a></em></p>
</div>

---

## 🎯 Visão Geral

A **SofiaVoice** é uma assistente de voz inteligente desenvolvida pela **Rs4Machine**. Com um clique no microfone, ela ouve, transcreve, processa e responde em voz — tudo em menos de 3 segundos, usando a infraestrutura ultra-rápida da Groq.

- 🎤 Captura de voz direto no browser (Web Audio API)
- 🧠 Transcrição com Whisper Large v3 via Groq
- 💬 Respostas inteligentes com LLaMA 3.3 70B
- 🔊 Síntese de voz em português (gTTS)
- 🖥️ Interface estilo terminal com visualizador animado
- 📝 Log de conversas salvo automaticamente

---

## 🏗️ Arquitetura

```
ai-voice-assistant-groq/
├── frontend/                        → Next.js 15 (Vercel)
│   ├── app/
│   │   └── sofia-voice/
│   │       └── page.jsx             → Orquestrador principal
│   ├── components/SofiaVoice/
│   │   ├── VoiceVisualizer.jsx      → Círculo animado por estado
│   │   ├── MicButton.jsx            → Botão do microfone
│   │   ├── TerminalLog.jsx          → Log estilo terminal
│   │   └── StatusBadge.jsx          → Badge de status da IA
│   ├── hooks/
│   │   └── useSofiaVoice.js         → Lógica + chamadas ao backend
│   ├── constants/
│   │   └── tokens.js                → Design DNA Rs4Machine
│   └── styles/
│       └── sofia-voice.css          → Animações e keyframes
└── backend/                         → Python + FastAPI (Render)
    ├── main.py                      → App FastAPI + CORS
    ├── config.py                    → Variáveis de ambiente
    ├── requirements.txt
    ├── routers/
    │   └── voice.py                 → Endpoints da API
    └── services/
        ├── stt.py                   → Whisper — áudio → texto
        ├── llm.py                   → LLaMA — texto → resposta
        └── tts.py                   → gTTS — texto → voz
```

---

## ✨ Funcionalidades

- Gravação de voz no browser sem plugins
- Transcrição automática com Whisper Large v3
- Respostas contextuais com histórico de conversa
- Síntese de voz em PT-BR com gTTS
- Pipeline completo em endpoint único (`/api/voice`)
- Visualizador animado com 4 estados: STANDBY · OUVINDO · PROCESSANDO · FALANDO
- Terminal de logs com timestamp em tempo real
- Log de conversas salvo em arquivo diário

---

## 🛠️ Stack Técnica

| Camada | Tecnologia |
|---|---|
| Frontend | Next.js 15 + React |
| Estilo | CSS-in-JS + Design Tokens Rs4Machine |
| Backend | Python 3.12+ + FastAPI + uvicorn |
| Transcrição | Whisper Large v3 (Groq) |
| IA | LLaMA 3.3 70B (Groq) |
| Voz | gTTS (PT-BR) |
| Deploy Frontend | Vercel |
| Deploy Backend | Render |

---

## 🚀 Como Rodar Localmente

### Backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

Crie o arquivo `.env` na pasta `backend/`:
```env
GROQ_API_KEY=sua_chave_aqui
```

```bash
uvicorn main:app --reload --port 8000
```
API disponível em: `http://localhost:8000/docs`

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Crie o arquivo `.env.local` na pasta `frontend/`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

App disponível em: `http://localhost:3000/sofia-voice`

> ⚠️ Rode os dois terminais ao mesmo tempo.

---

## 📡 Endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| GET | `/health` | Status da API |
| POST | `/api/transcribe` | Áudio → texto (Whisper) |
| POST | `/api/chat` | Texto → resposta da IA |
| POST | `/api/speak` | Texto → áudio base64 |
| POST | `/api/voice` | Pipeline completo em uma chamada |

---

## 🔑 Variáveis de Ambiente

| Variável | Onde | Descrição |
|---|---|---|
| `GROQ_API_KEY` | backend `.env` | Chave da API Groq |
| `NEXT_PUBLIC_API_URL` | frontend `.env.local` | URL do backend |

---

## 🤝 Contato

**Rs4Machine** — Corporação de Agentes Autônomos  
CEO: Raphael Mendes  
📧 python.dev.raphael@gmail.com  
🔗 [github.com/raphaelmendes-dev](https://github.com/raphaelmendes-dev)

---

⭐ Dê uma estrela se o projeto te ajudou!

*Última atualização: Março 2026*