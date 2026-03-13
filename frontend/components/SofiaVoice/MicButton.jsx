"use client";
import { STATE_CONFIG } from "@/constants/tokens";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// MicButton — botão do microfone com ripple
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
export default function MicButton({ state, onToggle }) {
  const cfg    = STATE_CONFIG[state];
  const color  = cfg.color;
  const active = state !== "idle";

  return (
    <div style={{ position: "relative", display: "flex", alignItems: "center", justifyContent: "center" }}>

      {/* Ripple waves */}
      {active && [0, 1].map(i => (
        <div key={i} style={{
          position:      "absolute",
          width:         "72px",
          height:        "72px",
          borderRadius:  "50%",
          border:        `1px solid ${color}`,
          animation:     `mic-ripple 2s ease-out ${i * 0.7}s infinite`,
          pointerEvents: "none",
        }} />
      ))}

      {/* Botão principal */}
      <button
        onClick={onToggle}
        aria-label={active ? "Desativar microfone" : "Ativar microfone"}
        style={{
          position:       "relative",
          width:          "64px",
          height:         "64px",
          borderRadius:   "50%",
          background:     active ? `${color}18` : "transparent",
          border:         `2px solid ${color}`,
          color:          color,
          cursor:         "pointer",
          display:        "flex",
          alignItems:     "center",
          justifyContent: "center",
          boxShadow:      active
            ? `0 0 20px ${color}66, 0 0 40px ${color}33, inset 0 0 20px ${color}22`
            : `0 0 8px ${color}33`,
          transition: "all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)",
          animation:  state === "listening" ? "mic-scale 1.5s ease-in-out infinite" : "none",
          outline:    "none",
        }}
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" style={{
          filter:     active ? `drop-shadow(0 0 6px ${color})` : "none",
          transition: "filter 0.3s ease",
        }}>
          <rect x="9" y="2" width="6" height="12" rx="3"
            fill={active ? color : "none"}
            stroke={color} strokeWidth="1.5"
            opacity={active ? 0.9 : 0.7}
          />
          <path d="M5 10a7 7 0 0 0 14 0" stroke={color} strokeWidth="1.5"
            strokeLinecap="round" opacity={active ? 1 : 0.7}
          />
          <line x1="12" y1="17" x2="12" y2="21" stroke={color} strokeWidth="1.5"
            strokeLinecap="round" opacity={active ? 1 : 0.7}
          />
          <line x1="9" y1="21" x2="15" y2="21" stroke={color} strokeWidth="1.5"
            strokeLinecap="round" opacity={active ? 1 : 0.7}
          />
        </svg>
      </button>

      {/* Label */}
      <div style={{
        position:      "absolute",
        bottom:        "-24px",
        fontFamily:    "'JetBrains Mono', monospace",
        fontSize:      "9px",
        letterSpacing: "0.18em",
        color:         color,
        textTransform: "uppercase",
        opacity:       0.7,
        whiteSpace:    "nowrap",
      }}>
        {active ? cfg.label : "PUSH TO TALK"}
      </div>
    </div>
  );
}