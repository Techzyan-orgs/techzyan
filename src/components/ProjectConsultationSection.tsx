'use client';

import React, { useState } from 'react';
import { Sparkles, ArrowRight, CheckCircle2, ShieldCheck, Clock, Layers } from 'lucide-react';
import { siteConfig } from '@/config/site';
import WhatsAppIcon from '@/components/WhatsAppIcon';

export default function ProjectConsultationSection({ onOpenConsultation }: { onOpenConsultation: (category?: string) => void }) {
  const [selectedRole, setSelectedRole] = useState<'doctor' | 'tutor' | 'business' | 'institute' | 'puja'>('doctor');

  const roleSpecs = {
    doctor: {
      label: 'Doctor / Clinic',
      title: 'Healthcare Practice & Smart Appointment Platform',
      tagline: 'Quiet authority, patient-friendly chamber schedules, and symptom-triage booking.',
      entryDeliverable: 'Custom clinic website with OPD timings, map directions, and doctor credentials.',
      customTech: '3-step symptom triage + WhatsApp appointment confirmation webhook.',
      timeline: '10 – 14 business days',
      investment: 'Transparent fixed project quote',
      category: 'Doctor & Healthcare',
    },
    tutor: {
      label: 'Private Tutor / Mentor',
      title: 'Academic Profile & Student Admission Hub',
      tagline: 'Organized course roadmaps, past student achievements, and live batch vacancy tracker.',
      entryDeliverable: 'Crisp curriculum showcase with syllabus downloads & batch vacancy cards.',
      customTech: 'Parent inquiry generator with auto-filled subject tags directly to your WhatsApp.',
      timeline: '8 – 12 business days',
      investment: 'Transparent fixed project quote',
      category: 'Private Tutor & Educator',
    },
    business: {
      label: 'Growing Business',
      title: 'High-Converting Brand Website & Order Pipeline',
      tagline: 'Distinctive visual craft, sub-second mobile speed, and structured quotation requests.',
      entryDeliverable: 'Custom lookbook / service showcase with modern responsive layout.',
      customTech: 'Bespoke price estimation tool or custom measurement consultation guide.',
      timeline: '12 – 18 business days',
      investment: 'Transparent fixed project quote',
      category: 'Growing Business',
    },
    institute: {
      label: 'Educational Institute',
      title: 'Multi-Department Academic Portal & Admissions System',
      tagline: 'Intuitive department explorer, prospectus delivery, and structured inquiry triage.',
      entryDeliverable: 'Institutional website with course directory and faculty profiles.',
      customTech: 'Student management dashboard & digital admissions inquiry pipeline.',
      timeline: '18 – 25 business days',
      investment: 'Scope-based architecture quote',
      category: 'Educational Institute',
    },
    puja: {
      label: 'Durga Puja Committee',
      title: 'Durga Puja Digital Hub & Corporate Sponsorship Suite',
      tagline: 'Sharodotsav schedule, theme art gallery, crowd guides, and brand sponsor proposals.',
      entryDeliverable: '5-Day interactive Puja calendar, theme art story, and visitor metro map.',
      customTech: 'Sponsor tier proposal builder with direct corporate brand inquiry flow.',
      timeline: '10 – 16 business days',
      investment: 'Transparent fixed project quote',
      category: 'Durga Puja Committee',
    },
  };

  const current = roleSpecs[selectedRole];

  return (
    <section className="py-20 lg:py-28 relative overflow-hidden bg-slate-950/80 border-t border-b border-slate-800/80">
      {/* Background Subtle Accents */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-full pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-sky-500/5 rounded-full blur-3xl" />
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-indigo-500/5 rounded-full blur-3xl" />
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="text-center max-w-3xl mx-auto mb-12 lg:mb-16">
          <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono mb-4">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Interactive Project Planner</span>
          </div>
          <h2 className="text-2xl sm:text-4xl font-display font-bold text-slate-100 tracking-tight">
            How Techzyan Approaches Your Project
          </h2>
          <p className="mt-3.5 text-slate-400 text-sm sm:text-base leading-relaxed">
            Select your field to see how we pair an entry website with right-sized technical solutions tailored to your operational realities.
          </p>
        </div>

        {/* Role Selector Tabs */}
        <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-10">
          {(Object.keys(roleSpecs) as Array<keyof typeof roleSpecs>).map((key) => {
            const isSelected = selectedRole === key;
            return (
              <button
                key={key}
                onClick={() => setSelectedRole(key)}
                className={`px-4 py-2.5 rounded-xl text-xs sm:text-sm font-medium transition-all duration-200 ${
                  isSelected
                    ? 'bg-slate-800 text-slate-100 border border-brand-cyan shadow-glow-cyan'
                    : 'bg-slate-900/60 text-slate-400 border border-slate-800 hover:text-slate-200 hover:bg-slate-800/40'
                }`}
              >
                {roleSpecs[key].label}
              </button>
            );
          })}
        </div>

        {/* Selected Role Blueprint Card */}
        <div className="max-w-4xl mx-auto glass-card rounded-2xl p-6 sm:p-10 border border-slate-800 shadow-2xl space-y-8">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800">
            <div>
              <span className="text-xs font-mono uppercase tracking-wider text-brand-cyan font-semibold">
                Tailored Studio Architecture
              </span>
              <h3 className="text-xl sm:text-2xl font-bold text-slate-100 mt-1">
                {current.title}
              </h3>
              <p className="text-sm text-slate-400 mt-1">
                {current.tagline}
              </p>
            </div>
            <div className="flex items-center gap-3 shrink-0">
              <div className="text-right sm:text-right">
                <div className="text-xs text-slate-500 font-mono">Estimated Cycle</div>
                <div className="text-sm font-semibold text-slate-200 flex items-center gap-1.5 justify-end mt-0.5">
                  <Clock className="w-3.5 h-3.5 text-brand-cyan" />
                  <span>{current.timeline}</span>
                </div>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Step 1: The Website Entry */}
            <div className="p-5 rounded-xl bg-slate-950/70 border border-slate-800/90 space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono uppercase tracking-wider text-slate-400 font-semibold">
                  1. The Primary Entry Point
                </span>
                <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-sky-500/10 text-brand-cyan border border-sky-500/30">
                  Essential Website
                </span>
              </div>
              <h4 className="text-sm font-bold text-slate-200">
                {current.entryDeliverable}
              </h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                Establishes immediate professional authority, loads in under a second on mobile networks, and explains your offering without fluff.
              </p>
            </div>

            {/* Step 2: The Custom Solution */}
            <div className="p-5 rounded-xl bg-slate-950/70 border border-slate-800/90 space-y-3">
              <div className="flex items-center justify-between">
                <span className="text-xs font-mono uppercase tracking-wider text-emerald-400 font-semibold">
                  2. Right-Sized Technical Solution
                </span>
                <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/30">
                  Optional Expansion
                </span>
              </div>
              <h4 className="text-sm font-bold text-slate-200">
                {current.customTech}
              </h4>
              <p className="text-xs text-slate-400 leading-relaxed">
                Eliminates administrative bottlenecks and automates communication without forcing you into bloated SaaS subscriptions.
              </p>
            </div>
          </div>

          {/* Pricing & Scoping Transparency Note */}
          <div className="p-4 rounded-xl bg-slate-900/60 border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 text-xs text-slate-400">
            <div className="flex items-center gap-2.5">
              <ShieldCheck className="w-5 h-5 text-brand-cyan shrink-0" />
              <span>
                <strong>Zero Hidden Charges:</strong> All websites are delivered with full ownership, complete source code, and transparent fixed deliverables.
              </span>
            </div>
            <div className="font-mono text-slate-300 shrink-0">
              {current.investment}
            </div>
          </div>

          {/* CTA Row */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-2">
            <p className="text-xs text-slate-400 text-center sm:text-left">
              Ready to discuss how this fits your exact requirements?
            </p>
            <div className="flex flex-col sm:flex-row items-center gap-3 w-full sm:w-auto">
              <a
                href={`${siteConfig.contact.whatsappLink}&text=${encodeURIComponent(`Hi Techzyan! I am looking for a digital solution for a ${current.label}.`)}`}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-2.5 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs font-semibold uppercase tracking-wider rounded-lg transition-colors"
              >
                <WhatsAppIcon className="w-4 h-4" />
                <span>Discuss on WhatsApp</span>
              </a>
              <button
                onClick={() => onOpenConsultation(current.category)}
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-2.5 bg-brand-cyan hover:bg-sky-300 text-slate-950 text-xs font-semibold uppercase tracking-wider rounded-lg shadow-glow-cyan transition-all"
              >
                <span>Request Project Scope</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
