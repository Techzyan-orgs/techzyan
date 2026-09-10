'use client';

import React, { useState } from 'react';
import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { siteConfig } from '@/config/site';
import {
  Mail,
  Phone,
  Clock,
  MapPin,
  Sparkles,
  Send,
  CheckCircle2,
  ShieldCheck,
  ArrowRight,
} from 'lucide-react';
import WhatsAppIcon from '@/components/WhatsAppIcon';

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    organization: '',
    category: 'Growing Business',
    contactMethod: 'WhatsApp',
    contactValue: '',
    requirementNote: '',
  });

  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (formData.contactMethod === 'WhatsApp') {
      const text = `Hi Techzyan! My name is ${formData.name || 'a visitor'} from ${formData.organization || 'my organization'}. Category: ${formData.category}. Note: ${formData.requirementNote || 'Would love to discuss details.'}`;
      window.open(siteConfig.helpers.getWhatsAppUrl(text), '_blank');
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
                    <WhatsAppIcon className="w-4 h-4" />
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
                        <option value="Growing Business">Growing Business</option>
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
                          { id: 'WhatsApp', label: 'WhatsApp', icon: WhatsAppIcon },
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
                        {formData.contactMethod === 'Email'
                          ? 'Your Email ID *'
                          : formData.contactMethod === 'WhatsApp'
                          ? 'Your WhatsApp Number *'
                          : 'Your Phone Number *'}
                      </label>
                      <input
                        type={formData.contactMethod === 'Email' ? 'email' : 'tel'}
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
