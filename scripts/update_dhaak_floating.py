import os

os.makedirs('public/images', exist_ok=True)

# 1. Create a detailed, beautiful floating Dhaak clipart SVG
dhaak_clipart_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 160" width="160" height="160" fill="none">
  <defs>
    <linearGradient id="drumBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBBF24" />
      <stop offset="40%" stop-color="#D97706" />
      <stop offset="100%" stop-color="#78350F" />
    </linearGradient>
    <linearGradient id="featherPlume" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#FEF3C7" />
      <stop offset="100%" stop-color="#FFFFFF" />
    </linearGradient>
    <filter id="drumGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#F59E0B" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Group with subtle angle -->
  <g transform="rotate(-10 80 80)" filter="url(#drumGlow)">
    <!-- White Plumes / Feathers on top -->
    <path d="M 80 32 C 55 5, 30 25, 45 42 C 30 15, 70 -5, 80 32 Z" fill="url(#featherPlume)" opacity="0.95" />
    <path d="M 82 32 C 105 5, 130 25, 115 42 C 130 15, 90 -5, 82 32 Z" fill="url(#featherPlume)" opacity="0.95" />
    <path d="M 80 30 C 70 8, 90 8, 80 30 Z" fill="#FFFFFF" />

    <!-- Red Ribbon / Tassel Tie on Top -->
    <ellipse cx="80" cy="38" rx="8" ry="4" fill="#DC2626" />
    <path d="M 78 40 L 72 56 M 82 40 L 88 56" stroke="#DC2626" stroke-width="2" stroke-linecap="round" />

    <!-- Main Barrel Drum (Dhaak Wood) -->
    <path d="M 38 48 Q 80 38 122 48 Q 134 85 122 122 Q 80 132 38 122 Q 26 85 38 48 Z" fill="url(#drumBody)" stroke="#FDE68A" stroke-width="2.5" />

    <!-- Top Drum Head (Leather Membrane & Ring) -->
    <ellipse cx="80" cy="48" rx="42" ry="12" fill="#B45309" stroke="#FEF3C7" stroke-width="2" />
    <ellipse cx="80" cy="48" rx="34" ry="8" fill="#78350F" />

    <!-- Bottom Drum Head (Leather Membrane & Ring) -->
    <ellipse cx="80" cy="122" rx="42" ry="12" fill="#78350F" stroke="#FEF3C7" stroke-width="2" />

    <!-- Tension Ropes (Cross Lacings - দড়ির জালিকৃতি) -->
    <path d="M 40 52 L 68 118 M 68 52 L 96 118 M 96 52 L 120 118" stroke="#FEF3C7" stroke-width="2" opacity="0.85" />
    <path d="M 68 52 L 40 118 M 96 52 L 68 118 M 120 52 L 96 118" stroke="#FEF3C7" stroke-width="2" opacity="0.85" />

    <!-- Central Tuning Rings (বালা / ধাতব রিং) -->
    <ellipse cx="80" cy="85" rx="46" ry="10" stroke="#FDE68A" stroke-width="2" stroke-dasharray="8 6" fill="none" opacity="0.6" />

    <!-- Pair of Traditional Wooden Drumsticks (Kathi) -->
    <g stroke-linecap="round">
      <line x1="16" y1="35" x2="65" y2="70" stroke="#FDE68A" stroke-width="4" />
      <circle cx="16" cy="35" r="4.5" fill="#EF4444" stroke="#FEF3C7" stroke-width="1.5" />

      <line x1="144" y1="35" x2="95" y2="70" stroke="#FDE68A" stroke-width="4" />
      <circle cx="144" cy="35" r="4.5" fill="#EF4444" stroke="#FEF3C7" stroke-width="1.5" />
    </g>
  </g>
</svg>"""

with open('public/images/dhaak-clipart.svg', 'w', encoding='utf-8') as f:
    f.write(dhaak_clipart_svg)

print("Created public/images/dhaak-clipart.svg")
dhaak_button_code = """'use client';

import React, { useState, useRef, useEffect } from 'react';
import Image from 'next/image';
import { Volume2, VolumeX, Play, Pause, Sparkles } from 'lucide-react';

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

    audio.addEventListener('ended', handleEnded);

    return () => {
      audio.pause();
      audio.removeEventListener('ended', handleEnded);
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
      playBeats(now, 180, 0.25);
      playBeats(now + 0.18, 220, 0.15);
      playBeats(now + 0.36, 150, 0.4);
      playBeats(now + 0.60, 220, 0.15);
      playBeats(now + 0.78, 180, 0.35);
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
          setTimeout(() => setIsPlaying(false), 2000);
        });
    }
  };

  return (
    <div className={`inline-flex items-center ${className}`}>
      <button
        onClick={togglePlayback}
        type="button"
        aria-label={isPlaying ? 'Pause Dhaak sound' : 'Play Dhaak festive sound'}
        className={`group relative h-[46px] px-4 rounded-xl border transition-all duration-300 flex items-center gap-3 backdrop-blur-md shadow-lg ${
          isPlaying
            ? 'bg-amber-500/25 border-amber-400 shadow-[0_0_20px_rgba(245,158,11,0.4)] scale-105'
            : 'bg-black/80 hover:bg-amber-950/40 border-amber-500/40 hover:border-amber-400 hover:shadow-glow-gold'
        }`}
      >
        {/* Floating Clipart Dhaak Drum */}
        <div className="relative w-8 h-8 shrink-0 flex items-center justify-center">
          <div className="relative w-full h-full group-hover:scale-110 transition-transform duration-300 animate-float">
            <Image
              src="/images/dhaak-clipart.svg"
              alt="Festive Dhaak Drum Clipart"
              width={32}
              height={32}
              className="object-contain drop-shadow-[0_2px_8px_rgba(245,158,11,0.5)]"
              priority
            />
          </div>

          {/* Mini Play / Pause State Badge */}
          <div className="absolute -bottom-1 -right-1 w-4 h-4 rounded-full bg-amber-500 text-slate-950 flex items-center justify-center shadow-md">
            {isPlaying ? (
              <Pause className="w-2 h-2 fill-current" />
            ) : (
              <Play className="w-2 h-2 fill-current ml-0.5" />
            )}
          </div>
        </div>

        {/* Text Label */}
        <div className="text-left flex items-center gap-2">
          <div>
            <div className="flex items-center gap-1">
              <span className="text-xs font-bold font-display uppercase tracking-wider text-amber-200">
                {isPlaying ? 'Dhaak Playing...' : 'Festive Dhaak Beats'}
              </span>
            </div>
            <p className="text-[10px] text-amber-300/70 font-mono leading-none">
              {isPlaying ? 'Tap to pause sound' : 'Authentic Sharodotsav audio'}
            </p>
          </div>

          {/* Sound Equalizer when active */}
          {isPlaying && (
            <div className="flex items-center gap-0.5 ml-1">
              <span className="w-1 h-3 bg-amber-400 rounded-full animate-pulse" />
              <span className="w-1 h-4 bg-amber-300 rounded-full animate-pulse delay-75" />
              <span className="w-1 h-2 bg-amber-400 rounded-full animate-pulse delay-150" />
            </div>
          )}
        </div>
      </button>
    </div>
  );
}
"""

with open('src/components/DhaakButton.tsx', 'w', encoding='utf-8') as f:
    f.write(dhaak_button_code)

print("Updated src/components/DhaakButton.tsx")
