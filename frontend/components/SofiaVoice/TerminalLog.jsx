"use client";
import { useEffect, useRef } from "react";
import { TOKENS } from "@/constants/tokens";

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// TerminalLog — painel de logs estilo terminal
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
export default function TerminalLog({ logs }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [logs]);

  const colorFor = (type) => ({
    user:   TOKENS.cyan,
    ai:     TOKENS.purple,
    system: TOKENS.dim,
    error:  TOKENS.red,
  }[type] ?? TOKENS.muted);

  const prefixFor = (type) => ({
    user:   "▸ USER",
    ai:     "◈ SOFIA",
    system: "⬡ SYS",
    error:  "✖ ERR",
  }[type] ?? "·");

  return (
    <div style={{
      width:        "100%",
      maxWidth:     "560px",
      height:       "180px",
      background:   "#080c10",
      border:       `1px solid ${TOKENS.border}`,
      borderRadius: "6px",
      overflow:     "hidden",
      position:     "relative",
      boxShadow:    "inset 0 0 40px rgba(0,0,0,0.6)",
    }}>

      {/* Header */}
      <div style={{
        display:      "flex",
        alignItems:   "center",
        gap:          "8px",
        padding:      "8px 14px",
        borderBottom: `1px solid ${TOKENS.border}`,
        background:   TOKENS.surface,
      }}>
        {["#ff5f57","#febc2e","#28c840"].map((c, i) => (
          <div key={i} style={{ width: "10px", height: "10px", borderRadius: "50%", background: c, opacity: 0.7 }} />
        ))}
        <span style={{
          marginLeft:    "8px",
          fontFamily:    "'JetBrains Mono', monospace",
          fontSize:      "10px",
          letterSpacing: "0.15em",
          color:         TOKENS.dim,
          textTransform: "uppercase",
        }}>
          rs4machine · sofia · terminal
        </span>
        <div style={{ marginLeft: "auto", display: "flex", gap: "4px" }}>
          {[TOKENS.green, TOKENS.blue, TOKENS.purple].map((c, i) => (
            <div key={i} style={{
              width:        "4px",
              height:       "4px",
              borderRadius: "50%",
              background:   c,
              animation:    `blink-stagger ${1 + i * 0.3}s ease-in-out ${i * 0.2}s infinite`,
            }} />
          ))}
        </div>
      </div>

      {/* Linhas de log */}
      <div style={{
        padding:        "10px 14px",
        height:         "calc(100% - 37px)",
        overflowY:      "auto",
        scrollbarWidth: "thin",
        scrollbarColor: `${TOKENS.border} transparent`,
      }}>
        {logs.map((log, i) => (
          <div key={i} style={{
            display:           "flex",
            gap:               "10px",
            marginBottom:      "4px",
            animation:         "fade-in-line 0.3s ease-out forwards",
            opacity:           0,
            animationFillMode: "forwards",
            animationDelay:    "0ms",
          }}>
            <span style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize:   "9px",
              color:      TOKENS.dim,
              whiteSpace: "nowrap",
              paddingTop: "1px",
              minWidth:   "42px",
            }}>
              {log.time}
            </span>
            <span style={{
              fontFamily:    "'JetBrains Mono', monospace",
              fontSize:      "9px",
              color:         colorFor(log.type),
              fontWeight:    "600",
              letterSpacing: "0.08em",
              whiteSpace:    "nowrap",
              paddingTop:    "1px",
              minWidth:      "52px",
              textShadow:    `0 0 8px ${colorFor(log.type)}88`,
            }}>
              {prefixFor(log.type)}
            </span>
            <span style={{
              fontFamily: "'JetBrains Mono', monospace",
              fontSize:   "11px",
              color:      log.type === "system" ? TOKENS.muted : TOKENS.text,
              lineHeight: "1.6",
              opacity:    log.type === "system" ? 0.5 : 0.9,
            }}>
              {log.text}
              {i === logs.length - 1 && (
                <span style={{
                  color:      colorFor(log.type),
                  animation:  "cursor-blink 1s step-end infinite",
                  marginLeft: "2px",
                }}>█</span>
              )}
            </span>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>
    </div>
  );
}