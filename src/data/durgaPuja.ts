import { DurgaPujaFeature, SponsorTier } from '@/types';

export const durgaPujaFeatures: DurgaPujaFeature[] = [
  {
    id: 'schedule-rituals',
    title: '5-Day Festival & Ritual Schedule',
    bengaliTitle: 'পূজা নির্ঘণ্ট ও অঞ্জলির সময়সূচী',
    description: 'Provide devotees and visitors with an accurate day-by-day timetable from Sasthi to Dashami, including Sandhi Puja, Kumari Puja, and Bhog distribution timings.',
    details: [
      'Day-by-day ritual timeline with morning & evening hours',
      'Pushpanjali & Bhog distribution time slots',
      'Cultural event program & artist performances',
      'Sindoor Khela & Bisorjon procession guidelines'
    ],
    iconName: 'Calendar'
  },
  {
    id: 'sponsor-suite',
    title: 'Digital Sponsorship Suite & Proposal Flow',
    bengaliTitle: 'কর্পোরেট স্পনসরশিপ ও ব্র্যান্ড শোকেস',
    description: 'Transform how you pitch to corporate brand managers with clean digital tier cards, prominent logo placements, and instant sponsorship inquiry capture.',
    details: [
      'Transparent sponsor tier breakdown (Title, Powered By, Associate, Food/Beverage)',
      'Digital branding deliverables & on-ground visibility matrix',
      '1-Click "Request Sponsorship Deck" and direct WhatsApp routing',
      'Year-round brand visibility archive'
    ],
    iconName: 'Award'
  },
  {
    id: 'crowd-transit',
    title: 'Crowd Guide & Metro Navigation',
    bengaliTitle: 'দর্শনার্থী গাইড ও রুট ম্যাপ',
    description: 'Ensure visitors reach your pandal safely with integrated interactive maps, nearest Kolkata Metro stations, designated parking spots, and VIP entry gates.',
    details: [
      'Nearest Metro Station (North-South, East-West Green Line) and walking time',
      'Designated parking zones & traffic police advisory links',
      'Senior citizen & wheelchair accessibility notes',
      'Real-time crowd queue advisory updates'
    ],
    iconName: 'MapPin'
  },
  {
    id: 'art-archive',
    title: 'Theme Concept & Pandal Art Gallery',
    bengaliTitle: 'ভাবনা, প্রতিমা ও মণ্ডপ শিল্পীদের শ্রদ্ধার্ঘ্য',
    description: 'Celebrate the visionary concept, artist, sculptor, and lighting designers behind your pandal with high-resolution photo galleries and editorial stories.',
    details: [
      'Detailed theme synopsis and cultural backstory',
      'Spotlight on the Chief Artist, Idol Sculptor, and Lighting Director',
      'High-resolution photo and video gallery optimized for mobile loading',
      'Historical awards & accolades archive'
    ],
    iconName: 'Image'
  },
  {
    id: 'donations-payments',
    title: 'Donation & Subscription Payment Gateways',
    bengaliTitle: 'অনলাইন চাঁদা ও অনুদান ব্যবস্থাপনা',
    description: 'Enable non-resident Bengalis (NRIs), patrons, and local members to contribute securely via UPI, QR code, or direct bank transfer with instant receipt acknowledgment.',
    details: [
      'Clean UPI QR code & bank NEFT/RTGS detail showcase',
      'Optional automated receipt generator for contributors',
      '80G / Tax exemption disclosure notices where applicable',
      'Transparent committee acknowledgment ledger'
    ],
    iconName: 'CreditCard'
  },
  {
    id: 'committee-hotline',
    title: 'Committee Directory & Emergency Hotline',
    bengaliTitle: 'কমিটি সদস্য ও জরুরি হেল্পলাইন',
    description: 'Equip visitors, authorities, and sponsors with direct one-tap access to key committee executives, medical aid desks, lost-and-found, and volunteer leads.',
    details: [
      'Official committee executive contacts (President, Secretary, Treasurer)',
      'One-tap WhatsApp volunteer and helpdesk hotline',
      'Emergency medical camp & ambulance station locator',
      'Police assistance booth & lost child helpline numbers'
    ],
    iconName: 'PhoneCall'
  }
];

export const sampleSponsorTiers: SponsorTier[] = [
  {
    name: 'Title Sponsor',
    tagline: 'Premier festival association across all digital & physical surfaces',
    recommendedFor: 'Leading National FMCG, Telecom & Automobile Brands',
    digitalPerks: [
      'Prime Hero Banner placement on official digital hub (50k+ visitors)',
      'Exclusive “In Association With” credit on all festival schedules',
      'Dedicated Brand Story & Video spotlight on homepage',
      'Direct sponsor CTA button linking to brand promotional offers',
      'Prominent mention in all digital press releases & social links'
    ],
    featuredPlacement: true,
  },
  {
    name: 'Co-Powered By Sponsor',
    tagline: 'High-visibility digital & on-ground branding throughout the festival',
    recommendedFor: 'Regional Leaders, Retail Chains, Real Estate & Banking',
    digitalPerks: [
      'Prominent logo on digital header & footer across all pages',
      'Branded section in the Interactive 5-Day Ritual Calendar',
      'Featured placement in the Visitor Metro & Crowd Guide',
      'Direct link to brand landing page from the Sponsor Showcase'
    ],
    featuredPlacement: false,
  },
  {
    name: 'Associate & Food Zone Sponsor',
    tagline: 'Targeted placement for dining, local retailers & youth brands',
    recommendedFor: 'Restaurants, Food Stalls, Fashion Outlets & Local Businesses',
    digitalPerks: [
      'Listed under official Puja Food & Beverage directory with map pinpoint',
      'Logo on the official Sponsor Partners wall',
      'Inclusion in the visitor digital brochure PDF download'
    ],
    featuredPlacement: false,
  }
];
