"""Build self-contained SVG graphics for the GitHub profile."""
from pathlib import Path
from xml.sax.saxutils import escape
import urllib.request
import re

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
INK, CREAM, BLUE = '#141819', '#f5f1e8', '#244bdb'

def svg(name, title, body, height=280):
    text = f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><pattern id="dots" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#141819" opacity=".16"/></pattern><clipPath id="frame"><rect width="960" height="{height}" rx="20"/></clipPath></defs><g clip-path="url(#frame)" font-family="Arial, Helvetica, sans-serif"><rect width="960" height="{height}" fill="{CREAM}"/>{body}</g></svg>'''
    (ASSETS / name).write_text(text)

cards = [
('swt', '01', 'Platforma SWT', 'Codzienna praca organizacji.', 'Zadania / granty / rozliczenia', '#dce3d0', '''
<rect x="663" y="34" width="245" height="217" rx="12" fill="#304d3f" transform="rotate(6 780 140)"/>
<rect x="636" y="42" width="254" height="193" rx="12" fill="#fffdf7" stroke="#c6ccbe"/>
<path d="M636 80H890" stroke="#c6ccbe"/><circle cx="655" cy="62" r="4" fill="#244bdb"/><circle cx="669" cy="62" r="4" fill="#a5b591"/>
<g fill="#e5e9df"><rect x="652" y="95" width="67" height="119" rx="6"/><rect x="730" y="95" width="67" height="119" rx="6"/><rect x="808" y="95" width="67" height="119" rx="6"/></g>
<g fill="#fffdf7"><rect x="660" y="119" width="51" height="37" rx="5"/><rect x="738" y="119" width="51" height="58" rx="5"/><rect x="816" y="119" width="51" height="37" rx="5"/></g>
<path d="m829 137 6 6 11-13" fill="none" stroke="#304d3f" stroke-width="3"/>
<rect x="660" y="167" width="51" height="31" rx="5" fill="#dfb35d"/>
<circle cx="875" cy="212" r="29" fill="#244bdb"/><path d="m863 213 8 8 16-19" fill="none" stroke="white" stroke-width="4"/>
'''),
('mrm', '02', 'Edukacja MRM', 'Pomysły młodych mają znaczenie.', 'Nauka / projekty / współpraca', '#dfe5f6', '''
<rect x="654" y="38" width="202" height="208" rx="4" fill="#244bdb" transform="rotate(-9 755 140)"/>
<path d="M643 75Q703 55 761 82Q824 55 886 75V212Q824 192 761 218Q703 193 643 212Z" fill="#fffdf7" stroke="#b9c3dc" stroke-width="2"/>
<path d="M761 82V218" stroke="#b9c3dc" stroke-width="2"/>
<g stroke="#bcc5dc" stroke-width="4"><path d="M663 136H733M663 150H718M663 164H733M787 157H864M787 171H848M787 185H864"/></g>
<circle cx="699" cy="105" r="15" fill="#244bdb"/><path d="m817 100 13 22 25-4-16 20 9 23-25-9-20 16 4-25-21-13 25-5Z" fill="#cf9d39"/>
<rect x="612" y="192" width="84" height="45" rx="22" fill="#141819"/><path d="M638 215h31m-10-10 10 10-10 10" stroke="white" stroke-width="3" fill="none"/>
'''),
('slaskie-slady', '03', 'Śląskie Ślady', 'Pamięć regionu. Cyfrowy dostęp.', 'Archiwum / mapa / multimedia', '#e8ddc9', '''
<rect x="658" y="43" width="205" height="197" fill="#324139" transform="rotate(-8 760 140)"/>
<rect x="643" y="54" width="220" height="180" fill="#fffdf7" stroke="#c6bda9"/>
<rect x="657" y="67" width="192" height="132" fill="#d3cebe"/>
<path d="M657 169 702 129 741 157 784 111 849 160V199H657Z" fill="#8d998a"/>
<path d="M706 120H785V199H706Z" fill="#3e4941"/><path d="m696 120 49-27 50 27Z" fill="#566350"/>
<path d="M789 85h13v114h-13Z" fill="#566350"/>
<g fill="#d9d6c8"><path d="M717 134h13v18h-13ZM745 134h13v18h-13ZM769 134h8v18h-8Z"/></g>
<path d="M660 217H737" stroke="#8b8d7f" stroke-width="3"/>
<path d="M856 124c-25 0-42 18-42 41 0 31 42 68 42 68s42-37 42-68c0-23-17-41-42-41Z" fill="#244bdb"/><circle cx="856" cy="165" r="13" fill="#f5f1e8"/>
'''),
('ai-bajka', '04', 'AI-Bajka', 'Opowieść, która odpowiada.', 'Teatr / AI / interakcja', '#e1dcec', '''
<rect x="640" y="41" width="247" height="203" rx="70" fill="#252443"/>
<path d="M640 68Q704 107 666 225H640ZM887 68Q823 107 861 225H887Z" fill="#645789"/>
<path d="M649 236Q765 209 878 236" stroke="#ab9cbf" stroke-width="4" fill="none"/>
<path d="M782 71a31 31 0 1 0 28 47 28 28 0 0 1-28-47Z" fill="#e8cb7a"/>
<g fill="#f5f1e8"><circle cx="705" cy="87" r="3"/><circle cx="835" cy="142" r="3"/><path d="m733 65 3 7 7 3-7 3-3 7-3-7-7-3 7-3Z"/></g>
<path d="M690 143Q731 129 768 145Q807 129 842 143V206Q804 193 768 212Q728 195 690 206Z" fill="#fffdf7"/>
<path d="M768 145V212" stroke="#b6abc7" stroke-width="2"/>
<path d="M834 164h49a15 15 0 0 1 15 15v10a15 15 0 0 1-15 15h-26l-17 15v-15h-6a15 15 0 0 1-15-15v-10a15 15 0 0 1 15-15Z" fill="#244bdb"/>
<g fill="white"><circle cx="840" cy="184" r="3"/><circle cx="855" cy="184" r="3"/><circle cx="870" cy="184" r="3"/></g>
''')]
for slug, number, title, subtitle, tags, bg, art in cards:
    body = f'''<rect x="599" width="361" height="280" fill="{bg}"/><rect x="599" y="15" width="345" height="251" fill="url(#dots)"/>
<text x="36" y="43" font-size="15" font-weight="700" letter-spacing="2" fill="{BLUE}">WYBRANE REALIZACJE / {number}</text>
<text x="34" y="104" font-size="43" font-weight="700" letter-spacing="-1" fill="{INK}">{title}</text>
<text x="36" y="149" font-size="25" fill="#343b3e">{subtitle}</text>
<text x="36" y="184" font-size="19" fill="#51585b">{tags}</text>
<path d="M36 210H560" stroke="#d3cfc6"/>
<text x="36" y="249" font-size="20" font-weight="700" fill="{BLUE}">Poznaj projekt</text><path d="M527 241h28m-9-9 9 9-9 9" stroke="{BLUE}" stroke-width="2" fill="none"/>{art}'''
    svg(f'project-{slug}.svg', f'{title}. {subtitle} {tags}. Poznaj projekt.', body)

# Keep icon source files locally, so rebuilding does not require a network after first run.
icons = ASSETS / 'icons'
icons.mkdir(exist_ok=True)
def icon(slug, x, y, color):
    path = icons / f'{slug}.svg'
    if not path.exists():
        url = f'https://cdn.jsdelivr.net/npm/simple-icons@16.0.0/icons/{slug}.svg'
        path.write_bytes(urllib.request.urlopen(url).read())
    paths = ''.join(re.findall(r'<path[^>]+>', path.read_text()))
    return f'<g transform="translate({x} {y}) scale(1.4)" fill="{color}">{paths}</g>'

rows = [
('01', 'WEB', 'Interfejsy i aplikacje', [('react','React','#087e9b'),('nextdotjs','Next.js',INK),('typescript','TypeScript','#2766a8')]),
('02', 'MOBILE', 'Aplikacje iOS / Android', [('react','React Native','#087e9b'),('expo','Expo',INK),(None,'iOS / Android',INK)]),
('03', 'BACKEND', 'Dane i logika aplikacji', [('supabase','Supabase','#18794e'),('postgresql','PostgreSQL','#336791'),('nodedotjs','Node.js','#397b2b')]),
('04', 'INTEGRACJE', 'IoT / ESP32 / automatyzacje', [('python','Python','#306998'),('arduino','Arduino','#007b80'),(None,'API / MQTT',INK)])]
body = ''
for i,(num,label,sub,techs) in enumerate(rows):
    y=i*126
    if i%2: body+=f'<rect y="{y}" width="960" height="126" fill="#ebe8df"/>'
    body+=f'<text x="30" y="{y+39}" fill="{BLUE}" font-size="14" font-weight="700">{num}</text><text x="65" y="{y+42}" fill="{INK}" font-size="22" font-weight="700" letter-spacing="1">{label}</text><text x="65" y="{y+75}" fill="#50585c" font-size="18">{sub}</text>'
    for j,(slug,name,color) in enumerate(techs):
        x=324+j*207
        body+=f'<rect x="{x}" y="{y+24}" width="190" height="78" rx="12" fill="#fffdf8" stroke="#d6d2c9"/>'
        if slug: body+=icon(slug,x+14,y+45,color)
        else: body+=f'<text x="{x+13}" y="{y+70}" font-size="26" fill="{BLUE}" font-weight="700">↔</text>'
        body+=f'<text x="{x+60}" y="{y+70}" font-size="18" font-weight="700" fill="{INK}">{name}</text>'
svg('technology-stack.svg','Technologie: Web — React, Next.js, TypeScript. Mobile — React Native, Expo. Backend — Supabase, PostgreSQL, Node.js. Integracje i IoT — Python, Arduino, API, MQTT.',body,504)

process_icons = {
'discover': '<path d="M17 24h76v51H52L32 91V75H17Z" fill="#f5f1e8" stroke="#9ca9e6" stroke-width="2"/><path d="M48 49h64v45H93l-17 15V94H48Z" fill="#244bdb"/><g fill="#fffdf7"><circle cx="65" cy="71" r="4"/><circle cx="81" cy="71" r="4"/><circle cx="97" cy="71" r="4"/></g>',
'plan': '<path d="M30 16h61l17 17v78H30Z" fill="#f5f1e8" stroke="#9ca9e6" stroke-width="2"/><path d="M91 16v19h17" fill="#c6cfef"/><g stroke="#8695c2" stroke-width="3"><path d="M44 46h46M44 60h33M44 74h39"/></g><circle cx="36" cy="92" r="24" fill="#244bdb"/><path d="m26 92 7 7 14-16" stroke="#fffdf7" stroke-width="4" fill="none"/>',
'build': '<rect x="15" y="23" width="98" height="72" rx="9" fill="#f5f1e8" stroke="#9ca9e6" stroke-width="2"/><path d="M15 43h98" stroke="#9ca9e6" stroke-width="2"/><circle cx="26" cy="33" r="3" fill="#244bdb"/><path d="m47 54-12 13 12 13m34-26 12 13-12 13M68 53l-9 29" stroke="#244bdb" stroke-width="5" fill="none"/><path d="M41 108h47" stroke="#9ca9e6" stroke-width="6"/><circle cx="103" cy="97" r="18" fill="#244bdb"/><path d="m95 97 6 6 10-13" stroke="white" stroke-width="3" fill="none"/>',
'grow': '<rect x="20" y="78" width="22" height="31" rx="4" fill="#f5f1e8" stroke="#9ca9e6" stroke-width="2"/><rect x="53" y="57" width="22" height="52" rx="4" fill="#c6cfef"/><rect x="86" y="32" width="22" height="77" rx="4" fill="#244bdb"/><path d="M22 57 54 34 68 39 95 13m-21 0h21v21" fill="none" stroke="#6888ff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'
}
for name, shapes in process_icons.items():
    (ASSETS / f'process-{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 128 128">{shapes}</svg>')
