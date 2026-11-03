"""'Before you grab the warehouse bottle' counter card + staff talk track.
Brand-neutral on the patient side; the staff side names the competitor the
floor actually hears.  Label-checkable claims only.  Run: python3 counter_card.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kit, sheets
from kit import icon, logo, theme_vars

CSS = r"""
.cc h1{font:900 30pt/1.05 Merriweather,Georgia,serif;color:#14664D;margin:.04in 0 .04in}
.cc .lead{font-size:10.5pt;color:#2B3236;margin:0 0 .12in}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:.12in}
.cd{border:1px solid #DCE3E0;border-radius:10px;padding:.12in .14in;background:#FBFCFB}
.cd h3{font:800 9pt Inter;letter-spacing:.12em;text-transform:uppercase;color:#F15F3F;margin:0 0 4px}
.cd h4{font:900 13pt Merriweather,Georgia,serif;color:#14664D;margin:0 0 6px}
.cd p{font-size:9.2pt;line-height:1.4;margin:0 0 6px}
.vs{display:grid;grid-template-columns:1fr auto 1fr;gap:8px;align-items:center;background:#fff;border-radius:8px;padding:6px 8px;border:1px dashed #CBD5D1}
.vs .s{text-align:center;font-size:8.2pt;line-height:1.25}
.vs .s b{display:block;font:900 15pt Merriweather,Georgia,serif;color:#14664D}
.vs .s.them b{color:#8B8F94}
.vs .mid{font:900 10pt Inter;color:#F15F3F}
.pills{display:flex;gap:3px;justify-content:center;margin:3px 0}
.pill{width:22px;height:11px;border-radius:6px;background:#E5B94E;border:1px solid #B88A1E}
.pill.g{background:#7FC3A3;border-color:#2F8A63}
.perks{margin-top:.12in;display:grid;grid-template-columns:repeat(3,1fr);gap:.1in}
.pk{background:#14664D;color:#fff;border-radius:10px;padding:.1in .12in;text-align:center}
.pk b{display:block;font:900 11pt Merriweather,Georgia,serif;margin:4px 0 2px}
.pk span{font-size:8.4pt;color:#DDEFE7}
.fill{border-bottom:1.5px solid #fff;display:inline-block;min-width:1.4in}
.talk{counter-reset:t;display:grid;gap:.08in}
.tt{display:grid;grid-template-columns:.34in 1fr;gap:10px;align-items:start;border-left:4px solid #14664D;background:#F6F9F8;border-radius:0 8px 8px 0;padding:.08in .12in}
.tt .n{width:.32in;height:.32in;border-radius:50%;background:#F15F3F;color:#fff;font:900 11pt Inter;display:flex;align-items:center;justify-content:center}
.tt b{font:800 10pt Inter;color:#14664D;display:block}
.tt p{margin:2px 0 0;font-size:9pt;line-height:1.38}
.tt q{font-style:italic;color:#3A4247}
.never{margin-top:.12in;border:1.6px solid #C0392B;background:#FDF1EF;border-radius:8px;padding:.08in .14in;font-size:9pt}
.never b{color:#A5281E}
"""

def build():
    front = f"""<section class="sheet cc" style="{theme_vars('gut')}"><div class="inner">
<div class="headrow">{logo('0.27in')}<span class="series" style="color:#14664D">Ask your pharmacist</span></div>
<h1>Before you grab the<br>warehouse bottle</h1>
<p class="lead">Big-box and warehouse vitamins can be a fair deal. Four things on the label decide what you are really paying for. Check them, or let us check them with you.</p>
<div class="cards">
<div class="cd"><h3>1 &middot; Count the pills</h3><h4>Dose per pill, not per bottle</h4>
<p>A typical &ldquo;1,000 mg fish oil&rdquo; softgel holds only <b>250 to 300 mg</b> of EPA and DHA, the omega-3s that do the work. Read the panel, not the front.</p>
<div class="vs"><div class="s them"><b>4 softgels</b><div class="pills"><i class="pill"></i><i class="pill"></i><i class="pill"></i><i class="pill"></i></div>to reach 1,000 mg EPA+DHA</div><div class="mid">VS</div>
<div class="s"><b>1 softgel</b><div class="pills"><i class="pill g"></i></div>Omega Pure EPA-DHA 1000</div></div></div>
<div class="cd"><h3>2 &middot; Read the form</h3><h4>Not all magnesium is the same</h4>
<p>Many low-cost bottles use <b>magnesium oxide</b>: cheap to make, poorly absorbed and the form most likely to upset your stomach. Chelated magnesium (glycinate, malate) is gentler and better used by the body.</p>
<div class="vs"><div class="s them"><b>Oxide</b>low absorption</div><div class="mid">VS</div><div class="s"><b>Chelated</b>Magnesium Glycinate, 260 mg per 2 capsules</div></div></div>
<div class="cd"><h3>3 &middot; Look for active forms</h3><h4>Ready-to-use B vitamins</h4>
<p>Most mass-market multis use <b>folic acid</b> and <b>cyanocobalamin</b>, which your body has to convert. Methylfolate (L-5-MTHF) and methylcobalamin arrive ready to use, which matters for the many people who convert poorly.</p></div>
<div class="cd"><h3>4 &middot; Check it against your medicines</h3><h4>The one thing an aisle can't do</h4>
<p>Some supplements and prescriptions need spacing or swapping. Doxycycline must be taken 2 to 3 hours apart from magnesium, calcium, iron and zinc. Acid blockers can drain magnesium and B12. Statins can lower CoQ10. <b>We check your list for free.</b></p></div>
</div>
<div class="perks"><div class="pk">{icon('house','0.42in',color='#BFE3D4')}<b>Stored right</b><span>Temperature-controlled here, never left in a hot truck or warehouse</span></div>
<div class="pk">{icon('clock','0.42in',color='#BFE3D4')}<b>In stock today</b><span>No shipping wait, no shipping fee, no running out mid-protocol</span></div>
<div class="pk">{icon('heart','0.42in',color='#BFE3D4')}<b>Rewards</b><span>Ask about our vitamin club: <span class="fill"></span></span></div></div>
<div class="foot"><span>Practitioner-exclusive formulas, sold through practitioners and pharmacies, not warehouse clubs.</span><span class="code">ND-RX-401 &middot; 11/2026</span></div>
</div></section>"""
    steps = [("Agree first", "<q>Costco has great prices, and a lot of their store brand is USP-verified. I'm not going to knock it.</q> Respect earns the next 45 seconds."),
             ("Count the pills", "<q>How many of those do you take to get your dose?</q> Turn the bottle around together. Fish oil is the easy one: four warehouse softgels to match one Omega Pure 1000."),
             ("Read the form", "Magnesium oxide versus chelated glycinate. Folic acid and cyanocobalamin versus methylfolate and methylcobalamin. Point at the panel, not the price."),
             ("Check their medicines", "Pull out the drug-induced nutrient depletion form. <q>Which prescriptions are you on?</q> This is the conversation the warehouse can never have."),
             ("Make it easy", "In stock today, no shipping, stored right, vitamin club credit. <q>If you ever run out, we have it this afternoon.</q>"),
             ("Leave the door open", "If they still want the warehouse bottle: <q>Bring it in next time and I'll check it against your meds, free.</q> They come back, and so does the conversation.")]
    tt = "".join(f'<div class="tt"><div class="n">{i + 1}</div><div><b>{a}</b><p>{b}</p></div></div>' for i, (a, b) in enumerate(steps))
    back = f"""<section class="sheet cc" style="{theme_vars('gut')}"><div class="inner">
<div class="headrow">{logo('0.27in')}<span class="series" style="color:#F15F3F">Staff only &middot; keep behind the counter</span></div>
<h1 style="font-size:24pt">&ldquo;I can get it at Costco.&rdquo;<br><span style="font-size:15pt;color:#3A4247">The 60-second answer</span></h1>
<p class="lead">Six moves, in order. Win on dose, form and the pharmacist, never on knocking the store.</p>
<div class="talk">{tt}</div>
<div class="never"><b>Never say</b> that warehouse vitamins are fake, junk or untested: many carry the USP Verified mark, and a customer who knows that stops trusting everything else you say. <b>Never</b> fight on price per bottle. Fight on price per effective dose.</div>
<div class="foot"><span>Label facts checked Nov 2026 against Costco's own product listings (Kirkland fish oil 1,000 mg lists 250 mg EPA + DHA per softgel; the daily multi lists folic acid and cyanocobalamin). Recheck a bottle before quoting it.</span><span class="code">ND-RX-401 &middot; staff side</span></div>
</div></section>"""
    tb = kit.toolbar("Counter card + staff talk track", "warehouse-bottle-counter-card.pdf")
    html = kit.page_shell("Warehouse Bottle Counter Card", tb + f'<div class="stack">{front}{back}</div>', "gut", sheets.EXTRA_CSS + CSS, font_base="fonts/")
    open(os.path.join(os.path.dirname(HERE), "warehouse-bottle-counter-card.html"), "w").write(html)

if __name__ == "__main__":
    build()
