import os

def write_file(rel_path, content):
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {rel_path}")

home_code = """'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
import DemonstrationModal from '@/components/DemonstrationModal';
import ProjectConsultationSection from '@/components/ProjectConsultationSection';
import { demonstrationProjects } from '@/data/demonstrations';
import { solutionsData } from '@/data/solutions';
import { audienceData } from '@/data/audiences';
import { durgaPujaFeatures } from '@/data/durgaPuja';
import { siteConfig } from '@/config/site';
import { DemonstrationProject } from '@/types';
import {
  ArrowRight,
  Sparkles,
  CheckCircle2,
  Layers,
  Cpu,
  ShieldCheck,
  Zap,
  Globe,
  Stethoscope,
  GraduationCap,
  Briefcase,
  Building,
  Flame,
  Calendar,
  Award,
  MapPin,
  MessageCircle,
  Clock,
  ArrowUpRight,
} from 'lucide-react';

export default function HomePage() {
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);
  const [consultationCategory, setConsultationCategory] = useState<string | undefined>();
  const [selectedDemonstration, setSelectedDemonstration] = useState<DemonstrationProject | null>(null);

  const handleOpenConsultation = (category?: string) => {
    setConsultationCategory(category);
    setIsConsultationOpen(true);
  };

  return (
    <>
      <Header onOpenConsultation={() => handleOpenConsultation()} />

      <main id="main-content" className="flex-1">
        {/* 1. HERO SECTION */}
        <section className="relative pt-32 pb-20 lg:pt-40 lg:pb-32 overflow-hidden bg-radial-gradient-subtle">
          <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] bg-sky-500/10 rounded-full blur-[120px] pointer-events-none" />

          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div className="max-w-4xl mx-auto text-center space-y-6">
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-slate-900/90 border border-slate-700/80 text-xs font-mono text-slate-300 shadow-sm">
                <span className="w-2 h-2 rounded-full bg-brand-cyan animate-ping" />
                <span className="text-slate-200 font-semibold">Specialist Technical Studio</span>
                <span className="text-slate-500">•</span>
                <span className="text-brand-cyan">Kolkata & Global</span>
              </div>

              <h1 className="text-3xl sm:text-5xl lg:text-6xl font-display font-extrabold text-slate-100 tracking-tight leading-[1.15] text-balance">
                Your technical partner, <br className="hidden sm:inline" />
                <span className="text-gradient-cyan">not just your website developer.</span>
              </h1>

              <p className="text-base sm:text-lg lg:text-xl text-slate-300 max-w-2xl mx-auto leading-relaxed text-balance">
                We partner with doctors, educators, local businesses, and Durga Puja committees to build high-performance websites and right-sized digital solutions tailored to how you actually operate.
              </p>

              <div className="py-2 text-xs font-mono uppercase tracking-widest text-slate-400">
                Understand the requirement first • Build the right digital solution second
              </div>

              <div className="flex flex-col sm:flex-row items-center justify-center gap-3.5 pt-2">
                <button
                  onClick={() => handleOpenConsultation()}
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-2.5 px-7 py-3.5 bg-brand-cyan hover:bg-sky-300 active:bg-sky-400 text-slate-950 font-semibold text-sm rounded-xl shadow-glow-cyan transition-all duration-200 hover:-translate-y-0.5"
                >
                  <span>Discuss Your Project</span>
                  <ArrowRight className="w-4 h-4" />
                </button>

                <Link
                  href="/solutions"
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-slate-900/80 hover:bg-slate-800 text-slate-200 hover:text-white border border-slate-700/80 font-medium text-sm rounded-xl transition-colors duration-200"
                >
                  <span>Explore Solutions</span>
                </Link>
              </div>

              <div className="pt-10 grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-3xl mx-auto border-t border-slate-800/80 text-left">
                <div className="p-3 rounded-lg bg-slate-900/40 border border-slate-800/60">
                  <div className="text-xs text-brand-cyan font-mono font-semibold">Sub-Second</div>
                  <div className="text-xs text-slate-400 mt-0.5">Mobile page loads</div>
                </div>
                <div className="p-3 rounded-lg bg-slate-900/40 border border-slate-800/60">
                  <div className="text-xs text-brand-cyan font-mono font-semibold">100% Ownership</div>
                  <div className="text-xs text-slate-400 mt-0.5">Zero monthly builder lock-in</div>
                </div>
                <div className="p-3 rounded-lg bg-slate-900/40 border border-slate-800/60">
                  <div className="text-xs text-brand-cyan font-mono font-semibold">Accessible</div>
                  <div className="text-xs text-slate-400 mt-0.5">WCAG AA high contrast</div>
                </div>
                <div className="p-3 rounded-lg bg-slate-900/40 border border-slate-800/60">
                  <div className="text-xs text-brand-cyan font-mono font-semibold">Requirement First</div>
                  <div className="text-xs text-slate-400 mt-0.5">Scoping without jargon</div>
                </div>
              </div>
            </div>
          </div>
        </section>
"""
home_code += """
        {/* 2. MORE THAN A WEBSITE POSITIONING MATRIX */}
        <section className="py-20 bg-slate-950 border-t border-slate-800/80">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center max-w-3xl mx-auto mb-14">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-mono mb-3">
                <Layers className="w-3.5 h-3.5" />
                <span>The Techzyan Distinction</span>
              </div>
              <h2 className="text-2xl sm:text-4xl font-display font-bold text-slate-100 tracking-tight">
                A website is the entry point. <br />
                <span className="text-slate-400 font-normal">Sometimes your operations need more.</span>
              </h2>
              <p className="mt-4 text-slate-400 text-sm sm:text-base leading-relaxed">
                Generic developers sell you static templates and walk away. Techzyan helps you determine if a website is enough, or if integrating a lightweight custom tool will save you dozens of administrative hours every week.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div className="glass-card rounded-2xl p-6 border border-slate-800 flex flex-col justify-between space-y-6">
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-sky-400 font-semibold">Doctor & Clinic</span>
                    <Stethoscope className="w-5 h-5 text-sky-400" />
                  </div>
                  <div className="space-y-2">
                    <div className="text-xs text-slate-400">
                      <span className="text-slate-500 font-mono">Website Level:</span> Authoritative clinic presence, OPD timings, chamber locations & doctor credentials.
                    </div>
                    <div className="text-xs text-brand-cyan font-medium p-2.5 rounded-lg bg-sky-950/40 border border-sky-800/40">
                      <span className="font-mono uppercase text-[10px] text-sky-300 block mb-0.5">+ Custom Solution:</span>
                      Symptom-aware appointment triage system that reduces receptionist call fatigue by 70%.
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => handleOpenConsultation('Doctor & Healthcare')}
                  className="text-xs font-semibold text-sky-400 hover:text-sky-300 flex items-center gap-1 self-start"
                >
                  <span>Explore clinic solution</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>

              <div className="glass-card rounded-2xl p-6 border border-slate-800 flex flex-col justify-between space-y-6">
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-indigo-400 font-semibold">Private Tutor & Mentor</span>
                    <GraduationCap className="w-5 h-5 text-indigo-400" />
                  </div>
                  <div className="space-y-2">
                    <div className="text-xs text-slate-400">
                      <span className="text-slate-500 font-mono">Website Level:</span> Subject curriculum, past student board/JEE results & academic philosophy.
                    </div>
                    <div className="text-xs text-indigo-300 font-medium p-2.5 rounded-lg bg-indigo-950/40 border border-indigo-800/40">
                      <span className="font-mono uppercase text-[10px] text-indigo-400 block mb-0.5">+ Custom Solution:</span>
                      Batch vacancy tracker and parent inquiry generator pre-filling structured WhatsApp messages.
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => handleOpenConsultation('Private Tutor & Educator')}
                  className="text-xs font-semibold text-indigo-400 hover:text-indigo-300 flex items-center gap-1 self-start"
                >
                  <span>Explore tutor solution</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>

              <div className="glass-card rounded-2xl p-6 border border-slate-800 flex flex-col justify-between space-y-6">
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-emerald-400 font-semibold">Small Business & Boutique</span>
                    <Briefcase className="w-5 h-5 text-emerald-400" />
                  </div>
                  <div className="space-y-2">
                    <div className="text-xs text-slate-400">
                      <span className="text-slate-500 font-mono">Website Level:</span> High-resolution artisanal lookbook, workshop story & service menu.
                    </div>
                    <div className="text-xs text-emerald-300 font-medium p-2.5 rounded-lg bg-emerald-950/40 border border-emerald-800/40">
                      <span className="font-mono uppercase text-[10px] text-emerald-400 block mb-0.5">+ Custom Solution:</span>
                      Bespoke measurement guide, interactive quotation calculator & custom inquiry pipeline.
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => handleOpenConsultation('Small Business & Boutique')}
                  className="text-xs font-semibold text-emerald-400 hover:text-emerald-300 flex items-center gap-1 self-start"
                >
                  <span>Explore business solution</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>

              <div className="glass-card rounded-2xl p-6 border border-slate-800 flex flex-col justify-between space-y-6">
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-purple-400 font-semibold">Educational Institute</span>
                    <Building className="w-5 h-5 text-purple-400" />
                  </div>
                  <div className="space-y-2">
                    <div className="text-xs text-slate-400">
                      <span className="text-slate-500 font-mono">Website Level:</span> Multi-department catalog, faculty directory & campus announcements.
                    </div>
                    <div className="text-xs text-purple-300 font-medium p-2.5 rounded-lg bg-purple-950/40 border border-purple-800/40">
                      <span className="font-mono uppercase text-[10px] text-purple-400 block mb-0.5">+ Custom Solution:</span>
                      Student admissions management pipeline and automated digital prospectus delivery.
                    </div>
                  </div>
                </div>
                <button
                  onClick={() => handleOpenConsultation('Educational Institute')}
                  className="text-xs font-semibold text-purple-400 hover:text-purple-300 flex items-center gap-1 self-start"
                >
                  <span>Explore institute solution</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>

              <div className="puja-card rounded-2xl p-6 border border-amber-500/30 md:col-span-2 flex flex-col justify-between space-y-6">
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-amber-400 font-semibold flex items-center gap-1.5">
                      <Flame className="w-4 h-4 text-amber-400" />
                      <span>Durga Puja & Cultural Committees (Strategic Solution)</span>
                    </span>
                    <span className="px-2.5 py-0.5 rounded text-[10px] font-mono bg-amber-500/20 text-amber-300 border border-amber-500/40">
                      Sharodotsav 2026
                    </span>
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="text-xs text-slate-300 bg-black/40 p-3 rounded-lg border border-amber-500/20">
                      <span className="text-amber-400 font-mono uppercase text-[10px] block mb-1">Essential Festival Hub:</span>
                      5-day interactive ritual schedule, theme concept story, sculptor tribute, photo gallery & nearest metro route guide.
                    </div>
                    <div className="text-xs text-amber-200 bg-amber-950/40 p-3 rounded-lg border border-amber-500/30">
                      <span className="text-amber-300 font-mono uppercase text-[10px] block mb-1">+ Corporate Sponsorship Platform:</span>
                      Digital sponsorship proposal deck, tier showcase (Title, Co-Sponsor, Associate), direct brand lead capture & VIP pass flows.
                    </div>
                  </div>
                </div>
                <div className="flex items-center justify-between pt-2 border-t border-amber-500/20">
                  <span className="text-xs text-amber-300/80">
                    Transforming how heritage committees present themselves to visitors and brand sponsors.
                  </span>
                  <Link
                    href="/solutions/durga-puja"
                    className="text-xs font-semibold text-amber-300 hover:text-amber-100 flex items-center gap-1 shrink-0"
                  >
                    <span>View dedicated Durga Puja hub</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </section>
"""
home_code += """
        {/* 3. STRATEGIC SHOWCASE: DURGA PUJA DIGITAL HUB */}
        <section className="py-20 lg:py-28 relative overflow-hidden bg-gradient-to-b from-[#0B0A08] to-[#080C14] border-b border-amber-950/40">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div className="p-8 sm:p-12 lg:p-16 rounded-3xl bg-gradient-to-br from-[#1A140E] to-[#120F0A] border border-amber-500/30 shadow-2xl relative overflow-hidden">
              <div className="absolute top-0 right-0 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />

              <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
                <div className="lg:col-span-7 space-y-6">
                  <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-500/30 text-amber-300 text-xs font-mono">
                    <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                    <span>Specialized Cultural Engineering</span>
                  </div>

                  <h2 className="text-2xl sm:text-4xl font-display font-bold text-amber-100 tracking-tight leading-tight">
                    A digital presence for your Puja, <br />
                    <span className="text-gradient-gold">built around your committee's real needs.</span>
                  </h2>

                  <p className="text-slate-300 text-sm sm:text-base leading-relaxed">
                    Durga Puja is Bengal’s greatest festival of public art and heritage. We design authoritative digital hubs that dignify your theme, guide 50,000+ daily visitors effortlessly, and provide corporate brand managers with clean, structured sponsorship proposals.
                  </p>

                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                    {durgaPujaFeatures.slice(0, 4).map((feat) => (
                      <div key={feat.id} className="flex items-start gap-2.5 text-xs text-slate-300 bg-black/40 p-3 rounded-lg border border-amber-500/20">
                        <CheckCircle2 className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
                        <div>
                          <div className="font-semibold text-amber-200">{feat.title}</div>
                          <div className="text-slate-400 text-[11px] mt-0.5">{feat.description.slice(0, 75)}...</div>
                        </div>
                      </div>
                    ))}
                  </div>

                  <div className="flex flex-col sm:flex-row items-center gap-4 pt-4">
                    <Link
                      href="/solutions/durga-puja"
                      className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 bg-amber-500 hover:bg-amber-400 text-slate-950 font-semibold text-xs uppercase tracking-wider rounded-xl shadow-glow-gold transition-all"
                    >
                      <span>Explore Puja Solution Platform</span>
                      <ArrowRight className="w-4 h-4" />
                    </Link>

                    <button
                      onClick={() => handleOpenConsultation('Durga Puja Committee')}
                      className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-3 bg-slate-900/80 hover:bg-slate-800 text-amber-300 border border-amber-500/30 text-xs font-semibold uppercase tracking-wider rounded-xl transition-colors"
                    >
                      <span>Discuss Your Puja Digital Needs</span>
                    </button>
                  </div>
                </div>

                <div className="lg:col-span-5 rounded-2xl bg-black/80 border border-amber-500/30 p-5 space-y-4 shadow-xl">
                  <div className="flex items-center justify-between pb-3 border-b border-amber-500/20 text-xs text-amber-400/80 font-mono">
                    <span>puja-hub-preview.ts</span>
                    <span className="text-[10px] bg-amber-500/20 text-amber-300 px-2 py-0.5 rounded">Live Blueprint</span>
                  </div>

                  <div className="space-y-3">
                    <div className="p-3.5 rounded-lg bg-amber-950/30 border border-amber-500/20">
                      <div className="text-[10px] font-mono uppercase text-amber-400">Festival Day Indicator</div>
                      <div className="text-sm font-bold text-amber-100 mt-0.5">Maha Saptami (মহা সপ্তমী) • Live</div>
                      <div className="text-[11px] text-slate-400 mt-1">Pushpanjali: 9:30 AM • Bhog Distribution: 1:00 PM</div>
                    </div>

                    <div className="p-3.5 rounded-lg bg-slate-900/80 border border-slate-800">
                      <div className="text-[10px] font-mono uppercase text-brand-cyan">Visitor Route Finder</div>
                      <div className="text-xs text-slate-200 mt-0.5">Nearest Metro: Kalighat / Netaji Bhavan (4 min walk)</div>
                      <div className="text-[11px] text-slate-400 mt-1">Designated VIP & Senior Citizen Gate: Gate 2</div>
                    </div>

                    <div className="p-3.5 rounded-lg bg-slate-900/80 border border-slate-800">
                      <div className="text-[10px] font-mono uppercase text-emerald-400">Corporate Sponsorship Deck</div>
                      <div className="text-xs text-slate-200 mt-0.5">Title, Co-Powered & Food Zone Tiers available</div>
                      <div className="text-[11px] text-emerald-300/80 mt-1">Instant digital PDF proposal + direct secretary hotline</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 4. REALISTIC DEMONSTRATION PROJECTS */}
        <section className="py-20 lg:py-28 bg-[#080C14] border-b border-slate-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="flex flex-col md:flex-row md:items-end justify-between mb-14 gap-6">
              <div className="max-w-2xl">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono mb-3">
                  <Cpu className="w-3.5 h-3.5" />
                  <span>Demonstration Architecture</span>
                </div>
                <h2 className="text-2xl sm:text-4xl font-display font-bold text-slate-100 tracking-tight">
                  Proof of Capability Through Craft
                </h2>
                <p className="mt-3 text-slate-400 text-sm sm:text-base leading-relaxed">
                  We don't invent fictional client logos or fake 5-star testimonials. Instead, we demonstrate our architectural depth through these fully designed, realistic technical prototypes.
                </p>
              </div>

              <Link
                href="/work"
                className="inline-flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-brand-cyan hover:text-sky-300 font-semibold"
              >
                <span>View Full Architecture Showcase</span>
                <ArrowRight className="w-4 h-4" />
              </Link>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {demonstrationProjects.map((project) => (
                <div
                  key={project.id}
                  className="glass-card rounded-2xl p-6 border border-slate-800 flex flex-col justify-between hover:border-brand-cyan/40 transition-all duration-300 group"
                >
                  <div className="space-y-4">
                    <div className="flex items-center justify-between">
                      <span className="px-2.5 py-0.5 rounded text-[10px] font-mono uppercase tracking-wider bg-slate-800 text-slate-300 border border-slate-700">
                        {project.clientType}
                      </span>
                      <span className="text-[10px] font-mono text-brand-cyan">Concept Prototype</span>
                    </div>

                    <div>
                      <h3 className="text-lg font-bold text-slate-100 group-hover:text-brand-cyan transition-colors">
                        {project.title}
                      </h3>
                      <p className="text-xs text-slate-400 mt-2 leading-relaxed line-clamp-3">
                        {project.summary}
                      </p>
                    </div>

                    <div className="p-3 rounded-lg bg-slate-950/60 border border-slate-800/80 space-y-1">
                      <div className="text-[10px] font-mono uppercase text-slate-500">Core Problem Solved:</div>
                      <div className="text-xs text-slate-300 line-clamp-2">
                        {project.operationalChallenge}
                      </div>
                    </div>

                    <div className="flex flex-wrap gap-1.5 pt-1">
                      {project.architectureStack.slice(0, 3).map((tech, i) => (
                        <span key={i} className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-900 text-slate-400 border border-slate-800">
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>

                  <div className="pt-6 mt-6 border-t border-slate-800/80 flex items-center justify-between">
                    <button
                      onClick={() => setSelectedDemonstration(project)}
                      className="text-xs font-semibold text-brand-cyan hover:text-sky-300 flex items-center gap-1.5"
                    >
                      <span>Inspect Architecture</span>
                      <ArrowUpRight className="w-3.5 h-3.5" />
                    </button>
                    <span className="text-[11px] text-slate-500 font-mono">100% WCAG AA</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* 5. INTERACTIVE PROJECT CONSULTATION PLANNER */}
        <ProjectConsultationSection onOpenConsultation={handleOpenConsultation} />

        {/* 6. HOW WE WORK: THE 4-STEP CRAFT PROCESS */}
        <section className="py-20 lg:py-28 bg-slate-950 border-b border-slate-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center max-w-3xl mx-auto mb-16">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono mb-3">
                <ShieldCheck className="w-3.5 h-3.5" />
                <span>The Engineering Process</span>
              </div>
              <h2 className="text-2xl sm:text-4xl font-display font-bold text-slate-100 tracking-tight">
                How We Deliver Without Friction
              </h2>
              <p className="mt-3 text-slate-400 text-sm sm:text-base leading-relaxed">
                Clear milestones, direct technical communication, and zero bloated agency overhead.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
              {[
                {
                  step: '01',
                  title: 'Operational Discovery',
                  desc: 'We analyze how your clinic, tutorial, or business actually operates before suggesting a single line of code.',
                },
                {
                  step: '02',
                  title: 'Intentional Design',
                  desc: 'We craft high-contrast typography, clear visual hierarchy, and intuitive information architecture.',
                },
                {
                  step: '03',
                  title: 'Precision Engineering',
                  desc: 'We write clean, strongly typed code optimized for sub-second mobile loads, SEO, and accessibility.',
                },
                {
                  step: '04',
                  title: '100% Ownership Delivery',
                  desc: 'You receive all code and assets with no ongoing mandatory builder subscriptions or lock-in.',
                },
              ].map((item, i) => (
                <div key={i} className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 relative space-y-3">
                  <div className="text-2xl font-mono font-bold text-slate-600">{item.step}</div>
                  <h3 className="text-base font-bold text-slate-100">{item.title}</h3>
                  <p className="text-xs text-slate-400 leading-relaxed">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* 7. TRANSPARENT PRICING & SCOPING PHILOSOPHY */}
        <section className="py-20 bg-[#080C14] border-b border-slate-800">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="max-w-3xl mx-auto text-center space-y-4 mb-12">
              <h2 className="text-2xl sm:text-3xl font-display font-bold text-slate-100">
                Transparent Scoping, Honest Commercials
              </h2>
              <p className="text-slate-400 text-sm leading-relaxed">
                We do not position ourselves as a bargain website marketplace. We price transparently based on project deliverables, giving you enterprise-grade engineering at small studio rates.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
              <div className="p-6 sm:p-8 rounded-2xl bg-slate-900/70 border border-slate-800 space-y-4">
                <div className="text-xs font-mono uppercase text-brand-cyan font-semibold">Websites</div>
                <h3 className="text-xl font-bold text-slate-100">One-Time Project Scoping</h3>
                <p className="text-xs text-slate-400 leading-relaxed">
                  Fixed project investment with complete source code ownership. Includes bespoke layout, mobile responsive testing, SEO foundations, and domain deployment.
                </p>
                <ul className="space-y-2 text-xs text-slate-300 pt-2">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                    <span>Transparent fixed project scope</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                    <span>No monthly page builder fees</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-brand-cyan shrink-0" />
                    <span>Sub-second page speeds guaranteed</span>
                  </li>
                </ul>
              </div>

              <div className="p-6 sm:p-8 rounded-2xl bg-slate-900/70 border border-slate-800 space-y-4">
                <div className="text-xs font-mono uppercase text-emerald-400 font-semibold">Custom Solutions</div>
                <h3 className="text-xl font-bold text-slate-100">Requirement-Based Scoping</h3>
                <p className="text-xs text-slate-400 leading-relaxed">
                  For appointment systems, student inquiry tools, and Durga Puja platforms, we scope according to exact functionality, database needs, and integration complexity.
                </p>
                <ul className="space-y-2 text-xs text-slate-300 pt-2">
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                    <span>Built specifically around your workflow</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                    <span>Direct WhatsApp & webhook routing</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                    <span>Optional ongoing maintenance & support</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* 8. CONVERSION CALL TO ACTION */}
        <section className="py-20 lg:py-28 relative overflow-hidden bg-slate-950">
          <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6 relative z-10">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Direct Studio Access</span>
            </div>

            <h2 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight text-balance">
              Let's talk about what you need to build.
            </h2>

            <p className="text-slate-400 text-sm sm:text-base max-w-xl mx-auto leading-relaxed">
              No sales pitches, no pushy follow-ups. Speak directly with a technical specialist to discuss your requirement, timeline, and options.
            </p>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
              <button
                onClick={() => handleOpenConsultation()}
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-3.5 bg-brand-cyan hover:bg-sky-300 active:bg-sky-400 text-slate-950 font-semibold text-sm rounded-xl shadow-glow-cyan transition-all"
              >
                <span>Start a Project Conversation</span>
                <ArrowRight className="w-4 h-4" />
              </button>

              <a
                href={siteConfig.contact.whatsappLink}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-7 py-3.5 bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-semibold text-sm rounded-xl transition-colors"
              >
                <MessageCircle className="w-4 h-4" />
                <span>Chat on WhatsApp</span>
              </a>
            </div>

            <div className="pt-6 text-xs text-slate-500 font-mono">
              Typically responding within 12 business hours • Kolkata, India
            </div>
          </div>
        </section>
      </main>

      <Footer />

      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
        initialCategory={consultationCategory}
      />

      <DemonstrationModal
        project={selectedDemonstration}
        onClose={() => setSelectedDemonstration(null)}
        onOpenConsultation={() => handleOpenConsultation(selectedDemonstration?.clientType)}
      />
    </>
  );
}
"""

write_file('src/app/page.tsx', home_code)
solutions_page_code = """'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
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
  ArrowRight,
  Sparkles,
  CheckCircle2,
  Layers,
  Clock,
  ShieldCheck,
  Filter,
} from 'lucide-react';

export default function SolutionsPage() {
  const [activeCategory, setActiveCategory] = useState<'all' | 'website' | 'custom-solution' | 'specialized'>('all');
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);
  const [consultationCategory, setConsultationCategory] = useState<string | undefined>();

  const filteredSolutions = activeCategory === 'all'
    ? solutionsData
    : solutionsData.filter(s => s.category === activeCategory);

  const getIcon = (name: string) => {
    switch (name) {
      case 'Globe': return <Globe className="w-5 h-5 text-brand-cyan" />;
      case 'Stethoscope': return <Stethoscope className="w-5 h-5 text-sky-400" />;
      case 'GraduationCap': return <GraduationCap className="w-5 h-5 text-indigo-400" />;
      case 'CalendarCheck': return <CalendarCheck className="w-5 h-5 text-emerald-400" />;
      case 'Users': return <Users className="w-5 h-5 text-purple-400" />;
      case 'Flame': return <Flame className="w-5 h-5 text-amber-400" />;
      case 'Cpu': return <Cpu className="w-5 h-5 text-teal-400" />;
      default: return <Sparkles className="w-5 h-5 text-brand-cyan" />;
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
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-12">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono mb-4">
              <Layers className="w-3.5 h-3.5" />
              <span>Studio Solutions Directory</span>
            </div>
            <h1 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight leading-tight">
              Crafted Websites & <br />
              <span className="text-gradient-cyan">Bespoke Technical Systems</span>
            </h1>
            <p className="mt-4 text-slate-300 text-base sm:text-lg leading-relaxed">
              We organize our capabilities around real problems, not technical jargon. Browse our standard website solutions and custom operational tools below.
            </p>
          </div>

          {/* Filter Pills */}
          <div className="flex flex-wrap gap-2 pt-8 border-t border-slate-800/80 mt-8">
            {[
              { id: 'all', label: 'All Capabilities' },
              { id: 'website', label: 'High-Performance Websites' },
              { id: 'custom-solution', label: 'Custom Technical Tools' },
              { id: 'specialized', label: 'Durga Puja Platform' },
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveCategory(tab.id as any)}
                className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-medium transition-all ${
                  activeCategory === tab.id
                    ? 'bg-slate-800 text-slate-100 border border-brand-cyan shadow-glow-cyan'
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
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {filteredSolutions.map((sol) => (
              <div
                key={sol.id}
                id={sol.id}
                className={`rounded-2xl p-6 sm:p-8 border transition-all duration-300 flex flex-col justify-between ${
                  sol.category === 'specialized'
                    ? 'puja-card border-amber-500/30'
                    : 'glass-card border-slate-800 hover:border-brand-cyan/40'
                }`}
              >
                <div className="space-y-6">
                  {/* Top Badge & Header */}
                  <div className="flex items-start justify-between gap-4">
                    <div className="flex items-center gap-3">
                      <div className="p-2.5 rounded-xl bg-slate-900 border border-slate-800">
                        {getIcon(sol.iconName)}
                      </div>
                      <div>
                        <span className="text-[11px] font-mono uppercase tracking-wider text-slate-400">
                          {sol.category === 'website'
                            ? 'Website Solution'
                            : sol.category === 'specialized'
                            ? 'Specialized Platform'
                            : 'Custom Operational System'}
                        </span>
                        <h2 className="text-xl sm:text-2xl font-bold text-slate-100 mt-0.5">
                          {sol.title}
                        </h2>
                      </div>
                    </div>
                  </div>

                  <p className="text-sm text-slate-300 leading-relaxed">
                    {sol.description}
                  </p>

                  {/* Target Audience Pills */}
                  <div className="space-y-1.5">
                    <div className="text-[11px] font-mono uppercase text-slate-500">Tailored For:</div>
                    <div className="flex flex-wrap gap-1.5">
                      {sol.audience.map((aud, i) => (
                        <span key={i} className="px-2.5 py-1 rounded bg-slate-900/80 border border-slate-800 text-xs text-slate-300 font-medium">
                          {aud}
                        </span>
                      ))}
                    </div>
                  </div>

                  {/* Key Features List */}
                  <div className="space-y-2">
                    <div className="text-[11px] font-mono uppercase text-slate-500">Key Capabilities:</div>
                    <div className="space-y-2">
                      {sol.keyFeatures.map((feat, i) => (
                        <div key={i} className="flex items-start gap-2 text-xs text-slate-300">
                          <CheckCircle2 className={`w-4 h-4 shrink-0 mt-0.5 ${
                            sol.category === 'specialized' ? 'text-amber-400' : 'text-brand-cyan'
                          }`} />
                          <span>{feat}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Technical Scope Box */}
                  <div className="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 space-y-1">
                    <div className="text-[10px] font-mono uppercase text-brand-cyan font-semibold">Technical Architecture:</div>
                    <p className="text-xs text-slate-400 leading-relaxed">
                      {sol.technicalScope}
                    </p>
                  </div>
                </div>

                {/* Card Footer */}
                <div className="pt-6 mt-6 border-t border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                  <div className="flex items-center gap-4 text-xs font-mono text-slate-400">
                    <div className="flex items-center gap-1.5">
                      <Clock className="w-3.5 h-3.5 text-brand-cyan" />
                      <span>{sol.timeline}</span>
                    </div>
                    <span>•</span>
                    <span className="text-slate-300 font-semibold">
                      {sol.pricingType === 'fixed-project' ? 'Fixed Project Investment' : 'Scope-Based Quote'}
                    </span>
                  </div>

                  <div className="flex items-center gap-2">
                    {sol.id === 'durga-puja-digital-hub' ? (
                      <Link
                        href="/solutions/durga-puja"
                        className="w-full sm:w-auto inline-flex items-center justify-center gap-1.5 px-4 py-2 bg-amber-500 hover:bg-amber-400 text-slate-950 text-xs font-semibold uppercase tracking-wider rounded-lg shadow-glow-gold transition-all"
                      >
                        <span>View Puja Showcase</span>
                        <ArrowRight className="w-3.5 h-3.5" />
                      </Link>
                    ) : (
                      <button
                        onClick={() => handleOpenConsultation(sol.title)}
                        className="w-full sm:w-auto inline-flex items-center justify-center gap-1.5 px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-100 text-xs font-semibold uppercase tracking-wider rounded-lg border border-slate-700 transition-colors"
                      >
                        <span>Discuss Scope</span>
                        <ArrowRight className="w-3.5 h-3.5 text-brand-cyan" />
                      </button>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Philosophy Callout Banner */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-20">
          <div className="p-8 sm:p-10 rounded-2xl bg-slate-950 border border-slate-800 text-center max-w-3xl mx-auto space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono">
              <ShieldCheck className="w-3.5 h-3.5" />
              <span>Direct Studio Guarantee</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-bold text-slate-100">
              Not sure which technical tier fits your needs?
            </h3>
            <p className="text-slate-400 text-sm leading-relaxed">
              You don’t need to know what technology stack or database to choose. Tell us your day-to-day operational pain points and we will advise you honestly.
            </p>
            <div className="pt-2">
              <button
                onClick={() => handleOpenConsultation()}
                className="inline-flex items-center gap-2 px-6 py-3 bg-brand-cyan hover:bg-sky-300 text-slate-950 text-xs font-semibold uppercase tracking-wider rounded-lg shadow-glow-cyan transition-all"
              >
                <span>Book a Technical Discovery Chat</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
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
"""

write_file('src/app/solutions/page.tsx', solutions_page_code)
durga_puja_page_code = """'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
import { durgaPujaFeatures, sampleSponsorTiers } from '@/data/durgaPuja';
import { siteConfig } from '@/config/site';
import {
  Flame,
  Calendar,
  Award,
  MapPin,
  Image,
  CreditCard,
  PhoneCall,
  Sparkles,
  ArrowRight,
  CheckCircle2,
  Download,
  MessageCircle,
  Clock,
  ShieldCheck,
  Building2,
  Users,
} from 'lucide-react';

export default function DurgaPujaPage() {
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);
  const [activeDay, setActiveDay] = useState<'sasthi' | 'saptami' | 'astami' | 'nabami' | 'dashami'>('astami');
  const [selectedTier, setSelectedTier] = useState<string>('Title Sponsor');

  const ritualSchedule = {
    sasthi: {
      day: 'Maha Sasthi (মহা ষষ্ঠী)',
      date: 'Day 1 of Sharodotsav',
      events: [
        { time: '07:30 AM', title: 'Bodhon & Amontron (বোধন ও আমন্ত্রণ)' },
        { time: '09:30 AM', title: 'Adhibas & Kalparambha' },
        { time: '06:30 PM', title: 'Official Pandal Theme Inauguration by Chief Guest' },
        { time: '08:00 PM', title: 'Dhaak Recital & Lighting Showcase' }
      ]
    },
    saptami: {
      day: 'Maha Saptami (মহা সপ্তমী)',
      date: 'Day 2 of Sharodotsav',
      events: [
        { time: '06:00 AM', title: 'Kola Bou Snan & Nabapatrika Prabesh (নবপত্রিকা প্রবেশ)' },
        { time: '09:30 AM', title: 'Saptami Morning Pushpanjali' },
        { time: '01:00 PM', title: 'Maha Bhog Distribution for Devotees' },
        { time: '07:30 PM', title: 'Evening Sandhya Arati & Dhunuchi Dance' }
      ]
    },
    astami: {
      day: 'Maha Astami & Sandhi Puja (মহা অষ্টমী ও সন্ধিপূজা)',
      date: 'Day 3 (Peak Devotion & Crowds)',
      events: [
        { time: '08:30 AM', title: 'Maha Astami Pushpanjali (Batches 1 – 4)' },
        { time: '11:00 AM', title: 'Kumari Puja (কুমারী পূজা)' },
        { time: '05:42 PM', title: 'Sacred Sandhi Puja (১০৮ প্রদীপ ও পদ্ম অর্পণ)' },
        { time: '08:00 PM', title: 'Special Evening Bhog & Cultural Classical Concert' }
      ]
    },
    nabami: {
      day: 'Maha Nabami (মহা নবমী)',
      date: 'Day 4 of Sharodotsav',
      events: [
        { time: '09:00 AM', title: 'Maha Nabami Puja & Hom/Yajna (যজ্ঞ)' },
        { time: '11:30 AM', title: 'Final Pushpanjali Session' },
        { time: '01:00 PM', title: 'Community Mahaprasad Feast' },
        { time: '08:30 PM', title: 'Mega Musical Night & Sponsor Recognition Ceremony' }
      ]
    },
    dashami: {
      day: 'Bijoya Dashami (বিজয়া দশমী)',
      date: 'Day 5 (Aparajita Puja & Immersion)',
      events: [
        { time: '08:30 AM', title: 'Dashami Puja & Darpan Bisorjon (দর্পণ বিসর্জন)' },
        { time: '10:30 AM', title: 'Devi Boron & Sindoor Khela (সিঁদুর খেলা)' },
        { time: '04:00 PM', title: 'Shobhayatra & Ghat Immersion Procession' },
        { time: '07:30 PM', title: 'Subho Bijoya Greetings & Sweet Distribution' }
      ]
    }
  };

  const getFeatureIcon = (name: string) => {
    switch (name) {
      case 'Calendar': return <Calendar className="w-5 h-5 text-amber-400" />;
      case 'Award': return <Award className="w-5 h-5 text-amber-400" />;
      case 'MapPin': return <MapPin className="w-5 h-5 text-amber-400" />;
      case 'Image': return <Image className="w-5 h-5 text-amber-400" />;
      case 'CreditCard': return <CreditCard className="w-5 h-5 text-amber-400" />;
      case 'PhoneCall': return <PhoneCall className="w-5 h-5 text-amber-400" />;
      default: return <Flame className="w-5 h-5 text-amber-400" />;
    }
  };

  return (
    <>
      <Header onOpenConsultation={() => setIsConsultationOpen(true)} />

      <main id="main-content" className="flex-1 pt-32 pb-24 bg-[#080705]">
        {/* Hero Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16 lg:mb-24 relative">
          <div className="p-8 sm:p-12 lg:p-16 rounded-3xl bg-gradient-to-br from-[#1C140A] via-[#140E06] to-[#0A0704] border border-amber-500/30 shadow-2xl relative overflow-hidden">
            <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-amber-500/10 rounded-full blur-[140px] pointer-events-none" />

            <div className="max-w-3xl space-y-6 relative z-10">
              <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-amber-500/15 border border-amber-500/40 text-amber-300 text-xs font-mono">
                <Flame className="w-3.5 h-3.5 text-amber-400" />
                <span>Sharodotsav 2026 Special Solution</span>
              </div>

              <h1 className="text-3xl sm:text-5xl lg:text-6xl font-display font-extrabold text-amber-100 tracking-tight leading-[1.15]">
                A dignified digital home for your <br />
                <span className="text-gradient-gold">Durga Puja & Cultural Committee.</span>
              </h1>

              <p className="text-amber-200/80 text-base sm:text-lg leading-relaxed">
                Durga Puja in Kolkata is an extraordinary cultural celebration of monumental public art, community devotion, and corporate engagement. Techzyan engineers specialized digital platforms that honor your theme, guide thousands of daily visitors, and attract premier corporate brand sponsors.
              </p>

              <div className="flex flex-col sm:flex-row items-center gap-4 pt-4">
                <button
                  onClick={() => setIsConsultationOpen(true)}
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-2.5 px-7 py-3.5 bg-amber-500 hover:bg-amber-400 active:bg-amber-600 text-slate-950 font-semibold text-xs uppercase tracking-wider rounded-xl shadow-glow-gold transition-all"
                >
                  <span>Discuss Your Puja Digital Plan</span>
                  <ArrowRight className="w-4 h-4" />
                </button>

                <a
                  href={`${siteConfig.contact.whatsappLink}&text=${encodeURIComponent("Hi Techzyan! We are from a Durga Puja Committee in Kolkata and would like to discuss a digital hub and sponsorship platform.")}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3.5 bg-slate-900/90 hover:bg-slate-800 text-amber-300 border border-amber-500/30 font-semibold text-xs uppercase tracking-wider rounded-xl transition-colors"
                >
                  <MessageCircle className="w-4 h-4 text-emerald-400" />
                  <span>WhatsApp Committee Lead</span>
                </a>
              </div>
            </div>
          </div>
        </section>

        {/* 6 Core Pillars of Techzyan Puja Platform */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20 lg:mb-28">
          <div className="text-center max-w-3xl mx-auto mb-14">
            <h2 className="text-2xl sm:text-4xl font-display font-bold text-amber-100 tracking-tight">
              Everything Your Committee Needs in One Elegant Platform
            </h2>
            <p className="mt-3 text-slate-400 text-sm sm:text-base leading-relaxed">
              Engineered with extreme reliability to withstand massive mobile traffic spikes during festival week without crashing.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {durgaPujaFeatures.map((feat) => (
              <div
                key={feat.id}
                className="puja-card rounded-2xl p-6 border border-amber-500/25 space-y-4 hover:border-amber-500/50 transition-all duration-300"
              >
                <div className="flex items-center justify-between">
                  <div className="p-2.5 rounded-xl bg-amber-950/40 border border-amber-500/30">
                    {getFeatureIcon(feat.iconName)}
                  </div>
                  {feat.bengaliTitle && (
                    <span className="text-xs text-amber-400/80 font-serif">
                      {feat.bengaliTitle}
                    </span>
                  )}
                </div>

                <div>
                  <h3 className="text-lg font-bold text-amber-100">{feat.title}</h3>
                  <p className="text-xs text-slate-300 mt-2 leading-relaxed">{feat.description}</p>
                </div>

                <div className="pt-2 space-y-1.5 border-t border-amber-500/15">
                  {feat.details.map((item, i) => (
                    <div key={i} className="flex items-start gap-2 text-xs text-slate-400">
                      <CheckCircle2 className="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5" />
                      <span>{item}</span>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Interactive Feature 1: 5-Day Ritual & Schedule Simulator */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20 lg:mb-28">
          <div className="p-8 sm:p-12 rounded-3xl bg-[#110D08] border border-amber-500/30 space-y-8">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-amber-500/20">
              <div>
                <div className="inline-flex items-center gap-1.5 text-xs font-mono uppercase tracking-wider text-amber-400 mb-1 font-semibold">
                  <Calendar className="w-3.5 h-3.5" />
                  <span>Interactive Component Preview</span>
                </div>
                <h3 className="text-xl sm:text-3xl font-bold text-amber-100">
                  5-Day Interactive Puja Schedule Engine
                </h3>
              </div>
              <div className="text-xs text-slate-400 max-w-xs">
                Visitors can easily check accurate Pushpanjali, Sandhi Puja, and Bhog timings from their smartphones.
              </div>
            </div>

            {/* Day Selector Tabs */}
            <div className="flex flex-wrap gap-2">
              {(Object.keys(ritualSchedule) as Array<keyof typeof ritualSchedule>).map((key) => {
                const isSelected = activeDay === key;
                return (
                  <button
                    key={key}
                    onClick={() => setActiveDay(key)}
                    className={`px-4 py-2 rounded-xl text-xs sm:text-sm font-medium transition-all ${
                      isSelected
                        ? 'bg-amber-500 text-slate-950 font-bold shadow-glow-gold'
                        : 'bg-black/60 text-amber-300/70 border border-amber-500/20 hover:text-amber-200'
                    }`}
                  >
                    {ritualSchedule[key].day.split('(')[0]}
                  </button>
                );
              })}
            </div>

            {/* Day Details Box */}
            <div className="p-6 rounded-2xl bg-black/60 border border-amber-500/20 space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="text-lg font-bold text-amber-200">{ritualSchedule[activeDay].day}</h4>
                  <p className="text-xs text-slate-400">{ritualSchedule[activeDay].date}</p>
                </div>
                <span className="px-3 py-1 rounded-full text-xs font-mono bg-amber-500/20 text-amber-300 border border-amber-500/30">
                  Verified Timetable
                </span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                {ritualSchedule[activeDay].events.map((evt, i) => (
                  <div key={i} className="p-3.5 rounded-xl bg-[#1A140C] border border-amber-500/15 flex items-start gap-3">
                    <span className="px-2 py-1 rounded bg-black/60 border border-amber-500/30 font-mono text-xs text-amber-400 font-bold shrink-0">
                      {evt.time}
                    </span>
                    <div className="text-xs font-medium text-slate-200 mt-0.5">
                      {evt.title}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Interactive Feature 2: Corporate Sponsorship Presentation Suite */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20 lg:mb-28">
          <div className="text-center max-w-3xl mx-auto mb-12">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-500/30 text-amber-300 text-xs font-mono mb-3">
              <Award className="w-3.5 h-3.5" />
              <span>Attract Premium Brand Partners</span>
            </div>
            <h2 className="text-2xl sm:text-4xl font-display font-bold text-amber-100 tracking-tight">
              Present Corporate Sponsorship Tiers with Authority
            </h2>
            <p className="mt-3 text-slate-400 text-sm sm:text-base leading-relaxed">
              Replace messy paper brochures with a digital sponsorship proposal page that brand marketing managers can review on their phones.
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {sampleSponsorTiers.map((tier) => {
              const isSelected = selectedTier === tier.name;
              return (
                <div
                  key={tier.name}
                  onClick={() => setSelectedTier(tier.name)}
                  className={`rounded-2xl p-6 sm:p-8 border cursor-pointer transition-all duration-300 flex flex-col justify-between ${
                    tier.featuredPlacement
                      ? 'bg-gradient-to-b from-[#22190E] to-[#140E06] border-amber-400 shadow-glow-gold'
                      : 'bg-[#110D08] border-amber-500/25 hover:border-amber-500/50'
                  }`}
                >
                  <div className="space-y-4">
                    <div className="flex items-center justify-between">
                      <span className="text-xs font-mono uppercase text-amber-400 font-semibold">
                        Sponsorship Tier
                      </span>
                      {tier.featuredPlacement && (
                        <span className="px-2 py-0.5 rounded text-[10px] font-mono bg-amber-400 text-slate-950 font-bold uppercase">
                          Premier Tier
                        </span>
                      )}
                    </div>

                    <div>
                      <h3 className="text-xl font-bold text-amber-100">{tier.name}</h3>
                      <p className="text-xs text-amber-200/80 mt-1">{tier.tagline}</p>
                    </div>

                    <div className="p-2.5 rounded-lg bg-black/40 border border-amber-500/20 text-xs text-slate-400">
                      <span className="text-amber-300 font-medium">Ideal For:</span> {tier.recommendedFor}
                    </div>

                    <div className="space-y-2 pt-2">
                      <div className="text-[11px] font-mono uppercase text-amber-400/80">Digital & Physical Deliverables:</div>
                      {tier.digitalPerks.map((perk, i) => (
                        <div key={i} className="flex items-start gap-2 text-xs text-slate-300">
                          <CheckCircle2 className="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5" />
                          <span>{perk}</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div className="pt-6 mt-6 border-t border-amber-500/20">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        setIsConsultationOpen(true);
                      }}
                      className={`w-full py-2.5 px-4 rounded-xl text-xs font-semibold uppercase tracking-wider transition-all ${
                        tier.featuredPlacement
                          ? 'bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-md'
                          : 'bg-black/60 hover:bg-amber-950/60 text-amber-300 border border-amber-500/30'
                      }`}
                    >
                      Request Proposal Template
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </section>

        {/* Call To Action Banner */}
        <section className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-6">
          <div className="p-8 sm:p-12 rounded-3xl bg-gradient-to-r from-[#1C140A] via-[#161008] to-[#1C140A] border border-amber-500/40 shadow-2xl space-y-6">
            <h3 className="text-2xl sm:text-4xl font-display font-bold text-amber-100">
              Ready to elevate your Puja's digital presence?
            </h3>
            <p className="text-slate-300 text-sm sm:text-base max-w-xl mx-auto leading-relaxed">
              We work with select committees in North, South, and Central Kolkata. Let’s discuss your pandal concept, schedule, and sponsor strategy.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-2">
              <button
                onClick={() => setIsConsultationOpen(true)}
                className="w-full sm:w-auto px-8 py-3.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-gold transition-all"
              >
                Schedule Committee Discussion
              </button>
              <a
                href={`${siteConfig.contact.whatsappLink}&text=${encodeURIComponent("Hi Techzyan! We would like to consult with you regarding our Durga Puja 2026 digital portal.")}`}
                target="_blank"
                rel="noopener noreferrer"
                className="w-full sm:w-auto px-6 py-3.5 bg-black/60 hover:bg-black/80 text-amber-300 border border-amber-500/40 text-xs font-bold uppercase tracking-wider rounded-xl transition-colors flex items-center justify-center gap-2"
              >
                <MessageCircle className="w-4 h-4 text-emerald-400" />
                <span>Instant WhatsApp Query</span>
              </a>
            </div>
          </div>
        </section>
      </main>

      <Footer />

      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
        initialCategory="Durga Puja Committee"
      />
    </>
  );
}
"""

write_file('src/app/solutions/durga-puja/page.tsx', durga_puja_page_code)
who_we_help_page_code = """'use client';

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
  MessageCircle,
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
"""

write_file('src/app/who-we-help/page.tsx', who_we_help_page_code)
work_page_code = """'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import DemonstrationModal from '@/components/DemonstrationModal';
import ConsultationModal from '@/components/ConsultationModal';
import { demonstrationProjects } from '@/data/demonstrations';
import { DemonstrationProject } from '@/types';
import {
  Cpu,
  ArrowRight,
  Sparkles,
  ShieldCheck,
  CheckCircle2,
  ExternalLink,
  Layers,
  ArrowUpRight,
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
        {/* Header */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-12">
          <div className="max-w-3xl space-y-4">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono">
              <Cpu className="w-3.5 h-3.5" />
              <span>Architectural Showcase</span>
            </div>
            <h1 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight leading-tight">
              Demonstration Concepts & <br />
              <span className="text-gradient-cyan">Engineered Solutions</span>
            </h1>
            <p className="text-slate-300 text-base sm:text-lg leading-relaxed">
              We do not fabricate fake clients, awards, or inflated review counts. Instead, we showcase our engineering standards and design sensibility through fully articulated concept architectures.
            </p>
          </div>

          {/* Ethics Banner */}
          <div className="mt-8 p-4 rounded-xl bg-slate-900/80 border border-slate-800 flex items-start gap-3 max-w-2xl text-xs text-slate-300">
            <ShieldCheck className="w-5 h-5 text-brand-cyan shrink-0 mt-0.5" />
            <p>
              <strong>Studio Transparency Commitment:</strong> Every project shown here is an authentic technical demonstration crafted by Techzyan to illustrate how we solve real operational friction. When we complete real client engagements, they will transition here with client consent.
            </p>
          </div>

          {/* Category Filter */}
          <div className="flex flex-wrap gap-2 pt-8 mt-8 border-t border-slate-800/80">
            {[
              { id: 'all', label: 'All Demonstration Projects' },
              { id: 'healthcare', label: 'Healthcare & Clinic' },
              { id: 'education', label: 'Tutors & Education' },
              { id: 'retail', label: 'Boutique & Retail' },
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

        {/* Portfolio Cards Grid */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {filteredProjects.map((project) => (
              <div
                key={project.id}
                className="glass-card rounded-2xl p-6 sm:p-8 border border-slate-800 hover:border-brand-cyan/40 transition-all duration-300 flex flex-col justify-between group"
              >
                <div className="space-y-5">
                  <div className="flex items-center justify-between">
                    <span className="px-2.5 py-0.5 rounded text-[10px] font-mono uppercase tracking-wider bg-slate-800 text-slate-300 border border-slate-700">
                      {project.clientType}
                    </span>
                    <span className="text-[10px] font-mono text-brand-cyan font-semibold">
                      Concept Prototype
                    </span>
                  </div>

                  <div>
                    <h2 className="text-xl font-bold text-slate-100 group-hover:text-brand-cyan transition-colors">
                      {project.title}
                    </h2>
                    <p className="text-xs text-slate-400 mt-2 leading-relaxed">
                      {project.summary}
                    </p>
                  </div>

                  {/* Problem / Solution Summary */}
                  <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-800/90 space-y-2 text-xs">
                    <div>
                      <span className="text-slate-500 font-mono uppercase text-[10px] block">The Operational Need:</span>
                      <p className="text-slate-300 line-clamp-2 mt-0.5">{project.operationalChallenge}</p>
                    </div>
                  </div>

                  {/* Architecture Stack */}
                  <div className="space-y-1.5">
                    <div className="text-[10px] font-mono uppercase text-slate-500">Tech Stack:</div>
                    <div className="flex flex-wrap gap-1.5">
                      {project.architectureStack.map((tech, i) => (
                        <span key={i} className="text-[10px] font-mono px-2 py-0.5 rounded bg-slate-900 text-slate-300 border border-slate-800">
                          {tech}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>

                <div className="pt-6 mt-6 border-t border-slate-800/80 flex items-center justify-between">
                  <button
                    onClick={() => setSelectedDemonstration(project)}
                    className="text-xs font-semibold text-brand-cyan hover:text-sky-300 flex items-center gap-1.5"
                  >
                    <span>Inspect Full Architecture</span>
                    <ArrowUpRight className="w-4 h-4" />
                  </button>
                  <span className="text-[11px] text-slate-500 font-mono">100% WCAG AA</span>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* CTA */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-20">
          <div className="p-8 sm:p-12 rounded-3xl bg-slate-950 border border-slate-800 text-center max-w-3xl mx-auto space-y-4">
            <h3 className="text-2xl sm:text-3xl font-display font-bold text-slate-100">
              Want a solution designed with this level of craft?
            </h3>
            <p className="text-slate-400 text-sm leading-relaxed">
              Every project we take on receives this same rigor in UX architecture, mobile performance, and visual polish.
            </p>
            <div className="pt-2">
              <button
                onClick={() => setIsConsultationOpen(true)}
                className="inline-flex items-center gap-2 px-6 py-3 bg-brand-cyan hover:bg-sky-300 text-slate-950 font-semibold text-xs uppercase tracking-wider rounded-lg shadow-glow-cyan transition-all"
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
about_page_code = """'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
import { siteConfig } from '@/config/site';
import {
  ShieldCheck,
  Sparkles,
  MapPin,
  CheckCircle2,
  ArrowRight,
  Code2,
  Compass,
  HeartHandshake,
  Cpu,
} from 'lucide-react';

export default function AboutPage() {
  const [isConsultationOpen, setIsConsultationOpen] = useState(false);

  return (
    <>
      <Header onOpenConsultation={() => setIsConsultationOpen(true)} />

      <main id="main-content" className="flex-1 pt-32 pb-24">
        {/* Header */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16">
          <div className="max-w-3xl space-y-4">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono">
              <Compass className="w-3.5 h-3.5" />
              <span>Studio Philosophy & Ethos</span>
            </div>
            <h1 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight leading-tight">
              A specialist studio with <br />
              <span className="text-gradient-cyan">quiet confidence and technical craft.</span>
            </h1>
            <p className="text-slate-300 text-base sm:text-lg leading-relaxed">
              Techzyan was founded in Kolkata on a simple observation: small businesses and independent professionals do not need generic agency jargon or bloated templates. They need a capable technical partner who listens first.
            </p>
          </div>
        </section>

        {/* The Techzyan Manifesto / Core Principles */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="p-8 rounded-3xl bg-slate-900/60 border border-slate-800 space-y-4">
              <div className="w-10 h-10 rounded-xl bg-sky-500/10 border border-sky-500/30 flex items-center justify-center text-brand-cyan">
                <Compass className="w-5 h-5" />
              </div>
              <h2 className="text-xl font-bold text-slate-100">
                1. Understand the Requirement First
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                Before writing a single line of code or recommending a framework, we dissect how your practice, coaching batch, or business operations flow. We will never sell you an expensive custom application if a crisp, high-speed website is all you need.
              </p>
            </div>

            <div className="p-8 rounded-3xl bg-slate-900/60 border border-slate-800 space-y-4">
              <div className="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400">
                <Code2 className="w-5 h-5" />
              </div>
              <h2 className="text-xl font-bold text-slate-100">
                2. Craft Over Templates
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                We reject slow, bloated WordPress themes and cookie-cutter page builders that slow down your website. Every Techzyan solution is engineered with modern typography, sub-second loading speeds, and clean code.
              </p>
            </div>

            <div className="p-8 rounded-3xl bg-slate-900/60 border border-slate-800 space-y-4">
              <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400">
                <HeartHandshake className="w-5 h-5" />
              </div>
              <h2 className="text-xl font-bold text-slate-100">
                3. Complete Client Ownership
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                You own 100% of your digital assets, code, and domains. We don’t hold your website hostage behind opaque proprietary platforms or forced monthly maintenance retainers.
              </p>
            </div>

            <div className="p-8 rounded-3xl bg-slate-900/60 border border-slate-800 space-y-4">
              <div className="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400">
                <MapPin className="w-5 h-5" />
              </div>
              <h2 className="text-xl font-bold text-slate-100">
                4. Kolkata Roots, Global Standards
              </h2>
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed">
                Rooted in Kolkata’s rich intellectual and cultural fabric, we bring world-class digital design and engineering rigor to local enterprises, doctors, educators, and Bengal’s magnificent Durga Puja committees.
              </p>
            </div>
          </div>
        </section>

        {/* Studio Details / Operating Norms */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="p-8 sm:p-12 rounded-3xl bg-slate-950 border border-slate-800">
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
              <div className="space-y-2">
                <div className="text-xs font-mono uppercase text-brand-cyan">Location & Base</div>
                <div className="text-lg font-bold text-slate-100">Kolkata, West Bengal, India</div>
                <p className="text-xs text-slate-400">Serving clients across Kolkata, Pan-India & Global markets.</p>
              </div>

              <div className="space-y-2">
                <div className="text-xs font-mono uppercase text-brand-cyan">Engagement Model</div>
                <div className="text-lg font-bold text-slate-100">Direct Senior Partner Collaboration</div>
                <p className="text-xs text-slate-400">No junior account managers. You speak directly with the designers and engineers building your solution.</p>
              </div>

              <div className="space-y-2">
                <div className="text-xs font-mono uppercase text-brand-cyan">Studio Availability</div>
                <div className="text-lg font-bold text-slate-100">{siteConfig.status.currentSlot}</div>
                <p className="text-xs text-slate-400">We deliberately limit concurrent projects to maintain exceptional craft quality.</p>
              </div>
            </div>

            <div className="pt-10 mt-10 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-4">
              <p className="text-xs text-slate-400 text-center sm:text-left">
                Ready to work with a studio that treats your project with genuine care?
              </p>
              <button
                onClick={() => setIsConsultationOpen(true)}
                className="inline-flex items-center gap-2 px-6 py-3 bg-brand-cyan hover:bg-sky-300 text-slate-950 font-semibold text-xs uppercase tracking-wider rounded-lg shadow-glow-cyan transition-all"
              >
                <span>Discuss Your Project</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </section>
      </main>

      <Footer />

      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
      />
    </>
  );
}
"""

write_file('src/app/about/page.tsx', about_page_code)
contact_page_code = """'use client';

import React, { useState } from 'react';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { siteConfig } from '@/config/site';
import {
  Mail,
  MessageCircle,
  Phone,
  Clock,
  MapPin,
  Sparkles,
  Send,
  CheckCircle2,
  ShieldCheck,
  ArrowRight,
} from 'lucide-react';

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    organization: '',
    category: 'Small Business & Boutique',
    contactMethod: 'WhatsApp',
    contactValue: '',
    requirementNote: '',
  });

  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.contactMethod === 'WhatsApp') {
      const text = `Hi Techzyan! My name is ${formData.name || 'a visitor'} from ${formData.organization || 'my organization'}. Category: ${formData.category}. Note: ${formData.requirementNote || 'Would love to discuss details.'}`;
      window.open(`https://wa.me/919876543210?text=${encodeURIComponent(text)}`, '_blank');
    }
    setSubmitted(true);
  };

  return (
    <>
      <Header />

      <main id="main-content" className="flex-1 pt-32 pb-24">
        {/* Header */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono mb-4">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Direct Studio Channel</span>
            </div>
            <h1 className="text-3xl sm:text-5xl font-display font-extrabold text-slate-100 tracking-tight leading-tight">
              Start a conversation <br />
              <span className="text-gradient-cyan">with a technical specialist.</span>
            </h1>
            <p className="mt-4 text-slate-300 text-base sm:text-lg leading-relaxed">
              No sales intermediaries or junior reps. Reach out directly via WhatsApp, email, or our structured form below. We typically respond within 12 business hours.
            </p>
          </div>
        </section>

        {/* Contact Layout Grid */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10">
            {/* Left Column: Direct Channels & Information */}
            <div className="lg:col-span-5 space-y-6">
              {/* WhatsApp Card */}
              <a
                href={siteConfig.contact.whatsappLink}
                target="_blank"
                rel="noopener noreferrer"
                className="p-6 rounded-2xl bg-emerald-950/20 border border-emerald-500/30 hover:border-emerald-500/60 transition-all duration-200 block space-y-2 group"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono uppercase text-emerald-400 font-semibold flex items-center gap-2">
                    <MessageCircle className="w-4 h-4" />
                    <span>Instant Direct Chat</span>
                  </span>
                  <ArrowRight className="w-4 h-4 text-emerald-400 group-hover:translate-x-1 transition-transform" />
                </div>
                <div className="text-lg font-bold text-slate-100">WhatsApp Consultation</div>
                <p className="text-xs text-slate-400">
                  Ideal for quick questions, project timelines, and sharing initial thoughts.
                </p>
              </a>

              {/* Email Card */}
              <a
                href={`mailto:${siteConfig.contact.email}`}
                className="p-6 rounded-2xl bg-slate-900/60 border border-slate-800 hover:border-brand-cyan/40 transition-all duration-200 block space-y-2 group"
              >
                <div className="flex items-center justify-between">
                  <span className="text-xs font-mono uppercase text-brand-cyan font-semibold flex items-center gap-2">
                    <Mail className="w-4 h-4" />
                    <span>Formal Inquiries</span>
                  </span>
                  <ArrowRight className="w-4 h-4 text-brand-cyan group-hover:translate-x-1 transition-transform" />
                </div>
                <div className="text-lg font-bold text-slate-100 font-mono text-sm sm:text-base">
                  {siteConfig.contact.email}
                </div>
                <p className="text-xs text-slate-400">
                  Send project scopes, RFP documents, or detailed requirements.
                </p>
              </a>

              {/* Studio Hours & Location */}
              <div className="p-6 rounded-2xl bg-slate-950 border border-slate-800 space-y-4 text-xs text-slate-300">
                <div className="flex items-center gap-3">
                  <MapPin className="w-4 h-4 text-brand-cyan shrink-0" />
                  <div>
                    <div className="font-semibold text-slate-200">Kolkata, West Bengal, India</div>
                    <div className="text-slate-500">Serving Local & Global Clients</div>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <Clock className="w-4 h-4 text-brand-cyan shrink-0" />
                  <div>
                    <div className="font-semibold text-slate-200">{siteConfig.contact.operatingHours}</div>
                    <div className="text-slate-500">Average response time: &lt; 12 hours</div>
                  </div>
                </div>

                <div className="flex items-center gap-3 pt-2 border-t border-slate-800">
                  <ShieldCheck className="w-4 h-4 text-emerald-400 shrink-0" />
                  <div className="text-slate-400">
                    Strict privacy guarantee. No spam, cold calls, or sold data.
                  </div>
                </div>
              </div>
            </div>

            {/* Right Column: Structured Inquiry Form */}
            <div className="lg:col-span-7">
              <div className="glass-card rounded-3xl p-6 sm:p-10 border border-slate-800 shadow-2xl">
                {submitted ? (
                  <div className="py-12 text-center space-y-4">
                    <div className="w-16 h-16 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded-full flex items-center justify-center mx-auto">
                      <CheckCircle2 className="w-8 h-8" />
                    </div>
                    <h2 className="text-2xl font-bold text-slate-100">Inquiry Received!</h2>
                    <p className="text-slate-400 text-sm max-w-md mx-auto leading-relaxed">
                      Thank you for sharing your project details. A senior technical partner from Techzyan will review and contact you shortly via {formData.contactMethod}.
                    </p>
                    <div className="pt-4">
                      <button
                        onClick={() => setSubmitted(false)}
                        className="px-6 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-100 font-medium text-xs uppercase tracking-wider rounded-lg"
                      >
                        Submit Another Requirement
                      </button>
                    </div>
                  </div>
                ) : (
                  <form onSubmit={handleSubmit} className="space-y-5">
                    <div>
                      <h2 className="text-xl font-bold text-slate-100">Send a Project Brief</h2>
                      <p className="text-xs text-slate-400 mt-1">
                        Fill in this short form and we’ll prepare a tailored recommendation.
                      </p>
                    </div>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                      <div>
                        <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                          Your Name *
                        </label>
                        <input
                          type="text"
                          required
                          value={formData.name}
                          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                          placeholder="e.g. Dr. A. Sen / R. Mukherjee"
                          className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 placeholder:text-slate-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                        />
                      </div>
                      <div>
                        <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                          Organization / Practice
                        </label>
                        <input
                          type="text"
                          value={formData.organization}
                          onChange={(e) => setFormData({ ...formData, organization: e.target.value })}
                          placeholder="e.g. Clinic, Tutorial, Boutique, Puja Club"
                          className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 placeholder:text-slate-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                        />
                      </div>
                    </div>

                    <div>
                      <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                        Your Industry / Archetype
                      </label>
                      <select
                        value={formData.category}
                        onChange={(e) => setFormData({ ...formData, category: e.target.value })}
                        className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                      >
                        <option value="Doctor & Healthcare">Doctor & Healthcare</option>
                        <option value="Private Tutor & Educator">Private Tutor & Educator</option>
                        <option value="Small Business & Boutique">Small Business & Boutique</option>
                        <option value="Educational Institute">Educational Institute</option>
                        <option value="Durga Puja Committee">Durga Puja Committee</option>
                        <option value="Other Specialist">Other Specialist</option>
                      </select>
                    </div>

                    <div>
                      <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                        Preferred Contact Mode
                      </label>
                      <div className="grid grid-cols-3 gap-2.5">
                        {[
                          { id: 'WhatsApp', label: 'WhatsApp', icon: MessageCircle },
                          { id: 'Email', label: 'Email', icon: Mail },
                          { id: 'Phone', label: 'Phone Call', icon: Phone },
                        ].map((method) => {
                          const isSelected = formData.contactMethod === method.id;
                          const Icon = method.icon;
                          return (
                            <button
                              type="button"
                              key={method.id}
                              onClick={() => setFormData({ ...formData, contactMethod: method.id })}
                              className={`flex items-center justify-center gap-1.5 p-2.5 rounded-lg border text-xs font-medium transition-all ${
                                isSelected
                                  ? 'bg-sky-500/10 border-brand-cyan text-brand-cyan font-semibold'
                                  : 'bg-slate-950/50 border-slate-800 text-slate-400 hover:text-slate-200'
                              }`}
                            >
                              <Icon className="w-3.5 h-3.5" />
                              <span>{method.label}</span>
                            </button>
                          );
                        })}
                      </div>
                    </div>

                    <div>
                      <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                        Your {formData.contactMethod} Address or Number *
                      </label>
                      <input
                        type="text"
                        required
                        value={formData.contactValue}
                        onChange={(e) => setFormData({ ...formData, contactValue: e.target.value })}
                        placeholder={
                          formData.contactMethod === 'WhatsApp'
                            ? 'e.g. +91 98300 XXXXX'
                            : formData.contactMethod === 'Email'
                            ? 'e.g. name@domain.com'
                            : 'e.g. +91 98300 XXXXX'
                        }
                        className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 placeholder:text-slate-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                      />
                    </div>

                    <div>
                      <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                        Brief Requirement Details
                      </label>
                      <textarea
                        rows={4}
                        value={formData.requirementNote}
                        onChange={(e) => setFormData({ ...formData, requirementNote: e.target.value })}
                        placeholder="Tell us what you are looking to build or solve..."
                        className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 placeholder:text-slate-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan resize-none"
                      />
                    </div>

                    <div className="pt-2">
                      <button
                        type="submit"
                        className="w-full flex items-center justify-center gap-2 py-3 px-4 bg-brand-cyan hover:bg-sky-300 active:bg-sky-400 text-slate-950 font-semibold text-xs uppercase tracking-wider rounded-lg shadow-glow-cyan transition-all"
                      >
                        <span>
                          {formData.contactMethod === 'WhatsApp'
                            ? 'Continue on WhatsApp'
                            : 'Submit Requirement to Techzyan'}
                        </span>
                        <ArrowRight className="w-4 h-4" />
                      </button>
                    </div>
                  </form>
                )}
              </div>
            </div>
          </div>
        </section>
      </main>

      <Footer />
    </>
  );
}
"""

write_file('src/app/contact/page.tsx', contact_page_code)
sitemap_code = """import { MetadataRoute } from 'next';
import { siteConfig } from '@/config/site';

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = siteConfig.url;
  const lastModified = new Date();

  return [
    {
      url: `${baseUrl}`,
      lastModified,
      changeFrequency: 'weekly',
      priority: 1.0,
    },
    {
      url: `${baseUrl}/solutions`,
      lastModified,
      changeFrequency: 'weekly',
      priority: 0.9,
    },
    {
      url: `${baseUrl}/solutions/durga-puja`,
      lastModified,
      changeFrequency: 'weekly',
      priority: 0.95,
    },
    {
      url: `${baseUrl}/who-we-help`,
      lastModified,
      changeFrequency: 'weekly',
      priority: 0.85,
    },
    {
      url: `${baseUrl}/work`,
      lastModified,
      changeFrequency: 'weekly',
      priority: 0.8,
    },
    {
      url: `${baseUrl}/about`,
      lastModified,
      changeFrequency: 'monthly',
      priority: 0.7,
    },
    {
      url: `${baseUrl}/contact`,
      lastModified,
      changeFrequency: 'monthly',
      priority: 0.85,
    },
  ];
}
"""

robots_code = """import { MetadataRoute } from 'next';
import { siteConfig } from '@/config/site';

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: '*',
      allow: '/',
    },
    sitemap: `${siteConfig.url}/sitemap.xml`,
  };
}
"""

write_file('src/app/sitemap.ts', sitemap_code)
write_file('src/app/robots.ts', robots_code)
print("ALL FILES GENERATED SUCCESSFULLY!")
