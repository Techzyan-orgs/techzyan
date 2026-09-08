import os

realistic_dhaak_code = """'use client';

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

      {/* Prominent, Realistic Floating Dhaak Instrument Button */}
      <button
        onClick={togglePlayback}
        type="button"
        aria-label={isPlaying ? 'Pause Durga Puja Dhaak beats' : 'Play authentic Durga Puja Dhaak beats'}
        title={isPlaying ? 'Click to Pause Dhaak' : 'Click to Play Authentic Bengali Dhaak'}
        className={`group relative w-24 h-24 sm:w-28 sm:h-28 rounded-3xl border flex items-center justify-center transition-all duration-300 backdrop-blur-md shadow-2xl ${
          isPlaying
            ? 'bg-gradient-to-br from-[#241407]/95 via-[#1A0E04]/95 to-[#0E0602]/98 border-amber-400 shadow-[0_0_40px_rgba(245,158,11,0.6)] scale-110'
            : 'bg-gradient-to-br from-[#160D05]/90 via-[#100903]/90 to-[#0A0502]/95 hover:from-[#221307]/95 hover:to-[#120803]/95 border-amber-500/40 hover:border-amber-400 hover:shadow-glow-gold hover:scale-105 animate-float'
        }`}
      >
        {/* Soft Golden Ambient Aura */}
        <div className="absolute inset-0 bg-amber-500/15 rounded-3xl blur-md pointer-events-none" />

        {/* Ultra-Realistic Bengali Dhaak SVG Illustration */}
        <svg
          viewBox="0 0 200 200"
          className="relative z-10 w-20 h-20 sm:w-24 sm:h-24 overflow-visible"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            {/* Realistic Cylindrical Wood Shading (Mahogany / Mango timber) */}
            <linearGradient id="realWoodCylinder" x1="20%" y1="0%" x2="80%" y2="100%">
              <stop offset="0%" stopColor="#92400E" />
              <stop offset="25%" stopColor="#B45309" />
              <stop offset="50%" stopColor="#78350F" />
              <stop offset="80%" stopColor="#451A03" />
              <stop offset="100%" stopColor="#1C0A00" />
            </linearGradient>

            {/* Specular Highlight along wooden barrel ridge */}
            <linearGradient id="woodSpecular" x1="0%" y1="0%" x2="100%" y2="50%">
              <stop offset="0%" stopColor="#FDE68A" stopOpacity="0.4" />
              <stop offset="40%" stopColor="#D97706" stopOpacity="0.1" />
              <stop offset="100%" stopColor="#000000" stopOpacity="0.6" />
            </linearGradient>

            {/* Real Calfskin / Parchment Leather Head with Stained Resonance Patch */}
            <radialGradient id="realLeatherSkin" cx="45%" cy="50%" r="50%">
              <stop offset="0%" stopColor="#FEF3C7" />
              <stop offset="45%" stopColor="#FDE68A" />
              <stop offset="75%" stopColor="#D97706" />
              <stop offset="95%" stopColor="#92400E" />
              <stop offset="100%" stopColor="#5B210B" />
            </radialGradient>

            {/* Natural White Feather Plume Gradient with Subtle Translucency */}
            <linearGradient id="realFeatherLight" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#FFFFFF" />
              <stop offset="60%" stopColor="#F8FAFC" />
              <stop offset="85%" stopColor="#E2E8F0" />
              <stop offset="100%" stopColor="#CBD5E1" />
            </linearGradient>

            {/* Polished Brass Ring Gradient */}
            <linearGradient id="realBrass" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#FEF08A" />
              <stop offset="40%" stopColor="#EAB308" />
              <stop offset="80%" stopColor="#A16207" />
              <stop offset="100%" stopColor="#713F12" />
            </linearGradient>

            {/* Deep Ambient Occlusion Shadow Filter */}
            <filter id="realDhaakShadow" x="-30%" y="-30%" width="160%" height="160%">
              <feDropShadow dx="0" dy="6" stdDeviation="5" floodColor="#000000" floodOpacity="0.7" />
            </filter>
          </defs>

          {/* ========================================================================= */}
          {/* 1. SOFT, ORGANIC WHITE CRANE/CHAMOR FEATHER PLUMES (সাদা পালক / কাশফুল গুচ্ছ) */}
          {/* ========================================================================= */}
          <g className={isPlaying ? 'animate-feather-lush' : 'group-hover:-rotate-3 transition-transform duration-300'}>
            {/* Rear Feathers (Layer 1 - Soft Shadowed) */}
            <path
              d="M 105 52 C 70 8, 30 25, 48 55 C 32 20, 85 -5, 105 52 Z"
              fill="#CBD5E1"
              opacity="0.75"
            />
            <path
              d="M 108 52 C 145 8, 185 25, 162 55 C 178 20, 125 -5, 108 52 Z"
              fill="#CBD5E1"
              opacity="0.75"
            />

            {/* Main Center-Left Arching Feather (Layer 2 - Detailed Vanes) */}
            <path
              d="M 106 50 C 72 15, 38 35, 58 65 C 40 30, 88 4, 106 50 Z"
              fill="url(#realFeatherLight)"
            />
            {/* Center Feather Spine / Quill */}
            <path d="M 106 50 Q 82 25 58 65" stroke="#E2E8F0" strokeWidth="1" fill="none" />

            {/* Main Center-Right Arching Feather */}
            <path
              d="M 107 50 C 142 15, 172 35, 152 65 C 170 30, 122 4, 107 50 Z"
              fill="url(#realFeatherLight)"
            />
            <path d="M 107 50 Q 132 25 152 65" stroke="#E2E8F0" strokeWidth="1" fill="none" />

            {/* Upright Center Plumes (Lush Soft Tuft) */}
            <path
              d="M 106 48 C 96 12, 116 12, 107 48 Z"
              fill="#FFFFFF"
            />
            <path
              d="M 104 49 C 88 28, 98 25, 105 49 Z"
              fill="url(#realFeatherLight)"
              opacity="0.9"
            />
            <path
              d="M 108 49 C 124 28, 114 25, 107 49 Z"
              fill="url(#realFeatherLight)"
              opacity="0.9"
            />

            {/* Drooping Fluffy Down Feathers at Base */}
            <path d="M 98 52 Q 82 42 88 58 Q 94 48 98 52" fill="#FFFFFF" />
            <path d="M 114 52 Q 130 42 124 58 Q 118 48 114 52" fill="#FFFFFF" />

            {/* Authentic Wrapped Crimson Silk Knot & Dangling Tassels (লাল রেশমী ফিতা) */}
            <ellipse cx="106" cy="56" rx="9" ry="5" fill="#B91C1C" stroke="#F87171" strokeWidth="1" />
            <path d="M 102 59 Q 92 78 96 92 M 110 59 Q 120 78 116 92" stroke="#DC2626" strokeWidth="3" strokeLinecap="round" />
            <circle cx="96" cy="92" r="2.5" fill="#F87171" />
            <circle cx="116" cy="92" r="2.5" fill="#F87171" />
          </g>

          {/* ========================================================================= */}
          {/* 2. REALISTIC SLANTED DHAAK DRUM BODY (কাঠ ও চামড়ার ত্রিমাত্রিক ঢাক)       */}
          {/* ========================================================================= */}
          <g className={isPlaying ? 'animate-dhaak-body-vibe' : ''} filter="url(#realDhaakShadow)">
            {/* Solid Turned Timber Barrel Body */}
            <path
              d="M 52 72 Q 95 56 142 78 Q 155 118 136 158 Q 88 170 42 144 Q 30 108 52 72 Z"
              fill="url(#realWoodCylinder)"
              stroke="#78350F"
              strokeWidth="2"
            />

            {/* Specular Curvature Highlight on Wood */}
            <path
              d="M 54 74 Q 95 58 140 80 Q 146 95 142 110 Q 95 90 48 105 Q 44 88 54 74 Z"
              fill="url(#woodSpecular)"
              opacity="0.7"
            />

            {/* Rear/Left Base Drum Head Rim (বাঁ দিকের বেস চামড়া) */}
            <ellipse cx="46" cy="108" rx="14" ry="36" fill="#3E1A07" stroke="#78350F" strokeWidth="2.5" transform="rotate(-18 46 108)" />
            <ellipse cx="46" cy="108" rx="10" ry="30" fill="#240E04" transform="rotate(-18 46 108)" />

            {/* Front/Right Primary Striking Membrane with Leather Hoop Rim (পুরী ও চামড়ার বেড়) */}
            {/* Outer Stitched Leather Hoop Rim */}
            <ellipse cx="140" cy="118" rx="19" ry="40" fill="#78350F" stroke="#B45309" strokeWidth="3" transform="rotate(-18 140 118)" />
            {/* Natural Calfskin Striking Surface */}
            <ellipse cx="140" cy="118" rx="15" ry="34" fill="url(#realLeatherSkin)" stroke="#FEF3C7" strokeWidth="1.5" transform="rotate(-18 140 118)" />
            {/* Inner Resonant Skin Tone Patch */}
            <ellipse cx="140" cy="118" rx="9" ry="24" fill="#92400E" opacity="0.65" transform="rotate(-18 140 118)" />

            {/* Woven Hemp Cord Tension Netting (দড়ির জালিকৃতি) */}
            <g stroke="#FEF3C7" strokeWidth="2" strokeLinecap="round" opacity="0.9">
              <path d="M 52 78 L 94 158 M 94 65 L 134 150 M 52 142 L 94 65 M 94 158 L 134 85" />
              <path d="M 58 92 L 115 142 M 58 128 L 115 78" strokeWidth="1.5" opacity="0.75" />
            </g>

            {/* Brass Tuning Rings Hugging Cord Contours (পিতলের টানা বালা) */}
            <ellipse cx="80" cy="112" rx="7" ry="14" fill="url(#realBrass)" stroke="#451A03" strokeWidth="1" transform="rotate(-18 80 112)" />
            <ellipse cx="110" cy="118" rx="7" ry="14" fill="url(#realBrass)" stroke="#451A03" strokeWidth="1" transform="rotate(-18 110 118)" />
          </g>

          {/* ========================================================================= */}
          {/* 3. CONTACT IMPACT SPARKS WHEN PLAYING                                     */}
          {/* ========================================================================= */}
          {isPlaying && (
            <>
              {/* Right Drumhead Contact Burst */}
              <g className="animate-impact-right">
                <circle cx="138" cy="108" r="10" fill="#FEF08A" opacity="0.9" />
                <path d="M 138 90 L 138 126 M 120 108 L 156 108 M 125 95 L 151 121 M 125 121 L 151 95" stroke="#F59E0B" strokeWidth="2.5" strokeLinecap="round" />
              </g>

              {/* Left Counter-Rhythm Strike Burst */}
              <g className="animate-impact-left">
                <circle cx="54" cy="102" r="8" fill="#FEF08A" opacity="0.85" />
                <path d="M 54 88 L 54 116 M 40 102 L 68 102" stroke="#F59E0B" strokeWidth="2" strokeLinecap="round" />
              </g>
            </>
          )}

          {/* ========================================================================= */}
          {/* 4. REALISTIC SLENDER CANE KATHI DRUMSTICKS (ডান ও বাঁ হাতের বেতের কাঠি)    */}
          {/* ========================================================================= */}
          {/* Primary Right Cane Stick (ডান হাতের বেতের কাঠি - Striking Directly on Drumhead) */}
          <g className={isPlaying ? 'animate-kathi-right-strike' : 'group-hover:-rotate-8 transition-transform duration-200'}>
            {/* Slender Flexible Bamboo Cane Shaft */}
            <path
              d="M 178 32 Q 160 70 138 106"
              stroke="#FEF08A"
              strokeWidth="4"
              strokeLinecap="round"
              fill="none"
            />
            <path
              d="M 178 32 Q 160 70 138 106"
              stroke="#B45309"
              strokeWidth="1.5"
              strokeLinecap="round"
              fill="none"
              opacity="0.6"
            />
            {/* Bamboo Joint / Node Notches */}
            <circle cx="166" cy="54" r="2.5" fill="#78350F" />
            <circle cx="152" cy="80" r="2.5" fill="#78350F" />
            {/* Crimson Grip Handle */}
            <circle cx="178" cy="32" r="5.5" fill="#EF4444" stroke="#FFFFFF" strokeWidth="2" />
          </g>

          {/* Secondary Left Cane Stick (বাঁ হাতের বেতের কাঠি - Accent Rhythm on Rear Rim) */}
          <g className={isPlaying ? 'animate-kathi-left-strike' : 'group-hover:rotate-8 transition-transform duration-200'}>
            {/* Slender Flexible Bamboo Cane Shaft */}
            <path
              d="M 22 42 Q 38 72 52 104"
              stroke="#FEF08A"
              strokeWidth="4"
              strokeLinecap="round"
              fill="none"
            />
            <path
              d="M 22 42 Q 38 72 52 104"
              stroke="#B45309"
              strokeWidth="1.5"
              strokeLinecap="round"
              fill="none"
              opacity="0.6"
            />
            {/* Bamboo Joint Nodes */}
            <circle cx="32" cy="62" r="2.5" fill="#78350F" />
            <circle cx="44" cy="86" r="2.5" fill="#78350F" />
            {/* Crimson Grip Handle */}
            <circle cx="22" cy="42" r="5.5" fill="#EF4444" stroke="#FFFFFF" strokeWidth="2" />
          </g>
        </svg>

        {/* Ambient Music Playing Badge in Corner */}
        <div className={`absolute -bottom-1 -right-1 w-6 h-6 rounded-full flex items-center justify-center text-[10px] font-bold shadow-md transition-all ${
          isPlaying
            ? 'bg-amber-400 text-slate-950 scale-110 shadow-[0_0_12px_#F59E0B]'
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
    f.write(realistic_dhaak_code)

print("Written ultra-realistic DhaakButton component successfully!")
