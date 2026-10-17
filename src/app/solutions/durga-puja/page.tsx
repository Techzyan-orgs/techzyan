import type { Metadata } from 'next';
import DurgaPujaClient from './DurgaPujaClient';
import { siteConfig } from '@/config/site';
import { durgaPujaFaqs, generateBreadcrumbSchema } from '@/data/seoData';
import { generateFaqSchema } from '@/components/FAQSection';

export const metadata: Metadata = {
  title: 'Durga Puja Digital Infrastructure & Sponsorship Platforms Kolkata',
  description:
    'Official Durga Puja committee website development in Kolkata. Feature corporate sponsorship packages, transit guides for 150,000+ visitors, 5-day ritual schedules, and interactive virtual dhaak audio.',
  keywords: [
    'Durga Puja website Kolkata',
    'Durga Puja sponsorship platform',
    'Sarbojanin Durga Puja committee website',
    'Baruipur Durga Puja digital guide',
    'Durga Puja sponsorship deck',
    'pandal route guide website',
    'Sharodotsav 2026 platform',
    'virtual dhaak sound Kolkata',
    'festival website development Kolkata',
    'Bengali festival digital infrastructure',
  ],
  alternates: {
    canonical: `${siteConfig.url}/solutions/durga-puja`,
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: `${siteConfig.url}/solutions/durga-puja`,
    siteName: siteConfig.name,
    title: 'Durga Puja Digital Infrastructure & Sponsorship Platforms Kolkata | Techzyan',
    description:
      'Official digital platforms for heritage and Sarbojanin Durga Puja committees in Kolkata. Corporate sponsorship tiers, ritual schedules, and visitor navigation.',
    images: [
      {
        url: `${siteConfig.url}/images/durga-idol.png`,
        width: 800,
        height: 800,
        alt: 'Durga Puja Digital Platform Idol Showcase',
      },
      {
        url: `${siteConfig.url}/images/baruipur-durga-puja.jpg`,
        width: 1200,
        height: 630,
        alt: 'Baruipur Bhattacharyapara Durga Puja Golden Jubilee Official Portal',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Durga Puja Digital Infrastructure Kolkata | Techzyan',
    description:
      'Official festival websites for Durga Puja committees in Kolkata. Sponsorship monetization, transit route maps, and virtual dhaak beats.',
    images: [`${siteConfig.url}/images/baruipur-durga-puja.jpg`],
  },
};

export default function DurgaPujaPage() {
  const breadcrumbSchema = generateBreadcrumbSchema([
    { name: 'Home', url: '/' },
    { name: 'Solutions', url: '/solutions' },
    { name: 'Durga Puja Digital Infrastructure', url: '/solutions/durga-puja' },
  ]);

  const faqSchema = generateFaqSchema(durgaPujaFaqs);

  const pujaServiceSchema = {
    '@context': 'https://schema.org',
    '@type': 'Service',
    name: 'Durga Puja Digital Infrastructure & Festival Platform',
    serviceType: 'Festival Web Development & Sponsorship Suite',
    description:
      'Comprehensive digital infrastructure engineered for Sarbojanin Durga Puja committees in Kolkata, featuring digital sponsorship decks, pandal navigation, ritual timetables, and crowd safety directories.',
    provider: {
      '@id': `${siteConfig.url}/#organization`,
    },
    areaServed: [
      { '@type': 'City', name: 'Kolkata' },
      { '@type': 'AdministrativeArea', name: 'West Bengal' },
    ],
    hasOfferCatalog: {
      '@type': 'OfferCatalog',
      name: 'Durga Puja Platform Modules',
      itemListElement: [
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Interactive Corporate Sponsorship Showcase',
            description: 'Dignified sponsor visibility with custom banner slots and digital prospectus download.',
          },
        },
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Pandal Transit Navigation & Crowd Guide',
            description: 'Direct Google Maps integration, nearest railway stations, metro gates, and parking areas.',
          },
        },
        {
          '@type': 'Offer',
          itemOffered: {
            '@type': 'Service',
            name: 'Interactive Virtual Dhaak Player',
            description: 'Atmospheric Bengali dhaak beats streamable instantly across global web visitors.',
          },
        },
      ],
    },
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
        dangerouslySetInnerHTML={{ __html: JSON.stringify(pujaServiceSchema) }}
      />
      <DurgaPujaClient />
    </>
  );
}
