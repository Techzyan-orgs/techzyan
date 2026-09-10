'use client';

import React, { useState, useEffect } from 'react';
import { X, Sparkles, Flame, CheckCircle2, Mail, Phone, ArrowRight, MapPin, Award } from 'lucide-react';
import { siteConfig } from '@/config/site';
import WhatsAppIcon from '@/components/WhatsAppIcon';

interface PujaConsultationModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function PujaConsultationModal({ isOpen, onClose }: PujaConsultationModalProps) {
  const [formData, setFormData] = useState({
    committeeName: '',
    zone: 'South Kolkata',
    contactPerson: '',
    designation: 'General Secretary',
    contactMethod: 'WhatsApp',
    contactValue: '',
    selectedPriorities: ['Corporate Sponsorship Deck', '5-Day Ritual & Anjali Schedule'],
    notes: '',
  });

  const [submitted, setSubmitted] = useState(false);

  const prioritiesList = [
    'Corporate Sponsorship Deck & Tiers',
    '5-Day Ritual & Pushpanjali Timetable',
    'Visitor Metro & Crowd Navigation Map',
    'Theme Concept & Artist/Sculptor Tribute',
    'Online UPI QR & Donation Gateway',
    'Committee Directory & Emergency Hotline',
  ];

  const togglePriority = (priority: string) => {
    setFormData(prev => {
      const exists = prev.selectedPriorities.includes(priority);
      return {
        ...prev,
        selectedPriorities: exists
          ? prev.selectedPriorities.filter(p => p !== priority)
          : [...prev.selectedPriorities, priority]
      };
    });
  };

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
      const prioritiesText = formData.selectedPriorities.join(', ');
      const text = `Hi Techzyan! We are from ${formData.committeeName || 'our Durga Puja Committee'} (${formData.zone}). Contact: ${formData.contactPerson || 'Committee Executive'} (${formData.designation}). We want to build: ${prioritiesText}. Notes: ${formData.notes || 'Looking forward to discussing.'}`;
      window.open(siteConfig.helpers.getWhatsAppUrl(text), '_blank');
    }
    setSubmitted(true);
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/85 backdrop-blur-md animate-in fade-in duration-200"
      role="dialog"
      aria-modal="true"
      aria-labelledby="puja-modal-title"
    >
      <div className="relative w-full max-w-xl bg-[#120D08] border border-amber-500/40 rounded-3xl shadow-2xl overflow-hidden text-slate-200 max-h-[92vh] flex flex-col">
        {/* Header */}
        <div className="p-6 border-b border-amber-500/25 flex items-center justify-between bg-[#1A120B]">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-xl bg-amber-500/20 text-amber-400 border border-amber-500/30">
              <Flame className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-1.5 text-[11px] font-mono uppercase tracking-wider text-amber-400 font-semibold">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Sharodotsav 2026 Committee Desk</span>
              </div>
              <h2 id="puja-modal-title" className="text-lg sm:text-xl font-display font-bold text-amber-100 mt-0.5">
                Discuss Your Puja Digital Platform
              </h2>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-2 text-amber-300/70 hover:text-amber-100 hover:bg-amber-950/60 rounded-lg transition-colors"
            aria-label="Close modal"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 sm:p-8 overflow-y-auto space-y-6">
          {submitted ? (
            <div className="py-10 text-center space-y-4">
              <div className="w-16 h-16 bg-amber-500/15 border border-amber-500/40 text-amber-400 rounded-full flex items-center justify-center mx-auto">
                <CheckCircle2 className="w-8 h-8" />
              </div>
              <h3 className="text-xl font-bold text-amber-100">Committee Requirement Received!</h3>
              <p className="text-slate-300 text-sm max-w-md mx-auto leading-relaxed">
                Thank you for reaching out from <strong>{formData.committeeName || 'your committee'}</strong>. Our specialized cultural engineering team will review your requirements and reach out via {formData.contactMethod} within a few hours.
              </p>
              <div className="pt-4">
                <button
                  onClick={() => {
                    setSubmitted(false);
                    onClose();
                  }}
                  className="px-6 py-2.5 bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl transition-all shadow-glow-gold"
                >
                  Close Window
                </button>
              </div>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <p className="text-xs text-amber-200/80 leading-relaxed">
                Tell us about your committee's pandal theme, schedule, and sponsorship requirements. We will prepare a tailored proposal.
              </p>

              {/* Committee Name & Zone */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
                    Puja / Committee Name *
                  </label>
                  <input
                    type="text"
                    required
                    value={formData.committeeName}
                    onChange={(e) => setFormData({ ...formData, committeeName: e.target.value })}
                    placeholder="e.g. Ballygunge Cultural / Bagbazar"
                    className="w-full px-3.5 py-2.5 bg-black/60 border border-amber-500/30 rounded-xl text-sm text-slate-100 placeholder:text-slate-600 focus:border-amber-400 focus:ring-1 focus:ring-amber-400"
                  />
                </div>
                <div>
                  <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
                    Kolkata Zone / Location
                  </label>
                  <select
                    value={formData.zone}
                    onChange={(e) => setFormData({ ...formData, zone: e.target.value })}
                    className="w-full px-3.5 py-2.5 bg-black/60 border border-amber-500/30 rounded-xl text-sm text-slate-100 focus:border-amber-400 focus:ring-1 focus:ring-amber-400"
                  >
                    <option value="South Kolkata">South Kolkata</option>
                    <option value="North Kolkata">North Kolkata</option>
                    <option value="Central Kolkata">Central Kolkata</option>
                    <option value="Salt Lake & New Town">Salt Lake & New Town</option>
                    <option value="Howrah">Howrah</option>
                    <option value="Pan-Bengal / Other">Pan-Bengal / Other</option>
                  </select>
                </div>
              </div>

              {/* Contact Person & Designation */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
                    Contact Person Name *
                  </label>
                  <input
                    type="text"
                    required
                    value={formData.contactPerson}
                    onChange={(e) => setFormData({ ...formData, contactPerson: e.target.value })}
                    placeholder="e.g. Sourav Mukherjee"
                    className="w-full px-3.5 py-2.5 bg-black/60 border border-amber-500/30 rounded-xl text-sm text-slate-100 placeholder:text-slate-600 focus:border-amber-400 focus:ring-1 focus:ring-amber-400"
                  />
                </div>
                <div>
                  <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
                    Committee Role / Designation
                  </label>
                  <select
                    value={formData.designation}
                    onChange={(e) => setFormData({ ...formData, designation: e.target.value })}
                    className="w-full px-3.5 py-2.5 bg-black/60 border border-amber-500/30 rounded-xl text-sm text-slate-100 focus:border-amber-400 focus:ring-1 focus:ring-amber-400"
                  >
                    <option value="General Secretary">General Secretary</option>
                    <option value="President">President</option>
                    <option value="Joint Secretary">Joint Secretary</option>
                    <option value="Treasurer">Treasurer</option>
                    <option value="Digital / Sponsorship In-charge">Digital / Sponsorship In-charge</option>
                    <option value="Executive Member">Executive Member</option>
                  </select>
                </div>
              </div>

              {/* What your committee needs */}
              <div>
                <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
                  What would you like built for your Puja? (Select all that apply)
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                  {prioritiesList.map((priority) => {
                    const isSelected = formData.selectedPriorities.includes(priority);
                    return (
                      <button
                        type="button"
                        key={priority}
                        onClick={() => togglePriority(priority)}
                        className={`text-left p-2.5 rounded-xl border text-xs flex items-center gap-2 transition-all ${
                          isSelected
                            ? 'bg-amber-500/20 border-amber-400 text-amber-200 font-semibold shadow-sm'
                            : 'bg-black/40 border-amber-500/20 text-slate-400 hover:text-slate-200'
                        }`}
                      >
                        <CheckCircle2 className={`w-4 h-4 shrink-0 ${isSelected ? 'text-amber-400' : 'text-slate-600'}`} />
                        <span>{priority}</span>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Preferred Contact Channel */}
              <div>
                <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
                  Preferred Contact Mode
                </label>
                <div className="grid grid-cols-3 gap-2.5">
                  {[
                    { id: 'WhatsApp', label: 'WhatsApp', icon: WhatsAppIcon },
                    { id: 'Phone', label: 'Phone Call', icon: Phone },
                    { id: 'Email', label: 'Email', icon: Mail },
                  ].map((method) => {
                    const isSelected = formData.contactMethod === method.id;
                    const Icon = method.icon;
                    return (
                      <button
                        type="button"
                        key={method.id}
                        onClick={() => setFormData({ ...formData, contactMethod: method.id })}
                        className={`flex items-center justify-center gap-1.5 p-2.5 rounded-xl border text-xs font-medium transition-all ${
                          isSelected
                            ? 'bg-amber-500/20 border-amber-400 text-amber-300 font-semibold'
                            : 'bg-black/40 border-amber-500/20 text-slate-400 hover:text-slate-200'
                        }`}
                      >
                        <Icon className="w-3.5 h-3.5" />
                        <span>{method.label}</span>
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Contact Value */}
              <div>
                <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
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
                      ? 'e.g. committee@puja.org'
                      : 'e.g. +91 98300 XXXXX'
                  }
                  className="w-full px-3.5 py-2.5 bg-black/60 border border-amber-500/30 rounded-xl text-sm text-slate-100 placeholder:text-slate-600 focus:border-amber-400 focus:ring-1 focus:ring-amber-400"
                />
              </div>

              {/* Notes */}
              <div>
                <label className="block text-xs font-mono uppercase text-amber-300/80 mb-1.5 font-medium">
                  Pandal Theme or Specific Requirement (Optional)
                </label>
                <textarea
                  rows={2}
                  value={formData.notes}
                  onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                  placeholder="e.g. We are celebrating our 50th year and need a corporate sponsorship presentation ready by July..."
                  className="w-full px-3.5 py-2.5 bg-black/60 border border-amber-500/30 rounded-xl text-sm text-slate-100 placeholder:text-slate-600 focus:border-amber-400 focus:ring-1 focus:ring-amber-400 resize-none"
                />
              </div>

              <div className="pt-2">
                <button
                  type="submit"
                  className="w-full flex items-center justify-center gap-2 py-3.5 px-4 bg-amber-500 hover:bg-amber-400 active:bg-amber-600 text-slate-950 font-bold text-xs uppercase tracking-wider rounded-xl shadow-glow-gold transition-all"
                >
                  <span>
                    {formData.contactMethod === 'WhatsApp'
                      ? 'Continue to WhatsApp Committee Discussion'
                      : 'Submit Committee Request to Techzyan'}
                  </span>
                  <ArrowRight className="w-4 h-4" />
                </button>
              </div>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
