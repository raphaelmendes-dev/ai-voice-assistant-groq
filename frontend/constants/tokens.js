// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Rs4Machine · Design DNA · tokens.js
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
export const TOKENS = {
  cyan:    "#00f0ff",
  purple:  "#8a2be2",
  green:   "#00ff9c",
  blue:    "#3b82f6",
  red:     "#ff3b3b",
  bg:      "#0d1117",
  surface: "#161b22",
  border:  "#21262d",
  text:    "#e0e0e0",
  muted:   "#888888",
  dim:     "#444444",
};

export const STATE_CONFIG = {
  idle: {
    color: TOKENS.cyan,
    label: "STANDBY",
    badge: "OFFLINE",
    rings: 1,
    speed: 3,
  },
  listening: {
    color: TOKENS.green,
    label: "OUVINDO",
    badge: "IA ATIVA",
    rings: 3,
    speed: 1.5,
  },
  thinking: {
    color: TOKENS.blue,
    label: "PROCESSANDO",
    badge: "PROCESSANDO",
    rings: 2,
    speed: 2.5,
  },
  speaking: {
    color: TOKENS.purple,
    label: "FALANDO",
    badge: "FALANDO",
    rings: 4,
    speed: 0.8,
  },
};

// Troca para a URL do Render no deploy
export const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";