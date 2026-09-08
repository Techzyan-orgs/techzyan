'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
import PujaConsultationModal from '@/components/PujaConsultationModal';
import { solutionsData } from '@/data/solutions';
import { siteConfig } from '@/config/site';
import {
  Globe,
  Stethoscope,
  GraduationCap,
  CalendarCheck,
  Users,
  Flame,
  Cpu,
  Zap,
  ArrowRight,
  CheckCircle2,
  Sparkles,
  Layers,
} from 'lucide-react';

export default function SolutionsPage() {
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);
  const [isPujaModalOpen, setIsPujaModalOpen] = useState(false);
  const [activeSolutionScope, setActiveSolutionScope] = useState<string | undefined>();

  const filteredSolutions = selectedCategory === 'all'
    ? solutionsData
    : solutionsData.filter(item => item.category === selectedCategory);

  const getIcon = (iconName: string) => {
    switch (iconName) {
      case 'Globe': return <Globe className="w-6 h-6 text-brand-cyan" />;
      case 'Stethoscope': return <Stethoscope className="w-6 h-6 text-brand-cyan" />;
      case 'GraduationCap': return <GraduationCap className="w-6 h-6 text-brand-cyan" />;
      case 'CalendarCheck': return <CalendarCheck className="w-6 h-6 text-emerald-400" />;
      case 'Users': return <Users className="w-6 h-6 text-emerald-400" />;
      case 'Flame': return <Flame className="w-6 h-6 text-amber-400" />;
      case 'Cpu': return <Cpu className="w-6 h-6 text-indigo-400" />;
      case 'Zap': return <Zap className="w-6 h-6 text-amber-300" />;
      default: return <Sparkles className="w-6 h-6 text-brand-cyan" />;
    }
  };

  const handleStartInquiry = (category: string, title: string) => {
    if (category === 'puja-special' || title.toLowerCase().includes('puja')) {
      setIsPujaModalOpen(true);
    } else {
      setActiveSolutionScope(title);
      setIsConsultationOpen(true);
    }
  };

  return (
    <>
      <Header onOpenConsultation={() => setIsConsultationOpen(true)} />

      <main id="main-content" className="flex-1 pt-32 pb-24">
        {/* Header Hero */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-12">
          <div className="max-w-3xl space-y-4">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono">
              <Layers className="w-3.5 h-3.5" />
              <span>Full Studio Directory</span>
            </div>
            <h1 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight leading-tight">
              Comprehensive Services & <br />
              <span className="text-gradient-cyan">Digital Solutions</span>
            </h1>
            <p className="text-slate-300 text-base sm:text-lg leading-relaxed">
              We engineer high-speed websites, purpose-built operational tools, and specialized festival platforms. Filter by requirement below.
            </p>
          </div>

          {/* Interactive Category Tabs */}
          <div className="flex flex-wrap gap-2 pt-6 mt-6 border-t border-slate-800/80">
            {[
              { id: 'all', label: 'All Services (8)' },
              { id: 'website', label: 'High-Performance Websites' },
              { id: 'custom-tool', label: 'Right-Sized Custom Tools' },
              { id: 'puja-special', label: 'Durga Puja Specialization' },
              { id: 'growth', label: 'Speed & Modernization' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setSelectedCategory(tab.id)}
                className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-medium transition-all ${
                  selectedCategory === tab.id
                    ? tab.id === 'puja-special'
                      ? 'bg-amber-500 text-slate-950 font-bold shadow-glow-gold'
                      : 'bg-slate-800 text-slate-100 border border-brand-cyan shadow-glow-cyan'
                    : 'bg-slate-900/60 text-slate-400 border border-slate-800 hover:text-slate-200'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </section>

        {/* Solutions Grid */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8">
            {filteredSolutions.map((sol) => (
              <div
                key={sol.id}
                id={sol.id}
                className={`rounded-3xl p-6 sm:p-8 border transition-all duration-300 flex flex-col justify-between space-y-6 ${
                  sol.category === 'puja-special'
                    ? 'puja-card border-amber-500/30 hover:border-amber-400/60'
                    : 'glass-card border-slate-800 hover:border-brand-cyan/40'
                }`}
              >
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <div className="p-3 rounded-2xl bg-slate-900/80 border border-slate-800">
                      {getIcon(sol.iconName)}
                    </div>
                    <div className="flex items-center gap-2">
                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-mono uppercase tracking-wider bg-slate-900 text-slate-400 border border-slate-800">
                        {sol.timeline}
                      </span>
                    </div>
                  </div>

                  <div>
                    <h2 className="text-xl sm:text-2xl font-bold text-slate-100">
                      {sol.title}
                    </h2>
                    <p className="text-xs sm:text-sm font-medium text-brand-cyan mt-1">
                      {sol.subtitle}
                    </p>
                    <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                      {sol.description}
                    </p>
                  </div>

                  {/* Key Capabilities */}
                  <div className="space-y-2 pt-2">
                    <div className="text-[11px] font-mono uppercase tracking-wider text-slate-400 font-semibold">
                      What We Deliver:
                    </div>
                    <div className="space-y-1.5">
                      {sol.keyFeatures.map((feat, i) => (
                        <div key={i} className="flex items-start gap-2 text-xs text-slate-300">
                          <CheckCircle2 className={`w-3.5 h-3.5 shrink-0 mt-0.5 ${sol.category === 'puja-special' ? 'text-amber-400' : 'text-brand-cyan'}`} />
                          <span>{feat}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                {/* Card Action */}
                <div className="pt-4 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-3">
                  <span className="text-[11px] font-mono text-slate-400">
                    {sol.pricingType === 'fixed-project' ? 'Fixed Project Scope' : 'Requirement-Based Quote'}
                  </span>
                  <button
                    onClick={() => handleStartInquiry(sol.category, sol.title)}
                    className={`w-full sm:w-auto px-5 py-2.5 text-xs font-bold uppercase tracking-wider rounded-xl transition-all flex items-center justify-center gap-1.5 ${
                      sol.category === 'puja-special'
                        ? 'bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-glow-gold'
                        : 'bg-brand-cyan hover:bg-sky-300 text-slate-950 shadow-glow-cyan'
                    }`}
                  >
                    <span>Discuss Scope</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>

      <Footer />

      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
        initialCategory={activeSolutionScope}
      />

      <PujaConsultationModal
        isOpen={isPujaModalOpen}
        onClose={() => setIsPujaModalOpen(false)}
      />
    </>
  );
}
