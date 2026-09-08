export interface SolutionItem {
  id: string;
  category: 'website' | 'custom-tool' | 'puja-special' | 'growth';
  title: string;
  subtitle: string;
  description: string;
  audience: string[];
  deliverables: string[];
  keyFeatures: string[];
  timeline: string;
  pricingType: 'fixed-project' | 'scope-based';
  iconName: string;
  highlight?: boolean;
}

export interface AudienceItem {
  id: string;
  title: string;
  roleSubtitle: string;
  context: string;
  commonFriction: string[];
  techzyanApproach: string;
  entrySolution: string;
  expansionSolution: string;
  keyOutcomes: string[];
  iconName: string;
}

export interface DemonstrationProject {
  id: string;
  title: string;
  shortTitle: string;
  category: string;
  clientType: string;
  badge: string;
  demoUrl: string;
  hasLiveSite: boolean;
  thumbnailImage: string;
  summary: string;
  problemSolved: string;
  engineeredSolution: string;
  keyFeatures: string[];
  mockData: {
    heroHeadline: string;
    heroSubheadline: string;
    metrics: { label: string; value: string }[];
    uiHighlights: string[];
  };
}

export interface DurgaPujaFeature {
  id: string;
  title: string;
  bengaliTitle?: string;
  description: string;
  details: string[];
  iconName: string;
}

export interface SponsorTier {
  name: string;
  tagline: string;
  recommendedFor: string;
  digitalPerks: string[];
  featuredPlacement: boolean;
}
