import { DemonstrationProject } from '@/types';

/**
 * =========================================================================
 * CORE BASE STUDIO VARIABLES (Single Point of Declaration)
 * =========================================================================
 * Change the phone number, email, or domain once here, and the entire website
 * (display texts, tel links, WhatsApp links, and forms) updates automatically!
 */
const COUNTRY_CODE = "+91";
const PHONE_NUMBER = "7439303013";
const PRIMARY_EMAIL = "contact@techzyan.org";
const SITE_DOMAIN = "https://techzyan.org";

// Derived phone strings (computed automatically)
const PHONE_CLEAN = `${COUNTRY_CODE.replace('+', '')}${PHONE_NUMBER}`; // "917439303013"
const PHONE_RAW = `${COUNTRY_CODE}${PHONE_NUMBER}`; // "+917439303013"
const PHONE_DISPLAY = `${COUNTRY_CODE}-${PHONE_NUMBER}`; // "+91-7439303013"

export const siteConfig = {
  name: "Techzyan",
  legalName: "Techzyan Technical Studio",
  tagline: "Websites & IT solutions that work for your business.",
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
      { label: "Growing Businesses", href: "/who-we-help#local-businesses" },
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
   * DEMONSTRATION & LIVE PROJECTS (Centralized)
   * =========================================================================
   */
  demonstrations: [
    {
      id: 'dr-aranya-sen',
      title: 'Dr. Aranya Sen — Neurologist & Clinic Platform',
      shortTitle: 'Neurology Clinic & OPD Booking',
      category: 'Healthcare & Clinical Practice',
      clientType: 'Doctor / Specialist Clinic',
      badge: 'Demo',
      demoUrl: 'https://demo-dr-aranya-sen-clinic.vercel.app',
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
      id: 'subhashish-banerjee-tutor',
      title: 'Prof. Subhashish Banerjee — Physics & Mathematics Tutor',
      shortTitle: 'Senior Academic Mentor & Board Guidance',
      category: 'Education & Independent Mentorship',
      clientType: 'Senior Educator / Academic Mentor',
      badge: 'Demo',
      demoUrl: 'https://demo-tutor-subhashish-banerjee.vercel.app',
      hasLiveSite: true,
      thumbnailImage: '/images/subhashish-tutor.jpg',
      summary: '16+ years of dedicated academic mentorship for ICSE, ISC, and CBSE students (Classes 9–12) with small 8-student batches and diagnostic feedback.',
      problemSolved: 'Managing student inquiries across Class 9–12 ICSE, ISC, and CBSE boards was causing lost WhatsApp messages and confusion regarding batch capacity.',
      engineeredSolution: 'Engineered an academic portal featuring curriculum roadmaps, small batch vacancy indicators, and parent diagnostic feedback tracking.',
      keyFeatures: [
        'Curriculum Roadmap for ICSE, ISC, and CBSE (Classes 9–12)',
        'Small 8-Student Batch Vacancy & Schedule Indicator',
        'Bi-Weekly Parent Diagnostic Feedback System',
        'Past Student Board Exam Results & Merit List',
        'Direct WhatsApp & Consultation Routing'
      ],
      mockData: {
        heroHeadline: 'Rigorous Physics & Mathematics Mentorship for Board Excellence',
        heroSubheadline: 'Ballygunge South Kolkata batches + Diagnostic Feedback.',
        metrics: [
          { label: 'Batch Size', value: 'Max 8 Students' },
          { label: 'Parent Feedback', value: 'Bi-Weekly' },
          { label: 'Experience', value: '16+ Years' }
        ],
        uiHighlights: [
          'Interactive Class & Board Filter',
          'Small Batch Capacity Matrix',
          'Direct Inquire for Batch Quick Action'
        ]
      }
    },
    {
      id: 'xyz-ladies-tailors',
      title: 'XYZ Ladies Tailors',
      shortTitle: 'Bespoke Ladies Tailoring & Style Lookbook',
      category: 'Retail & Custom Ladies Tailoring',
      clientType: 'Ladies Tailor / Custom Atelier',
      badge: 'Demo',
      demoUrl: 'https://demo-xyz-ladies-tailor.vercel.app',
      hasLiveSite: true,
      thumbnailImage: '/images/ladies_tailor.jpg',
      summary: 'An editorial digital lookbook with visual measurement guide and private consultation booking for bespoke ladies tailoring.',
      problemSolved: 'A well-established ladies tailoring atelier wanted to reach modern clients across Kolkata with digital lookbooks, neckline/sleeve designs, and fitting appointments.',
      engineeredSolution: 'Designed an elegant digital boutique featuring fabric lookbooks, illustrated measurement walkthroughs, custom blouse/kurti pattern previews, and a private fitting booking system.',
      keyFeatures: [
        'High-Resolution Editorial Fabric & Ladies Styling Lookbook',
        'Interactive Self-Measurement Visual Walkthrough',
        'Bespoke Trial & Fitting Appointment Scheduler',
        'Custom Pattern & Cut Previewer (Blouse, Kurti, Lehenga, Gown)',
        'Direct Master Tailor WhatsApp Consultation Link'
      ],
      mockData: {
        heroHeadline: 'Masterful Custom Ladies Tailoring & Bespoke Styling in Kolkata',
        heroSubheadline: 'Bespoke blouses, designer kurtis, ethnic suits, and handcrafted bridal wear.',
        metrics: [
          { label: 'Client Engagement', value: 'High Visual Retention' },
          { label: 'Booking Friction', value: 'Reduced by 60%' },
          { label: 'Mobile Load Time', value: '0.4s instant paint' }
        ],
        uiHighlights: [
          'Fabric Swatch & Embroidery Selector',
          'Neckline & Sleeve Silhouette Previewer',
          'Private Trial Slot Picker'
        ]
      }
    },
    {
      id: 'philomath-computer-classes',
      title: 'Philomath Computer Classes',
      shortTitle: 'ICSE, ISC & CBSE Computer Science Portal',
      category: 'Education & Computer Science Mentorship',
      clientType: 'Computer Training Academy / Academic Guidance',
      badge: 'Live Website',
      demoUrl: 'https://philomath.co.in',
      hasLiveSite: true,
      thumbnailImage: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=800&q=80',
      summary: 'A comprehensive academic portal for ICSE, ISC, and CBSE Computer Science students featuring concept-based curricula, printed notes support, and star achiever board results.',
      problemSolved: 'Students and parents across Kolkata needed structured guidance for ICSE/ISC Java and CBSE Python, along with transparent board results, notes support, and direct contact.',
      engineeredSolution: 'Built a high-performance, mobile-first academic platform showcasing Class 8-12 curricula (Java, Python, Digital Electronics, Data Structures), chapterwise printed notes system, and a star achiever board showcase.',
      keyFeatures: [
        'ICSE Computer Applications (Classes VIII – X) with Java & Logic Building',
        'ISC Computer Science (Classes XI & XII) with Digital Electronics & Data Structures',
        'CBSE Computer Science (Classes XI & XII) with Python Focus',
        'Star Achievers & Board Toppers Showcase (100/100 in ICSE Computer Applications)',
        'Concept-Based Learning, Printed Notes & Consistent Practice System'
      ],
      mockData: {
        heroHeadline: 'Quality Computer Education for a Bright Future',
        heroSubheadline: 'Expert guidance for ICSE, ISC and CBSE Computer Science students in Kolkata.',
        metrics: [
          { label: 'Top ICSE Score', value: '100 / 100' },
          { label: 'Curricula Covered', value: 'ICSE, ISC & CBSE' },
          { label: 'Core Tech Focus', value: 'Java, Python & Electronics' }
        ],
        uiHighlights: [
          'Concept-Based Learning & Printed Study Materials',
          'Classes VIII to XII Structured Tracks',
          'Star Achievers Board Marks Showcase'
        ]
      }
    },
    {
      id: 'baruipur-bhattacharyapara-puja',
      title: 'Baruipur Bhattacharyapara Durga Puja',
      shortTitle: '50th Golden Jubilee 2026 Official Festival Portal',
      category: 'Cultural & Community Organizations',
      clientType: 'Durga Puja & Cultural Committee',
      badge: 'Live Website',
      demoUrl: 'https://baruipurbhattacharyaparapujo.info',
      hasLiveSite: true,
      thumbnailImage: '/images/baruipur-durga-puja.jpg',
      summary: 'Official digital platform for the 50th Golden Jubilee celebration featuring theme ‘Anubhuti’ (অনুভূতি), sponsorship packages, and route guide for 150,000+ visitors.',
      problemSolved: 'The committee needed a dignified digital medium to present corporate sponsorship packages and assist 150,000+ festival visitors with live pandal routes.',
      engineeredSolution: 'Constructed a festival portal featuring the theme art tribute, sponsorship packages deck, 5-day puja timings, and transit navigation for Baruipur.',
      keyFeatures: [
        '50th Golden Jubilee Theme ‘Anubhuti’ (অনুভূতি) Showcase',
        'Interactive Corporate Sponsorship Packages & Media Reach',
        'Festival Timetable (Sasthi to Dashami) with Anjali Timings',
        'Transit Navigation with Nearest Train & Parking Route Guide',
        'Emergency & Volunteer Contact Directory'
      ],
      mockData: {
        heroHeadline: 'Celebrating 50 Years of Golden Jubilee, Art & Devotion',
        heroSubheadline: 'Official Digital Guide & Sponsorship Suite for Theme Anubhuti.',
        metrics: [
          { label: 'Visitors', value: '150,000+' },
          { label: 'Celebration', value: '50th Jubilee' },
          { label: 'Theme', value: 'Anubhuti' }
        ],
        uiHighlights: [
          'Theme Anubhuti Art Philosophy Showcase',
          'Corporate Sponsorship Deck & Tiers',
          'Baruipur Station & Pandal Route Map'
        ]
      }
    }
  ] as DemonstrationProject[],
};
