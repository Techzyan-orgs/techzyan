'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
import PujaConsultationModal from '@/components/PujaConsultationModal';
import DemonstrationModal from '@/components/DemonstrationModal';
import DhaakButton from '@/components/DhaakButton';
import { demonstrationProjects } from '@/data/demonstrations';
import { siteConfig } from '@/config/site';
import { DemonstrationProject } from '@/types';
import {
  ArrowRight,
  Sparkles,
  CheckCircle2,
  Layers,
  Globe,
  Stethoscope,
  GraduationCap,
  Briefcase,
  Flame,
  CalendarCheck,
  ExternalLink,
  MessageCircle,
  Eye,
} from 'lucide-react';

export default function HomePage() {
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);
  const [isPujaModalOpen, setIsPujaModalOpen] = useState(false);
  const [consultationCategory, setConsultationCategory] = useState<string | undefined>();
  const [selectedDemonstration, setSelectedDemonstration] = useState<DemonstrationProject | null>(null);
  const [activeAudienceTab, setActiveAudienceTab] = useState<'doctor' | 'tutor' | 'business' | 'puja'>('doctor');

  const handleOpenConsultation = (category?: string) => {
    if (category === 'Durga Puja Committee') {
      setIsPujaModalOpen(true);
    } else {
      setConsultationCategory(category);
      setIsConsultationOpen(true);
    }
  };

  const audienceInsights = {
    doctor: {
      role: 'Doctors & Specialist Clinics',
      entry: 'Authoritative Clinic Website & OPD Schedule',
      entryDesc: 'Fast, reassuring patient portal with chamber timings, location maps, and doctor credentials.',
      custom: '3-Step Symptom-Aware Appointment Triage',
      customDesc: 'Reduces receptionist call fatigue by 70% by letting patients check slots & confirm via WhatsApp.',
      impact: 'Patients arrive prepared, front-desk calls drop significantly.',
      category: 'Doctor & Healthcare'
    },
    tutor: {
      role: 'Private Tutors & Academies',
      entry: 'Academic Profile & Syllabus Roadmaps',
      entryDesc: 'Showcase past student board/JEE results, curriculum coverage, and teaching methodology.',
      custom: 'Live Batch Vacancy & Inquiry Generator',
      customDesc: 'Eliminates lost parent WhatsApp messages with auto-filled board/class inquiry routing.',
      impact: 'Fill seats faster during admission seasons with zero administrative chaos.',
      category: 'Private Tutor & Educator'
    },
    business: {
      role: 'Small Businesses & Boutiques',
      entry: 'Editorial Showcase & Brand Presence',
      entryDesc: 'Sub-second mobile speed with high-resolution lookbooks that build immediate credibility.',
      custom: 'Custom Price Estimator & Measurement Guide',
      customDesc: 'Pre-qualify customer inquiries and collect bespoke orders without manual friction.',
      impact: 'Turn passive web visitors into high-intent paying customers.',
      category: 'Small Business & Boutique'
    },
    puja: {
      role: 'Durga Puja & Cultural Committees',
      entry: 'Official 5-Day Festival Guide & Art Gallery',
      entryDesc: 'Live Pushpanjali & Bhog timetable, theme concept story, and nearest metro transit map.',
      custom: 'Corporate Sponsorship Presentation Suite',
      customDesc: 'Dignified digital sponsorship proposal deck with automated tier inquiry flows for brand managers.',
      impact: 'Attract premier corporate brand sponsors and guide 50k+ visitors effortlessly.',
      category: 'Durga Puja Committee'
    }
  };

  const currentAudience = audienceInsights[activeAudienceTab];

  return (
    <>
      <Header onOpenConsultation={() => handleOpenConsultation()} />

      <main id="main-content" className="flex-1">
        {/* 1. HERO SECTION */}
        <section className="relative pt-32 pb-16 lg:pt-44 lg:pb-28 overflow-hidden bg-radial-gradient-subtle">
          <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-sky-500/10 rounded-full blur-[120px] pointer-events-none" />

          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div className="max-w-4xl mx-auto text-center space-y-6">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900/90 border border-slate-700/80 text-xs font-mono text-slate-300 shadow-sm">
                <span className="w-2 h-2 rounded-full bg-brand-cyan animate-ping" />
                <span className="text-slate-200 font-semibold">Specialist Technical Studio</span>
                <span className="text-slate-500">•</span>
                <span className="text-brand-cyan">Kolkata & Global</span>
              </div>

              <h1 className="text-4xl sm:text-6xl lg:text-7xl font-display font-extrabold text-slate-100 tracking-tight leading-[1.12] text-balance">
                Websites engineered to work. <br className="hidden sm:inline" />
                <span className="text-gradient-cyan">Not just to exist.</span>
              </h1>

              <p className="text-base sm:text-lg lg:text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed text-balance font-normal">
                We craft high-speed websites and intelligent operational tools for doctors, educators, local businesses, and Durga Puja committees in Kolkata and beyond.
              </p>

              <div className="py-1 text-xs font-mono uppercase tracking-widest text-slate-400 font-medium">
                Understand the requirement first • Build the right digital solution second
              </div>

              <div className="flex flex-col sm:flex-row items-center justify-center gap-3.5 pt-2">
                <button
                  onClick={() => handleOpenConsultation()}
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-2.5 px-8 py-3.5 bg-brand-cyan hover:bg-sky-300 active:bg-sky-400 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-cyan transition-all duration-200 hover:-translate-y-0.5"
                >
                  <span>Discuss Your Project</span>
                  <ArrowRight className="w-4 h-4" />
                </button>

                <a
                  href="#demonstrations"
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-7 py-3.5 bg-slate-900/80 hover:bg-slate-800 text-slate-200 hover:text-white border border-slate-700/80 font-semibold text-xs uppercase tracking-wider rounded-xl transition-colors duration-200"
                >
                  <span>Explore Live Demos</span>
                </a>
              </div>

              <div className="pt-8 grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-3xl mx-auto border-t border-slate-800/80 text-left">
                <div className="p-3 rounded-xl bg-slate-900/50 border border-slate-800">
                  <div className="text-xs text-brand-cyan font-mono font-bold">Sub-Second Speed</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">Optimized for mobile 4G/5G</div>
                </div>
                <div className="p-3 rounded-xl bg-slate-900/50 border border-slate-800">
                  <div className="text-xs text-brand-cyan font-mono font-bold">100% Ownership</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">Zero monthly builder lock-in</div>
                </div>
                <div className="p-3 rounded-xl bg-slate-900/50 border border-slate-800">
                  <div className="text-xs text-brand-cyan font-mono font-bold">Accessible UI</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">High contrast & readable</div>
                </div>
                <div className="p-3 rounded-xl bg-slate-900/50 border border-slate-800">
                  <div className="text-xs text-brand-cyan font-mono font-bold">No Tech Jargon</div>
                  <div className="text-[11px] text-slate-400 mt-0.5">Focused on real outcomes</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 2. ALL OUR SERVICES AT A GLANCE */}
        <section className="py-16 lg:py-24 bg-slate-950 border-t border-slate-800/80">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center max-w-3xl mx-auto mb-12">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono mb-3">
                <Layers className="w-3.5 h-3.5" />
                <span>Everything We Provide</span>
              </div>
              <h2 className="text-2xl sm:text-4xl font-display font-bold text-slate-100 tracking-tight">
                Our Core Services & Solutions
              </h2>
              <p className="mt-3 text-slate-400 text-sm sm:text-base leading-relaxed">
                From fast websites that build credibility to custom operational tools that save you hours every week.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              {/* Pillar 1: Modern Websites */}
              <div className="glass-card rounded-3xl p-6 sm:p-8 border border-slate-800 hover:border-brand-cyan/40 transition-all flex flex-col justify-between space-y-6">
                <div className="space-y-4">
                  <div className="w-12 h-12 rounded-2xl bg-sky-500/10 border border-sky-500/30 flex items-center justify-center text-brand-cyan">
                    <Globe className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-slate-100">High-Performance Websites</h3>
                    <p className="text-xs text-slate-400 mt-1">
                      Fast, beautiful digital homes tailored for businesses, clinics, and educators.
                    </p>
                  </div>
                  <ul className="space-y-2 text-xs text-slate-300">
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                      <span>Business & Corporate Websites</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                      <span>Doctor & Clinic Practice Platforms</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                      <span>Tutor & Academic Course Portals</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                      <span>Heritage Boutiques & Lookbooks</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                      <span>Educational Institute Websites</span>
                    </li>
                  </ul>
                </div>
                <div className="pt-4 border-t border-slate-800 flex items-center justify-between">
                  <span className="text-[11px] font-mono text-slate-400">Fixed Project Scope</span>
                  <Link href="/solutions#business-websites" className="text-xs font-semibold text-brand-cyan hover:text-sky-300 flex items-center gap-1">
                    <span>Explore Websites</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>

              {/* Pillar 2: Custom Digital Tools */}
              <div className="glass-card rounded-3xl p-6 sm:p-8 border border-slate-800 hover:border-emerald-500/40 transition-all flex flex-col justify-between space-y-6">
                <div className="space-y-4">
                  <div className="w-12 h-12 rounded-2xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                    <CalendarCheck className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-slate-100">Right-Sized Custom Tools</h3>
                    <p className="text-xs text-slate-400 mt-1">
                      Lightweight tools built specifically around your day-to-day workflow.
                    </p>
                  </div>
                  <ul className="space-y-2 text-xs text-slate-300">
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      <span>Patient Appointment & OPD Triage</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      <span>Live Batch Vacancy & Seat Trackers</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      <span>Student Admission Inquiry Pipelines</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      <span>Bespoke Price Estimation Calculators</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                      <span>Automated WhatsApp Notifications</span>
                    </li>
                  </ul>
                </div>
                <div className="pt-4 border-t border-slate-800 flex items-center justify-between">
                  <span className="text-[11px] font-mono text-slate-400">Scope-Based Quote</span>
                  <Link href="/solutions#appointment-booking-systems" className="text-xs font-semibold text-emerald-400 hover:text-emerald-300 flex items-center gap-1">
                    <span>Explore Tools</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>

              {/* Pillar 3: Durga Puja & Festival Platforms */}
              <div className="puja-card rounded-3xl p-6 sm:p-8 border border-amber-500/30 hover:border-amber-400/60 transition-all flex flex-col justify-between space-y-6">
                <div className="space-y-4">
                  <div className="w-12 h-12 rounded-2xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400">
                    <Flame className="w-6 h-6" />
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-amber-100">Durga Puja Platforms</h3>
                    <p className="text-xs text-amber-200/80 mt-1">
                      Kolkata’s premier digital solution for Sharodotsav committees.
                    </p>
                  </div>
                  <ul className="space-y-2 text-xs text-slate-200">
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0" />
                      <span>5-Day Interactive Ritual & Bhog Timetable</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0" />
                      <span>Corporate Sponsorship Deck & Tiers</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0" />
                      <span>Visitor Metro & Crowd Route Maps</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0" />
                      <span>Pandal Theme & Sculptor Tribute Archive</span>
                    </li>
                    <li className="flex items-center gap-2">
                      <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0" />
                      <span>Online UPI QR & Contribution Gateways</span>
                    </li>
                  </ul>
                </div>
                <div className="pt-4 border-t border-amber-500/20 flex items-center justify-between">
                  <span className="text-[11px] font-mono text-amber-300">Sharodotsav 2026</span>
                  <Link href="/solutions/durga-puja" className="text-xs font-semibold text-amber-300 hover:text-amber-100 flex items-center gap-1">
                    <span>Explore Puja Suite</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 3. INTERACTIVE AUDIENCE SELECTOR */}
        <section className="py-16 lg:py-24 bg-[#080C14] border-t border-slate-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center max-w-2xl mx-auto mb-10">
              <h2 className="text-2xl sm:text-3xl font-display font-bold text-slate-100">
                How We Help Your Specific Field
              </h2>
              <p className="text-slate-400 text-sm mt-2">
                Tap your field to see the essential website entry + optional right-sized tool.
              </p>
            </div>

            <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-3 mb-8">
              {[
                { id: 'doctor', label: 'Doctor / Clinic', icon: Stethoscope },
                { id: 'tutor', label: 'Private Tutor', icon: GraduationCap },
                { id: 'business', label: 'Small Business / Shop', icon: Briefcase },
                { id: 'puja', label: 'Durga Puja Committee', icon: Flame },
              ].map((tab) => {
                const Icon = tab.icon;
                const isSelected = activeAudienceTab === tab.id;
                return (
                  <button
                    key={tab.id}
                    onClick={() => setActiveAudienceTab(tab.id as any)}
                    className={`flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs sm:text-sm font-medium transition-all ${
                      isSelected
                        ? tab.id === 'puja'
                          ? 'bg-amber-500 text-slate-950 font-bold shadow-glow-gold'
                          : 'bg-slate-800 text-slate-100 border border-brand-cyan shadow-glow-cyan'
                        : 'bg-slate-900/60 text-slate-400 border border-slate-800 hover:text-slate-200'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    <span>{tab.label}</span>
                  </button>
                );
              })}
            </div>

            <div className="max-w-4xl mx-auto glass-card rounded-3xl p-6 sm:p-10 border border-slate-800 space-y-6">
              <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-4 border-b border-slate-800">
                <div>
                  <span className="text-xs font-mono uppercase text-brand-cyan font-semibold">Tailored Architecture</span>
                  <h3 className="text-xl sm:text-2xl font-bold text-slate-100 mt-0.5">{currentAudience.role}</h3>
                </div>
                <div className="text-xs text-slate-400 font-mono">
                  {currentAudience.impact}
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-slate-400 font-semibold">1. The Primary Website</span>
                    <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-sky-500/10 text-brand-cyan">Essential</span>
                  </div>
                  <h4 className="text-sm font-bold text-slate-100">{currentAudience.entry}</h4>
                  <p className="text-xs text-slate-400 leading-relaxed">{currentAudience.entryDesc}</p>
                </div>

                <div className="p-5 rounded-2xl bg-slate-950/70 border border-slate-800 space-y-2">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-emerald-400 font-semibold">2. Right-Sized Tool</span>
                    <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-emerald-500/10 text-emerald-400">Optional</span>
                  </div>
                  <h4 className="text-sm font-bold text-slate-100">{currentAudience.custom}</h4>
                  <p className="text-xs text-slate-400 leading-relaxed">{currentAudience.customDesc}</p>
                </div>
              </div>

              <div className="pt-2 flex flex-col sm:flex-row items-center justify-between gap-4">
                <span className="text-xs text-slate-400 text-center sm:text-left">
                  100% transparent pricing with zero monthly builder lock-in.
                </span>
                <button
                  onClick={() => handleOpenConsultation(currentAudience.category)}
                  className="w-full sm:w-auto px-6 py-2.5 bg-brand-cyan hover:bg-sky-300 text-slate-950 text-xs font-bold uppercase tracking-wider rounded-xl shadow-glow-cyan transition-all"
                >
                  Discuss {activeAudienceTab === 'puja' ? 'Puja' : currentAudience.role.split(' ')[0]} Scope
                </button>
              </div>
            </div>
          </div>
        </section>

        {/* 4. DEDICATED DURGA PUJA SPOTLIGHT (2-COLUMN WITH BACKGROUNDLESS DURGA IDOL ON RIGHT) */}
        <section className="py-16 lg:py-24 bg-gradient-to-b from-[#0F0C08] to-[#080C14] border-t border-b border-amber-950/40">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="rounded-3xl bg-gradient-to-br from-[#1C140A] via-[#140E06] to-[#0D0A05] border border-amber-500/30 p-8 sm:p-12 lg:p-14 overflow-hidden shadow-2xl relative">
              <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch relative z-10">
                {/* Left Column: Content & Features (7 cols) */}
                <div className="lg:col-span-7 flex flex-col justify-between space-y-6">
                  <div className="space-y-6">
                    <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-amber-500/15 border border-amber-500/40 text-amber-300 text-xs font-mono">
                      <Flame className="w-3.5 h-3.5 text-amber-400" />
                      <span>Sharodotsav 2026 Special Platform</span>
                    </div>

                    <h2 className="text-2xl sm:text-4xl font-display font-extrabold text-amber-100 tracking-tight">
                      A digital presence for your Puja, <br />
                      <span className="text-gradient-gold">built around your committee's real needs.</span>
                    </h2>

                    <p className="text-slate-300 text-sm sm:text-base leading-relaxed">
                      Durga Puja is Bengal’s greatest festival of public art and heritage. We design authoritative digital hubs that dignify your theme, guide 50,000+ daily visitors effortlessly, and provide corporate brand managers with clean, structured sponsorship proposals.
                    </p>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                      <div className="p-3 rounded-xl bg-black/40 border border-amber-500/20 text-xs text-slate-300 flex items-start gap-2">
                        <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                        <div>
                          <div className="font-semibold text-amber-200">5-Day Ritual Timetable</div>
                          <div className="text-slate-400 text-[11px]">Accurate Pushpanjali & Bhog hours for devotees</div>
                        </div>
                      </div>

                      <div className="p-3 rounded-xl bg-black/40 border border-amber-500/20 text-xs text-slate-300 flex items-start gap-2">
                        <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                        <div>
                          <div className="font-semibold text-amber-200">Corporate Sponsorship Suite</div>
                          <div className="text-slate-400 text-[11px]">Digital decks for Title, Co-Powered & Food partners</div>
                        </div>
                      </div>

                      <div className="p-3 rounded-xl bg-black/40 border border-amber-500/20 text-xs text-slate-300 flex items-start gap-2">
                        <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                        <div>
                          <div className="font-semibold text-amber-200">Metro & Crowd Transit Map</div>
                          <div className="text-slate-400 text-[11px]">Direct routes to nearest Kolkata Metro stations & VIP gates</div>
                        </div>
                      </div>

                      <div className="p-3 rounded-xl bg-black/40 border border-amber-500/20 text-xs text-slate-300 flex items-start gap-2">
                        <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                        <div>
                          <div className="font-semibold text-amber-200">Theme Art & Sculptor Tribute</div>
                          <div className="text-slate-400 text-[11px]">Dignified editorial showcase of your pandal artists</div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="flex flex-col sm:flex-row items-center gap-3.5 pt-6">
                    <Link
                      href="/solutions/durga-puja"
                      className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-gold transition-all"
                    >
                      <span>Explore Puja Platform</span>
                      <ArrowRight className="w-4 h-4" />
                    </Link>

                    <button
                      onClick={() => setIsPujaModalOpen(true)}
                      className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 bg-black/70 hover:bg-black/90 text-amber-300 border border-amber-500/40 text-xs font-bold uppercase tracking-wider rounded-xl transition-colors"
                    >
                      <span>Discuss Your Puja Digital Needs</span>
                    </button>
                  </div>
                </div>

                {/* Right Column: User's Durga Idol Image + Floating Dhaak Button (5 cols) */}
                <div className="lg:col-span-5 flex flex-col justify-between items-center lg:items-end gap-6 pt-6 lg:pt-0 relative min-h-[280px]">
                  {/* User's Durga Idol Image Container */}
                  <div className="relative w-full max-w-[360px] sm:max-w-[420px] lg:max-w-[460px] flex items-center justify-center mx-auto lg:mr-0 group">
                    {/* Golden Ambient Glow Aura */}
                    <div className="absolute inset-0 bg-amber-500/25 rounded-full blur-3xl pointer-events-none" />
                    
                    <Image
                      src="/images/durga-idol.png"
                      alt="Durga Puja Pratima Idol"
                      width={800}
                      height={800}
                      quality={100}
                      className="w-full h-auto max-h-[380px] sm:max-h-[420px] object-contain drop-shadow-[0_12px_45px_rgba(245,158,11,0.4)] group-hover:scale-105 transition-transform duration-500 relative z-10"
                      priority
                    />
                  </div>

                  {/* Floating Dhaak Icon Player Aligned with Buttons */}
                  <div className="w-full flex justify-center lg:justify-end pt-4">
                    <DhaakButton />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 5. DEMONSTRATIONS SHOWCASE */}
        <section id="demonstrations" className="py-16 lg:py-24 bg-[#080C14] border-b border-slate-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
              <div className="max-w-2xl">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono mb-2">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Demonstration Showcase</span>
                </div>
                <h2 className="text-2xl sm:text-4xl font-display font-bold text-slate-100 tracking-tight">
                  Proof of Capability Through Real Prototypes
                </h2>
                <p className="mt-2 text-slate-400 text-sm sm:text-base leading-relaxed">
                  We don't invent fake client logos or made-up reviews. Explore these fully functional, realistic demonstration concepts.
                </p>
              </div>

              <Link
                href="/work"
                className="inline-flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-brand-cyan hover:text-sky-300 font-semibold"
              >
                <span>View Full Showcase</span>
                <ArrowRight className="w-4 h-4" />
              </Link>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {demonstrationProjects.map((project) => (
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
                      <h3 className="text-lg font-bold text-slate-100 group-hover:text-brand-cyan transition-colors">
                        {project.title}
                      </h3>
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

                      <a
                        href={project.demoUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-sky-500/10 hover:bg-sky-500/20 text-brand-cyan text-xs font-bold transition-colors border border-sky-500/30"
                      >
                        <span>Live Demo</span>
                        <ExternalLink className="w-3.5 h-3.5" />
                      </a>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* 6. HOW WE WORK */}
        <section className="py-16 lg:py-24 bg-slate-950 border-b border-slate-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center max-w-2xl mx-auto mb-12">
              <h2 className="text-2xl sm:text-3xl font-display font-bold text-slate-100">
                How We Deliver Without Friction
              </h2>
              <p className="mt-2 text-slate-400 text-sm">
                Direct senior collaboration, transparent milestones, and zero agency fluff.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {[
                { step: '01', title: 'Listen & Scope', desc: 'We analyze your real workflow and determine whether you need a website or a tool.' },
                { step: '02', title: 'Intentional Design', desc: 'High-contrast, mobile-first design with clean typography and zero clumsy layouts.' },
                { step: '03', title: 'Clean Engineering', desc: 'Sub-second mobile loading speeds, complete SEO setup, and high accessibility.' },
                { step: '04', title: '100% Ownership', desc: 'All code and domains delivered with full client ownership and zero monthly lock-in.' },
              ].map((item, i) => (
                <div key={i} className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-2">
                  <div className="text-2xl font-mono font-bold text-brand-cyan">{item.step}</div>
                  <h3 className="text-sm font-bold text-slate-100">{item.title}</h3>
                  <p className="text-xs text-slate-400 leading-relaxed">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* 7. CALL TO ACTION */}
        <section className="py-16 lg:py-24 bg-[#080C14]">
          <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Direct Studio Access</span>
            </div>

            <h2 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight text-balance">
              Let's build something that makes your business work better.
            </h2>

            <p className="text-slate-400 text-sm sm:text-base max-w-xl mx-auto leading-relaxed">
              No sales pitches or aggressive follow-ups. Speak directly with a technical specialist in Kolkata to discuss your project.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
              <button
                onClick={() => handleOpenConsultation()}
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-3.5 bg-brand-cyan hover:bg-sky-300 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-cyan transition-all"
              >
                <span>Start a Project Discussion</span>
                <ArrowRight className="w-4 h-4" />
              </button>

              <a
                href={siteConfig.contact.whatsappLink}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-7 py-3.5 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-bold text-xs uppercase tracking-wider rounded-xl transition-colors"
              >
                <MessageCircle className="w-4 h-4" />
                <span>Chat on WhatsApp</span>
              </a>
            </div>
          </div>
        </section>
      </main>

      <Footer />

      {/* Generic Consultation Modal */}
      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
        initialCategory={consultationCategory}
      />

      {/* Dedicated Durga Puja Committee Modal */}
      <PujaConsultationModal
        isOpen={isPujaModalOpen}
        onClose={() => setIsPujaModalOpen(false)}
      />

      {/* Demonstration Project Live Viewer */}
      <DemonstrationModal
        project={selectedDemonstration}
        onClose={() => setSelectedDemonstration(null)}
        onOpenConsultation={() => handleOpenConsultation(selectedDemonstration?.clientType)}
      />
    </>
  );
}
