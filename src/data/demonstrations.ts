import { DemonstrationProject } from '@/types';
import { siteConfig } from '@/config/site';

/**
 * Re-exported from centralized siteConfig for backward compatibility.
 * To add, edit, or remove demo projects, edit `src/config/site.ts`!
 */
export const demonstrationProjects: DemonstrationProject[] = siteConfig.demonstrations;
