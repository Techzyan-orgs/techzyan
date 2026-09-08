import os

site_config_content = """import { DemonstrationProject } from '@/types';

/**
 * =========================================================================
 * CORE BASE STUDIO VARIABLES (Single Point of Declaration)
 * =========================================================================
 * Change the phone number, email, or domain once here, and the entire website
 * (display texts, tel links, WhatsApp links, and forms) updates automatically!
 */
const COUNTRY_CODE = "+91";
const PHONE_NUMBER = "8100507200";
const PRIMARY_EMAIL = "contact@techzyan.org";
const SITE_DOMAIN = "https://techzyan.org";

// Derived phone strings (computed automatically)
const PHONE_CLEAN = `${COUNTRY_CODE.replace('+', '')}${PHONE_NUMBER}`; // "918100507200"
const PHONE_RAW = `${COUNTRY_CODE}${PHONE_NUMBER}`; // "+918100507200"
const PHONE_DISPLAY = `${COUNTRY_CODE} ${PHONE_NUMBER.slice(0, 5)} ${PHONE_NUMBER.slice(5)}`; // "+91 81005 07200"

export const siteConfig = {
  name: "Techzyan",
  legalName: "Techzyan Technical Studio",
  tagline: "Understand first. Build the right digital solution second.",
  description: "Techzyan is a premium specialist technical studio based in Kolkata, India. We partner with businesses, healthcare professionals, educators, and cultural organizations to build high-performance websites and bespoke digital solutions.",
  url: SITE_DOMAIN,
  ogImage: `${SITE_DOMAIN}/og-image.jpg`,
  foundingYear: 2024,

  location: {
    city: "Kolkata",
    state: "West Bengal",
    country: "India",
    fullAddress: "Kolkata, West Bengal, India",
    regionServed: ["Kolkata", "West Bengal", "India", "Global"],
  },

  contact: {
    email: PRIMARY_EMAIL,
    phoneDisplay: PHONE_DISPLAY,
    phoneRaw: PHONE_RAW,
    whatsappDisplay: PHONE_DISPLAY,
    whatsappNumber: PHONE_CLEAN,
    whatsappLink: `https://wa.me/${PHONE_CLEAN}?text=Hi%20Techzyan%2C%20I%20would%20like%20to%20discuss%20a%20digital%20project.`,
    operatingHours: "Mon – Sat, 10:00 AM – 7:00 PM IST",
    responseGuarantee: "Direct response within 24 business hours",
  },

  socials: {
    linkedin: "https://linkedin.com/company/techzyan",
    github: "https://github.com/techzyan",
    twitter: "https://twitter.com/techzyan",
  },

  status: {
    acceptingProjects: true,
    currentSlot: "Accepting select projects for Q3/Q4 2026",
    typicalTurnaround: "10 – 20 business days for standard projects",
  },

  durgaPuja: {
    title: "Durga Puja Digital Infrastructure",
    tagline: "Digital Excellence for Heritage & Sarbojanin Festivals",
    audioPath: "/audio/dhaak.mp3",
    idolImagePath: "/images/durga-idol.png",
  },

  nav: [
    { label: "Solutions", href: "/solutions" },
    { label: "Who We Help", href: "/who-we-help" },
    { label: "Durga Puja", href: "/solutions/durga-puja", isSpecial: true },
    { label: "Work", href: "/work" },
    { label: "About", href: "/about" },
    { label: "Contact", href: "/contact" },
  ],

  footer: {
    solutions: [
      { label: "Business Websites", href: "/solutions#business-websites" },
      { label: "Doctor & Clinic Platforms", href: "/solutions#healthcare-doctor-websites" },
      { label: "Tutor & Academic Portals", href: "/solutions#education-tutor-websites" },
      { label: "Custom Appointment Tools", href: "/solutions#appointment-booking-systems" },
      { label: "Student Inquiry Systems", href: "/solutions#student-inquiry-management" },
      { label: "Durga Puja Platform", href: "/solutions/durga-puja", isSpecial: true },
    ],
    whoWeHelp: [
      { label: "Doctors & Healthcare", href: "/who-we-help#doctors-healthcare" },
      { label: "Private Tutors & Mentors", href: "/who-we-help#tutors-educators" },
      { label: "Small Businesses & Boutiques", href: "/who-we-help#local-businesses" },
      { label: "Educational Institutes", href: "/who-we-help#educational-institutes" },
      { label: "Durga Puja Committees", href: "/who-we-help#durga-puja-committees" },
      { label: "Demonstration Portfolio", href: "/work" },
    ],
  },

  helpers: {
    getWhatsAppUrl: (message: string) =>
      `https://wa.me/${PHONE_CLEAN}?text=${encodeURIComponent(message)}`,
    getTelUrl: () => `tel:${PHONE_RAW}`,
    getMailtoUrl: (subject?: string, body?: string) => {
      const params = new URLSearchParams();
      if (subject) params.append('subject', subject);
      if (body) params.append('body', body);
      const query = params.toString();
      return `mailto:${PRIMARY_EMAIL}${query ? `?${query}` : ''}`;
    },
  },

  /**
   * =========================================================================
   * DEMONSTRATION PROJECTS & PROTOTYPES (Centralized)
   * =========================================================================
   * Easily edit project names, live hyperlinks, screenshots, features, and
   * case studies right here!
   */
  demonstrations: [
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
      id: 'philomath-computer-classes',
      title: 'Philomath Computer Classes',
      shortTitle: 'Computer Education & Practical Coding Academy',
      category: 'Educational Institutions & Computer Training',
      clientType: 'Computer Academy / Training Center',
      badge: 'Live Platform',
      demoUrl: 'https://philomath.co.in',
      hasLiveSite: true,
      thumbnailImage: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80',
      summary: 'A modern educational portal with interactive course explorer, syllabus details, practical batch schedules, and direct student admission inquiry.',
      problemSolved: 'Students and parents needed clarity on course curricula (Programming, Web Development, Office Applications), practical lab timings, and an easy way to enroll without cumbersome brochures.',
      engineeredSolution: 'Engineered an intuitive academic platform with searchable department catalogs, hands-on lab schedule indicators, transparent course roadmap, and instant WhatsApp inquiry routing.',
      keyFeatures: [
        'Interactive Course & Track Explorer (Python, Web Dev, Java, Office Suites)',
        'Practical Lab Batch Timetable & Capacity Matrix',
        'Syllabus & Certification Curriculum Roadmap',
        'Faculty Profile & Doubt-Clearing Session Booking',
        'One-Click WhatsApp & Online Admission Inquiry Flow'
      ],
      mockData: {
        heroHeadline: 'Master Real-World Computing & Software Skills with Hands-On Lab Training',
        heroSubheadline: 'Industry-standard computer courses, practical batches & personalized mentorship in Kolkata.',
        metrics: [
          { label: 'Practical Focus', value: '100% Hands-On' },
          { label: 'Inquiry Response', value: 'Instant via WhatsApp' },
          { label: 'Curriculum', value: 'Job & Academic Ready' }
        ],
        uiHighlights: [
          'Course Module & Practical Duration Filter',
          'Batch Timing & Seat Vacancy Matrix',
          'Direct "Inquire for Course" Action'
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
  ] as DemonstrationProject[],
};
"""

with open('src/config/site.ts', 'w', encoding='utf-8') as f:
    f.write(site_config_content)
print("Updated src/config/site.ts with demonstration projects!")

# 2. Update src/data/demonstrations.ts to re-export siteConfig.demonstrations
demonstrations_content = """import { DemonstrationProject } from '@/types';
import { siteConfig } from '@/config/site';

/**
 * Re-exported from centralized siteConfig for backward compatibility.
 * To add, edit, or remove demo projects, edit `src/config/site.ts`!
 */
export const demonstrationProjects: DemonstrationProject[] = siteConfig.demonstrations;
"""

with open('src/data/demonstrations.ts', 'w', encoding='utf-8') as f:
    f.write(demonstrations_content)
print("Updated src/data/demonstrations.ts to point to siteConfig.demonstrations!")
