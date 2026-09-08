import os

# 1. Update globals.css with authentic Dhaak animations
authentic_css = """
  /* Authentic Bengali Dhaak Striking & Resonance Animations */
  @keyframes authenticKathiRight {
    0%, 100% {
      transform: rotate(0deg);
    }
    20% {
      transform: rotate(-45deg);
    }
    40% {
      transform: rotate(18deg);
    }
    60% {
      transform: rotate(-15deg);
    }
    80% {
      transform: rotate(12deg);
    }
  }

  @keyframes authenticKathiLeft {
    0%, 100% {
      transform: rotate(0deg);
    }
    15% {
      transform: rotate(15deg);
    }
    35% {
      transform: rotate(-40deg);
    }
    55% {
      transform: rotate(20deg);
    }
    75% {
      transform: rotate(-25deg);
    }
    90% {
      transform: rotate(10deg);
    }
  }

  @keyframes impactFlashRight {
    0%, 35%, 45%, 100% {
      opacity: 0;
      transform: scale(0.4);
    }
    40% {
      opacity: 1;
      transform: scale(1.6);
    }
  }

  @keyframes impactFlashLeft {
    0%, 50%, 60%, 100% {
      opacity: 0;
      transform: scale(0.4);
    }
    55% {
      opacity: 1;
      transform: scale(1.6);
    }
  }

  @keyframes authenticDhaakVibe {
    0%, 100% {
      transform: rotate(0deg) scale(1);
    }
    20% {
      transform: rotate(-1.5deg) scale(1.03);
    }
    40% {
      transform: rotate(1deg) scale(0.98);
    }
    60% {
      transform: rotate(-1deg) scale(1.02);
    }
    80% {
      transform: rotate(0.8deg) scale(0.99);
    }
  }

  @keyframes featherSwayLush {
    0%, 100% {
      transform: rotate(0deg);
    }
    30% {
      transform: rotate(-12deg);
    }
    65% {
      transform: rotate(8deg);
    }
  }

  @keyframes soundRippleBig {
    0% {
      transform: scale(0.85);
      opacity: 0.9;
    }
    100% {
      transform: scale(2.5);
      opacity: 0;
    }
  }

  .animate-kathi-right-strike {
    transform-origin: 130px 40px;
    animation: authenticKathiRight 0.48s cubic-bezier(0.4, 0, 0.2, 1) infinite;
  }

  .animate-kathi-left-strike {
    transform-origin: 25px 40px;
    animation: authenticKathiLeft 0.48s cubic-bezier(0.4, 0, 0.2, 1) infinite;
  }

  .animate-impact-right {
    transform-origin: 92px 75px;
    animation: impactFlashRight 0.48s ease-out infinite;
  }

  .animate-impact-left {
    transform-origin: 48px 82px;
    animation: impactFlashLeft 0.48s ease-out infinite;
  }

  .animate-dhaak-body-vibe {
    transform-origin: 75px 80px;
    animation: authenticDhaakVibe 0.48s ease-in-out infinite;
  }

  .animate-feather-lush {
    transform-origin: 85px 45px;
    animation: featherSwayLush 0.48s ease-in-out infinite;
  }

  .animate-sound-ripple-big {
    animation: soundRippleBig 0.96s cubic-bezier(0.1, 0.9, 0.2, 1) infinite;
  }
"""

with open('src/app/globals.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace any existing Dhaak animations block
start_tag = '/* Dhaak Realistic Drumming Animations */'
if start_tag in css_content:
    css_content = css_content[:css_content.find(start_tag)]
    idx = css_content.rfind('}')
    if idx != -1:
        css_content = css_content[:idx] + authentic_css + '\n}\n'
else:
    idx = css_content.rfind('}')
    if idx != -1:
        css_content = css_content[:idx] + authentic_css + '\n}\n'

with open('src/app/globals.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Updated globals.css with authentic striking keyframes!")
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
    <div className={`relative inline-flex items-center justify-center ${className}`}>
      {/* Expanding Concentric Acoustic Ripples when playing */}
      {isPlaying && (
        <>
          <div className="absolute inset-0 rounded-full border-2 border-amber-400/60 animate-sound-ripple-big pointer-events-none" />
          <div className="absolute inset-0 rounded-full border-2 border-amber-500/40 animate-sound-ripple-big pointer-events-none [animation-delay:0.48s]" />
        </>
      )}

      {/* Prominent, High-Definition Floating Dhaak Instrument (No Text) */}
      <button
        onClick={togglePlayback}
        type="button"
        aria-label={isPlaying ? 'Pause Durga Puja Dhaak beats' : 'Play authentic Durga Puja Dhaak beats'}
        title={isPlaying ? 'Click to Pause Dhaak' : 'Click to Play Authentic Bengali Dhaak'}
        className={`group relative w-20 h-20 sm:w-24 sm:h-24 rounded-3xl border flex items-center justify-center transition-all duration-300 backdrop-blur-md shadow-2xl ${
          isPlaying
            ? 'bg-gradient-to-br from-[#2A180A]/90 to-[#180E05]/95 border-amber-400 shadow-[0_0_35px_rgba(245,158,11,0.55)] scale-110'
            : 'bg-gradient-to-br from-[#1A1008]/85 to-[#0D0804]/90 hover:from-[#26150A]/90 hover:to-[#140B05]/95 border-amber-500/40 hover:border-amber-400 hover:shadow-glow-gold hover:scale-105 animate-float'
        }`}
      >
        {/* Soft Golden Ambient Aura */}
        <div className="absolute inset-0 bg-amber-500/15 rounded-3xl blur-md pointer-events-none" />

        {/* High-Fidelity Authentic Bengali Dhaak SVG */}
        <svg
          viewBox="0 0 160 160"
          className="relative z-10 w-16 h-16 sm:w-20 sm:h-20 overflow-visible"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            {/* Seasoned Mango/Mahogany Timber Gradient */}
            <linearGradient id="dhaakWoodGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#F59E0B" />
              <stop offset="35%" stopColor="#B45309" />
              <stop offset="75%" stopColor="#78350F" />
              <stop offset="100%" stopColor="#451A03" />
            </linearGradient>

            {/* Leather Membrane Gradient */}
            <linearGradient id="leatherGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#FDE68A" />
              <stop offset="50%" stopColor="#D97706" />
              <stop offset="100%" stopColor="#92400E" />
            </linearGradient>

            {/* White Feather Plume Gradient (কাশফুল / বকের পালক) */}
            <linearGradient id="lushFeatherGrad" x1="0%" y1="100%" x2="0%" y2="0%">
              <stop offset="0%" stopColor="#FEF3C7" />
              <stop offset="60%" stopColor="#FFFFFF" />
              <stop offset="100%" stopColor="#F1F5F9" />
            </linearGradient>

            {/* Brass Tuning Rings Gradient */}
            <linearGradient id="brassGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#FEF08A" />
              <stop offset="100%" stopColor="#CA8A04" />
            </linearGradient>

            <filter id="dhaakGlow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="3" stdDeviation="4" floodColor="#F59E0B" floodOpacity="0.45" />
            </filter>
          </defs>

          {/* 1. LUSH WHITE FEATHER PLUMES (বকের পালক / সাদা চামর) bound with Crimson Ribbons */}
          <g className={isPlaying ? 'animate-feather-lush' : 'group-hover:-rotate-3 transition-transform duration-300'}>
            {/* Feather Blades Fan */}
            <path d="M 85 45 C 55 12, 22 30, 42 52 C 25 22, 70 -5, 85 45 Z" fill="url(#lushFeatherGrad)" opacity="0.95" />
            <path d="M 88 45 C 115 12, 148 30, 128 52 C 145 22, 100 -5, 88 45 Z" fill="url(#lushFeatherGrad)" opacity="0.95" />
            <path d="M 86 42 C 72 8, 98 8, 86 42 Z" fill="#FFFFFF" />
            <path d="M 75 48 C 50 25, 38 40, 58 56 Z" fill="url(#lushFeatherGrad)" opacity="0.85" />
            <path d="M 97 48 C 122 25, 134 40, 114 56 Z" fill="url(#lushFeatherGrad)" opacity="0.85" />

            {/* Crimson Red Ribbon Ties (লাল রেশমী ফিতে) */}
            <ellipse cx="86" cy="50" rx="8" ry="4.5" fill="#DC2626" stroke="#FEF2F2" strokeWidth="1" />
            <path d="M 82 54 Q 72 70 76 82 M 90 54 Q 98 70 94 82" stroke="#DC2626" strokeWidth="2.5" strokeLinecap="round" />
          </g>

          {/* 2. AUTHENTIC SLANTED DHAAK DRUM BODY (কাঠের মূল কাঠামো) */}
          <g className={isPlaying ? 'animate-dhaak-body-vibe' : ''} filter="url(#dhaakGlow)">
            {/* Slanted Cylindrical Barrel Body */}
            <path
              d="M 45 58 Q 78 48 118 64 Q 130 96 114 128 Q 74 138 38 118 Q 28 88 45 58 Z"
              fill="url(#dhaakWoodGrad)"
              stroke="#FDE68A"
              strokeWidth="2.5"
            />

            {/* Rear/Left Drum Head (বেস চামড়া) */}
            <ellipse cx="42" cy="88" rx="14" ry="30" fill="#78350F" stroke="#FEF3C7" strokeWidth="2" transform="rotate(-15 42 88)" />

            {/* Front/Right Primary Striking Membrane (পুরী / প্রধান মুখের চামড়া) */}
            <ellipse cx="116" cy="96" rx="16" ry="32" fill="url(#leatherGrad)" stroke="#FEF3C7" strokeWidth="2.5" transform="rotate(-15 116 96)" />
            <ellipse cx="116" cy="96" rx="11" ry="24" fill="#B45309" opacity="0.7" transform="rotate(-15 116 96)" />

            {/* Criss-Cross Tension Cords (দড়ির জালিকৃতি) */}
            <path d="M 46 62 L 78 126 M 78 52 L 110 120 M 46 114 L 78 52 M 78 126 L 110 68" stroke="#FEF3C7" strokeWidth="2" opacity="0.9" />
            <path d="M 52 75 L 95 115 M 52 102 L 95 62" stroke="#FEF3C7" strokeWidth="1.5" opacity="0.75" />

            {/* Brass Tuning Rings (পিতলের টানা বালা) */}
            <ellipse cx="68" cy="88" rx="6" ry="12" fill="url(#brassGrad)" stroke="#78350F" strokeWidth="1" transform="rotate(-15 68 88)" />
            <ellipse cx="92" cy="94" rx="6" ry="12" fill="url(#brassGrad)" stroke="#78350F" strokeWidth="1" transform="rotate(-15 92 94)" />
          </g>

          {/* 3. IMPACT CONTACT SPARK FLASHES ON DRUMHEAD */}
          {isPlaying && (
            <>
              {/* Right Drumhead Strike Flash */}
              <g className="animate-impact-right">
                <circle cx="112" cy="88" r="8" fill="#FEF08A" opacity="0.85" />
                <path d="M 112 74 L 112 102 M 98 88 L 126 88 M 102 78 L 122 98 M 102 98 L 122 78" stroke="#F59E0B" strokeWidth="2" strokeLinecap="round" />
              </g>

              {/* Left Rim Strike Flash */}
              <g className="animate-impact-left">
                <circle cx="48" cy="82" r="6" fill="#FEF08A" opacity="0.8" />
                <path d="M 48 72 L 48 92 M 38 82 L 58 82" stroke="#F59E0B" strokeWidth="1.5" strokeLinecap="round" />
              </g>
            </>
          )}

          {/* 4. PRIMARY RIGHT SLENDER CANE DRUMSTICK (ডান হাতের বেতের কাঠি) */}
          <g className={isPlaying ? 'animate-kathi-right-strike' : 'group-hover:-rotate-8 transition-transform duration-200'}>
            {/* Long Flexible Bamboo Stick */}
            <line x1="146" y1="28" x2="114" y2="86" stroke="#FEF08A" strokeWidth="3.5" strokeLinecap="round" />
            <line x1="146" y1="28" x2="114" y2="86" stroke="#B45309" strokeWidth="1.5" strokeLinecap="round" opacity="0.6" />
            {/* Red Grip Handle */}
            <circle cx="146" cy="28" r="4.5" fill="#EF4444" stroke="#FFFFFF" strokeWidth="1.5" />
          </g>

          {/* 5. SECONDARY LEFT SLENDER CANE DRUMSTICK (বাঁ হাতের বেতের কাঠি) */}
          <g className={isPlaying ? 'animate-kathi-left-strike' : 'group-hover:rotate-8 transition-transform duration-200'}>
            {/* Long Flexible Bamboo Stick */}
            <line x1="16" y1="36" x2="46" y2="84" stroke="#FEF08A" strokeWidth="3.5" strokeLinecap="round" />
            <line x1="16" y1="36" x2="46" y2="84" stroke="#B45309" strokeWidth="1.5" strokeLinecap="round" opacity="0.6" />
            {/* Red Grip Handle */}
            <circle cx="16" cy="36" r="4.5" fill="#EF4444" stroke="#FFFFFF" strokeWidth="1.5" />
          </g>
        </svg>

        {/* Small Ambient Music Playing Badge in Corner */}
        <div className={`absolute -bottom-1 -right-1 w-5 h-5 rounded-full flex items-center justify-center text-[9px] font-bold shadow-md transition-all ${
          isPlaying
            ? 'bg-amber-400 text-slate-950 scale-110 shadow-[0_0_10px_#F59E0B]'
            : 'bg-slate-900 text-amber-300 border border-amber-500/50'
        }`}>
          {isPlaying ? '▶' : '♫'}
        </div>
      </button>
    </div>
  );
}
"""

with open('src/components/DhaakButton.tsx', 'w', encoding='utf-8') as f:
    f.write(dhaak_code)

print("Deployed authentic Bengali DhaakButton component successfully!")
