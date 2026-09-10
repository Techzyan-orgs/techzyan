import React from 'react';
import Link from 'next/link';
import { siteConfig } from '@/config/site';
import { Sparkles, ArrowUpRight, Mail, Phone, MapPin, Clock, ShieldCheck } from 'lucide-react';
import WhatsAppIcon from '@/components/WhatsAppIcon';

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
              <span>{siteConfig.location.fullAddress}</span>
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
                “We understand your requirement first, then build the right digital solution.” Zero fake metrics, zero bloated templates.
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
                  <WhatsAppIcon className="w-4 h-4 text-emerald-400 shrink-0" />
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
          <p>© {new Date().getFullYear()} {siteConfig.legalName}. All rights reserved.</p>
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
