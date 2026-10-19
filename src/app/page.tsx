import type { Metadata } from 'next';
import HomeClient from './HomeClient';
import { siteConfig } from '@/config/site';
import { homeFaqs } from '@/data/seoData';
import { generateFaqSchema } from '@/components/FAQSection';

export const metadata: Metadata = {
  title: 'Techzyan — Specialist Technical Studio | Website Development Kolkata',
  description:
    'Techzyan is a premium technical studio in Kolkata engineering high-performance websites for businesses, healthcare clinics, independent tutors, and Durga Puja committees. Sub-second speed, bespoke design, and zero bloat.',
  keywords: [
    'Techzyan',
    'website development Kolkata',
    'web design studio Kolkata',
    'best web developer in Kolkata',
    'custom website design West Bengal',
    'doctor website development Kolkata',
    'clinic appointment booking portal',
    'tutor website portal Kolkata',
    'academic coaching website design',
    'Durga Puja website Kolkata',
    'Durga Puja sponsorship platform',
    'Next.js web agency Kolkata',
    'Baguiati technical studio',
    'high performance web development India',
  ],
  alternates: {
    canonical: siteConfig.url,
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: siteConfig.url,
    siteName: siteConfig.name,
    title: 'Techzyan — Specialist Technical Studio | Website Development Kolkata',
    description:
      'High-performance websites and bespoke digital solutions for businesses, healthcare clinics, educators, and cultural festivals in Kolkata.',
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'Techzyan Technical Studio Kolkata',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Techzyan — Specialist Technical Studio | Kolkata',
    description:
      'Bespoke websites and IT solutions engineered for businesses, doctors, tutors, and cultural organizations in Kolkata.',
    images: [siteConfig.ogImage],
  },
};

export default function HomePage() {
  const faqSchema = generateFaqSchema(homeFaqs);

  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />
      <HomeClient />
    </>
  );
}
