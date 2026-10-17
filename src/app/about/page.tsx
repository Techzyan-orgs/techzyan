import type { Metadata } from 'next';
import AboutClient from './AboutClient';
import { siteConfig } from '@/config/site';
import { aboutFaqs, generateBreadcrumbSchema } from '@/data/seoData';
import { generateFaqSchema } from '@/components/FAQSection';

export const metadata: Metadata = {
  title: 'About Techzyan | Engineering-First Technical Studio in Kolkata',
  description:
    'Learn about Techzyan: a specialist technical studio founded in Kolkata engineering bespoke, high-performance web applications for businesses, doctors, tutors, and cultural organizations.',
  keywords: [
    'about Techzyan',
    'technical studio Kolkata',
    'web development company Kolkata',
    'software engineering studio West Bengal',
    'Next.js web specialists India',
    'bespoke IT solutions Kolkata',
    'Ballygunge Kolkata web studio',
  ],
  alternates: {
    canonical: `${siteConfig.url}/about`,
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: `${siteConfig.url}/about`,
    siteName: siteConfig.name,
    title: 'About Techzyan | Engineering-First Technical Studio in Kolkata',
    description:
      'Purpose-built websites and digital tools engineered with care in Kolkata. Meet the studio and our core engineering philosophy.',
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'About Techzyan Technical Studio Kolkata',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'About Techzyan | Specialist Technical Studio Kolkata',
    description:
      'We partner with businesses, doctors, educators, and cultural committees to engineer thoughtful, high-performance websites.',
    images: [siteConfig.ogImage],
  },
};

export default function AboutPage() {
  const breadcrumbSchema = generateBreadcrumbSchema([
    { name: 'Home', url: '/' },
    { name: 'About', url: '/about' },
  ]);

  const faqSchema = generateFaqSchema(aboutFaqs);

  const aboutPageSchema = {
    '@context': 'https://schema.org',
    '@type': 'AboutPage',
    name: 'About Techzyan Technical Studio',
    url: `${siteConfig.url}/about`,
    description: siteConfig.description,
    mainEntity: {
      '@type': 'Organization',
      name: siteConfig.name,
      legalName: siteConfig.legalName,
      url: siteConfig.url,
      foundingDate: '2024',
      foundingLocation: {
        '@type': 'Place',
        name: 'Kolkata, West Bengal, India',
      },
      knowsAbout: [
        'Web Development',
        'Next.js',
        'Healthcare Applications',
        'Tutor Portals',
        'Durga Puja Platforms',
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
        dangerouslySetInnerHTML={{ __html: JSON.stringify(aboutPageSchema) }}
      />
      <AboutClient />
    </>
  );
}
