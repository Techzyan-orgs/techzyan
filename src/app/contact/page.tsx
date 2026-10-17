import type { Metadata } from 'next';
import ContactClient from './ContactClient';
import { siteConfig } from '@/config/site';
import { contactFaqs, generateBreadcrumbSchema } from '@/data/seoData';
import { generateFaqSchema } from '@/components/FAQSection';

export const metadata: Metadata = {
  title: 'Contact Techzyan | Project Inquiry & Technical Consultation Kolkata',
  description:
    'Start a direct project discussion with Techzyan Technical Studio in Kolkata. Transparent scoping, rapid 24-hour response guarantee, and direct WhatsApp consultations.',
  keywords: [
    'contact Techzyan',
    'hire web developer Kolkata',
    'web design studio inquiry Kolkata',
    'WhatsApp web development consultation',
    'Ballygunge technical studio contact',
    'doctor website inquiry Kolkata',
    'Durga Puja committee website consultation',
  ],
  alternates: {
    canonical: `${siteConfig.url}/contact`,
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: `${siteConfig.url}/contact`,
    siteName: siteConfig.name,
    title: 'Contact Techzyan | Technical Consultation & Inquiry Kolkata',
    description:
      'Connect directly with our engineering team in Kolkata. No junior account managers, no automated delays.',
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'Contact Techzyan Technical Studio',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Contact Techzyan Technical Studio | Kolkata',
    description:
      'Speak directly with technical specialists in Kolkata regarding your digital project.',
    images: [siteConfig.ogImage],
  },
};

export default function ContactPage() {
  const breadcrumbSchema = generateBreadcrumbSchema([
    { name: 'Home', url: '/' },
    { name: 'Contact', url: '/contact' },
  ]);

  const faqSchema = generateFaqSchema(contactFaqs);

  const contactPageSchema = {
    '@context': 'https://schema.org',
    '@type': 'ContactPage',
    name: 'Contact Techzyan Technical Studio',
    url: `${siteConfig.url}/contact`,
    description: 'Direct inquiry and technical consultation hub for Techzyan in Kolkata, India.',
    mainEntity: {
      '@type': 'LocalBusiness',
      name: siteConfig.name,
      legalName: siteConfig.legalName,
      telephone: siteConfig.contact.phoneRaw,
      email: siteConfig.contact.email,
      url: siteConfig.url,
      address: {
        '@type': 'PostalAddress',
        streetAddress: 'Ballygunge / South Kolkata',
        addressLocality: siteConfig.location.city,
        addressRegion: siteConfig.location.state,
        postalCode: siteConfig.location.postalCode,
        addressCountry: 'IN',
      },
      geo: {
        '@type': 'GeoCoordinates',
        latitude: siteConfig.location.latitude,
        longitude: siteConfig.location.longitude,
      },
      contactPoint: {
        '@type': 'ContactPoint',
        telephone: siteConfig.contact.phoneRaw,
        contactType: 'customer service',
        availableLanguage: ['English', 'Bengali', 'Hindi'],
      },
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
        dangerouslySetInnerHTML={{ __html: JSON.stringify(contactPageSchema) }}
      />
      <ContactClient />
    </>
  );
}
