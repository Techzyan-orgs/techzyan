import os

def write_file(rel_path, content):
    d = os.path.dirname(rel_path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated: {rel_path}")

next_config = """/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'images.unsplash.com',
      },
    ],
  },
};

export default nextConfig;
"""

write_file('next.config.mjs', next_config)

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
  thumbnailImage: string;
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
    thumbnailImage: 'https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=800&q=80',
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
    thumbnailImage: 'https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=800&q=80',
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
    thumbnailImage: 'https://images.unsplash.com/photo-1594938298603-c8148c4dae35?auto=format&fit=crop&w=800&q=80',
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
    thumbnailImage: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=800&q=80',
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
    thumbnailImage: 'https://images.unsplash.com/photo-1601058268499-e52658b8bb88?auto=format&fit=crop&w=800&q=80',
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
print("All files updated with images successfully!")
