import type { Metadata, Viewport } from 'next';
import './globals.css';
import { siteConfig } from '@/config/site';

export const viewport: Viewport = {
  themeColor: '#080C14',
  colorScheme: 'dark',
  width: 'device-width',
  initialScale: 1,
  maximumScale: 5,
};

export const metadata: Metadata = {
  metadataBase: new URL(siteConfig.url),
  title: {
    default: 'Techzyan — Specialist Technical Studio | Website Development Kolkata',
    template: '%s | Techzyan',
  },
  description: siteConfig.description,
  applicationName: 'Techzyan Technical Studio',
  category: 'Technology & Web Engineering',
  classification: 'Software, Web Development & IT Solutions',
  keywords: [
    'Techzyan',
    'Techzyan Technical Studio',
    'website development Kolkata',
    'web design studio Kolkata',
    'best web development company in Kolkata',
    'Next.js web developer Kolkata',
    'doctor website development Kolkata',
    'clinic appointment booking system',
    'healthcare website designer India',
    'tutor website portal Kolkata',
    'coaching institute web design',
    'Durga Puja website Kolkata',
    'Durga Puja sponsorship platform',
    'Sarbojanin Durga Puja digital platform',
    'custom web engineering India',
    'high performance web development',
    'bespoke IT solutions small business Kolkata',
    'Baguiati web development studio',
    'WhatsApp booking website developer',
  ],
  authors: [{ name: 'Techzyan Technical Studio', url: siteConfig.url }],
  creator: 'Techzyan Technical Studio',
  publisher: 'Techzyan Technical Studio',
  robots: {
    index: true,
    follow: true,
    nocache: false,
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
    title: 'Techzyan — Specialist Technical Studio | Website Development Kolkata',
    description: siteConfig.description,
    images: [
      {
        url: siteConfig.ogImage,
        width: 1200,
        height: 630,
        alt: 'Techzyan — Specialist Technical Studio Kolkata',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Techzyan — Specialist Technical Studio | Kolkata',
    description: siteConfig.description,
    images: [siteConfig.ogImage],
    creator: '@techzyan',
    site: '@techzyan',
  },
  alternates: {
    canonical: siteConfig.url,
  },
  other: {
    'geo.region': 'IN-WB',
    'geo.placename': 'Kolkata',
    'geo.position': `${siteConfig.location.latitude};${siteConfig.location.longitude}`,
    'ICBM': `${siteConfig.location.latitude}, ${siteConfig.location.longitude}`,
    'format-detection': 'telephone=no',
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
        '@id': `${siteConfig.url}/#organization`,
        name: siteConfig.name,
        legalName: siteConfig.legalName,
        alternateName: 'Techzyan Studio',
        url: siteConfig.url,
        logo: `${siteConfig.url}/icon.svg`,
        image: siteConfig.ogImage,
        description: siteConfig.description,
        telephone: siteConfig.contact.phoneRaw,
        email: siteConfig.contact.email,
        foundingDate: '2024',
        address: {
          '@type': 'PostalAddress',
          streetAddress: 'Baguiati',
          addressLocality: siteConfig.location.city,
          addressRegion: siteConfig.location.state,
          postalCode: siteConfig.location.postalCode,
          addressCountry: 'IN',
        },
        contactPoint: [
          {
            '@type': 'ContactPoint',
            telephone: siteConfig.contact.phoneRaw,
            contactType: 'customer support',
            areaServed: ['IN', 'Global'],
            availableLanguage: ['English', 'Bengali', 'Hindi'],
          },
          {
            '@type': 'ContactPoint',
            email: siteConfig.contact.email,
            contactType: 'technical inquiries',
            areaServed: ['IN', 'Global'],
            availableLanguage: ['English', 'Bengali', 'Hindi'],
          },
        ],
        sameAs: [
          siteConfig.socials.linkedin,
          siteConfig.socials.github,
          siteConfig.socials.twitter,
        ],
        knowsAbout: [
          'Website Development',
          'Next.js',
          'React',
          'TypeScript',
          'Python',
          'FastAPI',
          'PostgreSQL',
          'Healthcare Clinic Portals',
          'Tutor and Academic Platforms',
          'Durga Puja Digital Infrastructure',
          'High Performance Web Engineering',
        ],
      },
      {
        '@type': ['ProfessionalService', 'LocalBusiness'],
        '@id': `${siteConfig.url}/#service`,
        name: 'Techzyan Technical Studio',
        url: siteConfig.url,
        image: siteConfig.ogImage,
        telephone: siteConfig.contact.phoneRaw,
        email: siteConfig.contact.email,
        priceRange: '₹₹',
        address: {
          '@type': 'PostalAddress',
          streetAddress: 'Baguiati',
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
        openingHoursSpecification: [
          {
            '@type': 'OpeningHoursSpecification',
            dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            opens: '10:00',
            closes: '19:00',
          },
        ],
        areaServed: [
          { '@type': 'City', name: 'Kolkata' },
          { '@type': 'City', name: 'Howrah' },
          { '@type': 'City', name: 'Salt Lake' },
          { '@type': 'City', name: 'New Town' },
          { '@type': 'AdministrativeArea', name: 'West Bengal' },
          { '@type': 'Country', name: 'India' },
        ],
        hasOfferCatalog: {
          '@type': 'OfferCatalog',
          name: 'Techzyan Technical Engineering Services',
          itemListElement: [
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Service',
                name: 'Business Website Engineering',
                description: 'Custom high-performance websites engineered with Next.js, sub-second LCP, and conversion-focused design in Kolkata.',
              },
            },
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Service',
                name: 'Doctor & Clinic Appointment Platforms',
                description: 'Specialist clinical portals featuring symptom-aware appointment triage, OPD chamber timings, and direct WhatsApp routing.',
              },
            },
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Service',
                name: 'Private Tutor & Academy Portals',
                description: 'Academic platforms with curriculum roadmaps for ICSE, ISC, CBSE, small batch vacancy matrices, and parent feedback loops.',
              },
            },
            {
              '@type': 'Offer',
              itemOffered: {
                '@type': 'Service',
                name: 'Durga Puja Digital Infrastructure & Sponsorship Platforms',
                description: 'Official festival websites for Sarbojanin committees with sponsorship tier decks, transit maps, and interactive virtual dhaak.',
              },
            },
          ],
        },
      },
      {
        '@type': 'WebSite',
        '@id': `${siteConfig.url}/#website`,
        url: siteConfig.url,
        name: siteConfig.name,
        description: siteConfig.description,
        publisher: {
          '@id': `${siteConfig.url}/#organization`,
        },
        inLanguage: 'en-IN',
      },
    ],
  };

  return (
    <html lang="en" className="dark scroll-smooth">
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
