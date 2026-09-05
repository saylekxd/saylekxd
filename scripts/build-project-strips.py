"""Generate compact, square-cornered project links from real portfolio captures."""
from pathlib import Path
from base64 import b64encode
from xml.sax.saxutils import escape

root=Path(__file__).resolve().parents[1]
projects=[('swt','Platforma SWT','Projekty, granty i zespół'),('mrm','Edukacja MRM','Platforma młodzieżowych rad'),('slaskie-slady','Śląskie Ślady','Cyfrowe archiwum regionu'),('ai-bajka','AI-Bajka','Interaktywny narrator teatralny')]
for slug,title,caption in projects:
    screenshot=b64encode((root/f'assets/screenshots/{slug}.jpg').read_bytes()).decode()
    for mobile in [False,True]:
        w,h,start=(480,72,330) if mobile else (960,56,720)
        tx,ty,size=(18,29,21) if mobile else (24,35,23)
        cx,cy,cs=(18,52,12) if mobile else (272,33,13)
        arrow=300 if mobile else 670
        svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)} — {escape(caption)}</title>
<desc id="desc">Po prawej fragment rzeczywistego interfejsu projektu. Otwórz projekt.</desc>
<defs><pattern id="paper" width="13" height="11" patternUnits="userSpaceOnUse"><circle cx="2" cy="3" r=".5" fill="#746c5e" opacity=".15"/><path d="m8 7 2-1" stroke="#746c5e" stroke-width=".4" opacity=".08"/></pattern><clipPath id="screen"><rect x="{start}" width="{w-start}" height="{h}"/></clipPath></defs>
<rect width="{w}" height="{h}" fill="#f5f1e8"/><rect width="{start}" height="{h}" fill="url(#paper)"/>
<rect width="3" height="{h}" fill="#244bdb"/>
<g font-family="Arial, Helvetica, sans-serif"><text x="{tx}" y="{ty}" font-size="{size}" font-weight="700" fill="#141819">{escape(title)}</text><text x="{cx}" y="{cy}" font-size="{cs}" fill="#484b4e">{escape(caption)}</text></g>
<path d="M{arrow-7} {h/2+7}l14-14m-12 0h12v12" fill="none" stroke="#244bdb" stroke-width="1.7"/>
<g clip-path="url(#screen)"><image x="{start}" y="0" width="{w-start}" height="{h}" preserveAspectRatio="xMidY{'Min' if slug == 'ai-bajka' else 'Mid'} slice" href="data:image/jpeg;base64,{screenshot}"/></g>
<path d="M{start-8} 0h6l8 {h}h-6Z" fill="#244bdb"/>
</svg>'''
        (root/'assets'/f'project-{slug}-slim{"-mobile" if mobile else ""}.svg').write_text(svg)
