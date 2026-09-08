import type { Metadata } from 'next';
import './globals.css';
import { siteConfig } from '@/config/site';

export const metadata: Metadata = {
  metadataBase: new URL(siteConfig.url),
  title: {
    default: 'Techzyan — Specialist Technical Studio | Kolkata & Global',
    template: '%s | Techzyan',
  },
  description: siteConfig.description,
  keywords: [
    'Techzyan',
    'website development Kolkata',
    'web design studio Kolkata',
    'doctor website development',
    'tutor website portal',
    'Durga Puja website Kolkata',
    'Durga Puja sponsorship platform',
    'custom technical solutions small business',
    'clinic appointment system Kolkata',
    'high performance web engineering India',
  ],
  authors: [{ name: 'Techzyan Technical Studio' }],
  creator: 'Techzyan',
  publisher: 'Techzyan',
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  openGraph: {
    type: 'website',
    locale: 'en_IN',
    url: siteConfig.url,
    siteName: siteConfig.name,
    title: 'Techzyan — Specialist Technical Studio | Kolkata & Global',
    description: siteConfig.description,
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'Techzyan — Specialist Technical Studio',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Techzyan — Specialist Technical Studio',
    description: siteConfig.description,
    images: [siteConfig.ogImage],
  },
  alternates: {
    canonical: siteConfig.url,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const jsonLd = {
    '@context': 'https://schema.org',
    '@graph': [
      {
        '@type': 'Organization',
        '@id': 'https://techzyan.org/#organization',
        name: siteConfig.name,
        legalName: siteConfig.legalName,
        url: siteConfig.url,
        logo: 'https://techzyan.org/logo.png',
        description: siteConfig.description,
        address: {
          '@type': 'PostalAddress',
          addressLocality: siteConfig.location.city,
          addressRegion: siteConfig.location.state,
          addressCountry: siteConfig.location.country,
        },
        contactPoint: {
          '@type': 'ContactPoint',
          contactType: 'technical inquiries',
          email: siteConfig.contact.email,
        },
      },
      {
        '@type': 'ProfessionalService',
        '@id': 'https://techzyan.org/#service',
        name: 'Techzyan Technical Studio',
        url: siteConfig.url,
        priceRange: '$$',
        address: {
          '@type': 'PostalAddress',
          addressLocality: 'Kolkata',
          addressRegion: 'West Bengal',
          addressCountry: 'India',
        },
        areaServed: [
          { '@type': 'City', name: 'Kolkata' },
          { '@type': 'AdministrativeArea', name: 'West Bengal' },
          { '@type': 'Country', name: 'India' },
        ],
        description: 'Bespoke web development, clinical appointment systems, educational platforms, and Durga Puja digital hubs.',
      },
      {
        '@type': 'WebSite',
        '@id': 'https://techzyan.org/#website',
        url: siteConfig.url,
        name: siteConfig.name,
        publisher: {
          '@id': 'https://techzyan.org/#organization',
        },
      },
    ],
  };

  return (
    <html lang="en" className="dark">
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className="bg-[#080C14] text-slate-100 antialiased selection:bg-brand-cyan selection:text-slate-950 min-h-screen flex flex-col">
        {children}
      </body>
    </html>
  );
}
