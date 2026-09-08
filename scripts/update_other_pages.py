import os

def write_file(rel_path, content):
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {rel_path}")

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
                className="glass-card rounded-3xl p-6 sm:p-7 border border-slate-800 hover:border-brand-cyan/40 transition-all flex flex-col justify-between space-y-6 group"
              >
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] font-mono uppercase tracking-wider bg-slate-800 text-slate-300 border border-slate-700">
                      {project.clientType}
                    </span>
                    <span className="text-[10px] font-mono text-brand-cyan font-semibold">
                      {project.badge}
                    </span>
                  </div>

                  <div>
                    <h2 className="text-lg font-bold text-slate-100 group-hover:text-brand-cyan transition-colors">
                      {project.title}
                    </h2>
                    <p className="text-xs text-slate-400 mt-1.5 leading-relaxed">
                      {project.summary}
                    </p>
                  </div>

                  <div className="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800 space-y-1">
                    <div className="text-[10px] font-mono uppercase text-slate-500">Problem Solved:</div>
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

puja_page_code = """'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import PujaConsultationModal from '@/components/PujaConsultationModal';
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
  MessageCircle,
} from 'lucide-react';

export default function DurgaPujaPage() {
  const [isPujaModalOpen, setIsPujaModalOpen] = useState(false);
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
      <Header onOpenConsultation={() => setIsPujaModalOpen(true)} />

      <main id="main-content" className="flex-1 pt-32 pb-24 bg-[#080705]">
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16 lg:mb-20">
          <div className="p-8 sm:p-12 lg:p-14 rounded-3xl bg-gradient-to-br from-[#1C140A] via-[#140E06] to-[#0A0704] border border-amber-500/30 shadow-2xl relative overflow-hidden">
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

              <div className="flex flex-col sm:flex-row items-center gap-3.5 pt-4">
                <button
                  onClick={() => setIsPujaModalOpen(true)}
                  className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-7 py-3.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-gold transition-all"
                >
                  <span>Discuss Your Puja Plan</span>
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

        {/* 6 Core Pillars */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {durgaPujaFeatures.map((feat) => (
              <div
                key={feat.id}
                className="puja-card rounded-3xl p-6 border border-amber-500/25 space-y-4 hover:border-amber-500/50 transition-all"
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
                  <p className="text-xs text-slate-300 mt-1.5 leading-relaxed">{feat.description}</p>
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

        {/* Interactive 5-Day Schedule */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20">
          <div className="p-8 sm:p-10 rounded-3xl bg-[#110D08] border border-amber-500/30 space-y-6">
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-amber-500/20">
              <div>
                <span className="text-xs font-mono uppercase text-amber-400 font-semibold">Live Component</span>
                <h3 className="text-xl sm:text-2xl font-bold text-amber-100 mt-0.5">
                  5-Day Interactive Puja Schedule Engine
                </h3>
              </div>
              <span className="text-xs text-slate-400">Accurate Pushpanjali & Bhog Timetable</span>
            </div>

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

            <div className="p-5 rounded-2xl bg-black/60 border border-amber-500/20 space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="text-base font-bold text-amber-200">{ritualSchedule[activeDay].day}</h4>
                  <p className="text-xs text-slate-400">{ritualSchedule[activeDay].date}</p>
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                {ritualSchedule[activeDay].events.map((evt, i) => (
                  <div key={i} className="p-3 rounded-xl bg-[#1A140C] border border-amber-500/15 flex items-start gap-3">
                    <span className="px-2 py-0.5 rounded bg-black/60 border border-amber-500/30 font-mono text-xs text-amber-400 font-bold shrink-0">
                      {evt.time}
                    </span>
                    <span className="text-xs text-slate-200 mt-0.5">{evt.title}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Sponsorship Tiers */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20">
          <div className="text-center max-w-2xl mx-auto mb-10">
            <h2 className="text-2xl sm:text-3xl font-display font-bold text-amber-100">
              Corporate Sponsorship Presentation Suite
            </h2>
            <p className="mt-2 text-slate-400 text-sm">
              Present digital and on-ground brand visibility deliverables to corporate brand managers.
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {sampleSponsorTiers.map((tier) => (
              <div
                key={tier.name}
                className={`rounded-3xl p-6 sm:p-8 border flex flex-col justify-between space-y-6 ${
                  tier.featuredPlacement
                    ? 'bg-gradient-to-b from-[#22190E] to-[#140E06] border-amber-400 shadow-glow-gold'
                    : 'bg-[#110D08] border-amber-500/25'
                }`}
              >
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-mono uppercase text-amber-400 font-semibold">Tier Level</span>
                    {tier.featuredPlacement && (
                      <span className="px-2.5 py-0.5 rounded-full text-[10px] font-mono bg-amber-400 text-slate-950 font-bold uppercase">
                        Premier
                      </span>
                    )}
                  </div>
                  <div>
                    <h3 className="text-xl font-bold text-amber-100">{tier.name}</h3>
                    <p className="text-xs text-amber-200/80 mt-1">{tier.tagline}</p>
                  </div>
                  <ul className="space-y-2 text-xs text-slate-300">
                    {tier.digitalPerks.map((perk, i) => (
                      <li key={i} className="flex items-start gap-2">
                        <CheckCircle2 className="w-3.5 h-3.5 text-amber-400 shrink-0 mt-0.5" />
                        <span>{perk}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <button
                  onClick={() => setIsPujaModalOpen(true)}
                  className={`w-full py-2.5 px-4 rounded-xl text-xs font-bold uppercase tracking-wider transition-all ${
                    tier.featuredPlacement
                      ? 'bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-md'
                      : 'bg-black/60 hover:bg-amber-950/60 text-amber-300 border border-amber-500/30'
                  }`}
                >
                  Request Tier Proposal
                </button>
              </div>
            ))}
          </div>
        </section>

        {/* CTA */}
        <section className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="p-8 sm:p-12 rounded-3xl bg-gradient-to-r from-[#1C140A] via-[#161008] to-[#1C140A] border border-amber-500/40 shadow-2xl space-y-6">
            <h3 className="text-2xl sm:text-4xl font-display font-bold text-amber-100">
              Ready to elevate your Puja's digital presence?
            </h3>
            <p className="text-slate-300 text-sm max-w-xl mx-auto leading-relaxed">
              We work with select committees in North, South, and Central Kolkata. Let’s discuss your pandal concept and schedule.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-2">
              <button
                onClick={() => setIsPujaModalOpen(true)}
                className="w-full sm:w-auto px-8 py-3.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-gold transition-all"
              >
                Schedule Committee Discussion
              </button>
            </div>
          </div>
        </section>
      </main>

      <Footer />

      <PujaConsultationModal
        isOpen={isPujaModalOpen}
        onClose={() => setIsPujaModalOpen(false)}
      />
    </>
  );
}
"""

write_file('src/app/solutions/durga-puja/page.tsx', puja_page_code)
print("Other pages updated!")
