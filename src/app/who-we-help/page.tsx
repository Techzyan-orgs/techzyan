'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
import { audienceData } from '@/data/audiences';
import { siteConfig } from '@/config/site';
import {
  Stethoscope,
  GraduationCap,
  Briefcase,
  Building,
  Flame,
  ArrowRight,
  CheckCircle2,
  AlertCircle,
  Sparkles,
  Layers,
  ShieldCheck,
} from 'lucide-react';

export default function WhoWeHelpPage() {
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);
  const [consultationCategory, setConsultationCategory] = useState<string | undefined>();

  const getIcon = (name: string) => {
    switch (name) {
      case 'Stethoscope': return <Stethoscope className="w-6 h-6 text-sky-400" />;
      case 'GraduationCap': return <GraduationCap className="w-6 h-6 text-indigo-400" />;
      case 'Briefcase': return <Briefcase className="w-6 h-6 text-emerald-400" />;
      case 'Building': return <Building className="w-6 h-6 text-purple-400" />;
      case 'Flame': return <Flame className="w-6 h-6 text-amber-400" />;
      default: return <Sparkles className="w-6 h-6 text-brand-cyan" />;
    }
  };

  const handleOpenConsultation = (category?: string) => {
    setConsultationCategory(category);
    setIsConsultationOpen(true);
  };

  return (
    <>
      <Header onOpenConsultation={() => handleOpenConsultation()} />

      <main id="main-content" className="flex-1 pt-32 pb-24">
        {/* Page Header */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono mb-4">
              <Layers className="w-3.5 h-3.5" />
              <span>Tailored Problem-Solution Architecture</span>
            </div>
            <h1 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight leading-tight">
              Designed for how your <br />
              <span className="text-gradient-cyan">practice or business actually works.</span>
            </h1>
            <p className="mt-4 text-slate-300 text-base sm:text-lg leading-relaxed">
              We do not build generic one-size-fits-all websites. We deeply understand the real operational bottlenecks of doctors, tutors, boutique shops, institutes, and festival organizers.
            </p>
          </div>
        </section>

        {/* Audience Sections */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
          {audienceData.map((aud, index) => (
            <div
              key={aud.id}
              id={aud.id}
              className={`rounded-3xl p-6 sm:p-10 lg:p-12 border ${
                aud.id === 'durga-puja-committees'
                  ? 'puja-card border-amber-500/30'
                  : 'glass-card border-slate-800'
              }`}
            >
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
                {/* Left Column: Context & Problems */}
                <div className="lg:col-span-5 space-y-5">
                  <div className="flex items-center gap-3">
                    <div className="p-3 rounded-2xl bg-slate-900 border border-slate-800">
                      {getIcon(aud.iconName)}
                    </div>
                    <div>
                      <span className="text-xs font-mono uppercase tracking-wider text-slate-400">
                        Target Archetype #{index + 1}
                      </span>
                      <h2 className="text-2xl sm:text-3xl font-bold text-slate-100 mt-0.5">
                        {aud.title}
                      </h2>
                    </div>
                  </div>

                  <p className="text-xs font-mono text-brand-cyan">
                    {aud.roleSubtitle}
                  </p>

                  <p className="text-sm text-slate-300 leading-relaxed">
                    {aud.context}
                  </p>

                  {/* Common Friction */}
                  <div className="p-4 rounded-xl bg-rose-950/20 border border-rose-900/30 space-y-2">
                    <div className="text-xs font-mono uppercase text-rose-400 font-semibold flex items-center gap-1.5">
                      <AlertCircle className="w-3.5 h-3.5 shrink-0" />
                      <span>Common Operational Friction:</span>
                    </div>
                    <ul className="space-y-1.5 text-xs text-slate-300">
                      {aud.commonFriction.map((fric, i) => (
                        <li key={i} className="flex items-start gap-2">
                          <span className="text-rose-400 mt-0.5">•</span>
                          <span>{fric}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                {/* Right Column: Techzyan Engineered Solution */}
                <div className="lg:col-span-7 space-y-6 bg-slate-950/60 p-6 sm:p-8 rounded-2xl border border-slate-800/80">
                  <div>
                    <span className="text-xs font-mono uppercase tracking-wider text-emerald-400 font-semibold">
                      Techzyan Approach & Architecture
                    </span>
                    <p className="text-sm text-slate-200 mt-2 leading-relaxed font-medium">
                      {aud.techzyanApproach}
                    </p>
                  </div>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5">
                      <span className="text-[10px] font-mono uppercase text-brand-cyan block">1. The Entry Website</span>
                      <p className="text-xs text-slate-300">{aud.entrySolution}</p>
                    </div>

                    <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5">
                      <span className="text-[10px] font-mono uppercase text-emerald-400 block">2. Right-Sized Custom Tool</span>
                      <p className="text-xs text-slate-300">{aud.expansionSolution}</p>
                    </div>
                  </div>

                  {/* Key Outcomes */}
                  <div className="space-y-2 pt-2 border-t border-slate-800">
                    <div className="text-xs font-mono uppercase text-slate-400">Measurable Outcomes:</div>
                    <div className="space-y-2">
                      {aud.keyOutcomes.map((outcome, i) => (
                        <div key={i} className="flex items-start gap-2 text-xs text-slate-200">
                          <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0 mt-0.5" />
                          <span>{outcome}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* CTA Button */}
                  <div className="pt-4 flex flex-wrap gap-3">
                    <button
                      onClick={() => handleOpenConsultation(aud.title)}
                      className="px-5 py-2.5 bg-brand-cyan hover:bg-sky-300 text-slate-950 font-semibold text-xs uppercase tracking-wider rounded-lg shadow-glow-cyan transition-all"
                    >
                      Discuss {aud.title} Scope
                    </button>
                    {aud.id === 'durga-puja-committees' && (
                      <Link
                        href="/solutions/durga-puja"
                        className="px-5 py-2.5 bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-semibold uppercase tracking-wider rounded-lg transition-colors"
                      >
                        Explore Dedicated Puja Page
                      </Link>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </section>
      </main>

      <Footer />

      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
        initialCategory={consultationCategory}
      />
    </>
  );
}
