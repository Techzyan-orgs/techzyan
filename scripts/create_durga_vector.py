import os

os.makedirs('public/images', exist_ok=True)

# Create a rich, elegant, transparent SVG vector of Durga Idol (Maa Durga face, crown, tri-nayan, crescent, golden ornaments)
durga_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="500" height="500" fill="none">
  <defs>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FDE68A" />
      <stop offset="50%" stop-color="#F59E0B" />
      <stop offset="100%" stop-color="#B45309" />
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F43F5E" />
      <stop offset="100%" stop-color="#BE123C" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Halo / Prabhabali Arch -->
  <circle cx="250" cy="250" r="210" stroke="url(#goldGrad)" stroke-width="3" stroke-dasharray="8 6" opacity="0.6" filter="url(#glow)"/>
  <circle cx="250" cy="250" r="190" stroke="url(#goldGrad)" stroke-width="2" opacity="0.4"/>

  <!-- Ornate Crown (Mukut) -->
  <path d="M 170 170 Q 250 40 330 170 Q 250 140 170 170 Z" fill="url(#goldGrad)" />
  <path d="M 210 130 Q 250 20 290 130 Z" fill="url(#goldGrad)" />
  <!-- Crown Finial / Kalash -->
  <circle cx="250" cy="25" r="8" fill="#FDE68A" />
  <circle cx="250" cy="50" r="14" fill="url(#goldGrad)" />
  <path d="M 235 60 L 265 60 L 250 35 Z" fill="#FDE68A" />
  
  <!-- Crown Details -->
  <circle cx="250" cy="110" r="10" fill="url(#redGrad)" />
  <circle cx="210" cy="140" r="6" fill="url(#goldGrad)" />
  <circle cx="290" cy="140" r="6" fill="url(#goldGrad)" />
  <circle cx="185" cy="165" r="5" fill="url(#goldGrad)" />
  <circle cx="315" cy="165" r="5" fill="url(#goldGrad)" />

  <!-- Crown Base Band -->
  <path d="M 160 170 Q 250 195 340 170 L 335 185 Q 250 205 165 185 Z" fill="url(#goldGrad)" />

  <!-- Maa Durga Face Silhouette -->
  <path d="M 175 185 Q 165 290 250 380 Q 335 290 325 185 Z" fill="#140E06" stroke="url(#goldGrad)" stroke-width="3"/>

  <!-- Third Eye (Tri-nayan) on Forehead -->
  <path d="M 250 180 Q 262 210 250 240 Q 238 210 250 180 Z" fill="url(#redGrad)" stroke="url(#goldGrad)" stroke-width="2"/>
  <circle cx="250" cy="210" r="4" fill="#FDE68A" />
  <circle cx="250" cy="170" r="5" fill="url(#redGrad)" />

  <!-- Left Eye (Fish-shaped Traditional Patachitra Style) -->
  <path d="M 185 245 Q 215 230 240 260 Q 215 275 185 245 Z" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
  <path d="M 195 243 Q 220 235 235 255" stroke="url(#goldGrad)" stroke-width="3" fill="none"/>
  <!-- Eyeball -->
  <circle cx="215" cy="252" r="7" fill="#080C14" />
  <circle cx="217" cy="250" r="2.5" fill="#FFFFFF" />
  <!-- Eyelash / Surma curve -->
  <path d="M 180 242 Q 215 220 245 255 Q 260 260 250 265" stroke="#000000" stroke-width="3" fill="none"/>

  <!-- Right Eye (Mirrored) -->
  <path d="M 315 245 Q 285 230 260 260 Q 285 275 315 245 Z" fill="#FFFFFF" stroke="#000000" stroke-width="2"/>
  <path d="M 305 243 Q 280 235 265 255" stroke="url(#goldGrad)" stroke-width="3" fill="none"/>
  <!-- Eyeball -->
  <circle cx="285" cy="252" r="7" fill="#080C14" />
  <circle cx="283" cy="250" r="2.5" fill="#FFFFFF" />
  <!-- Eyelash / Surma curve -->
  <path d="M 320 242 Q 285 220 255 255 Q 240 260 250 265" stroke="#000000" stroke-width="3" fill="none"/>

  <!-- Eyebrows -->
  <path d="M 180 230 Q 215 205 245 235" stroke="url(#goldGrad)" stroke-width="4" stroke-linecap="round" fill="none"/>
  <path d="M 320 230 Q 285 205 255 235" stroke="url(#goldGrad)" stroke-width="4" stroke-linecap="round" fill="none"/>

  <!-- Nose -->
  <path d="M 250 235 L 246 295 Q 250 302 254 295 Z" stroke="url(#goldGrad)" stroke-width="2.5" fill="none"/>
  <path d="M 242 295 Q 250 305 258 295" stroke="url(#goldGrad)" stroke-width="2" fill="none"/>

  <!-- Traditional Nose Ring (Nath) -->
  <circle cx="232" cy="298" r="16" stroke="url(#goldGrad)" stroke-width="2.5" fill="none"/>
  <circle cx="220" cy="298" r="3" fill="url(#redGrad)" />
  <!-- Nath Chain extending to Ear -->
  <path d="M 216 298 Q 185 290 165 270" stroke="url(#goldGrad)" stroke-width="1.5" stroke-dasharray="3 3" fill="none"/>

  <!-- Lips -->
  <path d="M 230 325 Q 250 320 270 325 Q 250 345 230 325 Z" fill="url(#redGrad)" stroke="url(#goldGrad)" stroke-width="1.5"/>
  <path d="M 230 325 Q 250 332 270 325" stroke="#9F1239" stroke-width="1.5" fill="none"/>

  <!-- Traditional Chandan Art on Cheeks / Brow -->
  <circle cx="205" cy="215" r="2.5" fill="#FEF3C7"/>
  <circle cx="215" cy="210" r="2.5" fill="#FEF3C7"/>
  <circle cx="225" cy="208" r="2.5" fill="#FEF3C7"/>
  <circle cx="295" cy="215" r="2.5" fill="#FEF3C7"/>
  <circle cx="285" cy="210" r="2.5" fill="#FEF3C7"/>
  <circle cx="275" cy="208" r="2.5" fill="#FEF3C7"/>

  <!-- Ear Ornaments (Jhumka / Kaan-pasha) -->
  <path d="M 160 260 Q 140 280 155 310 Q 170 290 160 260 Z" fill="url(#goldGrad)" />
  <circle cx="155" cy="315" r="5" fill="url(#redGrad)" />
  <path d="M 340 260 Q 360 280 345 310 Q 330 290 340 260 Z" fill="url(#goldGrad)" />
  <circle cx="345" cy="315" r="5" fill="url(#redGrad)" />

  <!-- Sacred Trishul (Trident) Backdrop Motif -->
  <g opacity="0.35" stroke="url(#goldGrad)" stroke-width="3">
    <path d="M 250 10 L 250 480" />
    <path d="M 210 50 Q 250 120 250 160 Q 250 120 290 50" fill="none" stroke-width="4"/>
    <path d="M 250 10 L 240 50 L 260 50 Z" fill="url(#goldGrad)"/>
    <path d="M 210 50 L 200 80 L 220 80 Z" fill="url(#goldGrad)"/>
    <path d="M 290 50 L 280 80 L 300 80 Z" fill="url(#goldGrad)"/>
  </g>
</svg>"""

with open('public/images/durga-idol.svg', 'w', encoding='utf-8') as f:
    f.write(durga_svg)

print("Durga idol SVG written to public/images/durga-idol.svg")
