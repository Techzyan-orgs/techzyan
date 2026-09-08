import os

def write_file(rel_path, content):
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {rel_path}")

types_code = """export interface SolutionItem {
  id: string;
  category: 'website' | 'custom-tool' | 'puja-special' | 'growth';
  title: string;
  subtitle: string;
  description: string;
  audience: string[];
  deliverables: string[];
  keyFeatures: string[];
  timeline: string;
  pricingType: 'fixed-project' | 'scope-based';
  iconName: string;
  highlight?: boolean;
}

export interface AudienceItem {
  id: string;
  title: string;
  roleSubtitle: string;
  context: string;
  commonFriction: string[];
  techzyanApproach: string;
  entrySolution: string;
  expansionSolution: string;
  keyOutcomes: string[];
  iconName: string;
}

export interface DemonstrationProject {
  id: string;
  title: string;
  shortTitle: string;
  category: string;
  clientType: string;
  badge: string;
  demoUrl: string;
  hasLiveSite: boolean;
  summary: string;
  problemSolved: string;
  engineeredSolution: string;
  keyFeatures: string[];
  mockData: {
    heroHeadline: string;
    heroSubheadline: string;
    metrics: { label: string; value: string }[];
    uiHighlights: string[];
  };
}

export interface DurgaPujaFeature {
  id: string;
  title: string;
  bengaliTitle?: string;
  description: string;
  details: string[];
  iconName: string;
}

export interface SponsorTier {
  name: string;
  tagline: string;
  recommendedFor: string;
  digitalPerks: string[];
  featuredPlacement: boolean;
}
"""

write_file('src/types/index.ts', types_code)
demonstrations_code = """import { DemonstrationProject } from '@/types';

export const demonstrationProjects: DemonstrationProject[] = [
  {
    id: 'dr-aranya-sen',
    title: 'Dr. Aranya Sen — Neurologist & Clinic Platform',
    shortTitle: 'Neurology Clinic & OPD Booking',
    category: 'Healthcare & Clinical Practice',
    clientType: 'Doctor / Specialist Clinic',
    badge: 'Interactive Demo',
    demoUrl: 'https://demo-clinic.techzyan.org',
    hasLiveSite: true,
    summary: 'A fast, reassuring clinical portal with 3-step appointment triage, live OPD chamber timings, and instant WhatsApp confirmations.',
    problemSolved: 'The clinic receptionist was overwhelmed with 60+ repetitive calls every day asking for chamber timings, consultation fees, and rescheduling.',
    engineeredSolution: 'Built a calm, patient-friendly portal with a 3-step symptom-aware appointment booking system, chamber timing indicator, and direct WhatsApp routing.',
    keyFeatures: [
      '3-Step Symptom-Aware Appointment Triage Flow',
      'Real-time OPD Chamber Timing & Status Indicator',
      'Prescription Upload & Pre-Consultation Notes',
      'Instant Patient Directions with Parking & Landmark Guide',
      'One-tap Emergency Referral Contact Route'
    ],
    mockData: {
      heroHeadline: 'Specialist Neurological Care with Structured Clinical Consultations',
      heroSubheadline: 'Chamber appointments at Park Circus & Deshapriya Park, Kolkata.',
      metrics: [
        { label: 'Booking Time', value: '< 45 seconds' },
        { label: 'Reception Call Reduction', value: '70% less load' },
        { label: 'Mobile Speed', value: 'Sub-second on 4G' }
      ],
      uiHighlights: [
        'South vs Central Kolkata Chamber Switcher',
        'Morning & Evening Slot Filter',
        'Pre-consultation Symptom Checklist'
      ]
    }
  },
  {
    id: 'soma-mukherjee-math',
    title: 'Soma Mukherjee — Senior Mathematics Educator',
    shortTitle: 'Academic Mentor & Batch Portal',
    category: 'Education & Independent Tutoring',
    clientType: 'Private Tutor / Academic Mentor',
    badge: 'Interactive Demo',
    demoUrl: 'https://demo-tutor.techzyan.org',
    hasLiveSite: true,
    summary: 'A structured curriculum showcase with live batch vacancy tracking and seamless parent inquiry routing.',
    problemSolved: 'Managing student inquiries across Class 10, 11, and 12 CBSE/ISC boards was causing lost WhatsApp messages and confusion regarding seat availability.',
    engineeredSolution: 'Engineered an academic portal featuring curriculum roadmaps, live batch vacancy indicators (e.g. "3 seats left"), and a parent inquiry generator.',
    keyFeatures: [
      'Live Batch Vacancy Tracker (Class 10 / 11 / 12 / JEE)',
      'Syllabus & Past Student Board Exam Results Showcase',
      'Parent Inquiry Generator with Auto-populated Subject & Board',
      'Resource Hub for Homework & Test Schedules',
      'Doubt Clearing & Hybrid Session Guide'
    ],
    mockData: {
      heroHeadline: 'Rigorous Mathematics Mentorship for Board & Competitive Excellence',
      heroSubheadline: 'Offline batches in Gariahat & Salt Lake + Hybrid Interactive Sessions.',
      metrics: [
        { label: 'Inquiry Precision', value: '100% structured' },
        { label: 'Parent Response', value: 'Instant via WhatsApp' },
        { label: 'Mobile Experience', value: 'Zero lag on 4G' }
      ],
      uiHighlights: [
        'Interactive Class & Board Filter',
        'Live Batch Capacity Matrix',
        'Direct "Inquire for Batch" Quick Action'
      ]
    }
  },
  {
    id: 'debnath-artisans',
    title: 'Debnath Artisans & Clothiers — Heritage Boutique',
    shortTitle: 'Bespoke Tailoring & Style Lookbook',
    category: 'Retail & Bespoke Craftsmanship',
    clientType: 'Heritage Boutique / Custom Atelier',
    badge: 'Interactive Demo',
    demoUrl: 'https://demo-boutique.techzyan.org',
    hasLiveSite: true,
    summary: 'An editorial digital lookbook with visual measurement guide and private consultation booking for artisanal tailoring.',
    problemSolved: 'A 30-year-old bespoke tailoring atelier wanted to reach modern clients across Kolkata and out-of-town patrons without losing its bespoke human touch.',
    engineeredSolution: 'Designed an elegant digital boutique featuring fabric lookbooks, illustrated measurement walkthroughs, and a private fitting booking system.',
    keyFeatures: [
      'High-Resolution Editorial Fabric & Styling Lookbook',
      'Interactive Self-Measurement Visual Walkthrough',
      'Bespoke Trial & Fitting Appointment Scheduler',
      'Craftsmanship Story & Heritage Timeline',
      'Direct Artisan WhatsApp Consultation Link'
    ],
    mockData: {
      heroHeadline: 'Three Decades of Masterful Tailoring, Handcrafted in Kolkata',
      heroSubheadline: 'Bespoke suits, traditional kurtas, and handcrafted ethnic garments.',
      metrics: [
        { label: 'Client Engagement', value: 'High Visual Retention' },
        { label: 'Booking Friction', value: 'Reduced by 60%' },
        { label: 'Mobile Load Time', value: '0.4s instant paint' }
      ],
      uiHighlights: [
        'Fabric Swatch Texture Selector',
        'Silhouette Previewer (Collar, Lapel, Cut)',
        'Private Trial Slot Picker'
      ]
    }
  },
  {
    id: 'aura-institute',
    title: 'Aura Institute of Design & Media',
    shortTitle: 'Design Academy & Admissions Hub',
    category: 'Educational Institutions',
    clientType: 'Academy / Educational Institute',
    badge: 'Interactive Demo',
    demoUrl: 'https://demo-academy.techzyan.org',
    hasLiveSite: true,
    summary: 'A multi-department academic portal with interactive course explorer, digital prospectus delivery, and admissions pipeline.',
    problemSolved: 'The institute suffered from high drop-offs on their admissions page due to heavy, unreadable PDFs and fragmented registration workflows.',
    engineeredSolution: 'Constructed an intuitive academic website with searchable department catalogs, instant prospectus delivery, and a multi-step admissions inquiry tracker.',
    keyFeatures: [
      'Interactive Course & Department Filter (UI/UX, Animation, Graphic Design)',
      'Digital Prospectus Instant Delivery via Email/SMS',
      'Student Portfolio Showcase Grid with Tagging',
      'Faculty Directory & Industry Guest Lecturers',
      'Admissions Deadline Countdown & Application Checklist'
    ],
    mockData: {
      heroHeadline: 'Fostering the Next Generation of Designers, Animators & Media Artists',
      heroSubheadline: 'Admissions open for Autumn 2026 Academic Batch, Kolkata Campus.',
      metrics: [
        { label: 'Prospectus Delivery', value: 'Instant 1-Click' },
        { label: 'Application Completion', value: '3-stage guided flow' },
        { label: 'Accessibility', value: 'High contrast & readable' }
      ],
      uiHighlights: [
        'Department Grid with Duration & Eligibility Pills',
        'Curriculum Semester Breakdown',
        'Fast Application Form with Portfolio Link'
      ]
    }
  },
  {
    id: 'ballygunge-cultural-puja',
    title: 'Ballygunge Cultural Association — Durga Puja Hub',
    shortTitle: 'Sharodotsav 2026 Digital Hub & Sponsorship',
    category: 'Cultural & Community Organizations',
    clientType: 'Durga Puja & Cultural Committee',
    badge: 'Featured Showcase',
    demoUrl: 'https://demo-puja.techzyan.org',
    hasLiveSite: true,
    summary: 'An all-in-one festival guide, corporate sponsorship presentation platform, and visitor crowd management suite for Durga Puja.',
    problemSolved: 'The committee needed a dignified way to present sponsorship tiers to national brand managers and guide 50,000+ daily visitors effortlessly.',
    engineeredSolution: 'Engineered a specialized festival portal with interactive 5-day puja timetable, theme art tribute, digital sponsorship proposal builder, and metro transit guide.',
    keyFeatures: [
      '5-Day Puja Calendar (Sasthi to Dashami) with Anjali & Bhog Timings',
      'Theme & Art Philosophy Showcase with High-Res Imagery',
      'Interactive Sponsorship Tiers with Automated Proposal Request',
      'Crowd Management Guide with Nearest Metro & Parking Routes',
      'Committee & Volunteer Emergency Contact Directory'
    ],
    mockData: {
      heroHeadline: 'Celebrating 75 Years of Art, Devotion & Community Heritage',
      heroSubheadline: 'Official Digital Guide & Sponsorship Suite for Sharodotsav 2026.',
      metrics: [
        { label: 'Sponsor Leads', value: 'Structured corporate deck' },
        { label: 'Crowd Navigation', value: 'Instant metro route guide' },
        { label: 'Mobile Performance', value: 'Ultra-lightweight on 4G' }
      ],
      uiHighlights: [
        'Day-by-Day Festival Timeline Switcher',
        'Sponsorship Tier Comparison Matrix',
        'One-click Emergency & Volunteer WhatsApp Hotline'
      ]
    }
  }
];
"""

write_file('src/data/demonstrations.ts', demonstrations_code)
solutions_code = """import { SolutionItem } from '@/types';

export const solutionsData: SolutionItem[] = [
  {
    id: 'business-websites',
    category: 'website',
    title: 'High-Performance Business Websites',
    subtitle: 'Fast, credible, and built to turn visitors into real client conversations.',
    description: 'We design and craft websites with clean typography, purposeful whitespace, and crystal-clear value propositions that build immediate authority for your business.',
    audience: ['Local Businesses', 'Specialist Consultants', 'Retail Stores', 'Creative Agencies', 'Service Providers'],
    deliverables: ['Custom Web Design', 'Responsive Mobile Layout', 'Google Search & Local SEO Setup', 'Domain & Cloud Launch', '100% Code Ownership'],
    keyFeatures: [
      'Sub-second page loading on mobile networks',
      'Direct WhatsApp & phone call consultation routing',
      'Zero monthly page-builder subscription lock-in',
      'Custom visual hierarchy tailored to your brand'
    ],
    timeline: '2 – 3 weeks',
    pricingType: 'fixed-project',
    iconName: 'Globe',
    highlight: true,
  },
  {
    id: 'healthcare-doctor-websites',
    category: 'website',
    title: 'Doctor & Clinic Practice Platforms',
    subtitle: 'Authoritative, reassuring digital presence for healthcare practitioners.',
    description: 'Designed specifically for doctors and clinics who need to present chamber timings, qualifications, and clinic locations clearly while eliminating phone call clutter.',
    audience: ['Specialist Doctors', 'Polyclinics', 'Dentists', 'Therapists', 'Diagnostic Labs'],
    deliverables: ['Clinic Profile Design', 'Chamber Timing Schedule', 'Google Maps Location Guide', 'Doctor Credentials Showcase'],
    keyFeatures: [
      'Multi-chamber OPD schedule with morning/evening indicators',
      'Pre-appointment patient screening guidance',
      'One-tap emergency call & WhatsApp routing',
      'Accessible, high-contrast readable design for all age groups'
    ],
    timeline: '2 – 3 weeks',
    pricingType: 'fixed-project',
    iconName: 'Stethoscope',
    highlight: true,
  },
  {
    id: 'education-tutor-websites',
    category: 'website',
    title: 'Tutor & Educational Academy Portals',
    subtitle: 'Organized course roadmaps, batch availability, and admission inquiry flows.',
    description: 'Built for respected private tutors, coaching academies, and training institutes looking to showcase past student results and streamline batch enrollments.',
    audience: ['Private Tutors', 'Coaching Academies', 'Test Prep Mentors', 'Music & Arts Schools', 'Training Centers'],
    deliverables: ['Academic Portal Design', 'Batch Capacity Matrix', 'Syllabus Download Center', 'Direct Parent Inquiry Flow'],
    keyFeatures: [
      'Live batch vacancy indicator (e.g. "3 seats remaining")',
      'Subject & board syllabus breakdown with past results',
      'Structured parent inquiry generator pre-filling WhatsApp',
      'Clear fee and schedule transparency'
    ],
    timeline: '2 – 3 weeks',
    pricingType: 'fixed-project',
    iconName: 'GraduationCap',
  },
  {
    id: 'appointment-booking-systems',
    category: 'custom-tool',
    title: 'Smart Appointment & Scheduling Systems',
    subtitle: 'Custom booking workflows tailored to your real chamber or practice hours.',
    description: 'Unlike generic calendar plugins, we engineer lightweight booking workflows that respect your real chamber switches, patient limits, and triage requirements.',
    audience: ['Doctors & Clinics', 'Bespoke Tailors', 'Legal Consultants', 'Therapists', 'Specialist Studios'],
    deliverables: ['Patient Symptom Triage UX', 'Slot Booking Engine', 'WhatsApp & SMS Confirmation Webhook', 'Doctor Daily Schedule View'],
    keyFeatures: [
      'Multi-location chamber slot management',
      'Patient requirement screening before booking',
      'Instant WhatsApp booking confirmation notes',
      'Zero monthly per-user SaaS license fees'
    ],
    timeline: '3 – 4 weeks',
    pricingType: 'scope-based',
    iconName: 'CalendarCheck',
    highlight: true,
  },
  {
    id: 'student-inquiry-management',
    category: 'custom-tool',
    title: 'Student Inquiry & Batch Management Tools',
    subtitle: 'Eliminate lost leads and chaotic admission seasons with purpose-built tools.',
    description: 'When an institute or tutor receives hundreds of inquiries, spreadsheets cause lost leads. We build clean inquiry triage tools your staff can use in 5 minutes.',
    audience: ['Educational Institutes', 'Coaching Academies', 'Dance & Art Schools', 'Tutoring Networks'],
    deliverables: ['Inquiry Triage Dashboard', 'Batch Allocation Engine', 'WhatsApp Notification Links', 'Data Export Tools'],
    keyFeatures: [
      'Automated inquiry capture from website & social links',
      'Batch capacity status & waitlist tracking',
      'One-click WhatsApp broadcast templates for batch announcements',
      'Clutter-free, fast staff interface'
    ],
    timeline: '3 – 5 weeks',
    pricingType: 'scope-based',
    iconName: 'Users',
  },
  {
    id: 'durga-puja-digital-hub',
    category: 'puja-special',
    title: 'Durga Puja Digital Hub & Sponsorship Suite',
    subtitle: 'The premier digital solution for Kolkata & Bengal’s heritage Puja committees.',
    description: 'We build digital homes for committees that celebrate pandal art, organize 5-day festival timetables, guide thousands of visitors, and present clear corporate sponsorship tiers.',
    audience: ['Durga Puja Committees', 'Community Cultural Clubs', 'Sharodotsav Organizers', 'Heritage Trusts'],
    deliverables: ['Festival Digital Hub', 'Corporate Sponsorship Proposal Module', '5-Day Interactive Timetable', 'Visitor Metro & Crowd Map'],
    keyFeatures: [
      '5-Day interactive ritual timetable (Pushpanjali, Sandhi Puja, Bhog)',
      'Corporate sponsorship tier deck (Title, Co-Powered, Associate)',
      'Visitor crowd guide with nearest Kolkata Metro stations & VIP gates',
      'Theme concept & artist tribute gallery',
      'Emergency helpline & volunteer WhatsApp hotline'
    ],
    timeline: '2 – 3 weeks',
    pricingType: 'fixed-project',
    iconName: 'Flame',
    highlight: true,
  },
  {
    id: 'bespoke-business-tools',
    category: 'custom-tool',
    title: 'Custom Quotation & Order Intake Calculators',
    subtitle: 'Internal tools engineered around your specific operational bottleneck.',
    description: 'Sometimes you don’t need an enterprise ERP. You just need a custom price estimator, an order intake form, or a digital measurement guide that works smoothly.',
    audience: ['Manufacturing Workshops', 'Bespoke Tailors & Ateliers', 'B2B Suppliers', 'Local Distributors'],
    deliverables: ['Custom Tool UX', 'Calculation Engine', 'Customer Intake Form', 'WhatsApp/Email Notification Routing'],
    keyFeatures: [
      'Bespoke price quotation & requirement calculator',
      'Customer order & measurement intake workflows',
      'Instant summary generation for client review',
      'Direct synchronization with your existing workflow'
    ],
    timeline: '3 – 4 weeks',
    pricingType: 'scope-based',
    iconName: 'Cpu',
  },
  {
    id: 'website-modernization-speed',
    category: 'growth',
    title: 'Website Modernization & Speed Optimization',
    subtitle: 'Transform slow, outdated websites into sub-second, mobile-first platforms.',
    description: 'If your existing website was built years ago on bloated page builders, we rebuild it with modern standards, sub-second mobile loading, and complete SEO foundations.',
    audience: ['Existing Businesses', 'Clinics with Outdated Sites', 'Established Institutes'],
    deliverables: ['Complete Code Overhaul', 'Mobile Performance Optimization', 'SEO Audit & Redirects', 'Cloud Migration'],
    keyFeatures: [
      'Sub-second mobile loading speed guarantee',
      'Clean typography and modern visual hierarchy',
      'Google Local Search and SEO structured markup',
      '100% code ownership with zero lock-in'
    ],
    timeline: '1 – 2 weeks',
    pricingType: 'fixed-project',
    iconName: 'Zap',
  }
];
"""

write_file('src/data/solutions.ts', solutions_code)
puja_modal_code = """'use client';

import React, { useState, useEffect } from 'react';
import { X, Sparkles, Flame, CheckCircle2, MessageCircle, Mail, Phone, ArrowRight, MapPin, Award } from 'lucide-react';
import { siteConfig } from '@/config/site';

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
      window.open(`https://wa.me/919876543210?text=${encodeURIComponent(text)}`, '_blank');
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
                    { id: 'WhatsApp', label: 'WhatsApp', icon: MessageCircle },
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
"""

write_file('src/components/PujaConsultationModal.tsx', puja_modal_code)
demo_modal_code = """'use client';

import React, { useEffect } from 'react';
import { X, CheckCircle, Sparkles, ExternalLink, ArrowRight, ShieldCheck, Layers } from 'lucide-react';
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
      <div className="relative w-full max-w-3xl bg-slate-900 border border-slate-700/80 rounded-3xl shadow-2xl overflow-hidden text-slate-200 max-h-[92vh] flex flex-col">
        {/* Top Header */}
        <div className="p-6 border-b border-slate-800 flex items-start justify-between bg-slate-950/80">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-2">
              <span className="px-2.5 py-0.5 rounded-full text-[10px] font-mono uppercase tracking-wider bg-sky-500/10 text-brand-cyan border border-sky-500/30 font-semibold">
                {project.badge}
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

        {/* Scrollable Content */}
        <div className="p-6 sm:p-8 overflow-y-auto space-y-6">
          {/* Live Demo Banner Action */}
          <div className="p-4 rounded-2xl bg-gradient-to-r from-sky-950/40 via-slate-900 to-sky-950/30 border border-brand-cyan/30 flex flex-col sm:flex-row sm:items-center justify-between gap-4 shadow-sm">
            <div>
              <div className="text-xs font-mono uppercase text-brand-cyan font-semibold flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Interactive Demonstration Experience</span>
              </div>
              <p className="text-xs text-slate-300 mt-1">
                Explore the live interface flow, test user interactions, and review the design in action.
              </p>
            </div>
            <a
              href={project.demoUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center justify-center gap-2 px-5 py-2.5 bg-brand-cyan hover:bg-sky-300 text-slate-950 text-xs font-bold uppercase tracking-wider rounded-xl shadow-glow-cyan transition-all shrink-0"
            >
              <span>Launch Live Demo</span>
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </div>

          {/* Problem vs Solution Summary */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="p-5 rounded-2xl bg-slate-950/60 border border-slate-800 space-y-2">
              <div className="text-xs font-mono uppercase tracking-wider text-rose-400 font-semibold">
                The Real Operational Challenge
              </div>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                {project.problemSolved}
              </p>
            </div>

            <div className="p-5 rounded-2xl bg-slate-950/60 border border-slate-800 space-y-2">
              <div className="text-xs font-mono uppercase tracking-wider text-emerald-400 font-semibold">
                What We Engineered
              </div>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                {project.engineeredSolution}
              </p>
            </div>
          </div>

          {/* Key Deliverables & Capabilities */}
          <div className="space-y-3">
            <h3 className="text-xs font-mono uppercase tracking-wider text-slate-300 font-semibold flex items-center gap-2">
              <Layers className="w-4 h-4 text-brand-cyan" />
              <span>Key Features Built Into This Solution</span>
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
              {project.keyFeatures.map((feature, i) => (
                <div key={i} className="flex items-start gap-2.5 text-xs text-slate-200 p-3 rounded-xl bg-slate-950/40 border border-slate-800">
                  <CheckCircle className="w-4 h-4 text-brand-cyan shrink-0 mt-0.5" />
                  <span>{feature}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Target Performance & Business Impact */}
          <div className="grid grid-cols-3 gap-3 pt-2">
            {project.mockData.metrics.map((metric, i) => (
              <div key={i} className="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800 text-center">
                <div className="text-sm sm:text-base font-bold text-brand-cyan font-mono">{metric.value}</div>
                <div className="text-[11px] text-slate-400 mt-0.5">{metric.label}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Footer Actions */}
        <div className="p-6 border-t border-slate-800 bg-slate-950 flex flex-col sm:flex-row items-center justify-between gap-3">
          <p className="text-xs text-slate-400 text-center sm:text-left">
            Need a similar custom solution for your practice or business?
          </p>
          <div className="flex items-center gap-3 w-full sm:w-auto">
            <button
              onClick={onClose}
              className="w-1/2 sm:w-auto px-4 py-2.5 text-xs text-slate-400 hover:text-slate-200 border border-slate-800 hover:border-slate-700 rounded-xl transition-colors"
            >
              Close
            </button>
            <button
              onClick={() => {
                onClose();
                onOpenConsultation?.();
              }}
              className="w-1/2 sm:w-auto px-5 py-2.5 text-xs font-semibold uppercase tracking-wider text-slate-950 bg-brand-cyan hover:bg-sky-300 rounded-xl shadow-glow-cyan transition-all"
            >
              Discuss Your Project
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
"""

write_file('src/components/DemonstrationModal.tsx', demo_modal_code)
