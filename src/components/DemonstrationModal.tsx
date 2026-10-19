'use client';

import React, { useEffect } from 'react';
import Image from 'next/image';
import { X, CheckCircle, Sparkles, ExternalLink, ArrowRight, Layers, Smartphone } from 'lucide-react';
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
              <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-mono uppercase tracking-wider font-semibold ${
                project.badge === 'Live Application'
                  ? 'bg-emerald-500/15 text-emerald-400 border border-emerald-500/30'
                  : 'bg-sky-500/10 text-brand-cyan border border-sky-500/30'
              }`}>
                {project.badge}
              </span>
              <span className="text-xs text-slate-400 font-mono">
                {project.category}
              </span>
            </div>
            <h2 id="case-study-title" className="text-xl sm:text-2xl font-display font-bold text-slate-100">
              {project.hasLiveSite ? (
                <a
                  href={project.demoUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="hover:text-brand-cyan transition-colors"
                >
                  {project.title}
                </a>
              ) : (
                <span>{project.title}</span>
              )}
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
              {project.hasLiveSite ? (
                <a
                  href={project.demoUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1.5 px-3.5 py-1.5 bg-brand-cyan hover:bg-sky-300 text-slate-950 text-xs font-bold uppercase tracking-wider rounded-xl shadow-glow-cyan transition-all"
                >
                  <span>Visit Website</span>
                  <ExternalLink className="w-3.5 h-3.5" />
                </a>
              ) : (
                <div className="inline-flex items-center gap-1.5 px-3.5 py-1.5 bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-xs font-mono font-semibold rounded-xl backdrop-blur-sm shadow-sm">
                  <Smartphone className="w-3.5 h-3.5 text-emerald-400" />
                  <span>Native Android App</span>
                </div>
              )}
            </div>
          </div>

          {/* Metrics Bar */}
          {project.mockData?.metrics && (
            <div className="grid grid-cols-3 gap-3 p-3.5 rounded-2xl bg-slate-950/70 border border-slate-800">
              {project.mockData.metrics.map((metric, i) => (
                <div key={i} className="text-center">
                  <div className="text-xs sm:text-sm font-bold text-slate-100 font-mono">
                    {metric.value}
                  </div>
                  <div className="text-[10px] text-slate-400 uppercase tracking-wider font-mono">
                    {metric.label}
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* Verified Client Impact Callout for SMS Buddy */}
          {project.id === 'sms-buddy' && (
            <div className="p-4 sm:p-5 rounded-2xl bg-amber-500/10 border border-amber-500/30 flex items-start gap-3.5">
              <div className="p-2 rounded-xl bg-amber-500/20 text-amber-300 shrink-0 mt-0.5">
                <Sparkles className="w-4 h-4" />
              </div>
              <div className="space-y-1">
                <div className="text-xs font-mono uppercase tracking-wider text-amber-300 font-semibold">
                  Verified Client Impact & Appreciation
                </div>
                <p className="text-xs text-slate-300 leading-relaxed">
                  Endorsed by <strong className="text-amber-200">Amartya Saha</strong> (Secretary, Swaranika Abasan Puja Committee): 
                  <em> &ldquo;The application developed with your assistance enabled us to send subscription receipt copies to all residents via SMS. This initiative helped us streamline the collection process, save considerable costs, and analyse collection data more efficiently.&rdquo;</em>
                </p>
              </div>
            </div>
          )}

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
