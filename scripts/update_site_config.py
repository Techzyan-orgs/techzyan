import os

# 1. Update src/config/site.ts
site_config_content = """/**
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
};
"""

with open('src/config/site.ts', 'w', encoding='utf-8') as f:
    f.write(site_config_content)
print("Updated src/config/site.ts successfully!")
