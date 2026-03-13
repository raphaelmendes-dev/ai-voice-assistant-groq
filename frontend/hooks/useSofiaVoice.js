"use client";
import { useState, useEffect, useRef, useCallback } from "react";
import { API_URL } from "@/constants/tokens";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// useSofiaVoice — lógica completa da assistente
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
export function useSofiaVoice() {
  const [voiceState, setVoiceState] = useState("idle");
  const [logs, setLogs]             = useState([]);
  const [audioData, setAudioData]   = useState(null);

  const mediaRecorderRef = useRef(null);
  const audioChunksRef   = useRef([]);
  const frameRef         = useRef(null);

  // Timestamp atual
  const now = () => {
    const d = new Date();
    return `${String(d.getHours()).padStart(2,"0")}:${String(d.getMinutes()).padStart(2,"0")}:${String(d.getSeconds()).padStart(2,"0")}`;
  };

  // Adiciona linha no terminal
  const addLog = useCallback((entry) => {
    setLogs(prev => [...prev.slice(-40), { ...entry, time: now() }]);
  }, []);

  // Animação das barras no estado speaking
  useEffect(() => {
    if (voiceState === "speaking") {
      const animate = () => {
        setAudioData(Array.from({ length: 32 }, () => Math.random() * 180 + 20));
        frameRef.current = requestAnimationFrame(animate);
      };
      frameRef.current = requestAnimationFrame(animate);
    } else {
      cancelAnimationFrame(frameRef.current);
      setAudioData(null);
    }
    return () => cancelAnimationFrame(frameRef.current);
  }, [voiceState]);

  // Boot logs ao montar
  useEffect(() => {
    const bootLogs = [
      { type: "system", text: "Rs4Machine · Sofia v2.0 · inicializando..." },
      { type: "system", text: `Motor-Lite · FastAPI · ${API_URL}` },
      { type: "system", text: "Whisper + LLaMA · Groq · carregados" },
      { type: "system", text: "Sistema pronto · aguardando comando de voz" },
    ];
    bootLogs.forEach((log, i) => {
      setTimeout(() => addLog(log), i * 400 + 300);
    });
  }, []);

  // ── Gravar áudio pelo browser ──
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream, { mimeType: "audio/webm" });

      audioChunksRef.current = [];
      recorder.ondataavailable = (e) => audioChunksRef.current.push(e.data);
      recorder.start();
      mediaRecorderRef.current = recorder;
    } catch (err) {
      addLog({ type: "error", text: `Microfone bloqueado: ${err.message}` });
      setVoiceState("idle");
    }
  };

  const stopRecording = () => {
    return new Promise((resolve) => {
      const recorder = mediaRecorderRef.current;
      if (!recorder) return resolve(null);

      recorder.onstop = () => {
        const blob = new Blob(audioChunksRef.current, { type: "audio/webm" });
        recorder.stream.getTracks().forEach(t => t.stop());
        resolve(blob);
      };
      recorder.stop();
    });
  };

  // ── Pipeline completo: áudio → texto → IA → voz ──
  const runPipeline = async (audioBlob) => {
    try {
      // 1. Transcrição
      setVoiceState("thinking");
      addLog({ type: "system", text: "Transcrevendo áudio..." });

      const formData = new FormData();
      formData.append("file", audioBlob, "audio.webm");

      const sttRes = await fetch(`${API_URL}/api/transcribe`, {
        method: "POST",
        body: formData,
      });

      if (!sttRes.ok) throw new Error("Erro na transcrição");
      const { text: userText } = await sttRes.json();

      if (!userText) {
        addLog({ type: "error", text: "Não entendi. Tente novamente." });
        setVoiceState("idle");
        return;
      }

      addLog({ type: "user", text: userText });

      // 2. Resposta da IA
      addLog({ type: "system", text: "Sofia pensando..." });

      const chatRes = await fetch(`${API_URL}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText }),
      });

      if (!chatRes.ok) throw new Error("Erro no chat");
      const { response: aiText } = await chatRes.json();

      addLog({ type: "ai", text: aiText });

      // 3. Síntese de voz
      setVoiceState("speaking");
      addLog({ type: "system", text: "Sintetizando voz..." });

      const ttsRes = await fetch(`${API_URL}/api/speak`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: aiText }),
      });

      if (!ttsRes.ok) throw new Error("Erro no TTS");
      const { audio_base64 } = await ttsRes.json();

      // Toca o áudio no browser
      const audioSrc = `data:audio/mp3;base64,${audio_base64}`;
      const audio = new Audio(audioSrc);
      audio.onended = () => setVoiceState("idle");
      await audio.play();

    } catch (err) {
      addLog({ type: "error", text: `Erro: ${err.message}` });
      setVoiceState("idle");
    }
  };

  // ── Toggle do microfone ──
  const handleMicToggle = useCallback(async () => {
    if (voiceState === "idle") {
      setVoiceState("listening");
      addLog({ type: "system", text: "Microfone ativado · fale agora..." });
      await startRecording();

      // Grava por 5 segundos automaticamente
      setTimeout(async () => {
        const blob = await stopRecording();
        if (blob) await runPipeline(blob);
      }, 5000);

    } else {
      // Clicou de novo = interrompe a gravação na hora
      const blob = await stopRecording();
      if (blob && voiceState === "listening") {
        await runPipeline(blob);
      } else {
        setVoiceState("idle");
        addLog({ type: "system", text: "Entrada interrompida pelo usuário" });
      }
    }
  }, [voiceState]);

  return { voiceState, logs, audioData, handleMicToggle };
}