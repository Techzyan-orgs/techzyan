import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#080C14",
        surface: {
          DEFAULT: "#0F172A",
          subtle: "#131E32",
          card: "#111827",
          cardHover: "#182234",
          border: "rgba(255, 255, 255, 0.08)",
          borderHover: "rgba(56, 189, 248, 0.25)",
        },
        brand: {
          cyan: "#38BDF8",
          cyanGlow: "rgba(56, 189, 248, 0.12)",
          indigo: "#818CF8",
          gold: "#F59E0B",
          emerald: "#34D399",
          muted: "#94A3B8",
          subtle: "#64748B",
        }
      },
      fontFamily: {
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
        display: ["var(--font-jakarta)", "system-ui", "sans-serif"],
        mono: ["var(--font-mono)", "monospace"],
      },
      boxShadow: {
        'glow-cyan': '0 0 25px -5px rgba(56, 189, 248, 0.25)',
        'glow-gold': '0 0 25px -5px rgba(245, 158, 11, 0.25)',
        'card-subtle': '0 4px 20px -2px rgba(0, 0, 0, 0.4)',
      },
      backgroundImage: {
        'radial-gradient-subtle': 'radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.08) 0%, transparent 60%)',
        'puja-gradient': 'radial-gradient(circle at 50% 0%, rgba(245, 158, 11, 0.1) 0%, transparent 70%)',
      }
    },
  },
  plugins: [],
};
export default config;
