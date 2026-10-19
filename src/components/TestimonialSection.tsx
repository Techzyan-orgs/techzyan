import React from 'react';
import { Quote, CheckCircle2, ShieldCheck, Sparkles, Building2, Send } from 'lucide-react';
import { testimonials as defaultTestimonials } from '@/data/testimonials';
import { TestimonialItem } from '@/types';

interface TestimonialSectionProps {
  testimonial?: TestimonialItem;
  theme?: 'amber' | 'cyan';
  badge?: string;
  title?: string;
  subtitle?: string;
  id?: string;
}

export default function TestimonialSection({
  testimonial = defaultTestimonials[0],
  theme = 'cyan',
  badge = 'Client Endorsement',
  title = 'Real-World Impact & Client Appreciation',
  subtitle = 'How our custom engineering transformed operations and reduced costs for our clients in Kolkata.',
  id = 'testimonials',
}: TestimonialSectionProps) {
  const isAmber = theme === 'amber';

  return (
    <section id={id} className="py-16 lg:py-24 border-t border-slate-800/80 relative overflow-hidden">
      {/* Background Ambient Glow */}
      <div
        className={`absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[350px] rounded-full blur-[120px] pointer-events-none -z-10 ${
          isAmber ? 'bg-amber-500/10' : 'bg-sky-500/10'
        }`}
      />

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-2xl mx-auto mb-10 sm:mb-12">
          <div
            className={`inline-flex items-center gap-2 px-3.5 py-1 rounded-full text-xs font-mono mb-3 ${
              isAmber
                ? 'bg-amber-500/15 border border-amber-500/40 text-amber-300'
                : 'bg-sky-500/10 border border-sky-500/30 text-brand-cyan'
            }`}
          >
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>{badge}</span>
          </div>
          <h2 className="text-2xl sm:text-3xl lg:text-4xl font-display font-bold text-slate-100 tracking-tight">
            {title}
          </h2>
          {subtitle && (
            <p className="mt-3 text-sm sm:text-base text-slate-400 leading-relaxed">
              {subtitle}
            </p>
          )}
        </div>

        {/* Testimonial Card */}
        <div
          className={`rounded-3xl p-6 sm:p-10 lg:p-12 relative overflow-hidden border backdrop-blur-md transition-all ${
            isAmber
              ? 'bg-gradient-to-b from-[#1C150C]/90 via-[#130E07]/95 to-[#0A0704] border-amber-500/35 shadow-glow-gold'
              : 'bg-gradient-to-b from-slate-900/90 via-slate-950/95 to-slate-950 border-slate-800 hover:border-brand-cyan/40 shadow-2xl'
          }`}
        >
          {/* Subtle Watermark Quote Mark */}
          <div className="absolute -top-6 -right-6 text-slate-800/20 pointer-events-none select-none">
            <Quote className={`w-40 h-40 ${isAmber ? 'text-amber-500/5' : 'text-sky-500/5'}`} />
          </div>

          {/* Top Metadata Row */}
          <div className="flex flex-wrap items-center justify-between gap-3 pb-6 border-b border-slate-800/80">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-mono font-medium">
              <CheckCircle2 className="w-3.5 h-3.5" />
              <span>{testimonial.badge}</span>
            </div>
            <div className="text-xs font-mono text-slate-400 flex items-center gap-1.5">
              <Building2 className="w-3.5 h-3.5 text-slate-500" />
              <span>{testimonial.projectScope}</span>
            </div>
          </div>

          {/* Letter Body */}
          <div className="py-6 sm:py-8 space-y-4 text-sm sm:text-base text-slate-300 leading-relaxed">
            <p className={`font-semibold font-display text-base sm:text-lg ${isAmber ? 'text-amber-200' : 'text-slate-100'}`}>
              {testimonial.salutation}
            </p>

            {testimonial.paragraphs.map((para, idx) => (
              <p key={idx}>
                {para}
              </p>
            ))}
          </div>

          {/* Key Impact Metrics / Deliverables */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 py-4 border-y border-slate-800/80 my-2">
            <div className="p-3.5 rounded-xl bg-black/40 border border-slate-800/60 flex items-start gap-2.5">
              <Send className={`w-4 h-4 mt-0.5 shrink-0 ${isAmber ? 'text-amber-400' : 'text-brand-cyan'}`} />
              <div>
                <div className="text-xs font-bold text-slate-200">SMS Digital Receipts</div>
                <div className="text-[11px] text-slate-400">Instant delivery to all housing society residents</div>
              </div>
            </div>
            <div className="p-3.5 rounded-xl bg-black/40 border border-slate-800/60 flex items-start gap-2.5">
              <CheckCircle2 className="w-4 h-4 mt-0.5 shrink-0 text-emerald-400" />
              <div>
                <div className="text-xs font-bold text-slate-200">Considerable Cost Savings</div>
                <div className="text-[11px] text-slate-400">Eliminated physical receipt printing overhead</div>
              </div>
            </div>
            <div className="p-3.5 rounded-xl bg-black/40 border border-slate-800/60 flex items-start gap-2.5">
              <Sparkles className={`w-4 h-4 mt-0.5 shrink-0 ${isAmber ? 'text-amber-400' : 'text-brand-cyan'}`} />
              <div>
                <div className="text-xs font-bold text-slate-200">Real-Time Data Analytics</div>
                <div className="text-[11px] text-slate-400">Efficient collection tracking for faster decisions</div>
              </div>
            </div>
          </div>

          {/* Signature Block */}
          <div className="pt-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="space-y-1">
              <div className="text-xs font-mono uppercase tracking-wider text-slate-400">Best regards,</div>
              <div className={`text-lg font-bold font-display ${isAmber ? 'text-amber-100' : 'text-slate-100'}`}>
                {testimonial.clientName}
              </div>
              <div className="text-xs text-slate-300 font-medium">
                {testimonial.designation}, {testimonial.committee}
              </div>
              <div className="text-xs font-mono text-slate-400">
                {testimonial.organization}
              </div>
            </div>

            <div
              className={`inline-flex items-center gap-2 px-3.5 py-1.5 rounded-xl text-xs font-mono self-start sm:self-end ${
                isAmber
                  ? 'bg-amber-500/10 border border-amber-500/20 text-amber-300'
                  : 'bg-slate-900 border border-slate-800 text-slate-400'
              }`}
            >
              <Quote className="w-3.5 h-3.5" />
              <span>Official Letter of Appreciation</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
