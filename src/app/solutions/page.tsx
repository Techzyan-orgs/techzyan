import type { Metadata } from 'next';
import SolutionsClient from './SolutionsClient';
import { siteConfig } from '@/config/site';
import { solutionsFaqs, generateBreadcrumbSchema } from '@/data/seoData';
import { generateFaqSchema } from '@/components/FAQSection';

export const metadata: Metadata = {
  title: 'Web Engineering & Digital Solutions in Kolkata',
  description:
    'Custom web solutions engineered by Techzyan: business websites, doctor clinic appointment portals, private tutor mentorship platforms, and festival digital hubs in Kolkata.',
  keywords: [
    'web development solutions Kolkata',
    'doctor website design Kolkata',
    'clinic OPD appointment system',
    'tutor website portal West Bengal',
    'coaching batch management system',
    'custom business websites Kolkata',
    'Durga Puja digital platform',
    'appointment booking website developer',
    'Next.js development services Kolkata',
  ],
  alternates: {
    canonical: `${siteConfig.url}/solutions`,
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: `${siteConfig.url}/solutions`,
    siteName: siteConfig.name,
    title: 'Web Engineering & Digital Solutions in Kolkata | Techzyan',
    description:
      'High-performance web applications, clinical appointment portals, and educational platforms built for Kolkata and global businesses.',
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'Techzyan Digital Solutions Kolkata',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Digital Solutions & Web Engineering in Kolkata | Techzyan',
    description:
      'Explore bespoke website solutions for doctors, educators, retail businesses, and festival committees.',
    images: [siteConfig.ogImage],
  },
};

export default function SolutionsPage() {
  const breadcrumbSchema = generateBreadcrumbSchema([
    { name: 'Home', url: '/' },
    { name: 'Solutions', url: '/solutions' },
  ]);

  const faqSchema = generateFaqSchema(solutionsFaqs);

  const serviceCatalogSchema = {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: 'Techzyan Digital Solutions',
    description: 'Suite of custom website engineering and digital solutions',
    itemListElement: [
      {
        '@type': 'Service',
        position: 1,
        name: 'Business Websites & Corporate Portals',
        description: 'Clean, fast, high-contrast business websites built to communicate authority and convert visitors.',
        provider: { '@id': `${siteConfig.url}/#organization` },
      },
      {
        '@type': 'Service',
        position: 2,
        name: 'Doctor & Clinic Appointment Platforms',
        description: 'Specialist clinical portals featuring symptom-aware appointment triage, OPD chamber timings, and direct WhatsApp routing.',
        provider: { '@id': `${siteConfig.url}/#organization` },
      },
      {
        '@type': 'Service',
        position: 3,
        name: 'Tutor & Academic Mentorship Portals',
        description: 'Academic platforms with curriculum roadmaps for ICSE, ISC, and CBSE boards, batch vacancy counters, and parent feedback.',
        provider: { '@id': `${siteConfig.url}/#organization` },
      },
      {
        '@type': 'Service',
        position: 4,
        name: 'Durga Puja Digital Infrastructure & Sponsorship Platforms',
        description: 'Official digital portals for Sarbojanin Durga Puja committees with corporate sponsorship decks and visitor transit maps.',
        provider: { '@id': `${siteConfig.url}/#organization` },
      },
    ],
  };

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(serviceCatalogSchema) }}
      />
      <SolutionsClient />
    </>
  );
}
