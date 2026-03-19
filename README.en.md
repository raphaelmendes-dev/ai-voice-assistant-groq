[![Status](https://img.shields.io/badge/Status-Live%20in%20Production-brightgreen)](https://ai-voice-assistant-groq.vercel.app)
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
  <p>AI voice assistant — speaks, understands and responds in real time.</p>
  <p>
    <a href="https://ai-voice-assistant-groq.vercel.app" target="_blank"><strong>🚀 Live App</strong></a> •
    <a href="https://sofia-voice-backend.onrender.com/docs" target="_blank"><strong>📡 API Docs</strong></a> •
    <a href="https://github.com/raphaelmendes-dev"><strong>GitHub</strong></a> •
    <a href="mailto:python.dev.raphael@gmail.com">Contact</a>
  </p>
  <p><em>README em <a href="README.md">Português</a></em></p>
</div>

---

## 🎯 Overview

**SofiaVoice** is an intelligent voice assistant built by **Rs4Machine**. With a single click on the microphone, it listens, transcribes, processes and responds in voice — all in under 3 seconds, powered by Groq's ultra-fast inference infrastructure.

- 🎤 In-browser voice capture (Web Audio API)
- 🧠 Transcription with Whisper Large v3 via Groq
- 💬 Intelligent responses with LLaMA 3.3 70B
- 🔊 Text-to-speech in Brazilian Portuguese (gTTS)
- 🖥️ Terminal-style interface with animated visualizer
- 📝 Conversation logs saved automatically

---

## 🏗️ Architecture

```
ai-voice-assistant-groq/
├── frontend/                        → Next.js 15 (Vercel)
│   ├── app/
│   │   └── sofia-voice/
│   │       └── page.jsx             → Main orchestrator
│   ├── components/SofiaVoice/
│   │   ├── VoiceVisualizer.jsx      → State-driven animated circle
│   │   ├── MicButton.jsx            → Microphone button
│   │   ├── TerminalLog.jsx          → Terminal-style log
│   │   └── StatusBadge.jsx          → AI status badge
│   ├── hooks/
│   │   └── useSofiaVoice.js         → Logic + backend calls
│   ├── constants/
│   │   └── tokens.js                → Rs4Machine Design DNA
│   └── styles/
│       └── sofia-voice.css          → Animations and keyframes
└── backend/                         → Python + FastAPI (Render)
    ├── main.py                      → FastAPI app + CORS
    ├── config.py                    → Environment variables
    ├── requirements.txt
    ├── routers/
    │   └── voice.py                 → API endpoints
    └── services/
        ├── stt.py                   → Whisper — audio → text
        ├── llm.py                   → LLaMA — text → response
        └── tts.py                   → gTTS — text → speech
```

---

## ✨ Features

- Browser-native voice recording — no plugins required
- Automatic transcription with Whisper Large v3
- Contextual responses with conversation history
- PT-BR text-to-speech with gTTS
- Full pipeline in a single endpoint (`/api/voice`)
- Animated visualizer with 4 states: STANDBY · LISTENING · PROCESSING · SPEAKING
- Real-time terminal log with timestamps
- Daily conversation log saved to file

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 15 + React |
| Styling | CSS-in-JS + Rs4Machine Design Tokens |
| Backend | Python 3.12+ + FastAPI + uvicorn |
| Transcription | Whisper Large v3 (Groq) |
| AI | LLaMA 3.3 70B (Groq) |
| Voice | gTTS (PT-BR) |
| Frontend Deploy | Vercel |
| Backend Deploy | Render |

---

## 🚀 Running Locally

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

Create `.env` file inside `backend/`:
```env
GROQ_API_KEY=your_key_here
```

```bash
uvicorn main:app --reload --port 8000
```
API available at: `http://localhost:8000/docs`

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Create `.env.local` file inside `frontend/`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

App available at: `http://localhost:3000/sofia-voice`

> ⚠️ Run both terminals at the same time.

---

## 📡 API Endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/health` | API status |
| POST | `/api/transcribe` | Audio → text (Whisper) |
| POST | `/api/chat` | Text → AI response |
| POST | `/api/speak` | Text → base64 audio |
| POST | `/api/voice` | Full pipeline in one call |

---

## 🔑 Environment Variables

| Variable | Where | Description |
|---|---|---|
| `GROQ_API_KEY` | backend `.env` | Groq API key |
| `NEXT_PUBLIC_API_URL` | frontend `.env.local` | Backend URL |

---

## 🤝 Contact

**Rs4Machine** — Autonomous Agents Corporation  
CEO: Raphael Mendes  
📧 python.dev.raphael@gmail.com  
🔗 [github.com/raphaelmendes-dev](https://github.com/raphaelmendes-dev)

---

⭐ Star this repo if it helped you!

*Last updated: March 2026*