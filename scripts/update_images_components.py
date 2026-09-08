import os

def write_file(rel_path, content):
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {rel_path}")

demo_modal_code = """'use client';

import React, { useEffect } from 'react';
import Image from 'next/image';
import { X, CheckCircle, Sparkles, ExternalLink, ArrowRight, Layers } from 'lucide-react';
import { DemonstrationProject } from '@/types';

interface DemonstrationModalProps {
  project: DemonstrationProject | null;
  onClose: () => void;
  onOpenConsultation?: () => void;
}

export default function DemonstrationModal({ project, onClose, onOpenConsultation }: DemonstrationModalProps) {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (project) {
      document.body.style.overflow = 'hidden';
      window.addEventListener('keydown', handleKeyDown);
    } else {
      document.body.style.overflow = 'unset';
    }
    return () => {
      document.body.style.overflow = 'unset';
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [project, onClose]);

  if (!project) return null;

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/85 backdrop-blur-md animate-in fade-in duration-200"
      role="dialog"
      aria-modal="true"
      aria-labelledby="case-study-title"
    >
      <div className="relative w-full max-w-3xl bg-slate-900 border border-slate-700/80 rounded-3xl shadow-2xl overflow-hidden text-slate-200 max-h-[92vh] flex flex-col">
        {/* Top Header */}
        <div className="p-6 border-b border-slate-800 flex items-start justify-between bg-slate-950/80">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-2">
              <span className="px-2.5 py-0.5 rounded-full text-[10px] font-mono uppercase tracking-wider bg-sky-500/10 text-brand-cyan border border-sky-500/30 font-semibold">
                {project.badge}
              </span>
              <span className="text-xs text-slate-400 font-mono">
                {project.category}
              </span>
            </div>
            <h2 id="case-study-title" className="text-xl sm:text-2xl font-display font-bold text-slate-100">
              {project.title}
            </h2>
          </div>
          <button
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-slate-100 hover:bg-slate-800 rounded-lg transition-colors shrink-0 ml-4"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Scrollable Content */}
        <div className="p-6 sm:p-8 overflow-y-auto space-y-6">
          {/* Visual Preview Image */}
          <div className="relative w-full h-48 sm:h-60 rounded-2xl overflow-hidden border border-slate-800 bg-slate-950 shadow-inner">
            <Image
              src={project.thumbnailImage}
              alt={project.title}
              fill
              className="object-cover"
              sizes="(max-width: 768px) 100vw, 750px"
              priority
            />
            <div className="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/40 to-transparent" />
            <div className="absolute bottom-3 left-4 right-4 flex items-center justify-between">
              <span className="text-xs font-mono uppercase tracking-wider text-slate-300 font-semibold">
                {project.shortTitle}
              </span>
              <a
                href={project.demoUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1.5 px-3.5 py-1.5 bg-brand-cyan hover:bg-sky-300 text-slate-950 text-xs font-bold uppercase tracking-wider rounded-xl shadow-glow-cyan transition-all"
              >
                <span>Live Demo</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>

          {/* Problem vs Solution Summary */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="p-5 rounded-2xl bg-slate-950/60 border border-slate-800 space-y-2">
              <div className="text-xs font-mono uppercase tracking-wider text-rose-400 font-semibold">
                The Real Operational Challenge
              </div>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                {project.problemSolved}
              </p>
            </div>

            <div className="p-5 rounded-2xl bg-slate-950/60 border border-slate-800 space-y-2">
              <div className="text-xs font-mono uppercase tracking-wider text-emerald-400 font-semibold">
                What We Engineered
              </div>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                {project.engineeredSolution}
              </p>
            </div>
          </div>

          {/* Key Deliverables & Capabilities */}
          <div className="space-y-3">
            <h3 className="text-xs font-mono uppercase tracking-wider text-slate-300 font-semibold flex items-center gap-2">
              <Layers className="w-4 h-4 text-brand-cyan" />
              <span>Key Features Built Into This Solution</span>
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {project.keyFeatures.map((feature, i) => (
                <div key={i} className="flex items-start gap-2.5 text-xs text-slate-200 p-3 rounded-xl bg-slate-950/40 border border-slate-800">
                  <CheckCircle className="w-4 h-4 text-brand-cyan shrink-0 mt-0.5" />
                  <span>{feature}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Target Performance & Business Impact */}
          <div className="grid grid-cols-3 gap-3 pt-2">
            {project.mockData.metrics.map((metric, i) => (
              <div key={i} className="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800 text-center">
                <div className="text-sm sm:text-base font-bold text-brand-cyan font-mono">{metric.value}</div>
                <div className="text-[11px] text-slate-400 mt-0.5">{metric.label}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Footer Actions */}
        <div className="p-6 border-t border-slate-800 bg-slate-950 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p className="text-xs text-slate-400 text-center sm:text-left">
            Need a similar custom solution for your practice or business?
          </p>
          <div className="flex items-center gap-3 w-full sm:w-auto">
            <button
              onClick={onClose}
              className="w-1/2 sm:w-auto px-4 py-2.5 text-xs text-slate-400 hover:text-slate-200 border border-slate-800 hover:border-slate-700 rounded-xl transition-colors"
            >
              Close
            </button>
            <button
              onClick={() => {
                onClose();
                onOpenConsultation?.();
              }}
              className="w-1/2 sm:w-auto px-5 py-2.5 text-xs font-semibold uppercase tracking-wider text-slate-950 bg-brand-cyan hover:bg-sky-300 rounded-xl shadow-glow-cyan transition-all"
            >
              Discuss Your Project
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

write_file('src/components/DemonstrationModal.tsx', demo_modal_code)
work_page_code = """'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import DemonstrationModal from '@/components/DemonstrationModal';
import ConsultationModal from '@/components/ConsultationModal';
import { demonstrationProjects } from '@/data/demonstrations';
import { DemonstrationProject } from '@/types';
import {
  Sparkles,
  ShieldCheck,
  CheckCircle2,
  ExternalLink,
  Layers,
  ArrowRight,
  Eye,
} from 'lucide-react';

export default function WorkPage() {
  const [selectedDemonstration, setSelectedDemonstration] = useState<DemonstrationProject | null>(null);
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);
  const [activeFilter, setActiveFilter] = useState<string>('all');

  const filteredProjects = activeFilter === 'all'
    ? demonstrationProjects
    : demonstrationProjects.filter(p => p.category.toLowerCase().includes(activeFilter.toLowerCase()) || p.clientType.toLowerCase().includes(activeFilter.toLowerCase()));

  return (
    <>
      <Header onOpenConsultation={() => setIsConsultationOpen(true)} />

      <main id="main-content" className="flex-1 pt-32 pb-24">
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-12">
          <div className="max-w-3xl space-y-4">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Demonstration Showcase</span>
            </div>
            <h1 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight leading-tight">
              Demonstration Concepts & <br />
              <span className="text-gradient-cyan">Live Prototypes</span>
            </h1>
            <p className="text-slate-300 text-base sm:text-lg leading-relaxed">
              We don't invent fake client logos or made-up 5-star reviews. Explore these fully functional, realistic demonstration concepts designed for clinics, educators, boutiques, and festival organizers.
            </p>
          </div>

          <div className="flex flex-wrap gap-2 pt-6 mt-6 border-t border-slate-800/80">
            {[
              { id: 'all', label: 'All Demonstration Projects' },
              { id: 'healthcare', label: 'Healthcare & Clinic' },
              { id: 'education', label: 'Tutors & Academies' },
              { id: 'retail', label: 'Boutiques & Shops' },
              { id: 'cultural', label: 'Durga Puja & Cultural' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveFilter(tab.id)}
                className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-medium transition-all ${
                  activeFilter === tab.id
                    ? 'bg-slate-800 text-slate-100 border border-brand-cyan shadow-glow-cyan'
                    : 'bg-slate-900/60 text-slate-400 border border-slate-800 hover:text-slate-200'
                }`}
              >
                {tab.label}
              </button>
            ))}
          </div>
        </section>

        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredProjects.map((project) => (
              <div
                key={project.id}
                className="glass-card rounded-3xl overflow-hidden border border-slate-800 hover:border-brand-cyan/40 transition-all flex flex-col justify-between group"
              >
                {/* Thumbnail Image */}
                <div className="relative w-full h-44 bg-slate-950 overflow-hidden border-b border-slate-800/80">
                  <Image
                    src={project.thumbnailImage}
                    alt={project.title}
                    fill
                    className="object-cover group-hover:scale-105 transition-transform duration-500"
                    sizes="(max-width: 768px) 100vw, 400px"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/20 to-transparent" />
                  <div className="absolute top-3 left-3 right-3 flex items-center justify-between">
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] font-mono uppercase tracking-wider bg-slate-900/90 text-slate-200 border border-slate-700/80 backdrop-blur-sm">
                      {project.clientType}
                    </span>
                    <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-sky-500/20 text-brand-cyan border border-sky-500/40 backdrop-blur-sm font-semibold">
                      {project.badge}
                    </span>
                  </div>
                </div>

                <div className="p-6 sm:p-7 space-y-4 flex-1 flex flex-col justify-between">
                  <div className="space-y-3">
                    <h2 className="text-lg font-bold text-slate-100 group-hover:text-brand-cyan transition-colors">
                      {project.title}
                    </h2>
                    <p className="text-xs text-slate-400 leading-relaxed">
                      {project.summary}
                    </p>

                    <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800 space-y-1">
                      <div className="text-[10px] font-mono uppercase text-slate-500 font-semibold">Problem Solved:</div>
                      <div className="text-xs text-slate-300 line-clamp-2">
                        {project.problemSolved}
                      </div>
                    </div>
                  </div>

                  <div className="pt-4 border-t border-slate-800 flex items-center justify-between gap-2">
                    <button
                      onClick={() => setSelectedDemonstration(project)}
                      className="text-xs font-semibold text-slate-300 hover:text-white flex items-center gap-1.5"
                    >
                      <Eye className="w-3.5 h-3.5" />
                      <span>Inspect Details</span>
                    </button>

                    <button
                      onClick={() => setSelectedDemonstration(project)}
                      className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-brand-cyan text-xs font-bold transition-colors border border-sky-500/30"
                    >
                      <span>Live Demo</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-20">
          <div className="p-8 sm:p-10 rounded-3xl bg-slate-950 border border-slate-800 text-center max-w-3xl mx-auto space-y-4">
            <h3 className="text-2xl font-bold text-slate-100">
              Want a solution designed with this level of craft?
            </h3>
            <p className="text-slate-400 text-xs sm:text-sm leading-relaxed">
              Every project we take on receives this same rigor in user experience, mobile performance, and visual polish.
            </p>
            <div className="pt-2">
              <button
                onClick={() => setIsConsultationOpen(true)}
                className="inline-flex items-center gap-2 px-6 py-3 bg-brand-cyan hover:bg-sky-300 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-cyan transition-all"
              >
                <span>Start a Project Discussion</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </section>
      </main>

      <Footer />

      <DemonstrationModal
        project={selectedDemonstration}
        onClose={() => setSelectedDemonstration(null)}
        onOpenConsultation={() => setIsConsultationOpen(true)}
      />

      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
      />
    </>
  );
}
"""

write_file('src/app/work/page.tsx', work_page_code)
