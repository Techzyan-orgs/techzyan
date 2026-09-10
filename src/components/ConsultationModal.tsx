'use client';

import React, { useState, useEffect } from 'react';
import { X, Mail, Phone, CheckCircle2, Sparkles, ArrowRight } from 'lucide-react';
import { siteConfig } from '@/config/site';
import WhatsAppIcon from '@/components/WhatsAppIcon';

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
      window.open(siteConfig.helpers.getWhatsAppUrl(text), '_blank');
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
                    { id: 'WhatsApp', icon: WhatsAppIcon, label: 'WhatsApp' },
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
