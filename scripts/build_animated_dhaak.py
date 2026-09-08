import os

# 1. Update globals.css with precision drumming keyframe animations
css_additions = """
  /* Dhaak Realistic Drumming Animations */
  @keyframes strikeLeft {
    0%, 100% {
      transform: rotate(0deg);
    }
    30% {
      transform: rotate(28deg);
    }
    50% {
      transform: rotate(-8deg);
    }
    75% {
      transform: rotate(22deg);
    }
  }

  @keyframes strikeRight {
    0%, 100% {
      transform: rotate(0deg);
    }
    20% {
      transform: rotate(-10deg);
    }
    45% {
      transform: rotate(-30deg);
    }
    65% {
      transform: rotate(8deg);
    }
    85% {
      transform: rotate(-24deg);
    }
  }

  @keyframes dhaakPulse {
    0%, 100% {
      transform: scale(1) rotate(0deg);
    }
    25% {
      transform: scale(1.04) rotate(-1.5deg);
    }
    50% {
      transform: scale(0.98) rotate(1deg);
    }
    75% {
      transform: scale(1.03) rotate(-0.5deg);
    }
  }

  @keyframes featherSway {
    0%, 100% {
      transform: rotate(0deg);
    }
    35% {
      transform: rotate(-8deg);
    }
    70% {
      transform: rotate(6deg);
    }
  }

  @keyframes acousticRing {
    0% {
      transform: scale(0.8);
      opacity: 0.8;
    }
    100% {
      transform: scale(2.2);
      opacity: 0;
    }
  }

  .animate-kathi-left {
    transform-origin: 18px 30px;
    animation: strikeLeft 0.55s ease-in-out infinite;
  }

  .animate-kathi-right {
    transform-origin: 102px 30px;
    animation: strikeRight 0.55s ease-in-out infinite;
  }

  .animate-dhaak-body {
    transform-origin: center;
    animation: dhaakPulse 0.55s ease-in-out infinite;
  }

  .animate-feather-sway {
    transform-origin: 60px 25px;
    animation: featherSway 0.55s ease-in-out infinite;
  }

  .animate-acoustic-ring {
    animation: acousticRing 1.1s cubic-bezier(0.2, 0.8, 0.2, 1) infinite;
  }
"""

with open('src/app/globals.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace before the last closing bracket of @layer utilities
if '/* Dhaak Realistic Drumming Animations */' not in css_content:
    idx = css_content.rfind('}')
    if idx != -1:
        css_content = css_content[:idx] + css_additions + '\n}\n'
        with open('src/app/globals.css', 'w', encoding='utf-8') as f:
            f.write(css_content)
        print("Updated globals.css with drumming keyframes")

# 2. Create the purely icon-based, animated DhaakButton component
dhaak_component = """'use client';

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
          setTimeout(() => setIsPlaying(false), 2200);
        });
    }
  };

  return (
    <div className={`relative inline-flex items-center justify-center ${className}`}>
      {/* Expanding Acoustic Shockwave Rings when playing */}
      {isPlaying && (
        <>
          <div className="absolute inset-0 rounded-full border-2 border-amber-400/60 animate-acoustic-ring pointer-events-none" />
          <div className="absolute inset-0 rounded-full border-2 border-amber-500/40 animate-acoustic-ring pointer-events-none [animation-delay:0.55s]" />
        </>
      )}

      {/* Floating Animated Dhaak Icon Button (No Text) */}
      <button
        onClick={togglePlayback}
        type="button"
        aria-label={isPlaying ? 'Pause Dhaak drumming beats' : 'Play Dhaak drumming beats'}
        title={isPlaying ? 'Click to Pause Dhaak' : 'Click to Play Dhaak Drum'}
        className={`group relative w-14 h-14 sm:w-16 sm:h-16 rounded-2xl sm:rounded-3xl border flex items-center justify-center transition-all duration-300 backdrop-blur-md shadow-2xl ${
          isPlaying
            ? 'bg-amber-500/30 border-amber-400 shadow-[0_0_30px_rgba(245,158,11,0.5)] scale-110'
            : 'bg-black/80 hover:bg-amber-950/40 border-amber-500/40 hover:border-amber-400 hover:shadow-glow-gold hover:scale-105 animate-float'
        }`}
      >
        {/* Soft Golden Ambient Glow */}
        <div className="absolute inset-0 bg-amber-500/20 rounded-2xl sm:rounded-3xl blur-md pointer-events-none" />

        {/* Precision Multi-Layer Animated Dhaak SVG */}
        <svg
          viewBox="0 0 120 120"
          className="relative z-10 w-11 h-11 sm:w-12 sm:h-12 overflow-visible"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            <linearGradient id="drumWoodGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#FBBF24" />
              <stop offset="45%" stopColor="#D97706" />
              <stop offset="100%" stopColor="#78350F" />
            </linearGradient>
            <linearGradient id="featherPlumeGrad" x1="0%" y1="100%" x2="0%" y2="0%">
              <stop offset="0%" stopColor="#FEF3C7" />
              <stop offset="100%" stopColor="#FFFFFF" />
            </linearGradient>
            <filter id="drumGlowFilter" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="2" stdDeviation="4" floodColor="#F59E0B" floodOpacity="0.5" />
            </filter>
          </defs>

          {/* 1. Swaying Feather Plumes on Top (কাশফুল / শ্বেত চামর) */}
          <g className={isPlaying ? 'animate-feather-sway' : ''}>
            <path
              d="M 60 22 C 40 2, 20 18, 32 30 C 20 10, 52 -4, 60 22 Z"
              fill="url(#featherPlumeGrad)"
              opacity="0.95"
            />
            <path
              d="M 62 22 C 80 2, 100 18, 88 30 C 100 10, 68 -4, 62 22 Z"
              fill="url(#featherPlumeGrad)"
              opacity="0.95"
            />
            {/* Red Feather Knot Ribbon */}
            <circle cx="60" cy="27" r="4" fill="#DC2626" />
            <path d="M 58 29 L 52 39 M 62 29 L 68 39" stroke="#DC2626" strokeWidth="1.5" strokeLinecap="round" />
          </g>

          {/* 2. Resonating Drum Body (দোদুল্যমান ঢাক) */}
          <g className={isPlaying ? 'animate-dhaak-body' : ''} filter="url(#drumGlowFilter)">
            {/* Barrel Body */}
            <path
              d="M 30 35 Q 60 28 90 35 Q 98 62 90 90 Q 60 97 30 90 Q 22 62 30 35 Z"
              fill="url(#drumWoodGrad)"
              stroke="#FDE68A"
              strokeWidth="2"
            />

            {/* Top Drum Head (Leather Rim) */}
            <ellipse cx="60" cy="35" rx="30" ry="8" fill="#B45309" stroke="#FEF3C7" strokeWidth="1.5" />
            <ellipse cx="60" cy="35" rx="24" ry="5.5" fill="#78350F" />

            {/* Bottom Drum Head (Leather Rim) */}
            <ellipse cx="60" cy="90" rx="30" ry="8" fill="#78350F" stroke="#FEF3C7" strokeWidth="1.5" />

            {/* Cross Tension Lacings (দড়ির টান) */}
            <path d="M 32 38 L 52 87 M 52 38 L 72 87 M 72 38 L 88 87" stroke="#FEF3C7" strokeWidth="1.5" opacity="0.85" />
            <path d="M 52 38 L 32 87 M 72 38 L 52 87 M 88 38 L 72 87" stroke="#FEF3C7" strokeWidth="1.5" opacity="0.85" />

            {/* Central Metal Tuning Ring */}
            <ellipse cx="60" cy="62" rx="33" ry="7" stroke="#FDE68A" strokeWidth="1.5" strokeDasharray="6 4" fill="none" opacity="0.6" />
          </g>

          {/* 3. Left Striking Drumstick (Kathi - কাঠি) */}
          <g className={isPlaying ? 'animate-kathi-left' : 'group-hover:-rotate-6 transition-transform'}>
            <line x1="12" y1="20" x2="48" y2="44" stroke="#FDE68A" strokeWidth="3" strokeLinecap="round" />
            <circle cx="12" cy="20" r="3.5" fill="#EF4444" stroke="#FEF3C7" strokeWidth="1" />
          </g>

          {/* 4. Right Striking Drumstick (Kathi - কাঠি) */}
          <g className={isPlaying ? 'animate-kathi-right' : 'group-hover:rotate-6 transition-transform'}>
            <line x1="108" y1="20" x2="72" y2="44" stroke="#FDE68A" strokeWidth="3" strokeLinecap="round" />
            <circle cx="108" cy="20" r="3.5" fill="#EF4444" stroke="#FEF3C7" strokeWidth="1" />
          </g>
        </svg>

        {/* Subtle Live Play/Pause State Indicator Ring in corner */}
        <div className={`absolute -bottom-1 -right-1 w-4 h-4 rounded-full flex items-center justify-center text-[8px] font-bold shadow-md transition-colors ${
          isPlaying ? 'bg-amber-400 text-slate-950 animate-pulse' : 'bg-slate-800 text-amber-300 border border-amber-500/40'
        }`}>
          {isPlaying ? '▶' : '♫'}
        </div>
      </button>
    </div>
  );
}
"""

with open('src/components/DhaakButton.tsx', 'w', encoding='utf-8') as f:
    f.write(dhaak_component)

print("Built animated text-free DhaakButton component successfully!")
