import os

def write_file(rel_path, content):
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned & Written: {rel_path}")

header_code = """'use client';

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { siteConfig } from '@/config/site';
import { Menu, X, ArrowRight, Sparkles, MessageSquare } from 'lucide-react';

export default function Header({ onOpenConsultation }: { onOpenConsultation?: () => void }) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    setMobileMenuOpen(false);
  }, [pathname]);

  return (
    <>
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 z-50 px-4 py-2 bg-brand-cyan text-slate-900 font-semibold rounded-md shadow-lg"
      >
        Skip to main content
      </a>

      <header
        className={`fixed top-0 left-0 right-0 z-40 transition-all duration-300 ${
          scrolled ? 'glass-header shadow-lg shadow-black/40 py-3.5' : 'bg-transparent py-5'
        }`}
      >
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <Link
              href="/"
              className="group flex items-center gap-2 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-cyan rounded-lg p-1"
              aria-label="Techzyan Home"
            >
              <div className="flex items-center tracking-tight font-display font-semibold text-xl sm:text-2xl text-slate-100">
                <span>techzyan</span>
                <span className="inline-block w-2 h-2 rounded-full bg-brand-cyan ml-1 group-hover:scale-125 transition-transform duration-200" />
              </div>
              <span className="hidden sm:inline-block text-[11px] font-mono uppercase tracking-widest text-slate-400 border-l border-slate-700 pl-2.5 ml-1">
                Studio
              </span>
            </Link>

            <nav className="hidden md:flex items-center gap-1 lg:gap-2" aria-label="Main Navigation">
              {siteConfig.nav.map((item) => {
                const isActive = pathname === item.href || (item.href !== '/' && pathname.startsWith(item.href));
                return (
                  <Link
                    key={item.href}
                    href={item.href}
                    className={`relative px-3.5 py-2 text-sm font-medium rounded-md transition-colors duration-200 ${
                      item.isSpecial
                        ? isActive
                          ? 'text-amber-300 bg-amber-500/10 border border-amber-500/30'
                          : 'text-amber-400/90 hover:text-amber-200 hover:bg-amber-500/10'
                        : isActive
                        ? 'text-slate-100 bg-slate-800/80 border border-slate-700/60'
                        : 'text-slate-300 hover:text-slate-100 hover:bg-slate-800/40'
                    }`}
                  >
                    <span className="flex items-center gap-1.5">
                      {item.isSpecial && <Sparkles className="w-3.5 h-3.5 text-amber-400" />}
                      {item.label}
                    </span>
                  </Link>
                );
              })}
            </nav>

            <div className="hidden md:flex items-center gap-3">
              <button
                onClick={onOpenConsultation}
                className="inline-flex items-center gap-2 px-4 py-2 text-xs font-semibold uppercase tracking-wider text-slate-950 bg-brand-cyan hover:bg-sky-300 active:bg-sky-400 rounded-lg shadow-glow-cyan transition-all duration-200 hover:translate-y-[-1px]"
              >
                <span>Discuss Project</span>
                <ArrowRight className="w-3.5 h-3.5" />
              </button>
            </div>

            <div className="flex md:hidden items-center gap-2">
              <button
                onClick={onOpenConsultation}
                className="p-2 text-slate-900 bg-brand-cyan rounded-md"
                aria-label="Quick discuss project"
              >
                <MessageSquare className="w-4 h-4" />
              </button>
              <button
                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                className="p-2 text-slate-300 hover:text-slate-100 hover:bg-slate-800 rounded-lg focus-visible:ring-2 focus-visible:ring-brand-cyan"
                aria-label={mobileMenuOpen ? 'Close Navigation Menu' : 'Open Navigation Menu'}
                aria-expanded={mobileMenuOpen}
              >
                {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
              </button>
            </div>
          </div>
        </div>

        {mobileMenuOpen && (
          <div className="md:hidden glass-header border-t border-slate-800 px-4 pt-3 pb-6 mt-3 shadow-2xl">
            <nav className="flex flex-col gap-1.5" aria-label="Mobile Navigation">
              {siteConfig.nav.map((item) => {
                const isActive = pathname === item.href;
                return (
                  <Link
                    key={item.href}
                    href={item.href}
                    className={`flex items-center justify-between px-4 py-3 text-base font-medium rounded-lg ${
                      item.isSpecial
                        ? 'text-amber-300 bg-amber-500/10 border border-amber-500/30'
                        : isActive
                        ? 'text-slate-100 bg-slate-800 border border-slate-700'
                        : 'text-slate-300 hover:text-slate-100 hover:bg-slate-800/60'
                    }`}
                  >
                    <span className="flex items-center gap-2">
                      {item.isSpecial && <Sparkles className="w-4 h-4 text-amber-400" />}
                      {item.label}
                    </span>
                    <ArrowRight className="w-4 h-4 text-slate-500" />
                  </Link>
                );
              })}
              <div className="pt-3 mt-2 border-t border-slate-800">
                <button
                  onClick={() => {
                    setMobileMenuOpen(false);
                    onOpenConsultation?.();
                  }}
                  className="w-full flex items-center justify-center gap-2 px-4 py-3 text-sm font-semibold uppercase tracking-wider text-slate-950 bg-brand-cyan hover:bg-sky-300 rounded-lg shadow-glow-cyan"
                >
                  <span>Discuss Your Project</span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </nav>
          </div>
        )}
      </header>
    </>
  );
}
"""

write_file('src/components/Header.tsx', header_code)
footer_code = """import React from 'react';
import Link from 'next/link';
import { siteConfig } from '@/config/site';
import { Sparkles, ArrowUpRight, MessageCircle, Mail, Phone, MapPin, Clock, ShieldCheck } from 'lucide-react';

export default function Footer() {
  return (
    <footer className="bg-[#05080F] border-t border-slate-800/80 text-slate-400 text-sm relative z-20">
      <div className="border-b border-slate-800/60 py-8 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className="flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono">
              <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
              <span>{siteConfig.status.currentSlot}</span>
            </div>
            <span className="hidden sm:inline text-xs text-slate-500">•</span>
            <div className="hidden sm:flex items-center gap-1.5 text-xs text-slate-400">
              <MapPin className="w-3.5 h-3.5 text-brand-cyan" />
              <span>Kolkata, West Bengal, India</span>
            </div>
          </div>
          <div className="text-xs text-slate-400 flex items-center gap-2 font-mono">
            <span>Official Domain:</span>
            <span className="text-slate-200 font-semibold bg-slate-800/60 px-2 py-0.5 rounded border border-slate-700/60">
              techzyan.org
            </span>
          </div>
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-14 lg:py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 lg:gap-8">
          <div className="lg:col-span-2 space-y-4">
            <Link href="/" className="inline-flex items-center gap-1.5 text-xl font-display font-bold text-slate-100">
              <span>techzyan</span>
              <span className="w-2 h-2 rounded-full bg-brand-cyan" />
            </Link>
            <p className="text-slate-400 leading-relaxed text-sm max-w-sm">
              A premium technical studio based in Kolkata. We partner with businesses, doctors, educators, and cultural committees to engineer thoughtful websites and right-sized digital solutions.
            </p>
            <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 max-w-sm space-y-2">
              <div className="text-xs font-mono uppercase tracking-wider text-brand-cyan font-semibold flex items-center gap-1.5">
                <ShieldCheck className="w-4 h-4" />
                <span>Our Core Operating Principle</span>
              </div>
              <p className="text-xs text-slate-300 leading-relaxed">
                “Understand the requirement first. Build the right digital solution second.” Zero fake metrics, zero bloated templates.
              </p>
            </div>
          </div>

          <div className="space-y-3">
            <h3 className="text-xs font-mono uppercase tracking-widest text-slate-200 font-semibold">
              Solutions
            </h3>
            <ul className="space-y-2.5 text-sm">
              <li>
                <Link href="/solutions#business-websites" className="hover:text-brand-cyan transition-colors">
                  Business Websites
                </Link>
              </li>
              <li>
                <Link href="/solutions#healthcare-doctor-websites" className="hover:text-brand-cyan transition-colors">
                  Doctor & Clinic Platforms
                </Link>
              </li>
              <li>
                <Link href="/solutions#education-tutor-websites" className="hover:text-brand-cyan transition-colors">
                  Tutor & Academic Portals
                </Link>
              </li>
              <li>
                <Link href="/solutions#appointment-booking-systems" className="hover:text-brand-cyan transition-colors">
                  Custom Appointment Tools
                </Link>
              </li>
              <li>
                <Link href="/solutions#student-inquiry-management" className="hover:text-brand-cyan transition-colors">
                  Student Inquiry Systems
                </Link>
              </li>
              <li>
                <Link href="/solutions/durga-puja" className="inline-flex items-center gap-1 text-amber-400 hover:text-amber-300 font-medium transition-colors">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Durga Puja Platform</span>
                </Link>
              </li>
            </ul>
          </div>

          <div className="space-y-3">
            <h3 className="text-xs font-mono uppercase tracking-widest text-slate-200 font-semibold">
              Who We Help
            </h3>
            <ul className="space-y-2.5 text-sm">
              <li>
                <Link href="/who-we-help#doctors-healthcare" className="hover:text-brand-cyan transition-colors">
                  Doctors & Healthcare
                </Link>
              </li>
              <li>
                <Link href="/who-we-help#tutors-educators" className="hover:text-brand-cyan transition-colors">
                  Private Tutors & Mentors
                </Link>
              </li>
              <li>
                <Link href="/who-we-help#local-businesses" className="hover:text-brand-cyan transition-colors">
                  Small Businesses & Boutiques
                </Link>
              </li>
              <li>
                <Link href="/who-we-help#educational-institutes" className="hover:text-brand-cyan transition-colors">
                  Educational Institutes
                </Link>
              </li>
              <li>
                <Link href="/who-we-help#durga-puja-committees" className="hover:text-brand-cyan transition-colors">
                  Durga Puja Committees
                </Link>
              </li>
              <li>
                <Link href="/work" className="hover:text-brand-cyan transition-colors">
                  Demonstration Portfolio
                </Link>
              </li>
            </ul>
          </div>

          <div className="space-y-3">
            <h3 className="text-xs font-mono uppercase tracking-widest text-slate-200 font-semibold">
              Direct Contact
            </h3>
            <ul className="space-y-3 text-sm">
              <li>
                <a
                  href={`mailto:${siteConfig.contact.email}`}
                  className="flex items-center gap-2 hover:text-brand-cyan transition-colors"
                >
                  <Mail className="w-4 h-4 text-brand-cyan shrink-0" />
                  <span className="truncate">{siteConfig.contact.email}</span>
                </a>
              </li>
              <li>
                <a
                  href={siteConfig.contact.whatsappLink}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 hover:text-emerald-400 transition-colors"
                >
                  <MessageCircle className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span>WhatsApp Consultation</span>
                  <ArrowUpRight className="w-3 h-3 text-slate-500" />
                </a>
              </li>
              <li className="flex items-center gap-2 text-slate-400 text-xs">
                <Clock className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                <span>{siteConfig.contact.operatingHours}</span>
              </li>
              <li className="pt-2">
                <Link
                  href="/contact"
                  className="inline-flex items-center justify-center w-full px-3 py-2 text-xs font-semibold text-slate-900 bg-slate-200 hover:bg-white rounded-md transition-colors"
                >
                  Start a Project Inquiry
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="pt-12 mt-12 border-t border-slate-800/80 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-500">
          <p>© {new Date().getFullYear()} Techzyan Technical Studio. All rights reserved.</p>
          <div className="flex items-center gap-6">
            <Link href="/about" className="hover:text-slate-400">About Studio</Link>
            <Link href="/contact" className="hover:text-slate-400">Inquiry Hub</Link>
            <Link href="/solutions/durga-puja" className="hover:text-amber-400">Durga Puja Solution</Link>
          </div>
        </div>
      </div>
    </footer>
  );
}
"""

write_file('src/components/Footer.tsx', footer_code)
consultation_modal_code = """'use client';

import React, { useState, useEffect } from 'react';
import { X, MessageCircle, Mail, Phone, CheckCircle2, Sparkles, ArrowRight } from 'lucide-react';
import { siteConfig } from '@/config/site';

interface ConsultationModalProps {
  isOpen: boolean;
  onClose: () => void;
  initialCategory?: string;
}

export default function ConsultationModal({ isOpen, onClose, initialCategory }: ConsultationModalProps) {
  const [formData, setFormData] = useState({
    name: '',
    organization: '',
    category: initialCategory || 'Small Business',
    solutionType: 'Website & Digital Presence',
    contactMethod: 'WhatsApp',
    contactValue: '',
    requirementNote: '',
  });

  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    if (initialCategory) {
      setFormData(prev => ({ ...prev, category: initialCategory }));
    }
  }, [initialCategory]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (isOpen) {
      document.body.style.overflow = 'hidden';
      window.addEventListener('keydown', handleKeyDown);
    } else {
      document.body.style.overflow = 'unset';
    }
    return () => {
      document.body.style.overflow = 'unset';
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.contactMethod === 'WhatsApp') {
      const text = `Hi Techzyan! My name is ${formData.name || 'a visitor'} from ${formData.organization || 'my business'}. I am looking for ${formData.solutionType} (${formData.category}). Note: ${formData.requirementNote || 'Would love to discuss details.'}`;
      window.open(`https://wa.me/919876543210?text=${encodeURIComponent(text)}`, '_blank');
    }
    setSubmitted(true);
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/80 backdrop-blur-md animate-in fade-in duration-200"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
    >
      <div className="relative w-full max-w-xl bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl overflow-hidden text-slate-200 max-h-[90vh] flex flex-col">
        <div className="p-6 border-b border-slate-800 flex items-center justify-between bg-slate-950/60">
          <div>
            <div className="flex items-center gap-2 text-xs font-mono uppercase tracking-wider text-brand-cyan mb-1">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Direct Studio Inquiry</span>
            </div>
            <h2 id="modal-title" className="text-xl font-display font-bold text-slate-100">
              Start a Conversation with Techzyan
            </h2>
          </div>
          <button
            onClick={onClose}
            className="p-2 text-slate-400 hover:text-slate-100 hover:bg-slate-800 rounded-lg transition-colors"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="p-6 overflow-y-auto space-y-6">
          {submitted ? (
            <div className="py-10 text-center space-y-4">
              <div className="w-14 h-14 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded-full flex items-center justify-center mx-auto">
                <CheckCircle2 className="w-8 h-8" />
              </div>
              <h3 className="text-xl font-bold text-slate-100">Thank you for reaching out!</h3>
              <p className="text-slate-400 text-sm max-w-md mx-auto leading-relaxed">
                We have received your requirement. A senior technical partner from Techzyan will review your details and respond within 12 business hours.
              </p>
              <div className="pt-4">
                <button
                  onClick={() => {
                    setSubmitted(false);
                    onClose();
                  }}
                  className="px-6 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-100 font-medium text-sm rounded-lg"
                >
                  Close Window
                </button>
              </div>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <p className="text-xs text-slate-400 leading-relaxed">
                Share what you are trying to achieve. We will advise you on the right digital approach without aggressive sales pitches or jargon.
              </p>

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
                    Business / Organization
                  </label>
                  <input
                    type="text"
                    value={formData.organization}
                    onChange={(e) => setFormData({ ...formData, organization: e.target.value })}
                    placeholder="e.g. Clinic, Institute, Puja Club"
                    className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 placeholder:text-slate-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                  />
                </div>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                    You Are A:
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
                    Primary Digital Need:
                  </label>
                  <select
                    value={formData.solutionType}
                    onChange={(e) => setFormData({ ...formData, solutionType: e.target.value })}
                    className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan"
                  >
                    <option value="New Website & Brand Presence">New Website & Brand Presence</option>
                    <option value="Website + Appointment / Booking Tool">Website + Appointment / Booking Tool</option>
                    <option value="Student Inquiry & Admission System">Student Inquiry & Admission System</option>
                    <option value="Durga Puja Digital Hub & Sponsorship">Durga Puja Digital Hub & Sponsorship</option>
                    <option value="Custom Business Workflow Tool">Custom Business Workflow Tool</option>
                    <option value="Technical Consultation First">Technical Consultation First</option>
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-xs font-mono uppercase text-slate-400 mb-1.5 font-medium">
                  Preferred Contact Channel
                </label>
                <div className="grid grid-cols-3 gap-2.5">
                  {[
                    { id: 'WhatsApp', icon: MessageCircle, label: 'WhatsApp' },
                    { id: 'Email', icon: Mail, label: 'Email' },
                    { id: 'Phone', icon: Phone, label: 'Phone Call' },
                  ].map((method) => {
                    const Icon = method.icon;
                    const isSelected = formData.contactMethod === method.id;
                    return (
                      <button
                        type="button"
                        key={method.id}
                        onClick={() => setFormData({ ...formData, contactMethod: method.id })}
                        className={`flex items-center justify-center gap-1.5 p-2.5 rounded-lg border text-xs font-medium transition-all ${
                          isSelected
                            ? 'bg-sky-500/10 border-brand-cyan text-brand-cyan font-semibold shadow-sm'
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
                  Your {formData.contactMethod} Number or Address *
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
                  Tell us briefly what you want to achieve
                </label>
                <textarea
                  rows={3}
                  value={formData.requirementNote}
                  onChange={(e) => setFormData({ ...formData, requirementNote: e.target.value })}
                  placeholder="e.g. We are launching a new chamber in South Kolkata and need patients to be able to check timings and request slots..."
                  className="w-full px-3.5 py-2.5 bg-slate-950/80 border border-slate-800 rounded-lg text-sm text-slate-100 placeholder:text-slate-600 focus:border-brand-cyan focus:ring-1 focus:ring-brand-cyan resize-none"
                />
              </div>

              <div className="pt-2">
                <button
                  type="submit"
                  className="w-full flex items-center justify-center gap-2 py-3 px-4 bg-brand-cyan hover:bg-sky-300 active:bg-sky-400 text-slate-950 font-semibold text-sm rounded-lg shadow-glow-cyan transition-all"
                >
                  <span>
                    {formData.contactMethod === 'WhatsApp'
                      ? 'Continue to WhatsApp Consultation'
                      : 'Submit Requirement to Techzyan'}
                  </span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>

              <p className="text-[11px] text-center text-slate-500">
                🔒 We respect privacy. No unsolicited marketing emails or spam calls. Ever.
              </p>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
"""

write_file('src/components/ConsultationModal.tsx', consultation_modal_code)
demonstration_modal_code = """'use client';

import React, { useEffect } from 'react';
import { X, Layers, Cpu, CheckCircle, ShieldAlert, Sparkles } from 'lucide-react';
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
      <div className="relative w-full max-w-3xl bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl overflow-hidden text-slate-200 max-h-[92vh] flex flex-col">
        <div className="p-6 border-b border-slate-800 flex items-start justify-between bg-slate-950/80">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-2">
              <span className="px-2.5 py-0.5 rounded text-[11px] font-mono uppercase tracking-wider bg-sky-500/10 text-brand-cyan border border-sky-500/30">
                Demonstration Concept
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

        <div className="p-6 sm:p-8 overflow-y-auto space-y-8">
          <div className="p-3.5 rounded-xl bg-amber-500/5 border border-amber-500/20 text-xs text-amber-300/90 flex items-start gap-2.5">
            <ShieldAlert className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
            <p>
              <strong>Studio Transparency:</strong> This is an authentic technical demonstration architecture built by Techzyan to showcase real problem-solving capabilities, technical depth, and UX flow for {project.clientType.toLowerCase()}s. Zero fabricated client testimonials.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="p-5 rounded-xl bg-slate-950/60 border border-slate-800/80 space-y-2.5">
              <div className="text-xs font-mono uppercase tracking-wider text-rose-400 font-semibold flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-rose-400" />
                <span>The Operational Challenge</span>
              </div>
              <p className="text-sm text-slate-300 leading-relaxed">
                {project.operationalChallenge}
              </p>
            </div>

            <div className="p-5 rounded-xl bg-slate-950/60 border border-slate-800/80 space-y-2.5">
              <div className="text-xs font-mono uppercase tracking-wider text-emerald-400 font-semibold flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-emerald-400" />
                <span>The Engineered Solution</span>
              </div>
              <p className="text-sm text-slate-300 leading-relaxed">
                {project.engineeredSolution}
              </p>
            </div>
          </div>

          <div className="rounded-xl bg-slate-950 border border-slate-800 p-5 space-y-4">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800 text-xs text-slate-400 font-mono">
              <div className="flex items-center gap-1.5">
                <span className="w-2.5 h-2.5 rounded-full bg-red-500/80" />
                <span className="w-2.5 h-2.5 rounded-full bg-yellow-500/80" />
                <span className="w-2.5 h-2.5 rounded-full bg-green-500/80" />
                <span className="ml-2 text-slate-500">live-interface-preview.tsx</span>
              </div>
              <span className="text-brand-cyan">Techzyan Component Canvas</span>
            </div>

            <div className="space-y-4 pt-2">
              <div className="p-4 rounded-lg bg-slate-900/90 border border-slate-800">
                <div className="text-xs text-brand-cyan font-mono uppercase mb-1">Simulated Hero Section</div>
                <h4 className="text-lg font-bold text-slate-100 mb-1">{project.mockData.heroHeadline}</h4>
                <p className="text-xs text-slate-400">{project.mockData.heroSubheadline}</p>
              </div>

              <div className="grid grid-cols-3 gap-3">
                {project.mockData.metrics.map((metric, i) => (
                  <div key={i} className="p-3 rounded-lg bg-slate-900/50 border border-slate-800/80 text-center">
                    <div className="text-sm font-bold text-brand-cyan font-mono">{metric.value}</div>
                    <div className="text-[11px] text-slate-400 mt-0.5">{metric.label}</div>
                  </div>
                ))}
              </div>

              <div className="space-y-2">
                <div className="text-xs font-mono uppercase tracking-wider text-slate-400">Engineered Interface Highlights</div>
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
                  {project.mockData.uiHighlights.map((highlight, i) => (
                    <div key={i} className="p-2.5 rounded bg-slate-900/70 border border-slate-800 text-xs text-slate-300 flex items-center gap-1.5">
                      <Sparkles className="w-3.5 h-3.5 text-brand-cyan shrink-0" />
                      <span>{highlight}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

          <div className="space-y-3">
            <h3 className="text-xs font-mono uppercase tracking-wider text-slate-400 font-semibold flex items-center gap-2">
              <Layers className="w-4 h-4 text-brand-cyan" />
              <span>Full Feature Scope Built Into This Architecture</span>
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {project.keyFeatures.map((feature, i) => (
                <div key={i} className="flex items-start gap-2 text-xs text-slate-300 p-2.5 rounded-lg bg-slate-950/40 border border-slate-800/60">
                  <CheckCircle className="w-3.5 h-3.5 text-brand-cyan shrink-0 mt-0.5" />
                  <span>{feature}</span>
                </div>
              ))}
            </div>
          </div>

          <div className="space-y-2.5">
            <h3 className="text-xs font-mono uppercase tracking-wider text-slate-400 font-semibold flex items-center gap-2">
              <Cpu className="w-4 h-4 text-brand-cyan" />
              <span>Technical & Architectural Stack</span>
            </h3>
            <div className="flex flex-wrap gap-2">
              {project.architectureStack.map((tech, i) => (
                <span
                  key={i}
                  className="px-3 py-1 rounded-md bg-slate-800 border border-slate-700 text-xs font-mono text-slate-300"
                >
                  {tech}
                </span>
              ))}
            </div>
          </div>
        </div>

        <div className="p-6 border-t border-slate-800 bg-slate-950 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p className="text-xs text-slate-400 text-center sm:text-left">
            Need a similar custom solution built for your practice or business?
          </p>
          <div className="flex items-center gap-3 w-full sm:w-auto">
            <button
              onClick={onClose}
              className="w-1/2 sm:w-auto px-4 py-2 text-xs text-slate-400 hover:text-slate-200 border border-slate-800 hover:border-slate-700 rounded-lg transition-colors"
            >
              Back to Showcase
            </button>
            <button
              onClick={() => {
                onClose();
                onOpenConsultation?.();
              }}
              className="w-1/2 sm:w-auto px-4 py-2 text-xs font-semibold uppercase tracking-wider text-slate-950 bg-brand-cyan hover:bg-sky-300 rounded-lg shadow-glow-cyan transition-all"
            >
              Discuss Your Scope
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

write_file('src/components/DemonstrationModal.tsx', demonstration_modal_code)
print("All components written!")
