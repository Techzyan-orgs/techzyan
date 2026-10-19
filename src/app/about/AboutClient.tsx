'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConsultationModal from '@/components/ConsultationModal';
import { siteConfig } from '@/config/site';
import FAQSection from '@/components/FAQSection';
import { aboutFaqs } from '@/data/seoData';
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
  Database,
  Server,
  Globe,
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
                1. Understand the Requirement First, Then Build the Right Digital Solution
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

        {/* Core Technology Stack & Engineering Architecture */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-20">
          <div className="p-8 sm:p-12 rounded-3xl bg-slate-900/60 border border-slate-800 space-y-8">
            <div className="max-w-3xl space-y-3">
              <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-brand-cyan text-xs font-mono">
                <Cpu className="w-3.5 h-3.5" />
                <span>Our Technology Stack</span>
              </div>
              <h2 className="text-2xl sm:text-4xl font-display font-extrabold text-slate-100 tracking-tight">
                Modern, Fast &amp; Proven Technologies
              </h2>
              <p className="text-slate-300 text-sm sm:text-base leading-relaxed">
                We reject slow templates and version lock-in. Our software is engineered using modern, high-throughput programming languages, resilient microservices, and edge-native cloud platforms.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {/* Frontend */}
              <div className="p-6 rounded-2xl bg-slate-950/80 border border-slate-800/80 space-y-3 hover:border-brand-cyan/40 transition-colors">
                <div className="w-9 h-9 rounded-lg bg-sky-500/10 border border-sky-500/30 flex items-center justify-center text-brand-cyan mb-2">
                  <Code2 className="w-4 h-4" />
                </div>
                <div className="text-xs font-mono uppercase tracking-wider text-brand-cyan font-semibold">
                  Frontend &amp; Interface
                </div>
                <div className="text-base font-bold text-slate-100">Next.js &amp; React</div>
                <p className="text-xs text-slate-400 leading-relaxed">
                  Sub-second page paints, server-side rendering, TypeScript type safety, and clean Tailwind CSS design.
                </p>
                <div className="flex flex-wrap gap-1.5 pt-2 border-t border-slate-800/60">
                  {['Next.js', 'React', 'TypeScript', 'Tailwind CSS'].map(tag => (
                    <span key={tag} className="px-2 py-0.5 rounded bg-slate-800/80 text-[11px] font-mono text-slate-300 border border-slate-700/60">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>

              {/* Advanced Backend & APIs */}
              <div className="p-6 rounded-2xl bg-slate-950/80 border border-slate-800/80 space-y-3 hover:border-emerald-500/40 transition-colors">
                <div className="w-9 h-9 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-center justify-center text-emerald-400 mb-2">
                  <Server className="w-4 h-4" />
                </div>
                <div className="text-xs font-mono uppercase tracking-wider text-emerald-400 font-semibold">
                  Backend &amp; High-Speed APIs
                </div>
                <div className="text-base font-bold text-slate-100">Python &amp; FastAPI</div>
                <p className="text-xs text-slate-400 leading-relaxed">
                  Asynchronous high-throughput microservices, background job workers, intelligent data processing, and Node.js.
                </p>
                <div className="flex flex-wrap gap-1.5 pt-2 border-t border-slate-800/60">
                  {['Python', 'FastAPI', 'Node.js', 'Async APIs'].map(tag => (
                    <span key={tag} className="px-2 py-0.5 rounded bg-emerald-500/10 text-[11px] font-mono text-emerald-300 border border-emerald-500/20">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>

              {/* Data & Storage */}
              <div className="p-6 rounded-2xl bg-slate-950/80 border border-slate-800/80 space-y-3 hover:border-indigo-500/40 transition-colors">
                <div className="w-9 h-9 rounded-lg bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400 mb-2">
                  <Database className="w-4 h-4" />
                </div>
                <div className="text-xs font-mono uppercase tracking-wider text-indigo-400 font-semibold">
                  Data &amp; Persistence
                </div>
                <div className="text-base font-bold text-slate-100">PostgreSQL &amp; Redis</div>
                <p className="text-xs text-slate-400 leading-relaxed">
                  ACID-compliant relational schemas, lightning-fast in-memory caching, and structured cloud storage.
                </p>
                <div className="flex flex-wrap gap-1.5 pt-2 border-t border-slate-800/60">
                  {['PostgreSQL', 'Redis', 'REST & SQL', 'Prisma'].map(tag => (
                    <span key={tag} className="px-2 py-0.5 rounded bg-indigo-500/10 text-[11px] font-mono text-indigo-300 border border-indigo-500/20">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>

              {/* Edge & Cloud Infrastructure */}
              <div className="p-6 rounded-2xl bg-slate-950/80 border border-slate-800/80 space-y-3 hover:border-amber-500/40 transition-colors">
                <div className="w-9 h-9 rounded-lg bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400 mb-2">
                  <Globe className="w-4 h-4" />
                </div>
                <div className="text-xs font-mono uppercase tracking-wider text-amber-400 font-semibold">
                  Cloud &amp; Edge Delivery
                </div>
                <div className="text-base font-bold text-slate-100">Vercel &amp; Cloudflare</div>
                <p className="text-xs text-slate-400 leading-relaxed">
                  Worldwide edge network CDN, automated SSL certificates, enterprise DDoS shielding, and Docker containers.
                </p>
                <div className="flex flex-wrap gap-1.5 pt-2 border-t border-slate-800/60">
                  {['Vercel', 'Cloudflare', 'AWS', 'Docker'].map(tag => (
                    <span key={tag} className="px-2 py-0.5 rounded bg-amber-500/10 text-[11px] font-mono text-amber-300 border border-amber-500/20">
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
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

        {/* SEO FAQ SECTION */}
        <FAQSection
          id="about-faq"
          badge="Studio FAQ"
          title="Frequently Asked Questions About Techzyan"
          subtitle="Our engineering standards, Kolkata studio location, zero-lockin philosophy, and senior-level collaboration."
          items={aboutFaqs}
        />
      </main>

      <Footer />

      <ConsultationModal
        isOpen={isConsultationOpen}
        onClose={() => setIsConsultationOpen(false)}
      />
    </>
  );
}
