import os

dhaak_tsx_path = r"c:\Users\Samudra Ganguly\Antigravity\Website_005\techzyan\src\components\DhaakButton.tsx"

dhaak_code = """'use client';

import React, { useState, useRef, useEffect } from 'react';

interface DhaakButtonProps {
  className?: string;
}

export default function DhaakButton({ className = '' }: DhaakButtonProps) {
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  useEffect(() => {
    const audio = new Audio('/audio/dhaak.mp3');
    audio.loop = true;
    audioRef.current = audio;

    const handleEnded = () => setIsPlaying(false);
    const handlePause = () => setIsPlaying(false);
    const handlePlay = () => setIsPlaying(true);

    audio.addEventListener('ended', handleEnded);
    audio.addEventListener('pause', handlePause);
    audio.addEventListener('play', handlePlay);

    return () => {
      audio.pause();
      audio.removeEventListener('ended', handleEnded);
      audio.removeEventListener('pause', handlePause);
      audio.removeEventListener('play', handlePlay);
    };
  }, []);

  const playSynthesizedFallback = () => {
    try {
      const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      
      const playBeats = (time: number, freq: number, duration: number) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, time);
        osc.frequency.exponentialRampToValueAtTime(30, time + duration);
        gain.gain.setValueAtTime(0.4, time);
        gain.gain.exponentialRampToValueAtTime(0.01, time + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(time);
        osc.stop(time + duration);
      };

      const now = ctx.currentTime;
      playBeats(now, 190, 0.22);
      playBeats(now + 0.16, 230, 0.14);
      playBeats(now + 0.32, 160, 0.38);
      playBeats(now + 0.54, 230, 0.14);
      playBeats(now + 0.70, 190, 0.32);
    } catch (err) {
      console.warn('Audio fallback error:', err);
    }
  };

  const togglePlayback = () => {
    if (!audioRef.current) return;

    if (isPlaying) {
      audioRef.current.pause();
      setIsPlaying(false);
    } else {
      audioRef.current.currentTime = 0;
      audioRef.current.play()
        .then(() => {
          setIsPlaying(true);
        })
        .catch(() => {
          playSynthesizedFallback();
          setIsPlaying(true);
          setTimeout(() => setIsPlaying(false), 2400);
        });
    }
  };

  return (
    <div className={`relative inline-flex flex-col items-center select-none ${className}`}>
      {/* Floating Musical Notes when playing */}
      {isPlaying && (
        <div className="absolute -top-7 left-0 right-0 pointer-events-none z-30 flex justify-between px-3">
          <span className="text-amber-300 text-base font-bold animate-note-float-1 drop-shadow-[0_0_6px_rgba(245,158,11,0.9)]">
            ♪
          </span>
          <span className="text-amber-400 text-lg font-bold animate-note-float-2 drop-shadow-[0_0_6px_rgba(243,156,18,0.9)]">
            ♫
          </span>
          <span className="text-amber-100 text-sm font-bold animate-note-float-3 drop-shadow-[0_0_6px_rgba(255,255,255,0.9)]">
            ♩
          </span>
        </div>
      )}

      {/* Rounded-Corner Box Container around the Dhaak */}
      <button
        onClick={togglePlayback}
        type="button"
        aria-label={isPlaying ? 'Pause Durga Puja Dhaak beats' : 'Play authentic Durga Puja Dhaak beats'}
        title={isPlaying ? 'Click to Pause Dhaak beats' : 'Click to Play Durga Puja Dhaak beats'}
        className={`group relative px-4 py-3 sm:px-5 sm:py-3.5 rounded-3xl border flex flex-col items-center justify-center transition-all duration-300 backdrop-blur-md shadow-2xl cursor-pointer ${
          isPlaying
            ? 'bg-gradient-to-br from-[#241407]/95 via-[#1A0E04]/95 to-[#0E0602]/98 border-amber-400 shadow-[0_0_35px_rgba(245,158,11,0.6)] scale-105'
            : 'bg-gradient-to-br from-[#160D05]/90 via-[#100903]/90 to-[#0A0502]/95 hover:from-[#221307]/95 hover:to-[#120803]/95 border-amber-500/40 hover:border-amber-400 hover:shadow-glow-gold hover:scale-105 animate-float'
        }`}
      >
        {/* Soft Golden Ambient Aura */}
        <div className="absolute inset-0 bg-amber-500/15 rounded-3xl blur-md pointer-events-none" />

        {/* Authentic Bengali Dhaak SVG Illustration from baruipurbhattacharyaparapujo.info */}
        <svg
          viewBox="0 0 240 140"
          className={`relative z-10 w-28 h-16 sm:w-32 sm:h-20 filter drop-shadow-[0_6px_14px_rgba(0,0,0,0.85)] transition-all duration-300 ${
            isPlaying
              ? 'drop-shadow-[0_8px_22px_rgba(243,156,18,0.7)]'
              : 'hover:drop-shadow-[0_8px_20px_rgba(243,156,18,0.4)]'
          }`}
          preserveAspectRatio="xMidYMid meet"
        >
          <defs>
            {/* Realistic Wood Gradient */}
            <linearGradient id="framelessWood" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#962d0e" />
              <stop offset="25%" stopColor="#c03f16" />
              <stop offset="55%" stopColor="#6e210b" />
              <stop offset="85%" stopColor="#451406" />
              <stop offset="100%" stopColor="#250a03" />
            </linearGradient>

            {/* Red / Crimson Gamchha Cloth Wrap */}
            <linearGradient id="framelessCloth" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#ff4d4d" />
              <stop offset="35%" stopColor="#d9272e" />
              <stop offset="70%" stopColor="#961118" />
              <stop offset="100%" stopColor="#55080c" />
            </linearGradient>

            {/* Parchment Goat Leather Skin Drum Head */}
            <radialGradient id="framelessHead" cx="45%" cy="48%" r="52%">
              <stop offset="0%" stopColor="#fdf6ea" />
              <stop offset="55%" stopColor="#e8cca0" />
              <stop offset="85%" stopColor="#ba8d53" />
              <stop offset="100%" stopColor="#6e461b" />
            </radialGradient>

            {/* Cane Beating Sticks (Kathi) */}
            <linearGradient id="framelessKathi" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#fff4df" />
              <stop offset="40%" stopColor="#e5b061" />
              <stop offset="100%" stopColor="#9e6616" />
            </linearGradient>

            {/* Polished Brass Rings & Fixtures */}
            <linearGradient id="framelessBrass" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stopColor="#e67e22" />
              <stop offset="35%" stopColor="#f1c40f" />
              <stop offset="75%" stopColor="#f39c12" />
              <stop offset="100%" stopColor="#a85202" />
            </linearGradient>
          </defs>

          {/* Sound Wave Resonance Rings (When Playing) */}
          {isPlaying && (
            <g transform="translate(178, 70)">
              <ellipse
                cx="0"
                cy="0"
                rx="22"
                ry="38"
                fill="none"
                stroke="#f1c40f"
                strokeWidth="2.5"
                className="animate-sound-ring-1"
              />
              <ellipse
                cx="0"
                cy="0"
                rx="36"
                ry="54"
                fill="none"
                stroke="#f39c12"
                strokeWidth="2"
                className="animate-sound-ring-2"
              />
              <ellipse
                cx="0"
                cy="0"
                rx="50"
                ry="70"
                fill="none"
                stroke="#d9272e"
                strokeWidth="1.5"
                className="animate-sound-ring-3"
              />
            </g>
          )}

          {/* Dhaak Drum Body with Rhythmic Pulsing */}
          <g className={isPlaying ? 'animate-dhaak-beat origin-[115px_70px]' : ''}>
            {/* Left Drum Head */}
            <ellipse cx="48" cy="70" rx="14" ry="38" fill="#421a08" stroke="url(#framelessBrass)" strokeWidth="2" />
            <ellipse cx="50" cy="70" rx="11" ry="34" fill="url(#framelessHead)" stroke="#2b1104" strokeWidth="1" />
            <ellipse cx="50" cy="70" rx="5" ry="16" fill="#caa066" opacity="0.6" />

            {/* Wood Barrel Body */}
            <path
              d="M 48,36 C 95,20 135,20 178,36 L 178,104 C 135,120 95,120 48,104 Z"
              fill="url(#framelessWood)"
              stroke="#3e1204"
              strokeWidth="1.5"
            />

            {/* Brass Bands */}
            <path d="M 60,33 C 65,58 65,82 60,107" stroke="url(#framelessBrass)" strokeWidth="2.5" fill="none" />
            <path d="M 166,33 C 171,58 171,82 166,107" stroke="url(#framelessBrass)" strokeWidth="2.5" fill="none" />

            {/* Red / Crimson Decorative Gamchha Wrap */}
            <path
              d="M 88,26 C 114,23 128,23 150,27 L 150,113 C 128,117 114,117 88,114 Z"
              fill="url(#framelessCloth)"
              stroke="#f1c40f"
              strokeWidth="1.2"
            />
            <path d="M 90,26 L 90,114" stroke="#f1c40f" strokeWidth="2" strokeDasharray="3 1.5" />
            <path d="M 148,27 L 148,113" stroke="#f1c40f" strokeWidth="2" strokeDasharray="3 1.5" />

            {/* Center Golden Medallion */}
            <circle cx="119" cy="70" r="10" fill="#961118" stroke="#f1c40f" strokeWidth="1.5" />
            <circle cx="119" cy="70" r="5" fill="#f1c40f" />
            <path d="M 119,56 L 119,84 M 105,70 L 133,70" stroke="#f39c12" strokeWidth="1.2" />

            {/* Tension Cords & Tuning Rings */}
            <g stroke="#f39c12" strokeWidth="1.4" opacity="0.9" fill="none">
              <line x1="60" y1="35" x2="105" y2="114" />
              <line x1="105" y1="24" x2="150" y2="114" />
              <line x1="150" y1="27" x2="178" y2="104" />
              <line x1="60" y1="105" x2="105" y2="24" />
              <line x1="105" y1="114" x2="150" y2="27" />
              <line x1="150" y1="113" x2="178" y2="36" />
              <circle cx="82" cy="73" r="2.8" fill="#f1c40f" stroke="#78350f" strokeWidth="0.8" />
              <circle cx="127" cy="67" r="2.8" fill="#f1c40f" stroke="#78350f" strokeWidth="0.8" />
              <circle cx="164" cy="71" r="2.8" fill="#f1c40f" stroke="#78350f" strokeWidth="0.8" />
            </g>

            {/* Right Drum Head */}
            <ellipse cx="178" cy="70" rx="14" ry="38" fill="#421a08" stroke="url(#framelessBrass)" strokeWidth="2" />
            <ellipse cx="176" cy="70" rx="11" ry="34" fill="url(#framelessHead)" stroke="#2b1104" strokeWidth="1" />
            <ellipse cx="176" cy="70" rx="5.5" ry="16" fill="#caa066" opacity="0.6" />
            {isPlaying && (
              <ellipse cx="177" cy="68" rx="8" ry="18" fill="#ffffff" opacity="0.5" className="animate-pulse" />
            )}
          </g>

          {/* Primary Beating Stick (Kathi) */}
          <g className={`origin-[218px_26px] ${isPlaying ? 'animate-kathi-primary' : ''}`}>
            <path
              d="M 226,16 C 210,36 195,56 177,66"
              stroke="url(#framelessKathi)"
              strokeWidth="3.4"
              strokeLinecap="round"
              fill="none"
              filter="drop-shadow(1px 2px 2px rgba(0,0,0,0.7))"
            />
            <circle cx="177" cy="66" r="2.8" fill="#5c3807" stroke="#fff" strokeWidth="0.6" />
            <line x1="223" y1="20" x2="218" y2="28" stroke="#d9272e" strokeWidth="3.8" />
          </g>

          {/* Secondary Beating Stick (Kathi) */}
          <g className={`origin-[225px_42px] ${isPlaying ? 'animate-kathi-secondary' : ''}`}>
            <path
              d="M 232,32 C 216,50 200,66 179,76"
              stroke="url(#framelessKathi)"
              strokeWidth="3"
              strokeLinecap="round"
              fill="none"
              filter="drop-shadow(1px 2px 2px rgba(0,0,0,0.7))"
            />
            <circle cx="179" cy="76" r="2.6" fill="#5c3807" stroke="#fff" strokeWidth="0.6" />
            <line x1="229" y1="36" x2="224" y2="43" stroke="#d9272e" strokeWidth="3.4" />
          </g>
        </svg>

        {/* Status Text Indicator */}
        <span className="relative z-10 mt-1 text-[10px] font-mono tracking-wider uppercase text-amber-300/80 group-hover:text-amber-200 transition-colors">
          {isPlaying ? 'Beats Playing...' : 'Click to Play Dhaak'}
        </span>
      </button>
    </div>
  );
}
"""

with open(dhaak_tsx_path, "w", encoding="utf-8") as f:
    f.write(dhaak_code)

print("Updated DhaakButton.tsx successfully!")
