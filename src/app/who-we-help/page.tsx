import type { Metadata } from 'next';
import WhoWeHelpClient from './WhoWeHelpClient';
import { siteConfig } from '@/config/site';
import { whoWeHelpFaqs, generateBreadcrumbSchema } from '@/data/seoData';
import { generateFaqSchema } from '@/components/FAQSection';

export const metadata: Metadata = {
  title: 'Websites for Doctors, Private Tutors, Growing Businesses & Creator Brands | Techzyan',
  description:
    'Tailored web solutions for doctors, specialist clinics, private tutors, growing businesses, creator brands, and Durga Puja committees across Kolkata. High-performance, mobile-first engineering.',
  keywords: [
    'doctor website Kolkata',
    'clinic website development Kolkata',
    'private tutor website portal Kolkata',
    'academic mentor web design West Bengal',
    'growing business website design Kolkata',
    'creator brand website Kolkata',
    'creator portfolio website development',
    'Durga Puja committee platform',
    'salon boutique website development',
    'healthcare IT solutions Kolkata',
  ],
  alternates: {
    canonical: `${siteConfig.url}/who-we-help`,
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: `${siteConfig.url}/who-we-help`,
    siteName: siteConfig.name,
    title: 'Websites for Doctors, Private Tutors & Businesses in Kolkata | Techzyan',
    description:
      'Engineered digital platforms designed specifically for clinics, private educators, growing retail businesses, and festival committees.',
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'Who We Help - Techzyan Technical Studio Kolkata',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Who We Help | Web Solutions in Kolkata | Techzyan',
    description:
      'Purpose-built websites and digital tools for doctors, tutors, retail brands, and festival organizers in Kolkata.',
    images: [siteConfig.ogImage],
  },
};

export default function WhoWeHelpPage() {
  const breadcrumbSchema = generateBreadcrumbSchema([
    { name: 'Home', url: '/' },
    { name: 'Who We Help', url: '/who-we-help' },
  ]);

  const faqSchema = generateFaqSchema(whoWeHelpFaqs);

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
      <WhoWeHelpClient />
    </>
  );
}
