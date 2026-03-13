"use client";
import { STATE_CONFIG } from "@/constants/tokens";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// StatusBadge — badge de status da IA
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
export default function StatusBadge({ state }) {
  const cfg   = STATE_CONFIG[state];
  const color = cfg.color;

  return (
    <div style={{
      display:       "inline-flex",
      alignItems:    "center",
      gap:           "7px",
      padding:       "5px 12px",
      border:        `1px solid ${color}55`,
      borderRadius:  "4px",
      background:    `${color}0d`,
      fontFamily:    "'JetBrains Mono', monospace",
      fontSize:      "10px",
      letterSpacing: "0.15em",
      color:         color,
      textTransform: "uppercase",
      boxShadow:     `0 0 12px ${color}22`,
    }}>
      <div style={{
        width:        "6px",
        height:       "6px",
        borderRadius: "50%",
        background:   color,
        boxShadow:    `0 0 6px ${color}`,
        animation:    "dot-blink 1.2s ease-in-out infinite",
        flexShrink:   0,
      }} />
      {cfg.badge}
    </div>
  );
}