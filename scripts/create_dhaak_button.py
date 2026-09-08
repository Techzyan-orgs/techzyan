import os

os.makedirs('public/audio', exist_ok=True)

dhaak_button_code = """'use client';

import React, { useState, useRef, useEffect } from 'react';
import { Volume2, VolumeX, Play, Pause, Sparkles } from 'lucide-react';

interface DhaakButtonProps {
  className?: string;
}

export default function DhaakButton({ className = '' }: DhaakButtonProps) {
  const [isPlaying, setIsPlaying] = useState(false);
  const [audioError, setAudioError] = useState(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  useEffect(() => {
    const audio = new Audio('/audio/dhaak.mp3');
    audio.loop = true;
    audioRef.current = audio;

    const handleEnded = () => setIsPlaying(false);
    const handleError = () => {
      // Audio file might not be placed yet
      setAudioError(true);
    };

    audio.addEventListener('ended', handleEnded);
    audio.addEventListener('error', handleError);

    return () => {
      audio.pause();
      audio.removeEventListener('ended', handleEnded);
      audio.removeEventListener('error', handleError);
    };
  }, []);

  const playSynthesizedDhaakFallback = () => {
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
      // Traditional Taak-Dhum-Taak pattern
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
          // If real audio file is missing or blocked, play rhythmic acoustic fallback
          playSynthesizedDhaakFallback();
          setIsPlaying(true);
          setTimeout(() => setIsPlaying(false), 2000);
        });
    }
  };

  return (
    <div className={`inline-flex flex-col items-center gap-2 ${className}`}>
      <button
        onClick={togglePlayback}
        type="button"
        aria-label={isPlaying ? 'Pause Dhaak sound' : 'Play Dhaak festive sound'}
        className={`group relative p-3 sm:p-3.5 rounded-2xl border transition-all duration-300 flex items-center gap-3 ${
          isPlaying
            ? 'bg-amber-500/25 border-amber-400 shadow-[0_0_25px_rgba(245,158,11,0.4)] scale-105'
            : 'bg-black/70 border-amber-500/40 hover:border-amber-400 hover:bg-amber-950/40 hover:shadow-glow-gold'
        }`}
      >
        {/* Custom SVG Dhaak Drum Icon with Traditional Feathers and Straps */}
        <div className="relative w-11 h-11 shrink-0 flex items-center justify-center">
          <svg
            viewBox="0 0 100 100"
            className={`w-full h-full transition-transform duration-300 ${
              isPlaying ? 'animate-bounce' : 'group-hover:scale-110'
            }`}
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <defs>
              <linearGradient id="drumWood" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#F59E0B" />
                <stop offset="50%" stop-color="#D97706" />
                <stop offset="100%" stop-color="#78350F" />
              </linearGradient>
              <linearGradient id="featherGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#FEF3C7" />
                <stop offset="100%" stop-color="#FDE68A" />
              </linearGradient>
            </defs>

            {/* Traditional White Plumes / Feathers on top of Dhaak */}
            <path
              d="M 50 18 C 35 2, 20 15, 30 25 C 20 8, 45 -2, 50 18 Z"
              fill="url(#featherGrad)"
              opacity="0.9"
            />
            <path
              d="M 52 18 C 65 2, 80 15, 70 25 C 80 8, 55 -2, 52 18 Z"
              fill="url(#featherGrad)"
              opacity="0.9"
            />

            {/* Barrel Dhaak Body */}
            <path
              d="M 22 30 Q 50 24 78 30 Q 86 55 78 80 Q 50 86 22 80 Q 14 55 22 30 Z"
              fill="url(#drumWood)"
              stroke="#FDE68A"
              strokeWidth="2"
            />

            {/* Top Drum Head (Leather Rim) */}
            <ellipse cx="50" cy="30" rx="28" ry="8" fill="#B45309" stroke="#FEF3C7" strokeWidth="2" />
            <ellipse cx="50" cy="30" rx="22" ry="5" fill="#78350F" />

            {/* Bottom Drum Head (Leather Rim) */}
            <ellipse cx="50" cy="80" rx="28" ry="8" fill="#78350F" stroke="#FEF3C7" strokeWidth="1.5" />

            {/* Cross Tension Straps (দড়ির টান) */}
            <path d="M 24 33 L 42 78 M 42 33 L 60 78 M 60 33 L 76 78" stroke="#FEF3C7" strokeWidth="1.5" opacity="0.8" />
            <path d="M 42 33 L 24 78 M 60 33 L 42 78 M 76 33 L 60 78" stroke="#FEF3C7" strokeWidth="1.5" opacity="0.8" />

            {/* Traditional Drum Sticks (Kathi) */}
            <line x1="8" y1="20" x2="40" y2="45" stroke="#FDE68A" strokeWidth="3" strokeLinecap="round" />
            <line x1="92" y1="20" x2="60" y2="45" stroke="#FDE68A" strokeWidth="3" strokeLinecap="round" />
            <circle cx="8" cy="20" r="3.5" fill="#EF4444" />
            <circle cx="92" cy="20" r="3.5" fill="#EF4444" />
          </svg>

          {/* Action Badge Overlay */}
          <div className="absolute -bottom-1 -right-1 w-5 h-5 rounded-full bg-amber-500 text-slate-950 flex items-center justify-center shadow-md">
            {isPlaying ? (
              <Pause className="w-2.5 h-2.5 fill-current" />
            ) : (
              <Play className="w-2.5 h-2.5 fill-current ml-0.5" />
            )}
          </div>
        </div>

        {/* Text Label & Equalizer */}
        <div className="text-left">
          <div className="flex items-center gap-1.5">
            <span className="text-xs font-bold font-display text-amber-200 tracking-wide">
              {isPlaying ? 'Dhaak Playing...' : 'Play Festive Dhaak'}
            </span>
            <Sparkles className="w-3 h-3 text-amber-400" />
          </div>
          <p className="text-[10px] text-amber-300/80 font-mono">
            {isPlaying ? 'Tap drum to pause sound' : 'Sound of Bengal Sharodotsav'}
          </p>
        </div>

        {/* Animated Equalizer Waves when playing */}
        {isPlaying && (
          <div className="flex items-center gap-0.5 ml-1">
            <span className="w-1 h-3 bg-amber-400 rounded-full animate-pulse" />
            <span className="w-1 h-5 bg-amber-300 rounded-full animate-pulse delay-75" />
            <span className="w-1 h-4 bg-amber-400 rounded-full animate-pulse delay-150" />
          </div>
        )}
      </button>
    </div>
  );
}
"""

with open('src/components/DhaakButton.tsx', 'w', encoding='utf-8') as f:
    f.write(dhaak_button_code)

print("DhaakButton component written successfully!")
