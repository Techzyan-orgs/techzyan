'use client';

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
                  </div>

                  <div className="pt-4 border-t border-slate-800 flex items-center justify-between gap-2">
                    <button
                      onClick={() => setSelectedDemonstration(project)}
                      className="text-xs font-semibold text-slate-300 hover:text-white flex items-center gap-1.5"
                    >
                      <Eye className="w-3.5 h-3.5" />
                      <span>Inspect Details</span>
                    </button>

                    <a
                      href={project.demoUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-brand-cyan text-xs font-bold transition-colors border border-sky-500/30"
                    >
                      <span>Visit Website</span>
                      <ExternalLink className="w-3.5 h-3.5" />
                    </a>
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
