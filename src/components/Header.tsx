'use client';

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
  );
}
