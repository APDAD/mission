"""Content for the nine NutriDyn condition sheets (front = the condition,
back = lifestyle + nutrient solutions).  Original wording throughout.  Product
claims are structure/function only; every back page carries the DSHEA
disclaimer.  Product facts live in products.py so one label change updates
every sheet.
"""
import art
from kit import icon, THEMES

EXTRA_CSS = r"""
.outrow{display:grid;gap:0.1in;margin-top:0.06in}
.out{background:var(--c1);color:#fff;border-radius:6px;padding:0.07in 0.1in;text-align:center;position:relative}
.out::before{content:"";position:absolute;left:50%;top:-9px;margin-left:-9px;border:9px solid transparent;border-top:0;border-bottom:9px solid var(--c1)}
.out b{display:block;font-family:Merriweather,Georgia,serif;font-size:11pt}
.out span{display:block;font-size:8.4pt;opacity:.95;margin-top:2px}
.after{margin:0.1in auto 0;max-width:6.4in;text-align:center;font-size:8.6pt;color:#2B3236;background:var(--soft);
  border-radius:6px;padding:0.06in 0.14in}
.after b{color:var(--deep)}
.riskhead{font:900 12pt Merriweather,Georgia,serif;color:var(--c1);text-align:center;margin:0.1in 0 0.06in;letter-spacing:.02em}
.risk{display:grid;gap:0.08in 0.06in}
.rf{display:flex;flex-direction:column;align-items:center;text-align:center;color:#59636A}
.rf .ic{color:#7B7F86}
.rf span{font-size:8.3pt;line-height:1.2;color:#3A4247;margin-top:2px}
.twocol{display:grid;grid-template-columns:1.12fr 1fr;gap:0.16in;align-items:start}
.lst{columns:2;column-gap:0.2in;margin:0.04in 0 0.06in;padding-left:14px;font-size:9pt}
.lst li{margin:0 0 2px}
.alarm{border:1.6px solid #C0392B;border-radius:8px;padding:0.06in 0.12in;background:#FDF1EF;margin:0.06in 0}
.alarm b{color:#A5281E;font-size:8.6pt;letter-spacing:.04em;text-transform:uppercase}
.alarm p{margin:2px 0 0;font-size:8.6pt}
.p{font-size:9.1pt;line-height:1.42;margin:0 0 0.07in;color:#2B3236}
.p b{color:var(--deep)}
.fn{font-size:7pt;color:#5E686F;line-height:1.3;margin-top:auto}
.bp{width:100%;border-collapse:collapse;font-size:8.4pt}
.bp th{background:var(--c1);color:#fff;text-align:left;padding:5px 8px;font-size:8pt}
.bp td{padding:4px 8px;border-bottom:1px solid #EEE3E1}
.bp tr:nth-child(even) td{background:var(--tint)}
.bp td.n{text-align:center;font-variant-numeric:tabular-nums;font-weight:700}
.bp td.c{text-align:center;color:#7A848A;font-size:7.2pt}
.sd{display:grid;grid-template-columns:1fr;gap:6px}
.sd div{border-left:4px solid var(--c1);padding-left:8px;font-size:8.2pt}
.sd b{font-family:Merriweather,Georgia,serif;color:var(--deep);font-size:10pt;display:block}
.trig{display:grid;grid-template-columns:repeat(7,1fr);background:linear-gradient(90deg,var(--c1),var(--c2));color:#fff;
  border-radius:4px;margin:0.04in 0 0.06in}
.trig span{text-align:center;font:800 7.4pt Inter,sans-serif;letter-spacing:.06em;text-transform:uppercase;padding:5px 2px;line-height:1.15}
.cmp{width:100%;border-collapse:collapse;font-size:8.6pt;margin-top:0.02in}
.cmp th{font:900 10.5pt Merriweather,Georgia,serif;color:var(--deep);padding:4px 6px;text-align:center}
.cmp td{padding:5px 8px;border-top:1px solid #DDE7E6;vertical-align:top}
.cmp td.k{font:800 7.4pt Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#fff;background:var(--c1);
  text-align:center;width:1.05in;vertical-align:middle}
.cmp td.a{text-align:right}
.chev{display:grid;grid-template-columns:1fr 1fr 1fr;margin:0.04in 0 0.08in}
.chev div{padding:0.1in 0.22in 0.1in 0.3in;color:#fff;clip-path:polygon(0 0,90% 0,100% 50%,90% 100%,0 100%,8% 50%)}
.chev div:first-child{clip-path:polygon(0 0,90% 0,100% 50%,90% 100%,0 100%);padding-left:0.16in}
.chev div:last-child{clip-path:polygon(0 0,100% 0,100% 100%,0 100%,8% 50%)}
.chev h4{margin:0 0 3px;font:800 8.6pt Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase}
.chev ul{margin:0;padding:0;list-style:none;font-size:8.4pt;line-height:1.3}
.stat{display:flex;gap:0.14in;align-items:center;background:var(--soft);border-radius:8px;padding:0.07in 0.14in;margin-top:0.08in}
.stat>b{font:900 22pt Merriweather,Georgia,serif;color:var(--c1);line-height:1;white-space:nowrap}
.stat span{font-size:8.8pt;color:#2B3236}
.ticks{display:grid;grid-template-columns:repeat(3,1fr);gap:0.08in;margin-top:0.06in}
.tk{background:#FCEFE4;border-radius:8px;padding:0.06in 0.1in;display:flex;gap:8px;align-items:center}
.tk .ic{color:#5B3A22;flex:none}
.tk b{display:block;font-size:8.6pt;color:#4A2C80}
.tk span{font-size:7.8pt;color:#3A4247;line-height:1.25}
.ring{display:grid;grid-template-columns:repeat(5,1fr);gap:0.08in 0.06in;margin-top:0.04in}
.rg{display:flex;flex-direction:column;align-items:center;text-align:center}
.rg .c{width:0.62in;height:0.62in;border-radius:50%;background:#F1E7E2;display:flex;align-items:center;justify-content:center;
  color:#8A5A52;box-shadow:0 0 0 2px #fff,0 0 0 3px #E8D8D1}
.rg span{font-size:7.8pt;line-height:1.2;margin-top:3px;color:#3A4247}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:0.12in;margin-top:0.08in}
.fbox h4{margin:0 0 4px;background:var(--c1);color:#fff;font:800 8.4pt Inter,sans-serif;letter-spacing:.08em;text-transform:uppercase;
  padding:4px 10px;border-radius:3px}
.fbox p,.fbox li{font-size:8.6pt;line-height:1.35;margin:0}
.fbox ul{margin:0;padding-left:14px}
.sym{display:grid;grid-template-columns:repeat(7,1fr);gap:0.04in;margin:0.02in 0 0.08in}
.sym div{display:flex;flex-direction:column;align-items:center;text-align:center;color:var(--c1)}
.sym span{font-size:8pt;color:#3A4247;margin-top:2px;line-height:1.15}
.steps5{display:flex;flex-direction:column;gap:5px}
.st5{display:flex;gap:8px;align-items:flex-start}
.st5 .n{flex:none;width:0.26in;height:0.26in;border-radius:50%;background:var(--c1);color:#fff;font:800 9pt Inter,sans-serif;
  display:flex;align-items:center;justify-content:center}
.st5 b{font:800 9.6pt Inter,sans-serif;color:var(--deep);display:block}
.st5 span{font-size:8.3pt;color:#3A4247;line-height:1.3}
.note{border-left:4px solid #D9873A;background:#FDF4EC;padding:0.05in 0.12in;font-size:8.5pt;margin-top:0.08in;border-radius:0 6px 6px 0}
.note b{color:#9A4F12}
.lymebody svg{max-height:3.25in;width:auto!important;margin:0 auto}
"""


def risk_grid(items, cols=4, size="0.5in"):
    cells = "".join(f'<div class="rf">{icon(ic, size, sw=2.6)}<span>{lab}</span></div>' for ic, lab in items)
    return f'<div class="risk" style="grid-template-columns:repeat({cols},1fr)">{cells}</div>'


def outcomes(items):
    cells = "".join(f'<div class="out"><b>{a}</b><span>{b}</span></div>' for a, b in items)
    return f'<div class="outrow" style="grid-template-columns:repeat({len(items)},1fr)">{cells}</div>'


# =========================================================================== fronts
def front_gut(t):
    return (f'<div class="art">{art.art_gut_barrier(t)}</div>'
            + outcomes([("Food reactions", "Bloating or symptoms after foods such as gluten, dairy or soy"),
                        ("Immune overload", "Seasonal allergies, skin flare-ups, catching every cold"),
                        ("Poor absorption", "Running low on vitamin D, B12, iron, magnesium or zinc")])
            + '<p class="after">Researchers are also studying how a leaky barrier connects to <b>autoimmune conditions</b> '
              'such as Hashimoto\'s thyroiditis, rheumatoid arthritis and lupus. If you live with one, ask your practitioner '
              'whether gut support belongs in your plan.</p>')


def front_liver(t):
    return (f'<div class="riskhead" style="text-align:left;margin-top:0.02in">HOW FATTY LIVER PROGRESSES</div>'
            f'<div class="art">{art.art_fatty_liver(t)}</div>'
            '<div class="riskhead" style="margin-top:0.16in">RISK FACTORS</div>'
            + risk_grid([("sugar", "Sugary drinks and<br>excess sugar"), ("meter", "Insulin resistance<br>or prediabetes"),
                         ("waist", "Weight carried<br>at the belly"), ("heartpulse", "High blood<br>pressure"),
                         ("calendar", "PCOS"), ("gut", "Gut imbalance<br>(dysbiosis)"),
                         ("dna", "Family genes"), ("tube", "High triglycerides")], 4, "0.62in"))


def front_reflux(t):
    left = ('<p class="p">About <b>1 in 5 U.S. adults</b> has GERD. At the bottom of your esophagus sits a ring of muscle, '
            'the <b>lower esophageal sphincter (LES)</b>. It opens to let food into the stomach and closes to keep it there. '
            'In GERD the valve relaxes when it should not, so acid and digestive enzymes splash back into a tube that has '
            'no protective lining against them. Heartburn is the most common sign. Others include:</p>'
            '<ul class="lst"><li>A sour taste or food coming back up</li><li>Hoarse voice, throat clearing</li>'
            '<li>Chronic dry cough</li><li>Trouble swallowing</li><li>Bad breath</li><li>Fullness or upset stomach after meals</li></ul>'
            '<div class="alarm"><b>Call your doctor promptly if</b><p>food sticks when you swallow, you vomit blood or see black '
            'stools, you lose weight without trying, or you have chest pain (never assume it is only heartburn).</p></div>'
            '<p class="p" style="margin-top:0.06in">Left alone, reflux can inflame and scar the esophagus. A digestive tract that '
            'stays irritated also affects how well you absorb nutrients, and that ripples into energy, immunity and mood.</p>'
            '<p class="p"><b>About acid-reducing medicines.</b> Proton pump inhibitors (omeprazole, esomeprazole, pantoprazole) and '
            'H2 blockers lower acid and help many people heal. With long-term use they are linked to low <b>magnesium</b> and '
            '<b>vitamin B12</b>, and the FDA has warned about low magnesium and bone fractures with long-term, high-dose PPI use.<sup>1</sup> '
            'Do not stop one on your own: ask your prescriber and pharmacist for a plan. Food, habits and targeted nutrients can '
            'lower how often reflux shows up.</p>')
    return (f'<div class="twocol"><div>{left}</div><div class="art" style="padding-top:0.1in">{art.art_reflux(t)}</div></div>'
            '<p class="fn">1. U.S. Food and Drug Administration. Drug Safety Communications on proton pump inhibitors: possible '
            'increased risk of fractures (2010) and low magnesium levels with long-term use (2011).</p>')


def front_bp(t):
    table = ('<table class="bp"><tr><th>Category</th><th style="text-align:center">Top number<br>(systolic)</th><th></th>'
             '<th style="text-align:center">Bottom number<br>(diastolic)</th></tr>'
             '<tr><td>Normal</td><td class="n">under 120</td><td class="c">and</td><td class="n">under 80</td></tr>'
             '<tr><td>Elevated</td><td class="n">120 to 129</td><td class="c">and</td><td class="n">under 80</td></tr>'
             '<tr><td>Stage 1 high</td><td class="n">130 to 139</td><td class="c">or</td><td class="n">80 to 89</td></tr>'
             '<tr><td>Stage 2 high</td><td class="n">140 or more</td><td class="c">or</td><td class="n">90 or more</td></tr>'
             '<tr><td><b>Severe: call your doctor</b></td><td class="n">over 180</td><td class="c">and/or</td><td class="n">over 120</td></tr></table>'
             '<p class="fn" style="margin-top:3px">Categories from the American Heart Association and American College of Cardiology.</p>')
    sd = ('<div class="sd"><div><b>Systolic</b>The top number: pressure on artery walls while the heart pumps.</div>'
          '<div><b>Diastolic</b>The bottom number: pressure between beats, while the heart rests.</div>'
          '<div><b>Measure it right</b>Sit 5 minutes, feet flat, back supported, arm at heart level. Take two readings a minute apart.</div></div>')
    return (f'<div class="art">{art.art_bp(t)}</div>'
            '<div class="riskhead">RISK FACTORS</div>'
            + risk_grid([("scale", "Extra weight"), ("salt", "High-sodium,<br>processed food"), ("glass", "Too much<br>alcohol"),
                         ("smoke", "Smoking"), ("breath", "Chronic stress"), ("moon", "Poor sleep or<br>sleep apnea"),
                         ("kidney", "Kidney<br>disease"), ("hormone", "Hormone<br>changes"), ("dna", "Family<br>history"),
                         ("age", "Increasing age")], 5, "0.46in")
            + f'<div style="display:grid;grid-template-columns:0.95fr 1.6fr;gap:0.18in;margin-top:0.12in;align-items:start">{sd}<div>{table}</div></div>')


def front_ibd(t):
    trig = "".join(f"<span>{x}</span>" for x in ["Stress", "Poor sleep", "Ultra-processed food", "Food sensitivities", "NSAID pain relievers", "Smoking", "Infections"])
    rows = [("Where", "Colon and rectum only", "Anywhere from mouth to anus, most often the end of the small intestine"),
            ("Pattern", "One continuous stretch, no gaps", "Patches, with healthy tissue between them"),
            ("Depth", "Inner lining of the bowel", "Can reach through the full thickness of the bowel wall"),
            ("Pain", "Often lower left belly", "Often lower right belly"),
            ("Bleeding", "Common with bowel movements", "Less common")]
    tr = "".join(f'<tr><td class="a">{a}</td><td class="k">{k}</td><td>{b}</td></tr>' for k, a, b in rows)
    return (f'<div class="small" style="font:800 7.4pt Inter;letter-spacing:.12em;color:var(--deep);margin-top:2px">WHAT CAN STIR UP SYMPTOMS</div>'
            f'<div class="trig">{trig}</div>'
            f'<div class="art">{art.art_ibd(t)}</div>'
            f'<table class="cmp"><tr><th>Ulcerative colitis</th><th></th><th>Crohn\'s disease</th></tr>{tr}</table>'
            '<p class="after" style="margin-top:0.1in">Both conditions raise colon cancer risk over time, so keep up with the '
            '<b>colonoscopy schedule</b> your gastroenterologist sets, even in good stretches.</p>')


def front_insulin(t):
    def col(bg, h, items):
        lis = "".join(f"<li>{i}</li>" for i in items)
        return f'<div style="background:{bg}"><h4>{h}</h4><ul>{lis}</ul></div>'
    chev = ('<div class="chev">'
            + col("#8E8B95", "What drives it", ["Sugar and processed food", "Sitting most of the day", "Short or poor sleep", "Chronic stress", "Extra belly fat", "Low magnesium or vitamin D", "Family history"])
            + col("#C2392E", "Signs you may notice", ["Sugar cravings", "Tired after meals", "Weight gain at the waist", "Hungry soon after eating", "Hard to lose weight", "High triglycerides", "Skin tags, dark skin patches"])
            + col("#62121A", "Where it leads", ["Type 2 diabetes", "Heart disease and stroke", "High blood pressure", "Fatty liver (MASLD)", "PCOS and hormone shifts", "Memory decline"])
            + "</div>")
    return (chev + f'<div class="art">{art.art_insulin(t)}</div>'
            '<div class="stat"><b>1 in 3</b><span>U.S. adults has prediabetes, and <b>more than 8 in 10</b> of them do not know it '
            '(CDC). A fasting insulin, glucose and A1c panel can catch insulin resistance years before diabetes.</span></div>')


def front_lyme(t):
    body = art.art_lyme_body(t)
    ticks = ('<div class="ticks">'
             f'<div class="tk">{icon("tick", "0.42in", sw=2.6)}<div><b>Blacklegged (deer) tick</b><span>Eastern U.S., Georgia included. The main Lyme carrier.</span></div></div>'
             f'<div class="tk">{icon("tick", "0.38in", sw=2.6)}<div><b>Western blacklegged</b><span>Pacific coast states. Also spreads Lyme.</span></div></div>'
             f'<div class="tk">{icon("tick", "0.40in", sw=2.6)}<div><b>Lone star tick</b><span>Common across the Southeast. Ehrlichiosis, alpha-gal allergy.</span></div></div></div>')
    return (f'<div class="riskhead" style="text-align:left;margin:0.02in 0 0.02in">HOW IT SPREADS</div>'
            f'<div class="art">{art.art_lyme_transmission(t)}</div>'
            '<div style="display:grid;grid-template-columns:1.35fr 1fr;gap:0.12in;margin-top:0.08in;align-items:start">'
            f'<div><div class="riskhead" style="text-align:left;margin:0 0 2px">SYMPTOMS</div>'
            '<div style="display:flex;gap:10px;font:800 7.6pt Inter;letter-spacing:.08em;margin-bottom:2px">'
            '<span style="background:#4A2C80;color:#fff;padding:3px 10px;border-radius:3px">EARLY: DAYS TO WEEKS</span>'
            '<span style="background:#D9873A;color:#fff;padding:3px 10px;border-radius:3px">LATER: WEEKS TO MONTHS</span></div>'
            f'<div class="art lymebody">{body}</div></div>'
            '<div><div class="note" style="margin-top:0.3in"><b>See a clinician promptly</b> if a rash, fever, aches or joint '
            'swelling show up after a tick bite or time outdoors. Early antibiotic treatment works best.</div>'
            '<div class="note"><b>Not everyone sees the tick.</b> Nymphs are the size of a poppy seed, and many people never '
            'get the bull\'s-eye rash, which is why Lyme gets mistaken for flu, fibromyalgia or chronic fatigue.</div>'
            '<div class="note"><b>After treatment,</b> some people have fatigue, pain or brain fog that lingers for months. '
            'That recovery stretch is where food, sleep and the support on the back of this page come in.</div></div></div>'
            f'<div class="riskhead" style="text-align:left;margin:0.06in 0 0">KNOW YOUR TICKS</div>{ticks}')


def front_pcos(t):
    ring = "".join(f'<div class="rg"><div class="c">{icon(ic, "0.36in", sw=3)}</div><span>{lab}</span></div>' for ic, lab in [
        ("calendar", "Irregular or<br>missed periods"), ("acne", "Acne"), ("hair", "Extra facial or<br>body hair"),
        ("hair", "Thinning<br>scalp hair"), ("waist", "Weight gain<br>at the waist"), ("battery", "Fatigue"),
        ("brain", "Mood changes,<br>anxiety"), ("baby", "Trouble getting<br>pregnant"), ("flame", "Low-grade<br>inflammation"),
        ("meter", "Blood sugar<br>swings")])
    return (f'<div class="art">{art.art_pcos(t)}</div>'
            '<div class="riskhead" style="margin-top:0.04in">SIGNS AND SYMPTOMS</div>'
            f'<div class="ring">{ring}</div>'
            '<div class="facts"><div class="fbox"><h4>PCOS fact</h4><p>Up to <b>1 in 8</b> women of reproductive age has PCOS, '
            'and up to <b>70 percent</b> have never been diagnosed (World Health Organization). PCOS happens at every body size: '
            'you can have it at a normal weight.</p></div>'
            '<div class="fbox"><h4>Risk factors</h4><ul><li><b>You can change:</b> chronic stress, a high-sugar, low-nutrient diet, '
            'inactivity and weight swings, hormone-disrupting chemicals</li><li><b>Genetic:</b> a mother or sister with PCOS or '
            'type 2 diabetes raises your risk</li></ul></div></div>')


def front_mold(t):
    sym = "".join(f'<div>{icon(ic, "0.44in", sw=2.8)}<span>{lab}</span></div>' for ic, lab in [
        ("battery", "Fatigue"), ("bone", "Joint aches"), ("flame", "Inflammation"), ("brain", "Brain fog"),
        ("headache", "Headaches"), ("nose", "Sinus<br>congestion"), ("lungs", "Cough or<br>wheeze")])
    steps = [("Remove the exposure", "Find and fix the moisture first. A qualified inspector can test (ERMI or HERTSMI-2 dust tests are common). Check ceilings, crawl spaces, under sinks, HVAC and any water damage."),
             ("Support liver and bile flow", "Your liver packages toxins into bile for removal."),
             ("Support the gut and elimination", "Fiber and binders carry toxins out instead of letting them recirculate."),
             ("Address the sinuses", "Sinuses can hold on to mold long after you leave the building."),
             ("Treat fungal overgrowth if found", "Only when your practitioner confirms it.")]
    st = "".join(f'<div class="st5"><div class="n">{i + 1}</div><div><b>{a}</b><span>{b}</span></div></div>' for i, (a, b) in enumerate(steps))
    return (f'<div class="sym">{sym}</div>'
            '<div style="display:grid;grid-template-columns:1.05fr 1fr;gap:0.14in;align-items:start">'
            f'<div><div class="riskhead" style="text-align:left;margin:0 0 6px">YOUR RECOVERY, IN ORDER</div><div class="steps5">{st}</div></div>'
            f'<div class="art" style="padding-top:0.06in">{art.art_mold_home(t)}</div></div>'
            '<div class="riskhead" style="text-align:left;margin:0.1in 0 0">WHY BINDERS MATTER</div>'
            f'<div class="art">{art.art_binder(t)}</div>')


# =========================================================================== sheets
SHEETS = [
    {
        "slug": "intestinal-permeability", "code": "ND-GI-101", "theme": "gut", "series": "Gut Health Series",
        "title": "Intestinal Permeability", "sub": "Your gut barrier, and why it leaks",
        "intro": ("Your gut lining is a single layer of cells, sealed at the seams by <b>tight junctions</b>. It is built to let "
                  "nutrients through and keep everything else out: undigested food, microbes and the toxins they make. Poor diet, "
                  "infections, some medications, alcohol and chronic stress can loosen those seams. Researchers call this "
                  "<b>increased intestinal permeability</b>; you may have heard it called leaky gut. The good news: your gut lining "
                  "renews itself every few days, so the right food, habits and nutrients give it a real chance to rebuild."),
        "front": front_gut,
        "back": {
            "life_title": "Lifestyle Modifications", "style": "checks",
            "life": [("Find and remove food triggers", ["Gluten", "Dairy", "Soy", "Ask about a 3-week elimination trial"]),
                     ("Protect your gut flora", ["Use antibiotics only when truly needed", "Add one fermented food a day (kefir, yogurt, sauerkraut)"]),
                     ("Eat whole, unprocessed foods", ["Cut added sugar and ultra-processed snacks", "Fill half the plate with vegetables and fruit", "Work up to 25 to 30 g of fiber a day"]),
                     ("Ease the load on the lining", ["Keep alcohol low", "Ask before regular ibuprofen or naproxen", "Sleep 7 to 9 hours, manage stress"])],
            "cols": [
                {"p": "gi_integrity", "need": "Rebuild the lining", "needsub": "L-glutamine, zinc carnosine, DGL, aloe", "start": True,
                 "bullets": ["Fuel for the cells that line your gut", "Soothing botanicals coat and calm"],
                 "dose": "1 scoop daily", "dosesub": "in 6 to 8 oz water"},
                {"p": "ultrabiotic_dms", "need": "Rebalance gut flora", "needsub": "multi-strain probiotic + S. boulardii",
                 "bullets": ["Seven friendly strains", "S. boulardii keeps working alongside antibiotics"],
                 "dose": "1 capsule daily", "dosesub": "at bedtime"},
                {"p": "gi_defend", "need": "Bind and calm", "needsub": "serum-derived bovine immunoglobulins",
                 "bullets": ["Immunoglobulins bind microbial toxins in the gut", "Supports barrier function and immune balance"],
                 "dose": "dose_from_db"},
                {"p": "curcumin_bcm95", "need": "Cool the fire", "needsub": "curcumin, the active compound in turmeric",
                 "bullets": ["Supports a healthy inflammatory response", "Enhanced-absorption curcumin"],
                 "dose": "dose_from_db"},
                {"p": "enzymes", "need": "Digest it fully", "needsub": "digestive enzymes",
                 "bullets": ["Breaks food down so fewer large particles reach the lining", "Take with your largest meals"],
                 "dose": "dose_from_db"},
            ],
            "rx": ["<b>NSAIDs</b> (ibuprofen, naproxen) used regularly can irritate the gut lining. Ask about alternatives.",
                   "<b>Antibiotics:</b> take the probiotic 2 hours apart from each dose and keep going 2 weeks after the course.",
                   "<b>Acid blockers</b> long term can lower magnesium and B12. Ask about a check."],
        },
    },
    {
        "slug": "fatty-liver", "code": "ND-CM-201", "theme": "metab", "series": "Metabolic Health Series",
        "title": "Fatty Liver Disease", "sub": "MASLD, the condition formerly called NAFLD",
        "intro": ("Fatty liver disease is extra fat stored inside liver cells that is <b>not caused by heavy drinking</b>. In 2023, "
                  "liver specialists renamed it <b>MASLD</b> (metabolic dysfunction-associated steatotic liver disease) because it runs "
                  "on the same metabolism as insulin resistance, belly fat, high triglycerides and high blood pressure. It is the most "
                  "common liver condition in the world, affecting roughly <b>1 in 3 adults</b>, and most people feel nothing. Caught "
                  "early, it is often reversible."),
        "front": front_liver,
        "back": {
            "life_title": "Lifestyle Recommendations", "style": "circle",
            "life": [("plate", "Eat Mediterranean", "Vegetables, lean protein, olive oil, nuts and fish. Cut sugary drinks, juice and refined carbs: they turn into liver fat fastest."),
                     ("scale", "Lose 7 to 10 percent", "Losing 7 to 10 percent of body weight is the change most tied to clearing liver fat and calming inflammation."),
                     ("walk", "Move every day", "150 minutes a week of brisk walking plus 2 strength days. A 10-minute walk after meals blunts the sugar spike."),
                     ("glass", "Go easy on alcohol", "Even though alcohol did not cause it, alcohol adds to the liver's load. Keep it minimal or skip it.")],
            "cols": [
                {"p": "berberine", "need": "Steady sugar and fat", "needsub": "berberine", "start": True,
                 "bullets": ["Supports healthy glucose metabolism", "Supports healthy lipid levels already in a normal range"], "dose": "dose_from_db"},
                {"p": "lipo_flow", "need": "Help the liver process fat", "needsub": "lipotropic nutrients",
                 "bullets": ["Supports normal fat metabolism in the liver", "Supports healthy bile flow"], "dose": "dose_from_db"},
                {"p": "omega_1000", "need": "Balance fats", "needsub": "omega-3 fatty acids, EPA and DHA",
                 "bullets": ["Supports healthy triglyceride levels", "Supports a healthy inflammatory response"], "dose": "dose_from_db"},
                {"p": "mito", "need": "Protect cells", "needsub": "alpha lipoic acid, NAC, carnitine",
                 "bullets": ["Antioxidants that work in water and fat", "Supports cellular energy"], "dose": "dose_from_db"},
            ],
            "rx": ["<b>Statins:</b> often used alongside. They can lower CoQ10. Ask whether CoQ10 fits.",
                   "<b>Metformin</b> long term can lower B12. Ask for a B12 check once a year.",
                   "<b>Acetaminophen:</b> stay within label limits and never combine it with alcohol."],
        },
    },
    {
        "slug": "gerd", "code": "ND-GI-102", "theme": "gerd", "series": "Gut Health Series",
        "title": "Acid Reflux and GERD", "sub": "Gastroesophageal reflux disease",
        "intro": None,
        "front": front_reflux,
        "back": {
            "life_title": "Lifestyle Modifications", "style": "hex",
            "life": [("clock", "Close the kitchen early", "Finish eating 3 hours before you lie down."),
                     ("bed", "Raise the head", "Lift the head of your bed 6 to 8 inches."),
                     ("portion", "Smaller meals", "Eat slowly and stop before full."),
                     ("scale", "A healthy weight", "Even a few pounds lighter eases pressure on the valve."),
                     ("coffee", "Know your triggers", "Fried food, chocolate, mint, caffeine, alcohol, citrus, tomato, fizzy drinks."),
                     ("smoke", "Stop smoking", "Smoking relaxes the valve and slows healing.")],
            "cols": [
                {"p": "gi_integrity", "need": "Coat and soothe", "needsub": "DGL, aloe, slippery elm, marshmallow, glutamine", "start": True,
                 "bullets": ["Sip it slowly so it coats your throat on the way down", "Zinc carnosine supports the stomach lining"],
                 "dose": "1 scoop daily", "dosesub": "sip over 10 minutes"},
                {"p": "zinc_carnosine", "need": "Protect the stomach lining", "needsub": "zinc carnosine",
                 "bullets": ["Supports the stomach's natural mucosal defenses", "Studied for gastric comfort"], "dose": "dose_from_db"},
                {"p": "ultrabiotic_dms", "need": "Balance the gut", "needsub": "probiotic + S. boulardii",
                 "bullets": ["Seven friendly strains", "Supports comfortable digestion"], "dose": "1 capsule daily", "dosesub": "at bedtime"},
                {"p": "mag_glycinate", "need": "Refill magnesium", "needsub": "chelated magnesium",
                 "bullets": ["Acid blockers can drain magnesium", "Chelated forms are gentle on the stomach"], "dose": "dose_from_db"},
                {"p": "methyl_b", "need": "Refill B12", "needsub": "active B vitamins",
                 "bullets": ["Stomach acid is needed to absorb B12", "Methylated forms, ready to use"], "dose": "dose_from_db"},
            ],
            "rx": ["<b>PPIs and H2 blockers</b> can lower magnesium, B12, calcium and iron over time. Ask for levels once a year.",
                   "<b>Take soothing powders 2 hours apart</b> from other medicines: coating herbs can slow their absorption.",
                   "<b>Want to taper an acid blocker?</b> Plan it with your prescriber; stopping suddenly can bring a rebound."],
        },
    },
    {
        "slug": "high-blood-pressure", "code": "ND-CM-202", "theme": "metab", "series": "Metabolic Health Series",
        "title": "High Blood Pressure", "sub": "No symptoms, real risk",
        "intro": ("Nearly <b>half of U.S. adults</b> have high blood pressure, and many do not know it, because it rarely causes "
                  "symptoms. Over the years, the extra force strains the heart, kidneys, brain and eyes and raises the risk of heart "
                  "attack and stroke. One lever you control is <b>nitric oxide (NO)</b>, the signal that tells blood-vessel walls to "
                  "relax. What you eat, how you move, how you sleep and how you handle stress all change how much of it your body makes."),
        "front": front_bp,
        "back": {
            "life_title": "Lifestyle Recommendations", "style": "circle",
            "life": [("beet", "Eat for nitric oxide", "Beets, arugula, spinach and celery bring nitrate. Load up on potassium-rich produce."),
                     ("salt", "Cut the sodium", "Aim under 1,500 to 2,300 mg a day. Most hides in packaged and restaurant food."),
                     ("dumbbell", "Move, then hold", "Walk daily and add isometric holds (wall sits, hand grips) 3 times a week."),
                     ("moon", "Sleep and breathe", "Sleep 7 to 9 hours. Loud snoring? Ask about sleep apnea."),
                     ("smoke", "Quit smoking", "Each cigarette tightens vessels. Keep alcohol low, too."),
                     ("mouthwash", "Skip harsh mouthwash", "Antiseptic rinses wipe out the mouth bacteria that help make NO.")],
            "cols": [
                {"p": "mag_glycinate", "need": "Relax vessel walls", "needsub": "magnesium", "start": True,
                 "bullets": ["Supports healthy vascular tone", "Supports healthy blood pressure already in a normal range"], "dose": "dose_from_db"},
                {"p": "omega_1000", "need": "Calm and balance", "needsub": "omega-3 fatty acids, EPA and DHA",
                 "bullets": ["Supports heart and vessel health", "Supports healthy triglyceride levels"], "dose": "dose_from_db"},
                {"p": "coq10", "need": "Power the heart", "needsub": "CoQ10",
                 "bullets": ["Fuel for heart-muscle cells", "Statins can lower CoQ10 levels"], "dose": "dose_from_db"},
            ],
            "rx": ["<b>Diuretics</b> (HCTZ, furosemide) can drain magnesium and potassium. Ask about levels.",
                   "<b>ACE inhibitors, ARBs and spironolactone</b> raise potassium: skip potassium pills and salt substitutes unless prescribed.",
                   "<b>Beta blockers and statins</b> can lower CoQ10. Bring this sheet to your pharmacist."],
        },
    },
    {
        "slug": "ibd", "code": "ND-GI-103", "theme": "teal", "series": "Gut Health Series",
        "title": "Inflammatory Bowel Disease", "sub": "Crohn's disease and ulcerative colitis",
        "intro": ("Inflammatory bowel disease (IBD) is a long-term condition in which the immune system keeps part of the digestive "
                  "tract inflamed. About <b>3 million Americans</b> live with it. The two main types, <b>Crohn's disease</b> and "
                  "<b>ulcerative colitis</b>, share belly pain, urgent diarrhea, fatigue and weight loss, with flares that can last "
                  "weeks to months between quieter stretches. IBD is managed by a gastroenterologist. Food, lifestyle and nutrient "
                  "support work alongside that care, never instead of it."),
        "front": front_ibd,
        "back": {
            "life_title": "Lifestyle Modifications", "style": "hex",
            "life": [("sensitive", "Find food triggers", "Remove foods your care team identifies as a sensitivity or intolerance."),
                     ("sugar", "Limit sugar", "Sugar and ultra-processed food feed the wrong microbes."),
                     ("fish", "Eat enough", "More protein and calories during flares, to protect weight and muscle."),
                     ("breath", "Lower stress", "Stress is one of the most common flare triggers."),
                     ("rx", "Ask about NSAIDs", "Ibuprofen and naproxen can trigger flares. Use antibiotics only when needed."),
                     ("walk", "Move gently", "Regular low to moderate exercise.")],
            "cols": [
                {"p": "ultrabiotic_xs", "need": "Rebalance the microbiome", "needsub": "high-potency probiotic",
                 "bullets": ["Supports a balanced gut microbiome", "Supports healthy bowel function"], "dose": "dose_from_db"},
                {"p": "curcumin_bcm95", "need": "Inflammatory balance", "needsub": "curcumin", "start": True,
                 "bullets": ["Supports a healthy inflammatory response", "Enhanced-absorption curcumin"], "dose": "dose_from_db"},
                {"p": "d3_5000_k2", "need": "Vitamin D", "needsub": "D3 with K2",
                 "bullets": ["Supports normal immune function", "Low vitamin D is common in IBD"], "dose": "dose_from_db"},
                {"p": "gi_integrity", "need": "Repair the lining", "needsub": "L-glutamine, DGL, aloe",
                 "bullets": ["Fuel for the cells that line your gut", "Soothing botanicals"], "dose": "1 scoop daily", "dosesub": "in 6 to 8 oz water"},
                {"p": "gi_defend", "need": "Barrier and tolerance", "needsub": "serum-derived bovine immunoglobulins",
                 "bullets": ["Binds microbial toxins in the gut", "Supports barrier function"], "dose": "dose_from_db"},
            ],
            "rx": ["<b>Steroids</b> (prednisone, budesonide) lower vitamin D and calcium. Ask about bone health.",
                   "<b>Sulfasalazine and methotrexate</b> lower folate. Ask whether you need a folate supplement.",
                   "<b>Never stop IBD medicine</b> during a good stretch without your gastroenterologist. Ask before any new supplement."],
        },
    },
    {
        "slug": "insulin-resistance", "code": "ND-CM-203", "theme": "metab", "series": "Metabolic Health Series",
        "title": "Understanding Insulin Resistance", "sub": None,
        "intro": ("Insulin is the hormone your pancreas makes to move sugar out of your blood and into your cells for fuel. In "
                  "<b>insulin resistance</b>, the cells stop answering the signal well, so sugar lingers in the blood and the pancreas "
                  "works harder to keep up. Years can pass this way, with normal-looking blood sugar, before it rises far enough to be "
                  "called prediabetes or type 2 diabetes. Insulin resistance also feeds inflammation, high blood pressure, high "
                  "cholesterol and fatty liver."),
        "front": front_insulin,
        "back": {
            "life_title": "Lifestyle-Based Medicine", "style": "circle3",
            "life": [("plate", "Low-glycemic Mediterranean plate", ["Protein first at every meal", "Half the plate vegetables", "Whole-food carbs, paired with protein or fat", "Three to five balanced meals", "Limit sugar and sweet drinks"]),
                     ("breath", "Lower stress, better sleep", ["Commit to a simple plan", "Deep breathing, 5 minutes a day", "7 to 9 hours of sleep, same times daily", "One 10-minute mindful walk a day"]),
                     ("walk", "Move your muscles", ["Walk 10 minutes after meals", "Strength training 2 to 3 times a week", "Stand up every 30 to 60 minutes", "Moderate to hard exercise 3 to 5 days a week"])],
            "cols": [
                {"p": "gluco_ir", "need": "All-in-one glucose support", "needsub": "dihydroberberine, chromium, ALA, cinnamon", "start": True,
                 "bullets": ["Supports healthy glucose metabolism", "Supports insulin sensitivity"], "dose": "dose_from_db"},
                {"p": "berberine", "need": "Metabolic signaling", "needsub": "berberine",
                 "bullets": ["Supports healthy glucose levels already in a normal range", "Supports healthy lipid levels"], "dose": "dose_from_db"},
                {"p": "mag_glycinate", "need": "Insulin's helper mineral", "needsub": "magnesium",
                 "bullets": ["Needed for normal insulin signaling", "Low magnesium is common with high blood sugar"], "dose": "dose_from_db"},
                {"p": "omega_1000", "need": "Balance fats", "needsub": "omega-3 fatty acids",
                 "bullets": ["Supports healthy triglyceride levels", "Supports a healthy inflammatory response"], "dose": "dose_from_db"},
            ],
            "rx": ["<b>Metformin</b> lowers B12 over time. Ask for a B12 check every year.",
                   "<b>On diabetes medicine?</b> Berberine adds to sugar-lowering effects: check your glucose and tell your prescriber.",
                   "<b>Berberine interacts</b> with some medicines (for example cyclosporine). Let your pharmacist review your list."],
        },
    },
    {
        "slug": "lyme", "code": "ND-IM-301", "theme": "immune", "series": "Immune Health Series",
        "title": "Lyme Disease", "sub": "and other tickborne infections",
        "intro": ("Lyme disease is the most common illness spread by ticks in the U.S. An estimated <b>476,000 Americans</b> are "
                  "diagnosed and treated for it each year. It is caused by <i>Borrelia</i> bacteria passed on by the bite of an infected "
                  "blacklegged (deer) tick, and the same ticks can carry other infections at the same time. The best intervention is "
                  "prevention, and the second best is early treatment."),
        "front": front_lyme,
        "back": {
            "life_title": "Lifestyle Recommendations", "life_sub": "Avoiding tick bites", "style": "icons",
            "life": [("shirt", "Clothing", "Light colors, long sleeves, pants tucked into socks. Treat gear with permethrin."),
                     ("drop", "Repellent", "Use an EPA-registered repellent: DEET, picaridin, IR3535 or oil of lemon eucalyptus."),
                     ("dryer", "High heat", "Tumble dry clothes on high for 10 minutes after outdoor time to kill ticks."),
                     ("shower", "Shower and check", "Shower within 2 hours. Check scalp, ears, armpits, waist and behind knees."),
                     ("paw", "Pets", "Check pets daily and ask your vet about tick prevention."),
                     ("clipboard", "Remove it right", "Fine-tipped tweezers, close to the skin, pull straight up. Note the date.")],
            "cols": [
                {"p": "ultrabiotic_dms", "need": "Protect your gut", "needsub": "probiotic + S. boulardii", "start": True,
                 "bullets": ["S. boulardii keeps working during antibiotics", "Supports normal bowel function"], "dose": "1 capsule daily", "dosesub": "2 hours from antibiotics"},
                {"p": "immunity_pro", "need": "Immune readiness", "needsub": "beta-glucan",
                 "bullets": ["Supports a healthy immune response", "One capsule a day"], "dose": "dose_from_db"},
                {"p": "curcumin_bcm95", "need": "Inflammatory balance", "needsub": "curcumin",
                 "bullets": ["Supports a healthy inflammatory response", "Supports joint comfort"], "dose": "dose_from_db"},
                {"p": "gi_defend", "need": "Barrier support", "needsub": "serum-derived bovine immunoglobulins",
                 "bullets": ["Binds microbial toxins in the gut", "Supports immune balance"], "dose": "dose_from_db"},
                {"p": "mito", "need": "Cellular energy", "needsub": "mitochondrial support",
                 "bullets": ["Supports energy production in every cell", "Antioxidant support"], "dose": "dose_from_db"},
            ],
            "rx": ["<b>Doxycycline:</b> take it 2 to 3 hours apart from calcium, magnesium, iron and zinc, which block it.",
                   "<b>During any antibiotic,</b> take the probiotic 2 hours apart from each dose, then keep going 2 weeks after.",
                   "<b>Antibiotics can lower vitamin K and B vitamins.</b> Eat leafy greens and ask before adding herbs."],
        },
    },
    {
        "slug": "pcos", "code": "ND-CM-204", "theme": "metab", "series": "Metabolic Health Series",
        "title": "Polycystic Ovary Syndrome", "sub": "PCOS",
        "intro": ("PCOS is a hormone condition in which the ovaries make more <b>androgens</b> (male-type hormones that women normally "
                  "make in small amounts) than usual. It can disrupt periods, ovulation and fertility, and it shows up in skin, hair, "
                  "weight and mood. Genes play a part, but <b>insulin resistance</b> is the engine behind most cases, which is why food, "
                  "movement, sleep and stress change how PCOS behaves."),
        "front": front_pcos,
        "back": {
            "life_title": "Lifestyle Recommendations", "style": "circle",
            "life": [("plate", "Diet", "Protein and fiber at every meal. Limit refined sugar and starch to steady blood sugar."),
                     ("dumbbell", "Exercise", "150 minutes a week of activity plus 2 strength days improves insulin sensitivity."),
                     ("moon", "Sleep", "Seven to eight hours a night supports weight and healthy hormone production."),
                     ("plastic", "Limit hormone disruptors", "Glass or steel containers, never heat food in plastic, fragrance-free products.")],
            "cols": [
                {"p": "gluco_ir", "need": "Blood sugar and insulin", "needsub": "dihydroberberine, chromium, ALA", "start": True,
                 "bullets": ["Supports healthy glucose metabolism", "Supports insulin sensitivity"], "dose": "dose_from_db"},
                {"p": "inositol", "need": "Insulin signaling", "needsub": "inositol",
                 "bullets": ["Supports healthy ovarian function", "Supports insulin signaling"], "dose": "dose_from_db"},
                {"p": "d3_5000_k2", "need": "Vitamin D", "needsub": "D3 with K2",
                 "bullets": ["Low vitamin D is common in PCOS", "Supports hormone and immune health"], "dose": "dose_from_db"},
                {"p": "omega_1000", "need": "Calm inflammation", "needsub": "omega-3 fatty acids",
                 "bullets": ["Supports a healthy inflammatory response", "Supports healthy triglycerides"], "dose": "dose_from_db"},
                {"p": "ultrabiotic_dms", "need": "Gut and hormones", "needsub": "multi-strain probiotic",
                 "bullets": ["Your gut bacteria help process hormones", "Seven strains, one capsule"], "dose": "1 capsule daily", "dosesub": "same time each day"},
            ],
            "rx": ["<b>Birth control pills</b> can lower B6, B12, folate, magnesium and zinc. Ask about a quality multi.",
                   "<b>Metformin</b> lowers B12 over time. Ask for a yearly check.",
                   "<b>Spironolactone</b> raises potassium: avoid potassium supplements unless prescribed."],
        },
    },
    {
        "slug": "mold", "code": "ND-IM-302", "theme": "immune", "series": "Immune Health Series",
        "title": "Mold Illness", "sub": "Mycotoxin exposure and recovery",
        "intro": ("Mold grows wherever water lingers: a slow roof leak, a damp crawl space, a sweating HVAC line. Some molds release "
                  "<b>mycotoxins</b> and other irritants into the air you breathe. Damp, moldy buildings are linked with coughing, "
                  "wheezing and asthma flares, and many people also report fatigue, headaches, joint aches and brain fog. Because the "
                  "symptoms are so broad, mold is easy to overlook. Recovery starts with removing the exposure; only then does "
                  "supporting the body's clearance make sense."),
        "front": front_mold,
        "back": {
            "life_title": "Lifestyle Recommendations", "style": "circle",
            "life": [("sensitive", "Limit moldy foods", "Peanuts, corn, long-stored grains, dried fruit, wine and aged cheese carry more mycotoxins."),
                     ("wheat", "More fiber", "Fiber binds toxins carried in bile. Aim for 30 g a day."),
                     ("house", "Dry the air", "Keep indoor humidity between 30 and 50 percent with a dehumidifier."),
                     ("filter", "Filter it", "HEPA air purifiers and HEPA vacuums trap mold spores."),
                     ("sauna", "Sweat", "Sauna or a good workout helps you sweat. Drink water."),
                     ("clipboard", "Fix fast", "Dry or repair any leak within 24 to 48 hours.")],
            "cols": [
                {"p": "gi_defend", "need": "Bind toxins in the gut", "needsub": "serum-derived bovine immunoglobulins", "start": True,
                 "bullets": ["Immunoglobulins bind microbial toxins in the gut", "Supports barrier function"], "dose": "dose_from_db"},
                {"p": "lipo_flow", "need": "Keep bile flowing", "needsub": "liver and bile support",
                 "bullets": ["Supports healthy bile flow", "Supports the liver's clearance pathways"], "dose": "dose_from_db"},
                {"p": "glutathione", "need": "Master antioxidant", "needsub": "liposomal glutathione",
                 "bullets": ["Supports the liver's detox pathways", "Liposomal form for absorption"], "dose": "dose_from_db"},
                {"p": "mito", "need": "Cellular energy and glutathione", "needsub": "NAC, carnitine, ALA",
                 "bullets": ["Supports mitochondria and detoxification", "Antioxidant support"], "dose": "dose_from_db"},
                {"p": "nac600", "need": "Build glutathione", "needsub": "N-acetyl-L-cysteine",
                 "bullets": ["The building block your body uses to make glutathione", "Supports respiratory health"], "dose": "dose_from_db"},
            ],
            "rx": ["<b>Binders block absorption.</b> Take them 2 hours apart from food, supplements and every medicine.",
                   "<b>Antifungal drugs,</b> if prescribed, interact with many medicines. Have your pharmacist review your list.",
                   "<b>Stay regular.</b> Binders need a daily bowel movement to work. Constipated? Call your practitioner."],
        },
    },
]
