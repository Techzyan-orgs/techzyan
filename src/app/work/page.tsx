import type { Metadata } from 'next';
import WorkClient from './WorkClient';
import { siteConfig } from '@/config/site';
import { demonstrationProjects } from '@/data/demonstrations';
import { workFaqs, generateBreadcrumbSchema } from '@/data/seoData';
import { generateFaqSchema } from '@/components/FAQSection';

export const metadata: Metadata = {
  title: 'Client Showcase & Demonstration Portfolio | Techzyan',
  description:
    'Explore Techzyan’s demonstration portfolio and live client platforms: Dr. Aranya Sen Clinic, Prof. Subhashish Banerjee Tutor Platform, Baruipur Durga Puja Golden Jubilee, and bespoke retail lookbooks in Kolkata.',
  keywords: [
    'web development portfolio Kolkata',
    'doctor website case study',
    'tutor portal showcase',
    'Durga Puja official website portfolio',
    'salon web design example',
    'custom tailoring lookbook website',
    'Next.js project demonstrations',
    'Techzyan work showcase',
  ],
  alternates: {
    canonical: `${siteConfig.url}/work`,
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: `${siteConfig.url}/work`,
    siteName: siteConfig.name,
    title: 'Client Showcase & Demonstration Portfolio | Techzyan',
    description:
      'Real demonstration prototypes engineered for doctors, educators, retail atelièrs, and festival committees by Techzyan.',
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'Techzyan Project Showcase',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Project Showcase & Demonstrations | Techzyan',
    description:
      'Functional prototypes engineered for clinics, educators, and local businesses in Kolkata.',
    images: [siteConfig.ogImage],
  },
};

export default function WorkPage() {
  const breadcrumbSchema = generateBreadcrumbSchema([
    { name: 'Home', url: '/' },
    { name: 'Work', url: '/work' },
  ]);

  const faqSchema = generateFaqSchema(workFaqs);

  const portfolioSchema = {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name: 'Techzyan Demonstration Portfolio',
    description: 'Demonstration and live technical projects engineered by Techzyan Technical Studio.',
    url: `${siteConfig.url}/work`,
    mainEntity: {
      '@type': 'ItemList',
      itemListElement: demonstrationProjects.map((project, index) => ({
        '@type': 'ListItem',
        position: index + 1,
        item: {
          '@type': 'CreativeWork',
          name: project.title,
          headline: project.shortTitle,
          description: project.summary,
          image: project.thumbnailImage.startsWith('http')
            ? project.thumbnailImage
            : `${siteConfig.url}${project.thumbnailImage}`,
          url: project.demoUrl,
          author: {
            '@id': `${siteConfig.url}/#organization`,
          },
        },
      })),
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
        dangerouslySetInnerHTML={{ __html: JSON.stringify(portfolioSchema) }}
      />
      <WorkClient />
    </>
  );
}
