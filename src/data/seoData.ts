import { siteConfig } from '@/config/site';
import { FAQItem } from '@/components/FAQSection';

export interface BreadcrumbItem {
  name: string;
  url: string;
}

export function generateBreadcrumbSchema(items: BreadcrumbItem[]) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: item.url.startsWith('http') ? item.url : `${siteConfig.url}${item.url}`,
    })),
  };
}

export const homeFaqs: FAQItem[] = [
  {
    question: 'What web development and technical services does Techzyan provide?',
    answer:
      'Techzyan is a specialist technical studio based in Kolkata. We build bespoke, high-performance websites and digital platforms for growing businesses, healthcare clinics, independent tutors, and cultural organizations like Durga Puja committees. Our solutions include custom appointment booking systems, student batch portals, interactive lookbooks, and mobile-first web engineering.',
  },
  {
    question: 'How much does a custom website cost in Kolkata?',
    answer:
      'We offer transparent, value-driven pricing tailored to the exact requirements of your business. Rather than selling bloated generic packages, we assess your operational needs—such as WhatsApp integration, appointment booking, or responsive catalogs—and provide a clear, fixed quote without hidden costs.',
  },
  {
    question: 'How fast does Techzyan deliver a production website?',
    answer:
      'Our typical turnaround is 10 to 20 business days for standard projects. Because we utilize an engineered component architecture with modern frameworks like Next.js and Tailwind CSS, we deliver rapid turnarounds without sacrificing code quality, security, or mobile speed.',
  },
  {
    question: 'Why choose Techzyan over generic website builders like WordPress or Wix?',
    answer:
      'Generic website builders often produce bloated code, sluggish loading times on mobile 4G networks, and frequent plugin vulnerabilities. Techzyan builds clean, zero-bloat Next.js applications that load in under a second, score 95+ on Google PageSpeed, rank significantly higher on search engines, and are tailored to your exact business workflows.',
  },
  {
    question: 'Does Techzyan support WhatsApp booking and direct inquiry integration?',
    answer:
      'Yes. In the Indian market, WhatsApp is the primary communication channel. All our platforms feature deep WhatsApp integration, formatted inquiry links, and click-to-chat appointment confirmations so your leads are never lost in confusing email threads.',
  },
  {
    question: 'Where is Techzyan based, and can we meet in person in Kolkata?',
    answer:
      'Techzyan is based in Baguiati, Kolkata, West Bengal (serving Salt Lake, New Town, Rajarhat, South & Central Kolkata, and all Kolkata regions, as well as global clients). We are happy to coordinate in-person strategy consultations in Kolkata or connect over video calls.',
  },
];

export const solutionsFaqs: FAQItem[] = [
  {
    question: 'What makes Techzyan doctor and clinic platforms unique?',
    answer:
      'Our clinical platforms are engineered with a 3-step symptom-aware appointment triage system, real-time OPD chamber status indicators, and direct WhatsApp booking. This reduces receptionist call overload by up to 70% while giving patients immediate clarity on consulting hours.',
  },
  {
    question: 'How does the private tutor and academic mentorship portal work?',
    answer:
      'Our tutor portals showcase curriculum roadmaps for ICSE, ISC, and CBSE boards, live batch vacancy counts, parent feedback mechanisms, and past student board results. Parents can easily check batch suitability and initiate direct admissions queries.',
  },
  {
    question: 'Are all Techzyan websites optimized for mobile devices and 4G networks in India?',
    answer:
      'Yes, 100%. Over 80% of web traffic in India comes from mobile phones on cellular data. We engineer lightweight bundles, optimized WebP/AVIF images, and streamlined CSS to guarantee sub-second initial paint times and zero cumulative layout shift (CLS).',
  },
  {
    question: 'Can you build custom appointment and lead management systems?',
    answer:
      'Absolutely. Whether you run a healthcare clinic, tailoring salon, fitness club, or consultancy, we design tailored scheduling and intake flows that match your operational routine without forcing you into expensive third-party SaaS subscriptions.',
  },
  {
    question: 'Do you offer ongoing technical maintenance and hosting support?',
    answer:
      'Yes. Every platform built by Techzyan comes with comprehensive deployment setup, high-availability cloud hosting configuration, SSL security certificates, and optional ongoing maintenance packages.',
  },
];

export const durgaPujaFaqs: FAQItem[] = [
  {
    question: 'Why does a Sarbojanin Durga Puja committee in Kolkata need an official digital platform?',
    answer:
      'An official festival website establishes digital prestige, makes your committee effortlessly discoverable to brand marketers and corporate sponsors searching for high-impact cultural partnerships, and provides them with a complete, transparent showcase of your pandal theme, footfall metrics, and sponsorship deliverables. Simultaneously, it serves 150,000+ festival visitors with real-time transit guides and anjali schedules while preserving your artistic legacy permanently on the web.',
  },
  {
    question: 'How does the digital sponsorship deck help attract corporate sponsors?',
    answer:
      'Corporate brands look for measurable reach and dignified branding. An official web portal presents structured sponsorship tiers (Title, Co-Sponsor, Associate), audience footfall metrics, and direct committee contact, making sponsorship pitches significantly more professional.',
  },
  {
    question: 'Can the website feature live pandal maps and transit navigation for visitors?',
    answer:
      'Yes. We incorporate interactive route guides indicating nearest railway stations, metro stops, auto-rickshaw stands, designated parking zones, and step-by-step pedestrian entry gates.',
  },
  {
    question: 'Can we publish our daily Puja schedule, pushpanjali timings, and cultural programs?',
    answer:
      'Yes. The platform includes a dedicated 5-day festival timetable (Sasthi to Dashami) detailing Sandhi Puja, Pushpanjali batches, Bhog distribution, and cultural program itineraries.',
  },
  {
    question: 'What is the virtual dhaak audio feature?',
    answer:
      'Our proprietary interactive virtual dhaak audio button allows visitors worldwide—especially Bengalis living abroad—to experience the authentic festive resonance of Bengal dhaak beats right on your committee website.',
  },
  {
    question: 'How quickly can Techzyan launch our Durga Puja website before Sharodotsav 2026?',
    answer:
      'We can launch a fully featured, custom-branded Durga Puja committee website within 7 to 14 days upon receiving the theme concept, committee details, and sponsor logos.',
  },
];

export const whoWeHelpFaqs: FAQItem[] = [
  {
    question: 'How do you tailor website solutions specifically for doctors and clinics?',
    answer:
      'We focus on trust and operational clarity. We eliminate repetitive front-desk phone inquiries by displaying precise OPD chamber timings, location landmarks, and structured pre-consultation symptom intake.',
  },
  {
    question: 'I am an independent teacher/educator. How does a website benefit my coaching batches?',
    answer:
      'A dedicated academic website establishes senior authority, eliminates lost WhatsApp messages about batch timings, highlights student board exam achievements, and presents structured syllabus coverage for parents.',
  },
  {
    question: 'We are a boutique, salon, or custom tailoring business. How does custom web engineering help us?',
    answer:
      'For bespoke businesses, imagery and styling confidence are everything. We design sensory editorial lookbooks, illustrated measurement guides, and private fitting schedulers that attract high-ticket clients across Kolkata. Crucially, our localized SEO architecture and structured business schema help you achieve significantly better search results on Google and Google Maps, ensuring clients searching for premier local styling and custom tailoring discover your studio first.',
  },
  {
    question: 'Can educational academies and coaching institutes manage multiple subjects and teachers?',
    answer:
      'Yes. We build structured multi-program directories with branch locations, faculty credentials, subject-wise curriculum breakdowns, and centralized admission inquiry pipelines.',
  },
];

export const workFaqs: FAQItem[] = [
  {
    question: 'Are the demonstration projects on Techzyan functional?',
    answer:
      'Yes. All demonstration prototypes—including Dr. Aranya Sen Neurology Clinic, Prof. Subhashish Banerjee Tutor Platform, XYZ Ladies Tailors, Stoic Men Salon, and Baruipur Bhattacharyapara Durga Puja—are functional, interactive platforms built to demonstrate real-world solutions.',
  },
  {
    question: 'Can you customize any of these showcase models for my business?',
    answer:
      'Absolutely. Every concept can be fully adapted to your branding, color palette, services, pricing structure, and contact channels within 10 to 14 business days.',
  },
  {
    question: 'Can we inspect the live demonstration websites on mobile?',
    answer:
      'Yes! Each demonstration project includes a direct live link. You can open them on any smartphone to experience the speed, responsive layout, and intuitive user experience.',
  },
];

export const aboutFaqs: FAQItem[] = [
  {
    question: "What is Techzyan's core operating philosophy?",
    answer:
      '“Understand the operational requirement first, then engineer the right digital solution.” We reject bloated templates, fake marketing metrics, and unnecessary complexity, focusing instead on speed, clarity, and business outcomes.',
  },
  {
    question: 'What technology stack does Techzyan use?',
    answer:
      'We specialize in modern, high-performance full-stack engineering without relying on bloated templates. Our frontend architecture is built on Next.js, React, TypeScript, and Tailwind CSS. For advanced backend systems, intelligent APIs, and high-throughput data processing, we engineer with Python, FastAPI, and Node.js, backed by robust relational databases like PostgreSQL. Deployments are managed on high-availability edge and cloud networks including Vercel and Cloudflare for sub-second performance.',
  },
  {
    question: 'Does Techzyan outsource client projects to third parties?',
    answer:
      'Never. All design, code, optimization, and technical infrastructure are engineered directly in-house by our studio team in Kolkata.',
  },
];

export const contactFaqs: FAQItem[] = [
  {
    question: 'What is the fastest way to get a response from Techzyan?',
    answer:
      'Reaching out via WhatsApp (+91-7439303013) or submitting the project inquiry form gives you a direct response from our technical team within 24 business hours.',
  },
  {
    question: 'Do you offer a free initial consultation?',
    answer:
      'Yes. We provide a 30-minute discovery consultation to discuss your business goals, technical needs, timeline, and recommended digital architecture.',
  },
  {
    question: 'What information should I provide when contacting you?',
    answer:
      'A brief description of your business, the primary goal of your website (e.g. appointment booking, lead generation, festival showcase), any reference websites you like, and your estimated launch timeline.',
  },
];
