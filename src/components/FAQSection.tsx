import React from 'react';
import { HelpCircle, ChevronDown } from 'lucide-react';

export interface FAQItem {
  question: string;
  answer: string;
}

interface FAQSectionProps {
  title: string;
  subtitle?: string;
  badge?: string;
  items: FAQItem[];
  id?: string;
  theme?: 'dark' | 'amber';
}

export function generateFaqSchema(items: FAQItem[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: items.map((item) => ({
      '@type': 'Question',
      name: item.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: item.answer,
      },
    })),
  };
}

export default function FAQSection({
  title,
  subtitle,
  badge = 'Common Questions',
  items,
  id = 'faq',
  theme = 'dark',
}: FAQSectionProps) {
  const isAmber = theme === 'amber';

  return (
    <section id={id} className="py-16 lg:py-24 border-t border-slate-800/80 relative">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-12">
          <div
            className={`inline-flex items-center gap-2 px-3 py-1 rounded-full text-xs font-mono mb-3 ${
              isAmber
                ? 'bg-amber-500/15 border border-amber-500/40 text-amber-300'
                : 'bg-sky-500/10 border border-sky-500/30 text-brand-cyan'
            }`}
          >
            <HelpCircle className="w-3.5 h-3.5" />
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

        <div className="space-y-4">
          {items.map((item, index) => (
            <details
              key={index}
              name={`faq-${id}`}
              className={`group rounded-2xl border transition-all duration-200 overflow-hidden ${
                isAmber
                  ? 'bg-amber-950/20 border-amber-500/20 hover:border-amber-500/40 open:border-amber-500/60 open:bg-amber-950/40'
                  : 'bg-slate-900/60 border-slate-800 hover:border-slate-700 open:border-brand-cyan/50 open:bg-slate-900/90'
              }`}
            >
              <summary className="flex items-center justify-between gap-4 p-5 sm:p-6 cursor-pointer list-none select-none focus:outline-none">
                <span className="text-sm sm:text-base font-medium text-slate-200 group-open:text-white transition-colors">
                  {item.question}
                </span>
                <span
                  className={`p-1 rounded-lg shrink-0 transition-transform duration-300 group-open:rotate-180 ${
                    isAmber
                      ? 'bg-amber-500/10 text-amber-400'
                      : 'bg-slate-800 text-slate-400 group-open:text-brand-cyan'
                  }`}
                >
                  <ChevronDown className="w-4 h-4" />
                </span>
              </summary>
              <div className="px-5 pb-5 sm:px-6 sm:pb-6 pt-1 text-sm text-slate-400 leading-relaxed border-t border-slate-800/40 mt-1">
                {item.answer}
              </div>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}
