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


# Editorial panels share the project cards' palette and typography.
def text(x,y,value,size=24,color=INK,weight=400,extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(value)}</text>'

def panel(name,title,body,width,height):
    (ASSETS/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><defs><pattern id="grain" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".6" fill="#141819" opacity=".1"/></pattern><clipPath id="frame"><rect width="{width}" height="{height}" rx="20"/></clipPath></defs><g clip-path="url(#frame)" font-family="Arial, Helvetica, sans-serif"><rect width="{width}" height="{height}" fill="{CREAM}"/>{body}</g></svg>')

steps=[('01','Rozmowa',['Poznajemy misję, ludzi','i potrzeby organizacji.'],'Diagnoza / kierunek'),('02','Plan',['Łączymy zakres, budżet','i możliwości finansowania.'],'Strategia / granty'),('03','Wdrożenie',['Budujemy narzędzia.','Przygotowujemy zespół.'],'Produkt / szkolenia'),('04','Rozwój',['Utrzymanie, automatyzacja','i analiza efektów.'],'Wsparcie / rezultaty')]
for mobile in [False,True]:
    w,h=(480,1010) if mobile else (960,600)
    body=text(36,45,'OD PIERWSZEJ ROZMOWY DO DALSZEGO ROZWOJU',12,BLUE,700,'letter-spacing="1.1"')
    body+=text(34,98,'Wspólnie. Krok po kroku.',32 if mobile else 42,INK,700,'letter-spacing="-1"')
    for i,(num,title,lines,tag) in enumerate(steps):
        x,y=(36,160+i*215) if mobile else (36+(i%2)*472,168+(i//2)*225)
        body+=f'<path d="M{x} {y-32}h{408 if mobile else 416}" stroke="#ccc8bf"/>'
        body+=text(x,y+33,num,64,BLUE,700,'letter-spacing="-4"')
        body+=text(x+100,y+9,title,34,INK,700)
        for j,line in enumerate(lines):body+=text(x+100,y+47+j*29,line,20 if mobile else 22,'#40464a')
        body+=text(x+100,y+124,tag.upper(),12,BLUE,700,'letter-spacing="1.1"')
    panel('working-together'+('-mobile' if mobile else '')+'.svg','Jak pracujemy: rozmowa i diagnoza potrzeb; plan projektu i finansowania; wdrożenie oraz szkolenia; rozwój, utrzymanie i analiza efektów.',body,w,h)

techs=[('react','React'),('nextdotjs','Next.js'),('typescript','TypeScript'),('react','React Native'),('expo','Expo'),('nodedotjs','Node.js'),('supabase','Supabase'),('postgresql','PostgreSQL'),('python','Python')]
for mobile in [False,True]:
    w,h=(480,740) if mobile else (960,470)
    split=260 if mobile else 355
    body=f'<rect width="{w if mobile else split}" height="{split if mobile else h}" fill="{BLUE}"/>'
    body+=text(34,43,'NASZ WARSZTAT / TECH4GOOD',13,CREAM,700,'letter-spacing="1.3"')
    body+=text(32,106,'Narzędzia',44,CREAM,700,'letter-spacing="-1"')+text(32,158,'dobrane do misji.',34 if mobile else 32,CREAM,700,'letter-spacing="-1"')
    for j,line in enumerate(['Web / Mobile','Dane / Automatyzacje']):body+=text(35,(202 if mobile else 239)+j*31,line,20,CREAM)
    if not mobile:
        body+='<path d="M36 331h278" stroke="#8b9fec"/>'
        body+=text(35,370,'OD INTERFEJSU',12,CREAM,700,'letter-spacing="2"')+text(35,394,'PO INTEGRACJE.',12,CREAM,700,'letter-spacing="2"')
    for i,(slug,label) in enumerate(techs):
        x=(80+(i%3)*160) if mobile else (456+(i%3)*192)
        y=(298+(i//3)*120) if mobile else (55+(i//3)*115)
        body+=icon(slug,x-17,y,INK)
        body+=text(x,y+64,label,17 if mobile else 18,INK,500,'text-anchor="middle"')
    yy=668 if mobile else 392
    xx=25 if mobile else 390
    body+=f'<path d="M{xx} {yy}H{w-30}" stroke="#ccc8bf"/>'
    body+=text(xx,yy+31,'TAKŻE W NASZYM ZESTAWIE',11,BLUE,700,'letter-spacing="1.4"')
    body+=text(xx,yy+57,'Arduino / ESP32 / API / MQTT',17,INK)
    panel('technology-workshop'+('-mobile' if mobile else '')+'.svg','Technologie: React, Next.js, TypeScript, React Native, Expo, Node.js, Supabase, PostgreSQL, Python. Także Arduino, ESP32, API i MQTT.',body,w,h)
