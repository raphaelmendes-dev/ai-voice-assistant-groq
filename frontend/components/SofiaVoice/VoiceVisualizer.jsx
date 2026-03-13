"use client";
import { STATE_CONFIG } from "@/constants/tokens";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// VoiceVisualizer — círculo animado central
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
export default function VoiceVisualizer({ state, audioData }) {
  const cfg   = STATE_CONFIG[state];
  const color = cfg.color;

  const bars = Array.from({ length: 32 }, (_, i) => {
    const base   = audioData?.[i] ?? 0;
    const height = state === "speaking"
      ? 8 + base * 0.6 + Math.sin(Date.now() / 200 + i * 0.4) * 12
      : state === "listening"
      ? 4 + Math.sin(Date.now() / 400 + i * 0.3) * 8
      : 2;
    return Math.max(2, Math.min(60, height));
  });

  return (
    <div style={{
      position:       "relative",
      width:          "260px",
      height:         "260px",
      display:        "flex",
      alignItems:     "center",
      justifyContent: "center",
    }}>

      {/* Anéis de expansão */}
      {Array.from({ length: cfg.rings }).map((_, i) => (
        <div key={i} style={{
          position:     "absolute",
          width:        `${140 + i * 36}px`,
          height:       `${140 + i * 36}px`,
          borderRadius: "50%",
          border:       `1px solid ${color}`,
          opacity:      state === "idle" ? 0.08 : 0,
          animation:    state !== "idle"
            ? `ring-expand ${cfg.speed + i * 0.4}s ease-out ${i * (cfg.speed / cfg.rings)}s infinite`
            : "none",
          boxShadow: `0 0 12px ${color}22`,
        }} />
      ))}

      {/* Anel outer estático */}
      <div style={{
        position:     "absolute",
        width:        "200px",
        height:       "200px",
        borderRadius: "50%",
        border:       `1px solid ${color}33`,
        boxShadow:    `0 0 20px ${color}22, inset 0 0 20px ${color}11`,
      }} />

      {/* Círculo principal */}
      <div style={{
        position:       "relative",
        width:          "140px",
        height:         "140px",
        borderRadius:   "50%",
        border:         `2px solid ${color}`,
        background:     `radial-gradient(circle at center, ${color}18 0%, ${color}06 50%, transparent 70%)`,
        boxShadow:      `0 0 30px ${color}55, 0 0 60px ${color}22, inset 0 0 30px ${color}22`,
        display:        "flex",
        alignItems:     "center",
        justifyContent: "center",
        animation:      state === "thinking"
          ? "spin-slow 4s linear infinite"
          : state === "idle"
          ? "idle-breathe 3s ease-in-out infinite"
          : "core-pulse 1.2s ease-in-out infinite",
        transition: "border-color 0.6s ease, box-shadow 0.6s ease",
      }}>

        {/* Scan lines — thinking */}
        {state === "thinking" && (
          <div style={{ position: "absolute", inset: "4px", borderRadius: "50%", overflow: "hidden", opacity: 0.3 }}>
            {Array.from({ length: 6 }).map((_, i) => (
              <div key={i} style={{
                position:   "absolute",
                left: 0, right: 0,
                height:     "1px",
                background: color,
                top:        `${10 + i * 16}%`,
                opacity:    0.6,
              }} />
            ))}
          </div>
        )}

        {/* Barras — speaking */}
        {state === "speaking" && (
          <div style={{ display: "flex", alignItems: "center", gap: "2px", height: "60px" }}>
            {bars.slice(0, 18).map((h, i) => (
              <div key={i} style={{
                width:        "3px",
                height:       `${h}px`,
                background:   `linear-gradient(to top, ${color}, ${color}88)`,
                borderRadius: "2px",
                boxShadow:    `0 0 4px ${color}88`,
                transition:   "height 0.05s ease",
              }} />
            ))}
          </div>
        )}

        {/* Ondas — listening */}
        {state === "listening" && (
          <svg width="80" height="40" viewBox="0 0 80 40">
            {[0, 1, 2].map((i) => (
              <path key={i}
                d={`M ${8 + i * 8} 20 Q ${20 + i * 6} ${10 - i * 3} ${32 + i * 8} 20 Q ${44 + i * 4} ${30 + i * 3} ${56 + i * 4} 20`}
                fill="none"
                stroke={color}
                strokeWidth="1.5"
                strokeLinecap="round"
                style={{
                  opacity:   0.6 - i * 0.15,
                  animation: `wave-move ${1 + i * 0.3}s ease-in-out ${i * 0.2}s infinite alternate`,
                }}
              />
            ))}
          </svg>
        )}

        {/* Ícone idle */}
        {state === "idle" && (
          <svg width="32" height="32" viewBox="0 0 24 24" fill="none">
            <circle cx="12" cy="12" r="3" fill={color} opacity="0.8" />
            <circle cx="12" cy="12" r="6" stroke={color} strokeWidth="1" opacity="0.4" />
          </svg>
        )}
      </div>

      {/* Label de estado */}
      <div style={{
        position:      "absolute",
        bottom:        "-8px",
        fontFamily:    "'JetBrains Mono', monospace",
        fontSize:      "10px",
        letterSpacing: "0.2em",
        color:         color,
        textTransform: "uppercase",
        textShadow:    `0 0 10px ${color}`,
        opacity:       0.9,
      }}>
        {cfg.label}
      </div>
    </div>
  );
}