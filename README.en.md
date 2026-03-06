[![Status](https://img.shields.io/badge/Status-MVP%20Completed-brightgreen)](https://github.com/raphaelmendes-dev/ai-voice-assistant-groq)
[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-Ultra%20Low%20Latency-00A86B?logo=groq&logoColor=white)](https://groq.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<div align="center">
  <h1>AI Voice Assistant Groq</h1>
  <p><strong>Intelligent Voice Assistant with Ultra-Low Latency</strong></p>
  <p>Listen, understand, respond, and speak – real-time conversation powered by Groq + Llama 3.3.</p>

  <p>
    <a href="https://github.com/raphaelmendes-dev"><strong>My GitHub</strong></a> •
    <a href="https://www.linkedin.com/in/raphaelmendes-dev/">LinkedIn</a> •
    <a href="mailto:python.dev.raphael@gmail.com">Contact</a>
  </p>

  <p><em>README in <a href="README.md">Português</a></em></p>
</div>

## 🎯 Overview

Multilingual voice conversational assistant that:
- Captures audio (recording or upload)
- Transcribes using Whisper
- Processes with Groq (Llama 3.3) for ultra-fast responses
- Synthesizes natural voice output (gTTS)

Designed for **ultra-low latency** (Groq LPU™) and **deterministic audio/text handling**, perfect for real-world applications like customer support, education, or automation.

Customizable persona (e.g., elegant Jarvis or financial agent).

## ✨ Key Features

- Audio recording and file upload (WAV/MP3/M4A)
- Automatic multilingual transcription (Whisper)
- Intelligent responses with Groq + Llama 3.3 (< 500ms latency)
- Natural voice synthesis in PT-BR (gTTS)
- Interactive Streamlit interface (chat + settings)
- Conversation history persistence + logs
- Adjustable temperature, max tokens, and speech speed

Flow: Audio → Deterministic transcription → Fast LLM → Natural voice.

## 🛠️ Tech Stack

- LLM / Inference → Groq Cloud (Llama 3.3)
- Speech-to-Text → OpenAI Whisper
- Text-to-Speech → gTTS (Google Text-to-Speech)
- UI → Streamlit (interactive web app)
- Audio Handling → sounddevice, scipy, playsound
- Environment → python-dotenv

## 🚀 Quick Start

- Clone the repositoryBashgit clone https://github.com/raphaelmendes-dev/ai-voice-assistant-groq.git
- cd ai-voice-assistant-groq
- Create virtual environmentBashpython -m venv venv
- venv\Scripts\activate  # Windows
- or source venv/bin/activate  # Linux/Mac
- Install dependenciesBashpip install -r requirements.txt
- Set up API key in .envtextGROQ_API_KEY=your-groq-key-here
- Run the web interfaceBashstreamlit run src/app_streamlit.py

Access: http://localhost:8501
(For CLI mode: python src/main.py)

## 📊 Highlights & Differentiators

- Ultra-low latency thanks to Groq LPU™
- Deterministic audio pipeline (STT/TTS)
- Fully customizable persona via system prompt
- Multilingual support (auto detection + adapted responses)
- Conversation logs for debugging and analysis

## 🤝 Contribute
Contributions welcome! Fork → branch → PR.

Voice assistants, voice-to-text/text-to-voice systems, hybrid architectures (deterministic + LLM), Groq, FastAPI, Azure AI, Redis, low-latency solutions.
Functional projects delivered.

Contact: raphaelmendes-dev | python.dev.raphael@gmail.com | LinkedIn


## ⭐ Star if you like it!


Last update: March 2026
    C --> D["gTTS - Text-to-Speech Synthesis"]
    D --> E["Audio & Text Output"]
    E --> F["Streamlit UI - Playback + Chat"]
