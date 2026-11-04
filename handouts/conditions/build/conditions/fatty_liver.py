"""Fatty Liver Disease (MASLD) condition sheet, slug "fatty-liver".

Self-contained: the art below was copied out of art.py / sheets.py and rebuilt on
2026-11-03 for Asher's notes on the first draft.
  1. The stage labels sit inside the viewBox with real top margin, large and crisp.
  2. The least-to-most-severe direction is a labelled gradient arrow across the top and
     the stages are numbered 1 to 4.  The green "often reversible" arcs and the red
     "hardest to reverse" bracket keep the first draft's logic (Asher approved it).
  3. A KEY names everything inside the magnified tissue circles.
  4. The old empty space at the bottom holds an "Ask about liver checks" panel.
  5. The risk-factor icons stay, polished into one row of tinted discs.
Art-director pass (front only): immune cells never stack, scar is drawn edges-then-fills, every arc end
and T-bar stops clear of the white ring, the band holds the arcs and their labels, the livers sit
bottom-aligned 4 units above the band, all three check cards end in two sourced dots, and the pharmacy
edition says the doctor orders the checks.
Front recheck pass (2026-11-03, the reviewer's front recheck list), no redesign beyond the listed items:
  - ALT dots read as upper limits, the FIB-4 dot names the FibroScan, the specialist dot is red.
  - The zoom tag says "Close-up", the same word as the key.  Every key swatch sits on a dark tissue
    chip like the art, the scar swatch is a straight piece of septum, the key names the pink nucleus.
  - The cirrhotic liver is warm tan-brown, its nodules packed without overlap, lit by a soft lower
    shadow and a highlight instead of dark rings.
  - Close-up 4 shows rounded nodules ringed by scar: a gapped Voronoi layout (septa 6 to 11 wide that
    swell, thin and fork where three nodules meet), each nodule with its own tilted cell grid.
  - Close-up 3's immune cells sit in four tight foci of three in the gaps between cells, never on fat
    or a nucleus (checked by asserts).
  - The gut caption and the gut risk label are hedged ("may add to it", "being studied").
  - The sugar icon is a soda cup with a straw; PCOS is a uterus-and-ovaries glyph in the kit's style.
  - The severity row, the band and the key share one 8-unit margin on both sides.
Back (products pass, same day; column 4 swapped 2026-11-04): four columns, the competitor's count, matching its
four nutrient categories (berberine; bergamot + artichoke; aged black garlic; alpha lipoic acid) with NutriDyn's
own protocol products where they fit.  Berberine Pro and Milk Thistle Complex are on the NutriDyn CSO's GLC 2026
"Metabolic Fatty Liver (MAFLD, MASLD, MASH)" list [CSO26]; Lipo-Flow is the NutriDyn science-team
lipotropic (400 mg artichoke + tangerine peel: the citrus-and-artichoke match) Asher sends "to promote healthy
liver function".  Milk Thistle Complex stands in for aged black garlic (both are antioxidant liver-cell
support; NutriDyn has no liver protocol with garlic).  Column 4 is Cellular Energy (R145; 150 mg alpha-lipoic
acid, the ALA match) [ND325].  The GLC 2026 list names Mito Recharge for that slot and earlier rounds printed it,
but Mito Recharge carries 100 mg EGCG from green tea extract and USP's caution for green tea extract says "Do not
use if you have a liver problem" [USP20], which covers every reader of this sheet; Cellular Energy has no green
tea.  Asher can reverse the swap (see products.d fl_cellular_energy "src").  Label facts:
products.d/fatty-liver.json (fl_* keys, so no other sheet's override reaches this page), each with its sell-sheet
source.
Shared helpers come only from svgkit / kit.  Every SVG id starts with "fl-" and every
CSS class with "flv-", so nothing collides with other sheets in the all-sheets bundle.

SOURCES (each number on the page carries one of these tags in a comment)
  [AASLD23]   Rinella ME et al. AASLD Practice Guidance on the clinical assessment and
              management of NAFLD. Hepatology 2023;77:1797-1835.
              doi:10.1097/HEP.0000000000000323 (full text read via PubMed Central, PMC10735173)
  [DELPHI23]  Rinella ME et al. A multisociety Delphi consensus statement on new fatty liver
              disease nomenclature, June 2023 (NAFLD -> MASLD, NASH -> MASH; the same scheme names MetALD,
              MASLD plus greater alcohol intake, so alcohol and MASLD can travel together).
              doi:10.1016/j.aohep.2023.101133 (published jointly in Hepatology / J Hepatol)
  [NHANES25]  Kim D et al. Current burden of steatotic liver disease and fibrosis among adults
              in the United States, 2017-2023. Clin Mol Hepatol 2025;31:382-393.
              doi:10.3350/cmh.2024.0987 (US adults, age-adjusted MASLD prevalence 31.9%)
  [YOUNOSSI23] Younossi ZM et al. The global epidemiology of NAFLD and NASH. Hepatology
              2023;77:1335-1347. doi:10.1097/HEP.0000000000000004 (global 30%; 38% in 2016-2019)
  [EASL24]    EASL-EASD-EASO Clinical Practice Guidelines on the management of MASLD. J Hepatol
              2024;81:492-542. doi:10.1016/j.jhep.2024.04.031; executive summary read in full,
              Diabetologia 2024;67:2375-2392, doi:10.1007/s00125-024-06196-3 (PMC11519095)
  [HHS18]     Physical Activity Guidelines for Americans, 2nd ed. US HHS, 2018 (muscle-strengthening
              activity on 2 or more days a week).
  [REYNOLDS16] Reynolds AN et al. Advice to walk after meals is more effective for lowering postprandial
              glycaemia in type 2 diabetes. Diabetologia 2016;59:2572-2578. doi:10.1007/s00125-016-4085-2
  [ZHANG08]   Zhang Y et al. Treatment of type 2 diabetes and dyslipidemia with the natural plant alkaloid
              berberine. J Clin Endocrinol Metab 2008;93:2559-2565 (cited on Berberine Pro SS ND1130)
  [GUO12]     Guo Y et al. Repeated administration of berberine inhibits cytochromes P450 in humans.
              Eur J Clin Pharmacol 2012;68:213-217. doi:10.1007/s00228-011-1108-2 (CYP2D6, 2C9, 3A4)
  [KAMINSKY97] Kaminsky LS, Zhang ZY. Human P450 metabolism of warfarin. Pharmacol Ther 1997;73(1):67-74.
              doi:10.1016/s0163-7258(96)00140-4, PMID 9014207 (abstract read 2026-11-04 via PubMed): "S-warfarin is
              metabolized primarily by CYP2C9"; R-warfarin partly "by CYP3A4"; "The efficacy of warfarin is affected
              primarily when metabolism of S-warfarin is altered."  Berberine slowed CYP2C9 and 3A4 in people
              [GUO12], so the medicines check names warfarin among the drugs those enzymes clear.  (Mito Recharge's
              vitamin K1 clause and its NIH ODS source left in the swap pass; the vitamin-K-type concern did not, since
              Cellular Energy's CoQ10 is chemically similar to vitamin K: see [COQ10].)
  [COQ10]     CoQ10 and warfarin (polish round 2b, PubMed records read 2026-11-04).  Landbo C, Almdal TP. Ugeskr Laeger
              1998;160(22):3226-7, PMID 9621803 (case report: a woman on warfarin responded less to it while taking
              CoQ10, and as before once it was stopped; "Coenzyme Q10 is chemically similar to K-vitamins, which may
              explain the interaction with warfarin").  Shalansky S et al. Pharmacotherapy 2007;27(9):1237-47,
              doi:10.1592/phco.27.9.1237, PMID 17723077 (prospective cohort, 171 adults on warfarin: CoQ10 independently
              tied to self-reported bleeding, OR 3.69, 95% CI 1.88-7.24).  Engelsen J, Nielsen JD, Winther K. Thromb
              Haemost 2002;87(6):1075-6, PMID 12083489 (randomised, double-blind, placebo crossover in stable long-term
              warfarin outpatients: no change in warfarin's effect at CoQ10 100 mg a day for 4 weeks; PubMed has no
              abstract, the dose is from the Danish abstract as a web search shows it).  Mixed in direction and size,
              hence "may change how warfarin works".  Cellular Energy gives 200 mg CoQ10 per 2 capsules [ND325].  NCCIH's
              CoQ10 page (nccih.nih.gov/health/coenzyme-q10) flags a possible interaction with warfarin in a web-search
              excerpt, but nccih.nih.gov is not reachable from this session: re-check the page before print.
  [ALA]       Alpha-lipoic acid, CoQ10 and diabetes medicines (polish round 2b, PubMed records read 2026-11-04).  ALA
              lowers blood sugar a little: fasting glucose -5.28 mg/dL pooled over 63 RCTs (Mohammadi S et al. Nutr Metab
              Cardiovasc Dis 36(2):104370, e-published 2025-09-27, doi:10.1016/j.numecd.2025.104370, PMID 41077538; also
              Akbari M et al. Metabolism 2018;87:56-69, doi:10.1016/j.metabol.2018.07.002, PMID 29990473).  Berberine's
              pooled drop is about three times that, -0.82 mmol/L (about -15 mg/dL) over 37 RCTs in type 2 diabetes (Xie W
              et al. Front Pharmacol 2022;13:1015045, doi:10.3389/fphar.2022.1015045, PMID 36467075; different trial
              groups, so a rough comparison), and Cellular Energy's 150 mg a day is below the usual trial doses, hence
              "more mildly".  Interaction checkers rate ALA with insulin and oral diabetes medicines minor: drugs.com's
              alpha-lipoic acid page lists 30 interacting drugs, all minor, and DDInter calls it a theoretical boost to
              the glucose lowering of insulin and oral antidiabetic agents (web-search excerpts, 2026-11-04; drugs.com and
              medlineplus.gov are not reachable from this session).  CoQ10's effect is of the same small size: fasting
              glucose -5.22 mg/dL over 40 RCTs, largest at 100-200 mg a day (Liang Y et al. EClinicalMedicine
              2022;52:101602, doi:10.1016/j.eclinm.2022.101602, PMID 35958521), and NCCIH's CoQ10 page flags insulin in
              the same excerpt as warfarin; the page names ALA only (see the RX notes for why).
  [USP20]     Oketch-Rabah HA et al. USP comprehensive review of the hepatotoxicity of green tea extracts.
              Toxicol Rep 2020;7:386-402. doi:10.1016/j.toxrep.2020.02.008, PMC7044683 (fasting bolus doses
              raise EGCG exposure; case reports at 140 to about 1000 mg/day EGCG; the review supports a caution
              on green tea extract "especially when ingested under fasting conditions or in cases where there is
              underlying liver vulnerability"; "The public should be informed about the potential risk of liver
              injury with a high, sustained dose of GTE as a dietary supplement, especially for those who are
              obese or have preexisting liver disease", and NAFLD or NASH "may exacerbate the GTE induced liver
              injury" (PMC full text, read 2026-11-03)).  The label caution in USP's Powdered Decaffeinated Green
              Tea Extract monograph (official 2019-03-01), in full: "Do not take on an empty stomach. Take with
              food. Do not use if you have a liver problem and discontinue use and consult a healthcare
              practitioner if you develop symptoms of liver trouble, such as abdominal pain, dark urine, or
              jaundice (yellowing of the skin or eyes)."  The PubMed and PMC copies of the abstract drop the quoted
              statement; its opening and closing words were read earlier, and the middle clause ("Do not use if you
              have a liver problem", then stop and consult at liver-trouble signs) is as library-catalog copies of
              the abstract print it (web search 2026-11-03; USP's own site is not reachable from this session).
              This caution is why column 4 is Cellular Energy (no green tea) and not the GLC 2026 list's Mito
              Recharge (100 mg EGCG from green tea extract, sell sheet ND812 Rev. 2/25): the swap pass of
              2026-11-04.  Re-check the wording against the monograph if Mito Recharge is ever put back.
  [EASL24X]   The same EASL-EASD-EASO guideline, executive summary (PMC11519095, read 2026-11-03): "In adults with
              MASLD and overweight, dietary and behavioural therapy-induced weight loss should aim at a sustained
              reduction of >=5% to reduce liver fat, 7-10% to improve liver inflammation and >=10% to improve
              fibrosis"; "In normal-weight adults with MASLD, diet and exercise interventions should be recommended
              to reduce liver fat"; "Individuals with SLD ... should be discouraged from consuming alcohol"; "Statins
              can be used in adults with chronic liver disease, including those with compensated cirrhosis".
  [STATINS]   US prescribing information: simvastatin (ZOCOR) and lovastatin are CYP3A4 substrates (strong CYP3A4
              inhibitors are contraindicated with both); atorvastatin (LIPITOR) "is a substrate of CYP3A4".  Berberine
              slowed CYP3A4 in people [GUO12], so the check names those three statins.  Statins are common on this
              plan's readers: [AASLD23] "Management of dyslipidemia in NAFLD should include the use of
              moderate-intensity to high-intensity statins as first-line therapy".
  [CSO26]     NutriDyn CSO, GLC 2026 protocol PDF (read 2026-11-03), "Metabolic Fatty Liver (MAFLD, MASLD, MASH)":
              PPC Silymarin (coming soon), Ganoderma Plus, Inflam-Eze Plus, Milk Thistle Complex, Berberine Pro,
              Detox, Mito Recharge, UltraBiotic Prebiotic.  NutriDyn CSO, GLC 2026 marketing outline (2026): the
              gut barrier and the "total toxic load of xenobiotics and inflammatory endotoxins".
  [CSO24]     NutriDyn CSO, GLC 2024 protocols PDF: UltraBiotic Prebiotic's polyphenols "all reduce LPS", listed as
              an Akkermansia booster.  Asher's Direct Mail blast "NutriDyn New Formula: Akkermansia Plus"
              (2024-05-09) ties Akkermansia to "colon and liver health".
  [LABELS]    NutriDyn sell sheets read 2026-11-03 (Dropbox NutriDyn Marketing Materials): Berberine Pro
              ND1130 Rev. 11/25, Lipo-Flow ND606 Rev. 4/26, Milk Thistle Complex ND764 Rev. 2/25; Cellular
              Energy ND325 Rev. 8/24 read 2026-11-04 [ND325].  Amounts are in products.d/fatty-liver.json.
              Berberine Pro's caution reads "If you are pregnant, nursing, or taking medication, consult your
              healthcare practitioner before use" (the source of the check panel's pregnancy line); Cellular
              Energy's caution is the same sentence.
  [ND325]     Cellular Energy sell sheet ND325 Rev. 8/24, read 2026-11-04: per 2 capsules, acetyl L-carnitine HCl
              300 mg, N-acetyl L-cysteine 300 mg, coenzyme Q10 200 mg, alpha-lipoic acid 150 mg, grape seed extract
              150 mg, magnesium 35 mg, manganese 2 mg; "Take two capsules daily"; vegetarian, no green tea.  Claims
              on the page are the sheet's own: "Supports energy production", "Provides antioxidant support".
  [ND606]     Lipo-Flow sell sheet ND606 Rev. 4/26, re-read 2026-11-04: "Lipo-Flow provides choleretic and cholagogue
              gastrointestinal agents. Choleretic agents increase the volume of bile produced by the liver ...
              Cholagogue agents promote the healthy flow of bile from the liver and gall bladder into the
              intestines"; "Artichoke extract and beetroot powder have choleretic and cholagogue properties.
              Dandelion root extract, tangerine extract, and gentian extract have cholagogue properties."
  [SILVA25]   Silva H, Daia AM. Exploring the cardiovascular potential of artichoke: a comprehensive review. Biology
              (Basel) 2025;14(4):397. doi:10.3390/biology14040397, PMID 40282262, PMC12024969 (full text read
              2026-11-04, section 3.7): "Due to its bile-stimulating (choleretic) effect, artichoke products should
              not be used by individuals with bile duct obstruction, including those with gallstones".  On allergy
              the same section says cross-reactivity with other daisy-family plants "has not been reported" but
              "caution is advised in sensitive individuals", so the daisy line rests on milk thistle [GILLESSEN20].
  [GILLESSEN20] Gillessen A, Schmidt HH. Silymarin as supportive treatment in liver diseases: a narrative review. Adv
              Ther 2020;37(4):1279-1301. doi:10.1007/s12325-020-01251-y, PMID 32065376, PMC7140758 (full text read
              2026-11-04, Toxicity and Safety): after rare anaphylactic reactions to milk thistle, "caution is
              advised in patients with a known sensitivity to plants in the Asteraceae/Compositae family (members of
              this family include chrysanthemums, daisies, marigolds and ragweed)".  The NCCIH milk thistle fact
              sheet and EMA's artichoke-leaf (Cynarae folium) summary carry the same cautions in web-search
              snippets, but neither site is reachable from this session, so the sheet cites the two papers read in
              full.  Re-check NCCIH and EMA before print if a reviewer asks for them by name.

Reviewer pass (2026-11-03, round 2), what changed and why:
  - Check panel, both editions: the green tea extract caution has its own bullet (it used to sit under
    "Statins"); berberine's drug-enzyme note (CYP2D6, 2C9, 3A4) is in both editions under "Other medicines,
    warfarin too", never called "liver enzymes" (on this sheet that phrase means the ALT/AST blood test);
    the practitioner edition names the doctor who prescribes or manages the medicine, since a DC or ND
    usually does not adjust diabetes medicines or warfarin; a pregnancy and nursing line for Berberine Pro.
  - Lipo-Flow prints its label dose (2 tablets 3 times daily); no lunch dose sits under "Evening meal".
  - Milk Thistle Complex mirrors its panel without a silymarin total (300 vs 600 mg is an open question).
  - Need headers avoid liver-fat and disease readings; every claim bullet carries the FDA diamond.
  - Intro and the alcohol tile no longer say alcohol plays no part [AASLD23][DELPHI23]; ALT dots say U/L.
  - Caption 2 between close-ups 2 and 3 is rewrapped so its widest line sits where the zoom beams are apart.
  - Fit (that round had five checks; polish round 1 merged two into one, polish round 2 added the gallstone check):
    the check panel takes the wider part of the duo, the empty Bedtime box is hidden (no bedtime doses; asserted),
    the lifestyle discs are 0.68 in and the "Nutrient Solutions" title sits 0.04 in higher.  Measured both editions
    in the build's Chromium: no overflow, 8 px or more above the footer, no bullet ending on a single word.
  - Open questions are in products.d/fatty-liver.json "src": total silymarin (NutriDyn), and whether a
    green-tea-extract product belongs on a liver sheet (Asher or the CSO).
Polish round 1 (2026-11-03, residual reviewer list), no redesign beyond the listed items:
  - Mito Recharge stays, with the USP green-tea-extract caution now covering the reader: the check panel says
    that with fatty liver or any liver problem it is taken only if the provider (pharmacy edition: the doctor)
    says so, always with food [USP20].  The reviewer's default swap, Alpha-Lipoic Acid R270, is blocked: the only
    R270 photo anywhere in reach shows the
    Progressive P872 60-capsule bottle, not NutriDyn's 100-capsule R270, so the swap would print the wrong bottle
    or a blank; the insulin-resistance and neuropathy sheets left R270 off for the same reason, and Mito Recharge
    is on the CSO's own GLC 2026 fatty-liver list [CSO26].  Keep-or-swap stays open for Asher or the CSO.
  - Check panel: the diabetes line is a plain caution ("may lower blood sugar along with them"); the CoQ10 line
    (no action, read as a pitch) is gone and the enzyme bullet, now led by "Statins, warfarin and other
    medicines", names simvastatin, lovastatin and atorvastatin [STATINS]; both editions say INR is a clotting test
    and the pharmacy edition adds the recheck; the pregnancy line covers all four products (all four labels carry
    the pregnant-or-nursing caution [LABELS]).  Fit, measured: the practitioner green-tea bullet takes the
    reviewer's wording without the old liver-enzyme recheck sentence, and one enzyme bullet replaces two.
  - Column 2 reads "Liver and bile support" / "Supports healthy fat metabolism" (ND606's own claim, without
    "in the liver"), so on a fatty-liver page it never reads as "clears fat from the liver".
  - Milk Thistle Complex's serving line drops the "(label)" tag and goes amount-first like the other three.
  - The rhythm's first box is relabelled "Breakfast and lunch" on this sheet (it holds the lunch doses), every
    product in it says which meal, and it takes the wider share of the panel.
  - Tiles: "Lose extra weight" opens on "Extra weight?" (EASL ties the 5 / 7-10 / 10 percent targets to
    overweight [EASL24X]); "Less alcohol, or none" matches the crossed-out glass and EASL's "discouraged".
  - The gut icon is an intestine drawn here (the kit's "gut" glyph is a stomach), on the front and the back.
  - The intro spells MASLD out at its first use; the stage subtitles are upright (no italic Inter ships, so the
    browser was faking one); both "liver's" on page 2 now use the curly apostrophe (&rsquo;) like the rx panel.
Polish round 2 (2026-11-04, residual reviewer list), no redesign beyond the listed items:
  - Check panel, both editions: a fifth check, "Gallstones, a blocked bile duct, or a ragweed or daisy allergy? Ask
    {who} or your doctor before Lipo-Flow (it boosts bile flow) and Milk Thistle Complex" [ND606][SILVA25]
    [GILLESSEN20].  Room for it: the notes box shows two writing lines 0.22 in apart instead of three at 0.24 in.
  - Mito Recharge (keep path while the CSO's keep-or-swap call is open; a swap still needs the real R270 photo): the
    gate is also where the reader builds the plan.  back["rhythm_note"] says to add it last, only once the provider
    writes it in the box below (pharmacy edition: once the doctor says yes), and the practitioner check asks for
    that written yes instead of "says so", which the handout met by itself.
  - The serving blocks sit at the bottom of each column: three "In each serving" rules line up (527.6 px), Lipo-Flow's
    one line higher (515.7 px), was two pairs 12.4 px apart; the dose bars stay level.
  - "Lose extra weight" puts a % on every figure (5%, 7-10%, 10% or more), one clause per line as before.
  - Notes only: the Berberine Pro src bracket and box name, the CSO citations by title and date (no machine paths),
    the fit notes above and in the CSS.
  - Measured, both editions, print media: 12.5 px clear above the footer (was 10.2), no overflow on either page, no
    bullet ending on one word, every check at two or three lines except the five-line medicines check.
Swap pass (2026-11-04, the reviewer's residual list: one major defect), no redesign beyond it:
  - Column 4 is Cellular Energy (R145) in place of Mito Recharge.  Mito Recharge carries 100 mg EGCG from green tea
    extract (ND812) and USP's caution for green tea extract says "Do not use if you have a liver problem" [USP20], so
    the sheet told a reader with fatty liver not to take a product it also counted in the plan.  Cellular Energy has no
    green tea; its 150 mg alpha-lipoic acid keeps the competitor's ALA match, and both bullets are its sell sheet's own
    claims [ND325].  The GLC 2026 list [CSO26] names Mito Recharge, so Asher can reverse the swap (products.d
    fl_cellular_energy "src" says where Mito Recharge's facts are); the fl_mito entry left products.d.
  - Gone with it: the green tea check in both editions, the rhythm-note gate (back["rhythm_note"], its marker spans, the
    .flv-gpr/.flv-gph CSS and the marker assert) and Mito Recharge's vitamin K1 sentence in the medicines check.  The
    medicines check now names warfarin among the drugs the slowed enzymes clear [KAMINSKY97] and keeps the INR recheck.
    (Corrected in polish round 2b: the vitamin-K-type warfarin concern did not leave with Mito Recharge, since Cellular
    Energy's 200 mg CoQ10 is chemically similar to vitamin K, so the medicines check now names it [COQ10].)  The plan
    line is the kit's own again, recounted by the kit: 13 pills a day (was 14).  These items in the earlier notes above
    are history only.  Still open for NutriDyn: Milk Thistle Complex's total silymarin (products.d fl_milk_thistle).
  - The notes box is the kit's own again, three writing lines 0.24 in apart: the two-line squeeze existed only to make
    room for a fifth check.
  - Measured, both editions, print media: no overflow on either page, 13.5 px clear above the page-2 footer (12.5
    before), checks at 2, 4, 2 and 2 lines, no bullet ending on one word or on a lone diamond, all four header bars on
    one line, the "In each serving" rules of columns 1, 3 and 4 level at 527.6 px (Lipo-Flow 515.7 px, as before) and
    the dose bars level at 596.1 px.
  - Photo: only Cellular Energy's 89x160 web thumbnail is in reach; the page prints the central stopgap step's smooth
    4x copy of it (img-src/R145.png, 356x640, marked SOFT, so the build lists it under SOFT PRODUCT PHOTOS).  The print
    master is Dropbox /NutriDyn/Product Images/Product Images (1)/R145_Web, which this session cannot download.
Polish round 2b (2026-11-04, the reviewer's list after the swap pass), no redesign beyond it:
  - Check panel, both editions: the medicines check adds "and the CoQ10 in Cellular Energy may change how warfarin works"
    [COQ10], so a warfarin user who takes Cellular Energy without Berberine Pro is warned too; the diabetes check names
    "(and, more mildly, the alpha-lipoic acid in Cellular Energy)" [ALA].  Practitioner edition: both drug lines tell the
    reader to tell the doctor who prescribes them / manages the warfarin before starting (they were passive).  The
    swap-pass notes that said the vitamin-K-type concern left with Mito Recharge are corrected (see [KAMINSKY97]).
  - Serving lines: "2 tablets:" (Lipo-Flow, also "tangerine" for the peel extract and no "and" before methionine) and
    "2 capsules:" (Cellular Energy) instead of "Per 2 ...:"; the one-capsule servings keep "Per capsule:".  Lipo-Flow's
    line drops from five lines to four, so all four "In each serving" rules line up (with "Per", every wording tried set
    in five; dropping "Per" on all four instead took Berberine Pro's line to three, which misaligned column 1).
  - Column 4's header sub spells "alpha-lipoic acid" like its serving line and ND325 (one line, nowrap).
  - Close-ups 2 to 4: squeezed nuclei, big droplets and the small side droplets stay inside their own cells, off the dark
    walls (FAT_NUC_D, FAT_BIG, FAT_OFF, FAT_SMALL_D, FAT_SMALL; 6.5 in close-up 4), each checked by an assert.  Same rnd
    calls, so the same cells hold fat, and the immune cells did not move (compared with the old numbers).  Measured gap to
    the inner edge of the wall stroke, worst case: nuclei +0.48 (was -0.72), big droplets +0.55 (was -0.85, one reaching
    the next cell), small droplets +0.33 (was -0.48), close-up 4 nuclei +0.39 (was -0.49).
  - Dead CSS: ".flv-risk .x{display:none}" is gone (it matched nothing since the risk strip drew its own soda glyph).
  - Measured, both editions, print media: no overflow on either page, 12.2 px clear above the page-2 footer (13.5
    before), checks at 3, 5, 2 and 2 lines, no bullet ending on one word, all four "In each serving" rules level at 527.6
    px and the dose bars at 596.1 px, all four header subs on one line; page 1 keeps 0.201 in above its footer, no
    text overlaps in the diagram, 7.4 pt smallest text.
  - Not fixable here: the Berberine Pro photo (img-src/R2125.png, shared with the insulin-resistance and PCOS sheets) has
    21 px of clear padding at the top and 26 px at the bottom, so the Start-here bottle prints 0.87 in tall against 0.98
    in for the others; trimming it belongs to the central photo-staging step, not this module's CSS.
"""
import json
import math
import os
import random

import kit
from kit import icon
from svgkit import T, svg

# ============================================================== text measuring
_FACES = {}
_WEIGHTS = {400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold", 800: "ExtraBold", 900: "Black"}
_FONT_DIRS = ("/usr/share/fonts/opentype/inter", "/usr/share/fonts/truetype/inter",
              os.path.expanduser("~/Library/Fonts"), "/Library/Fonts")


def _face(name):
    if name not in _FACES:
        from PIL import ImageFont
        for d in _FONT_DIRS:
            for ext in ("otf", "ttf"):
                f = os.path.join(d, f"Inter-{name}.{ext}")
                if os.path.exists(f):
                    _FACES[name] = ImageFont.truetype(f, 100)
                    return _FACES[name]
        raise FileNotFoundError(name)
    return _FACES[name]


def tw(text, size, weight=700, ls=0.0):
    """Advance width of `text` in Inter at `size` px.  Used to centre badge+label groups
    and to space the key.  Without Pillow or the font it falls back to a generous guess
    (checked: the layout still fits with the guess)."""
    try:
        w = _face(_WEIGHTS[weight]).getlength(text) * size / 100
    except Exception:
        w = len(text) * size * (0.68 if text.isupper() else 0.6)
    return w + ls * len(text)


# ============================================================== palette
INK, INK2 = "#23292D", "#57616A"
SEV = ("#3E8A27", "#B87A0C", "#D2611F", "#BE2F2F")        # stage badges, green -> red (white text >= 3.6:1)
SEV_BAR = ("#4E9A2E", "#E8A824", "#E26A2A", "#C8343B")    # the brighter severity arrow
GREEN, GREEN_TX = "#5A9E2C", "#3E7F22"                    # "often reversible" arcs + label
RED, RED_TX = "#D23F37", "#B32A2A"                        # "hardest to reverse" bracket + label
# magnified tissue (same values feed the art and the key, so they always match)
TISSUE_BG, CELL, CELL_EDGE, NUC = "#5A1C1F", "#8E3B3D", "#4A1416", "#C9787A"
FAT, FAT_EDGE, FAT_HI = "#F2B72E", "#C98A12", "#FFF4CF"
IMM, IMM_RING = "#FFFFFF", "#E2463E"
SCAR, SCAR_EDGE = "#D3CAC2", "#968B83"

# ============================================================== geometry
W = 760                       # viewBox width; rendered 7.66 in wide (1 unit = 0.73 pt, so 7 pt text >= 9.7)
EDGE = 8                      # one outer margin for the severity row, the band and the key, both sides
XS = (95, 285, 475, 665)      # stage centres, symmetric about x = 380
BAND = (156, 357)             # light arrow band behind the circles (top, bottom); it holds the arcs AND their labels
LIVER_S = 0.92                # base liver scale (each stage multiplies its own factor below)
LIVER_BOT = BAND[0] - 4       # every liver's lowest point (stroke included) sits 4 units above the band
LENS_Y, LENS_R = 116, 10      # the magnified spot, mid-body on all four livers
CY, R = 258, 54               # magnified tissue circles
ANCHOR = R + 11               # arc ends and bracket bars sit here, so tips and caps stop clear of the
                              # white ring round each circle (outer edge R + 3.4)
LOW_Y = 331                   # lowest point of every arc and of the bracket (so the labels share one baseline)
LABEL_Y = LOW_Y + 18          # baseline of OFTEN REVERSIBLE / HARDEST TO REVERSE (8 above the band bottom)
KEY_Y, KEY_H = BAND[1] + 6, 28
H = KEY_Y + KEY_H + 3         # total viewBox height

STAGES = [
    # label, subtitle (2023 names per [DELPHI23]), liver scale (fatty livers enlarge, cirrhotic ones shrink)
    ("HEALTHY", "little or no fat", 1.00),
    ("FATTY LIVER", "first stage of MASLD", 1.07),      # MASLD spans steatosis -> MASH -> fibrosis -> cirrhosis [EASL24]
    ("INFLAMED", "MASH, formerly NASH", 1.04),
    ("SCARRING", "fibrosis, then cirrhosis", 0.90),
]
# What pushes each step forward (plain words; mechanisms per [AASLD23] pathogenesis section:
# insulin resistance raises fat delivery to the liver; lipotoxic stress on liver cells drives the
# inflammation of MASH, and "exposure to products derived from the gut microbiome ... may also
# contribute to the NASH phenotype" [AASLD23], hence the hedge "may add to it"; ongoing inflammation
# drives fibrosis).  Wrapped so the widest line sits where the two zoom beams are farthest apart: the
# beams close in going down, so caption 2's last line is its shortest (checked: every line clears both beam
# edges by 7 units or more, about 1.8 mm printed; "bacteria may add to it" there cleared by only 3).
DRIVERS = [["Insulin resistance", "sends extra fat", "into liver cells"],
           ["Stressed cells spark", "inflammation; the gut", "may add to it"],
           ["Years of", "inflammation", "leave scars"]]

# ============================================================== the liver
# Anterior view: the big right lobe is on the viewer's left, the left lobe tapers right.
# Points walk clockwise; the third value is tangent tension (low = a sharper corner, used
# for the left-lobe tip and the notch where the round ligament enters).
_LIVER_PTS = [
    (3, 38, 1.0), (12, 15, 1.0), (36, 4, 1.0), (64, 3, 1.0), (88, 9, 1.0), (100, 11.5, 0.7),
    (118, 10, 1.0), (134, 15, 0.9), (141, 21, 0.3), (132, 27, 1.0), (112, 34, 1.0),
    (96, 41, 0.6), (90, 46.5, 0.25), (82, 49, 0.8), (62, 59, 1.0), (40, 69, 1.0),
    (20, 70, 1.0), (7, 58, 1.0),
]


def _spline(pts):
    """Closed Catmull-Rom curve through pts as cubic Bezier path data."""
    n = len(pts)
    tan = []
    for i in range(n):
        (x0, y0, _), (_, _, k), (x2, y2, _) = pts[i - 1], pts[i], pts[(i + 1) % n]
        tan.append((k * (x2 - x0) / 2, k * (y2 - y0) / 2))
    d = [f"M{pts[0][0]},{pts[0][1]}"]
    for i in range(n):
        j = (i + 1) % n
        (xa, ya, _), (xb, yb, _) = pts[i], pts[j]
        d.append(f"C{xa + tan[i][0] / 3:.1f},{ya + tan[i][1] / 3:.1f} "
                 f"{xb - tan[j][0] / 3:.1f},{yb - tan[j][1] / 3:.1f} {xb},{yb}")
    return "".join(d) + "Z"


LIVER_D = _spline(_LIVER_PTS)


def _cubic(p0, p1, p2, p3, t):
    m = 1 - t
    return tuple(m ** 3 * p0[k] + 3 * m * m * t * p1[k] + 3 * m * t * t * p2[k] + t ** 3 * p3[k] for k in (0, 1))


def _path_extent(d):
    """(x0, y0, x1, y1) of an M/C path, sampled: the spline bulges a little past its points."""
    nums = [float(v) for v in d.replace("M", " ").replace("C", " ").replace("Z", " ").replace(",", " ").split()]
    cur, pts = (nums[0], nums[1]), []
    for i in range(2, len(nums), 6):
        c1, c2, end = (nums[i], nums[i + 1]), (nums[i + 2], nums[i + 3]), (nums[i + 4], nums[i + 5])
        pts += [_cubic(cur, c1, c2, end, k / 32) for k in range(33)]
        cur = end
    return (min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts))


LIVER_EXT = _path_extent(LIVER_D)       # about (2.8, 2.4, 141.0, 71.0) in liver units
# stage 4 is a warm tan-brown (a diseased liver), not grey stone
LIVER_FILL = [("#C55B47", "#8C2E24"), ("#EEC468", "#C88E2E"), ("#DE8457", "#A8432A"), ("#B8936E", "#7A5843")]
LIVER_EDGE = ["#6E241C", "#94661D", "#84331F", "#5A3E2C"]


def _nodule_layout():
    """Regrowth nodules for the cirrhotic liver, packed without overlap (centre spacing at least
    r1 + r2 + 0.8), biggest first, so they read as separate bumps rather than bubble wrap.  A 12-unit
    grid keeps the packing fast (it only ever compares neighbours)."""
    rnd = random.Random(77)
    x0, y0, x1, y1 = LIVER_EXT
    placed, grid, g, tries = [], {}, 12.0, 40000
    for k in range(tries):
        hi = 5.6 - 3.0 * min(1.0, k / (tries * 0.6))
        r = rnd.uniform(max(2.6, hi - 1.2), hi)
        x, y = rnd.uniform(x0 - 3, x1 + 3), rnd.uniform(y0 - 3, y1 + 3)
        gx, gy = int(x // g), int(y // g)
        if all(math.hypot(x - a, y - b) >= r + rb + 0.8
               for i in (gx - 1, gx, gx + 1) for j in (gy - 1, gy, gy + 1) for a, b, rb in grid.get((i, j), ())):
            placed.append((x, y, r))
            grid.setdefault((gx, gy), []).append((x, y, r))
    return placed


NODULES = _nodule_layout()


def _liver_texture(stage):
    if stage == 1:   # pale fat mottling
        return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFF2C6" opacity=".55"/>'
                       for x, y, r in [(30, 30, 9), (57, 20, 6.5), (50, 45, 8), (84, 27, 6), (112, 21, 5), (24, 55, 6), (73, 38, 5)])
    if stage == 2:   # red, angry patches with a little fat left
        return ("".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#9E2A1C" opacity=".3"/>'
                        for x, y, r in [(34, 32, 10), (63, 42, 9), (92, 25, 7), (118, 19, 5), (22, 52, 7)])
                + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFE3A6" opacity=".5"/>'
                          for x, y, r in [(52, 20, 5.5), (78, 32, 4.5), (40, 50, 4)]))
    if stage == 3:   # cirrhosis: separate regrowth nodules, each a lit bump with a soft shadow below it
        return "".join(f'<circle cx="{x + r * .10:.1f}" cy="{y + r * .30:.1f}" r="{r * 1.02:.1f}" fill="#4A2E1E" opacity=".34"/>'
                       f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="url(#fl-nod)"/>'
                       f'<circle cx="{x - r * .34:.1f}" cy="{y - r * .36:.1f}" r="{r * .34:.1f}" fill="#FFF1DC" opacity=".38"/>'
                       for x, y, r in NODULES)
    return ""


def liver(cx, bot, s, stage):
    """One liver at scale s, centred on cx, its lowest point (half the 1.4 stroke included) on y = bot.
    Bottom-aligned, so all four sit the same distance above the band whatever their size."""
    x0, _, x1, y1 = LIVER_EXT
    return (f'<g transform="translate({cx - (x0 + x1) / 2 * s:.1f},{bot - (y1 + 0.7) * s:.1f}) scale({s:.3f})">'
            f'<path d="{LIVER_D}" fill="url(#fl-lv{stage})" stroke="{LIVER_EDGE[stage]}" stroke-width="1.4"/>'
            f'<g clip-path="url(#fl-lclip)">{_liver_texture(stage)}</g>'
            # falciform ligament, and a soft sheen along the dome
            '<path d="M100,12.5 C97,24 93.5,35 90.5,45.5" stroke="rgba(0,0,0,.2)" stroke-width="1.4" fill="none"/>'
            '<path d="M17,19 C29,10 46,7.5 62,7.5" stroke="rgba(255,255,255,.5)" stroke-width="3" fill="none" '
            'stroke-linecap="round"/></g>')


# ============================================================== magnified tissue
def _hex(px, py, r, rot=0.0):
    return " ".join(f"{px + r * math.cos(math.radians(a + rot)):.1f},{py + r * math.sin(math.radians(a + rot)):.1f}"
                    for a in range(30, 390, 60))


def sw_cell(r=8.5):
    return (f'<polygon points="{_hex(0, 0, r)}" fill="{CELL}" stroke="{CELL_EDGE}" stroke-width="1.4"/>'
            f'<circle r="{r * 0.3:.1f}" fill="{NUC}"/>')


def sw_fat(r=6.2, x=0, y=0):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{FAT}" stroke="{FAT_EDGE}" stroke-width="1"/>'
            f'<circle cx="{x - r * 0.36:.1f}" cy="{y - r * 0.36:.1f}" r="{r * 0.26:.1f}" fill="{FAT_HI}" opacity=".85"/>')


IMM_R = 4.4                   # immune cell radius in the art; its ring's outer edge is IMM_R + 0.9
IMM_GAP = 11.5                # minimum centre spacing, so rings (10.6 across) never stack


def sw_immune(r=5.0, x=0, y=0):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{IMM}" stroke="{IMM_RING}" stroke-width="1.8"/>'


SCAR_FIBRE = "#B5AAA1"        # faint collagen strands along each band of scar

# Close-up 3 (INFLAMED): the immune cells, relative to the circle centre.  Four tight foci of three
# (top, left, bottom, lower right), all in the dark gaps between liver cells.  The positions came from a
# free-space search over this circle's own droplets and nuclei (seed 2026 + 2): every spot keeps
# droplet r + IMM_R + 1 from fat, nucleus r + IMM_R + 1.2 from a nucleus and IMM_GAP from its neighbours.
# _immune_foci re-checks all of that, so the build fails if the tissue ever changes under them.
IMM_FOCI = [(-4, -34), (2, -23), (8, -33),        # top
            (-41, 10), (-36, -1), (-29, 11),      # left
            (-8, 32), (-3, 21), (4, 31),          # bottom
            (21, 30), (28, 20), (33, 31)]         # lower right


# Inside a fat-filled cell (polish round 2b).  A cell of circumradius 12 has its flat sides 10.39 from its centre, and
# its 1.6 wall stroke has its inner edge at 9.59.  The squeezed nucleus sits 7.4 out (radial half-height 1.7, so its
# outer edge is at 9.1), a big droplet has radius 6.6 to 8.4 and sits at most 0.4 off centre on each axis (9.45 at most,
# its own stroke included), and a small droplet sits 6.0 out with radius 2.2 to 2.9 (9.4 at most).  Each shape stays
# inside its own cell and off the dark wall, so the nuclei read as pressed inside the cell rather than as pink flecks
# on the walls.  (They sat at 8.6, droplets up to 9.4 + 1.0 per axis, small droplets 6.4 out up to 3.4.)  The ranges
# changed, the rnd calls did not, so the layout keeps its place.  _wall_gap re-checks every shape at build time.
FAT_NUC_D = 7.4
FAT_BIG, FAT_OFF = (6.6, 8.4), 0.4
FAT_SMALL_D, FAT_SMALL = 6.0, (2.2, 2.9)


def _wall_gap(px, py, cr, wall, reach, rot=0.0):
    """Gap from a shape to the inner edge of its own hexagon's wall stroke (negative: it covers the wall).  The hexagon
    is _hex(px, py, cr, rot), so its flat sides face 0 + rot, 60 + rot ... degrees; reach(nx, ny) is the shape's
    farthest point along that unit normal."""
    h = cr * math.cos(math.radians(30)) - wall / 2
    return min(h - (reach(math.cos(t), math.sin(t)) - (px * math.cos(t) + py * math.sin(t)))
               for t in (math.radians(60 * k + rot) for k in range(6)))


def _circle_reach(x, y, r):
    return lambda nx, ny: x * nx + y * ny + r


def _ellipse_reach(x, y, rx, ry, deg):
    """An ellipse whose rx axis points along deg (SVG rotate)."""
    c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
    return lambda nx, ny: x * nx + y * ny + math.hypot(rx * (c * nx + s * ny), ry * (-s * nx + c * ny))


def _immune_foci(cx, cy, r, drops, nucs):
    out, placed = [], []
    for ix, iy in IMM_FOCI:
        x, y = cx + ix, cy + iy
        assert math.hypot(ix, iy) <= r - IMM_R - 2.9, "immune cell outside the close-up"
        assert all(math.hypot(x - a, y - b) >= rd + IMM_R + 1 for a, b, rd in drops), "immune cell on fat"
        assert all(math.hypot(x - a, y - b) >= rn + IMM_R + 1.2 for a, b, rn in nucs), "immune cell on a nucleus"
        assert all(math.hypot(x - a, y - b) >= IMM_GAP for a, b in placed), "immune cells stacked"
        placed.append((x, y))
        out.append(sw_immune(IMM_R, x, y))
    return "".join(out)


def tissue(cx, cy, r, stage):
    """Magnified liver tissue: a honeycomb of liver cells, then fat and immune cells.
    Stage 3 (scarring) has its own nodular layout, see _tissue_scarred."""
    if stage == 3:
        return _tissue_scarred(cx, cy, r)
    rnd = random.Random(2026 + stage)
    out = [f'<clipPath id="fl-tc{stage}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
           f'<g clip-path="url(#fl-tc{stage})"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{TISSUE_BG}"/>']
    cr, dx, dy = 12, 25, 21.65
    cells = []
    for gy in range(-3, 4):
        for gx in range(-3, 4):
            px, py = cx + gx * dx + (dx / 2 if gy % 2 else 0), cy + gy * dy
            if math.hypot(px - cx, py - cy) < r + cr:
                cells.append((px, py))
    p_fat = {0: 0, 1: 0.66, 2: 0.5}[stage]
    drops, nucs = [], []
    wall = 1.6
    for px, py in cells:
        out.append(f'<polygon points="{_hex(px, py, cr)}" fill="{CELL}" stroke="{CELL_EDGE}" stroke-width="{wall}"/>')
        if rnd.random() < p_fat:
            big = rnd.uniform(*FAT_BIG)
            fx, fy = px + rnd.uniform(-FAT_OFF, FAT_OFF), py + rnd.uniform(-FAT_OFF, FAT_OFF)
            out.append(sw_fat(big, fx, fy))
            drops.append((fx, fy, big))
            a = rnd.uniform(0, 2 * math.pi)       # the big droplet squeezes the nucleus toward the cell's edge
            nx, ny = px + FAT_NUC_D * math.cos(a), py + FAT_NUC_D * math.sin(a)
            deg = round(math.degrees(a) + 90)
            out.append(f'<ellipse cx="{nx:.1f}" cy="{ny:.1f}" rx="2.7" ry="1.7" fill="{NUC}" '
                       f'transform="rotate({deg} {nx:.1f} {ny:.1f})"/>')
            nucs.append((nx, ny, 2.7))
            assert _wall_gap(px, py, cr, wall, _circle_reach(fx, fy, big + 0.5)) >= 0.1, "fat droplet on a cell wall"
            assert _wall_gap(px, py, cr, wall, _ellipse_reach(nx, ny, 2.7, 1.7, deg)) >= 0.1, "nucleus on a cell wall"
        else:
            out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{NUC}"/>')
            nucs.append((px, py, 3.6))
            if stage in (1, 2) and rnd.random() < 0.55:   # a few small droplets beside the nucleus
                a = rnd.uniform(0, 2 * math.pi)
                rs = rnd.uniform(*FAT_SMALL)
                sx, sy = px + FAT_SMALL_D * math.cos(a), py + FAT_SMALL_D * math.sin(a)
                out.append(sw_fat(rs, sx, sy))
                drops.append((sx, sy, rs))
                assert _wall_gap(px, py, cr, wall, _circle_reach(sx, sy, rs + 0.5)) >= 0.1, "fat droplet on a cell wall"
    if stage == 2:
        out.append(_immune_foci(cx, cy, r, drops, nucs))
    out.append("</g>")
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2.2}" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#2F2222" stroke-width="2.6"/>')
    return "".join(out)


# ---- close-up 4: rounded nodules ringed by scar
SCAR_SEEDS = [(-6, 0), (22, -34), (40, -2), (16, 38), (-30, 30), (-36, -24)]   # one nodule each, centre first
SCAR_WIDTH = (6, 11)          # septum width between two nodules, drawn per pair
SCAR_CR = 10.5                # liver cells in the nodules (a touch smaller, so each nodule holds more)


def _clip_half(poly, nx, ny, c):
    """The part of a polygon where nx*x + ny*y <= c (Sutherland-Hodgman)."""
    out = []
    for i in range(len(poly)):
        a, b = poly[i], poly[(i + 1) % len(poly)]
        da, db = nx * a[0] + ny * a[1] - c, nx * b[0] + ny * b[1] - c
        if da <= 0:
            out.append(a)
        if (da < 0) != (db < 0) and da != db:
            t = da / (da - db)
            out.append((a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])))
    return out


def _voronoi(seeds, widths, reach):
    """Each seed's Voronoi cell inside a circle of radius `reach`, pulled back from every neighbour by
    half the septum width between them (widths[(i, j)], 0 when absent)."""
    base = [(reach * math.cos(math.pi * k / 36), reach * math.sin(math.pi * k / 36)) for k in range(72)]
    cells = []
    for i, s in enumerate(seeds):
        poly = base
        for j, t in enumerate(seeds):
            if i != j:
                m = math.hypot(t[0] - s[0], t[1] - s[1])
                ux, uy = (t[0] - s[0]) / m, (t[1] - s[1]) / m
                mx, my = (s[0] + t[0]) / 2, (s[1] + t[1]) / 2
                poly = _clip_half(poly, ux, uy, ux * mx + uy * my - widths.get((min(i, j), max(i, j)), 0) / 2)
        cells.append(poly)
    return cells


def _rounded(poly, rho, step=1.2):
    """Dense outline of a convex polygon whose corners are rounded (quadratic, about radius rho)."""
    n, pts = len(poly), []
    for i in range(n):
        p0, p1, p2 = poly[i - 1], poly[i], poly[(i + 1) % n]
        l1, l2 = math.hypot(p1[0] - p0[0], p1[1] - p0[1]), math.hypot(p2[0] - p1[0], p2[1] - p1[1])
        if l1 < 1e-6 or l2 < 1e-6:
            continue
        t1, t2 = min(rho / l1, 0.5), min(rho / l2, 0.5)
        a = (p1[0] + (p0[0] - p1[0]) * t1, p1[1] + (p0[1] - p1[1]) * t1)
        b = (p1[0] + (p2[0] - p1[0]) * t2, p1[1] + (p2[1] - p1[1]) * t2)
        k = max(3, int((l1 * t1 + l2 * t2) / step))
        for s in range(k):
            u = s / k
            pts.append(((1 - u) ** 2 * a[0] + 2 * (1 - u) * u * p1[0] + u * u * b[0],
                        (1 - u) ** 2 * a[1] + 2 * (1 - u) * u * p1[1] + u * u * b[1]))
        a2 = (p2[0] + (p1[0] - p2[0]) * t2, p2[1] + (p1[1] - p2[1]) * t2)   # the next corner's start
        k = max(1, int(math.hypot(a2[0] - b[0], a2[1] - b[1]) / step))
        pts += [(b[0] + (a2[0] - b[0]) * s / k, b[1] + (a2[1] - b[1]) * s / k) for s in range(k)]
    return pts


def _wobble(pts, amp, rnd):
    """Push each outline point along its outward normal by a smooth random wave, so nodule edges
    (and the scar between them) swell and thin a little like real septa."""
    n = len(pts)
    ph1, ph2 = rnd.uniform(0, 6.28), rnd.uniform(0, 6.28)
    f1, f2 = rnd.choice([3, 4, 5]), rnd.choice([7, 8, 9])
    mx, my = sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n
    out = []
    for i, (x, y) in enumerate(pts):
        a, b = pts[i - 1], pts[(i + 1) % n]
        tx, ty = b[0] - a[0], b[1] - a[1]
        m = math.hypot(tx, ty) or 1
        nx, ny = ty / m, -tx / m
        if (x - mx) * nx + (y - my) * ny < 0:
            nx, ny = -nx, -ny
        s = i / n * 2 * math.pi
        w = amp * (0.7 * math.sin(f1 * s + ph1) + 0.3 * math.sin(f2 * s + ph2))
        out.append((x + nx * w, y + ny * w))
    return out


def _inside(poly, x, y):
    c = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


def _seg_in_circle(a, b, rr):
    """The part of segment a-b inside a circle of radius rr round the origin, or None."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    qa, qb, qc = dx * dx + dy * dy, 2 * (a[0] * dx + a[1] * dy), a[0] ** 2 + a[1] ** 2 - rr * rr
    disc = qb * qb - 4 * qa * qc
    if qa < 1e-9 or disc <= 0:
        return None
    t0, t1 = max(0.0, (-qb - math.sqrt(disc)) / (2 * qa)), min(1.0, (-qb + math.sqrt(disc)) / (2 * qa))
    if t1 - t0 < 1e-6:
        return None
    return (a[0] + dx * t0, a[1] + dy * t0), (a[0] + dx * t1, a[1] + dy * t1)


def _tissue_scarred(cx, cy, r):
    """Close-up 4 (cirrhosis): rounded nodules of liver cells walled off by scar.  Six seeds make a Voronoi
    layout; each nodule is its seed's cell pulled back by half the septum width on every side (6 to 11
    units, per pair), its corners rounded and its edge given a gentle wobble.  Where three nodules meet
    the scar forks.  Each nodule has its own tilted cell grid, so cell rows never run on across the scar.
    A few immune cells sit on the scar's edge (inflammation at the border)."""
    wr = random.Random(5)
    n = len(SCAR_SEEDS)
    widths = {(i, j): wr.uniform(*SCAR_WIDTH) for i in range(n) for j in range(i + 1, n)}
    rnd = random.Random(4)
    nodules = _voronoi(SCAR_SEEDS, widths, r + 30)
    plain = _voronoi(SCAR_SEEDS, {}, r + 30)
    out = [f'<clipPath id="fl-tc3"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
           f'<g clip-path="url(#fl-tc3)"><rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{SCAR}"/>']
    # collagen fibres: two faint strands along every septum centre line (the plain Voronoi edges),
    # trimmed short of the junctions so strands from different septa do not cross there
    for poly in plain:
        for k in range(len(poly)):
            a, b = poly[k], poly[(k + 1) % len(poly)]
            if math.hypot(*a) > r + 25 and math.hypot(*b) > r + 25:
                continue                       # part of the outer frame, not a septum
            tx, ty = b[0] - a[0], b[1] - a[1]
            m = math.hypot(tx, ty) or 1
            ux, uy, nx, ny = tx / m, ty / m, -ty / m, tx / m
            a, b = (a[0] + ux * 3.5, a[1] + uy * 3.5), (b[0] - ux * 3.5, b[1] - uy * 3.5)
            for off in (-1.6, 1.4):
                out.append(f'<path d="M{cx + a[0] + nx * off:.1f},{cy + a[1] + ny * off:.1f} '
                           f'L{cx + b[0] + nx * off:.1f},{cy + b[1] + ny * off:.1f}" stroke="{SCAR_FIBRE}" '
                           'stroke-width=".8" fill="none" stroke-linecap="round"/>')
    drops, nucs, rims = [], [], []
    ddx, ddy = SCAR_CR * math.sqrt(3), SCAR_CR * 1.5
    for i, poly in enumerate(nodules):
        rim = [(cx + x, cy + y) for x, y in _wobble(_rounded(poly, 7), 1.1, rnd)]
        rims.append(rim)
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in rim) + "Z"
        out.append(f'<clipPath id="fl-isl{i}"><path d="{d}"/></clipPath><g clip-path="url(#fl-isl{i})">'
                   f'<path d="{d}" fill="{TISSUE_BG}"/>')
        rot = rnd.uniform(-25, 25)
        ox, oy = rnd.uniform(0, 2 * SCAR_CR), rnd.uniform(0, 2 * SCAR_CR)
        ca, sa = math.cos(math.radians(rot)), math.sin(math.radians(rot))
        sx, sy = cx + SCAR_SEEDS[i][0], cy + SCAR_SEEDS[i][1]
        for gy in range(-6, 7):
            for gx in range(-6, 7):
                lx, ly = gx * ddx + (ddx / 2 if gy % 2 else 0) + ox, gy * ddy + oy
                px, py = sx + lx * ca - ly * sa, sy + lx * sa + ly * ca
                edge = min(math.hypot(px - q[0], py - q[1]) for q in rim)
                inside = _inside(rim, px, py)
                if not inside and edge > SCAR_CR:
                    continue
                out.append(f'<polygon points="{_hex(px, py, SCAR_CR, rot)}" fill="{CELL}" stroke="{CELL_EDGE}" stroke-width="1.5"/>')
                if rnd.random() < 0.18:
                    big = rnd.uniform(4.2, 6.0)
                    fx, fy = px + rnd.uniform(-1, 1), py + rnd.uniform(-1, 1)
                    a = rnd.uniform(0, 2 * math.pi)
                    if inside and edge >= big + 1.5:      # fat only where the whole droplet fits in the nodule
                        out.append(sw_fat(big, fx, fy))
                        drops.append((fx, fy, big))
                        # 6.5 out of a 10.5 cell (outer edge 8.0, wall-stroke inner edge 8.34), the same share of the
                        # cell as close-ups 2 and 3 (polish round 2b; it sat at 7.4 and covered the wall by up to 0.5)
                        nx, ny = px + 6.5 * math.cos(a), py + 6.5 * math.sin(a)
                        deg = round(math.degrees(a) + 90)
                        out.append(f'<ellipse cx="{nx:.1f}" cy="{ny:.1f}" rx="2.4" ry="1.5" fill="{NUC}" '
                                   f'transform="rotate({deg} {nx:.1f} {ny:.1f})"/>')
                        nucs.append((nx, ny, 2.4))
                        assert _wall_gap(px, py, SCAR_CR, 1.5, _ellipse_reach(nx, ny, 2.4, 1.5, deg), rot) >= 0.1, \
                            "nucleus on a cell wall"
                        assert _wall_gap(px, py, SCAR_CR, 1.5, _circle_reach(fx, fy, big + 0.5), rot) >= 0.1, \
                            "fat droplet on a cell wall"
                        continue
                out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="{NUC}"/>')
                if inside:                            # a centre outside the nodule is clipped away
                    nucs.append((px, py, 3.2))
        out.append("</g>")
        out.append(f'<path d="{d}" fill="none" stroke="{SCAR_EDGE}" stroke-width="1.6" stroke-linejoin="round"/>')
    # immune cells in the scar: points along each septum's centre line inside the view (its middle,
    # then its thirds), kept clear of fat, visible nuclei, each other and the circle's edge
    placed = []
    for i in range(n):
        for j in range(i + 1, n):
            si, sj = SCAR_SEEDS[i], SCAR_SEEDS[j]
            m = math.hypot(sj[0] - si[0], sj[1] - si[1])
            ux, uy = (sj[0] - si[0]) / m, (sj[1] - si[1]) / m
            mx, my = (si[0] + sj[0]) / 2, (si[1] + sj[1]) / 2
            on = [v for v in plain[i] if abs((v[0] - mx) * ux + (v[1] - my) * uy) < 1e-6]
            if len(on) < 2:
                continue                       # not neighbours
            seg = _seg_in_circle(on[0], on[1], r - IMM_R - 6)
            if not seg:
                continue
            (ax, ay), (bx, by) = seg
            for f in (0.5, 0.33, 0.67):
                x, y = cx + ax + (bx - ax) * f, cy + ay + (by - ay) * f
                if (all(math.hypot(x - a, y - b) >= rd + IMM_R + 1 for a, b, rd in drops)
                        and all(math.hypot(x - a, y - b) >= rn + IMM_R + 0.9 for a, b, rn in nucs)
                        and all(math.hypot(x - a, y - b) >= 2 * IMM_GAP for a, b in placed)):
                    placed.append((x, y))
                    out.append(sw_immune(IMM_R, x, y))
                    break
            if len(placed) == 5:
                break
        if len(placed) == 5:
            break
    out.append("</g>")
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 2.2}" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#2F2222" stroke-width="2.6"/>')
    return "".join(out)


def _cone(cx):
    """Zoom callout: the two outer tangents from the lens on the liver to its tissue circle."""
    d = CY - LENS_Y
    s = (R - LENS_R) / d
    c = math.sqrt(1 - s * s)
    p1y, p2y = LENS_Y - LENS_R * s, CY - R * s
    a, b = LENS_R * c, R * c
    # the beam runs round the underside of the lens, so the lens itself stays one even tint
    beam = (f"M{cx - a:.1f},{p1y:.1f} A{LENS_R},{LENS_R} 0 1 0 {cx + a:.1f},{p1y:.1f} "
            f"L{cx + b:.1f},{p2y:.1f} L{cx - b:.1f},{p2y:.1f} Z")
    return (f'<path d="{beam}" fill="#FFFFFF" fill-opacity=".45"/>'
            f'<path d="M{cx - a:.1f},{p1y:.1f} L{cx - b:.1f},{p2y:.1f} M{cx + a:.1f},{p1y:.1f} L{cx + b:.1f},{p2y:.1f}" '
            'stroke="#6F6763" stroke-width="1.2" stroke-opacity=".7" fill="none"/>')


def _lens(cx):
    return (f'<circle cx="{cx}" cy="{LENS_Y}" r="{LENS_R}" fill="#FFFFFF" fill-opacity=".18" stroke="#FFFFFF" stroke-width="2.4"/>'
            f'<circle cx="{cx}" cy="{LENS_Y}" r="{LENS_R + 1.6}" fill="none" stroke="#2F2222" stroke-width=".9" stroke-opacity=".55"/>')


# ============================================================== arrows and labels
def _q(p0, c, p1, t):
    return tuple((1 - t) ** 2 * p0[i] + 2 * (1 - t) * t * c[i] + t * t * p1[i] for i in (0, 1))


def _unit(vx, vy):
    m = math.hypot(vx, vy) or 1
    return vx / m, vy / m


def _on_circle(cx, deg, rr):
    return cx + rr * math.cos(math.radians(deg)), CY + rr * math.sin(math.radians(deg))


def _span(s, e):
    """Control point that puts the curve's lowest point on LOW_Y (s and e sit at the same height)."""
    return ((s[0] + e[0]) / 2, 2 * LOW_Y - (s[1] + e[1]) / 2)


def _reverse_arc(a, b):
    """Green arc from under circle a back to circle b (toward healthy), arrowhead at b.
    Both ends stop at ANCHOR, so the tail and the arrow tip sit just clear of the white ring."""
    s, e = _on_circle(XS[a], 125, ANCHOR), _on_circle(XS[b], 55, ANCHOR)
    c = _span(s, e)
    ux, uy = _unit(e[0] - c[0], e[1] - c[1])
    tip = (e[0] + ux * 6, e[1] + uy * 6)
    base = (e[0] - ux * 7, e[1] - uy * 7)
    head = (f"{tip[0]:.1f},{tip[1]:.1f} {base[0] - uy * 8:.1f},{base[1] + ux * 8:.1f} "
            f"{base[0] + uy * 8:.1f},{base[1] - ux * 8:.1f}")
    low = _q(s, c, e, 0.5)
    return (f'<path d="M{s[0]:.1f},{s[1]:.1f} Q{c[0]:.1f},{c[1]:.1f} {e[0]:.1f},{e[1]:.1f}" stroke="{GREEN}" '
            f'stroke-width="6" fill="none" stroke-linecap="round"/><polygon points="{head}" fill="{GREEN}" stroke="{GREEN}" '
            f'stroke-width="1.5" stroke-linejoin="round"/>', low)


def _hard_bracket(a, b):
    """Red bracket spanning circles a..b: the step that is hardest to undo.  Its T-bars are centred
    on ANCHOR, so even their round caps stop short of the white ring."""
    s, e = _on_circle(XS[a], 55, ANCHOR), _on_circle(XS[b], 125, ANCHOR)
    c = _span(s, e)
    out = [f'<path d="M{s[0]:.1f},{s[1]:.1f} Q{c[0]:.1f},{c[1]:.1f} {e[0]:.1f},{e[1]:.1f}" stroke="{RED}" '
           'stroke-width="6" fill="none" stroke-linecap="round"/>']
    for p, (tx, ty) in ((s, (c[0] - s[0], c[1] - s[1])), (e, (e[0] - c[0], e[1] - c[1]))):
        ux, uy = _unit(tx, ty)
        out.append(f'<path d="M{p[0] - uy * 9:.1f},{p[1] + ux * 9:.1f} L{p[0] + uy * 9:.1f},{p[1] - ux * 9:.1f}" '
                   f'stroke="{RED}" stroke-width="6" stroke-linecap="round"/>')
    return "".join(out), _q(s, c, e, 0.5)


def _severity_row(y):
    """LEAST SEVERE ====gradient arrow====> MOST SEVERE, across the top of the diagram, on the shared margin."""
    fs, ls = 12.5, 0.8
    wl, wr = tw("LEAST SEVERE", fs, 800, ls), tw("MOST SEVERE", fs, 800, ls)
    m, gap = EDGE, 12
    x0, x1 = m + wl + gap, W - m - wr - gap
    h, hh = 10, 9.5          # bar thickness, arrowhead half-height
    bar = (f'<path d="M{x0 + h / 2:.1f},{y - h / 2} H{x1 - 20:.1f} V{y - hh} L{x1:.1f},{y} L{x1 - 20:.1f},{y + hh} '
           f'V{y + h / 2} H{x0 + h / 2:.1f} A{h / 2},{h / 2} 0 0 1 {x0 + h / 2:.1f},{y - h / 2} Z" fill="url(#fl-sev)"/>')
    grad = ('<linearGradient id="fl-sev" gradientUnits="userSpaceOnUse" '
            f'x1="{x0:.1f}" y1="0" x2="{x1:.1f}" y2="0">'
            + "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in zip((0, .38, .68, 1), SEV_BAR))
            + "</linearGradient>")
    return grad, (bar + T(m, y + 4.5, "LEAST SEVERE", fs, 800, GREEN_TX, ls=ls)
                  + T(W - m, y + 4.5, "MOST SEVERE", fs, 800, RED_TX, "end", ls=ls))


def _stage_label(i, cx):
    lab, sub, _ = STAGES[i]
    fs, ls, br, gap = 17, 0.6, 12, 7
    w = 2 * br + gap + tw(lab, fs, 800, ls)
    bx = cx - w / 2 + br
    return (f'<circle cx="{bx:.1f}" cy="49" r="{br}" fill="{SEV[i]}"/>'
            + T(bx, 53.6, str(i + 1), 13, 800, "#FFFFFF", "middle")
            + T(bx + br + gap, 55, lab, fs, 800, INK, ls=ls)
            # upright: fonts/ ships no italic Inter, so italic=True made the browser skew SemiBold into a faux italic;
            # the grey and the smaller size already set the subtitle apart
            + T(cx, 73, sub, 11.5, 600, INK2, "middle"))


# ---- the key: every swatch sits on a small dark tissue chip, exactly as it looks in the close-ups
CHIP_W, CHIP_H = 26, 19


def _chip(inner, clip_id=None):
    x, y = -CHIP_W / 2, -CHIP_H / 2
    rect = f'<rect x="{x}" y="{y}" width="{CHIP_W}" height="{CHIP_H}" rx="4" fill="{TISSUE_BG}"/>'
    if not clip_id:
        return rect + inner
    return (f'<clipPath id="{clip_id}"><rect x="{x}" y="{y}" width="{CHIP_W}" height="{CHIP_H}" rx="4"/></clipPath>'
            + rect + f'<g clip-path="url(#{clip_id})">{inner}</g>')


def sw_scar():
    """Key swatch: a straight piece of septum as wide as the art's bands, with the same pale fill,
    dark edges (the nodule rims) and two fibre strands, cut off by its chip."""
    hw = 3.9
    band = (f'<g transform="rotate(-26)"><rect x="-22" y="{-hw}" width="44" height="{2 * hw}" fill="{SCAR}"/>'
            f'<path d="M-22,{-hw} H22 M-22,{hw} H22" stroke="{SCAR_EDGE}" stroke-width="1.6"/>'
            f'<path d="M-22,-1.6 H22 M-22,1.4 H22" stroke="{SCAR_FIBRE}" stroke-width=".8"/></g>')
    return _chip(band, "fl-kscar")


def _key(y):
    """KEY to everything drawn inside the magnified circles (same swatch code as the art)."""
    hw = CHIP_W / 2
    items = [(_chip(sw_cell(7.4)), "Liver cell (pink = nucleus)"), (_chip(sw_fat(5.8)), "Fat droplet"),
             (_chip(sw_immune(4.6)), "Immune cell"), (sw_scar(), "Scar tissue")]
    x0, x1, h = EDGE, W - EDGE, KEY_H
    title, fs, base = "KEY TO THE CLOSE-UPS", 11.5, y + h / 2 + 4.1
    tx = x0 + 14
    start = tx + tw(title, 10.5, 800, 1.2) + 24
    widths = [2 * hw + 7 + tw(lab, fs, 600) for _, lab in items]
    gap = (x1 - 16 - start - sum(widths)) / (len(items) - 1)
    assert gap >= 14, "key too crowded"
    out = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" rx="8" fill="#FFFFFF" stroke="#D9D1CD" stroke-width="1.2"/>',
           T(tx, base - 0.2, title, 10.5, 800, INK, ls=1.2)]
    x = start
    for (sw, lab), wd in zip(items, widths):
        out.append(f'<g transform="translate({x + hw:.1f},{y + h / 2})">{sw}</g>')
        out.append(T(f"{x + 2 * hw + 7:.1f}", base, lab, fs, 600, INK))
        x += wd + gap
    return "".join(out)


def _cone_half(y):
    """Half-width of a zoom beam at height y (between the tangent points it is a straight taper)."""
    s = (R - LENS_R) / (CY - LENS_Y)
    c = math.sqrt(1 - s * s)
    p1y, p2y = LENS_Y - LENS_R * s, CY - R * s
    return LENS_R * c + (R - LENS_R) * c * (y - p1y) / (p2y - p1y)


def _zoom_tag(cx, y):
    """'Close-up' tag inside the first zoom beam (the key's own word), so a reader knows the circles are
    close-ups of the liver.  Checked: the pill stays inside the beam with room to spare (see the assert)."""
    lab, fs = "Close-up", 10.2
    w, h = tw(lab, fs, 700) + 9, 14.5
    assert w / 2 + 6 <= _cone_half(y), "zoom tag too wide for the beam"
    return (f'<rect x="{cx - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h}" rx="{h / 2}" '
            'fill="#FFFFFF" stroke="#B9AFA9" stroke-width=".9"/>'
            + T(cx, y + 3.7, lab, fs, 700, INK2, "middle"))


def art_progression(t):
    defs = ['<defs>',
            f'<clipPath id="fl-lclip"><path d="{LIVER_D}"/></clipPath>',
            '<linearGradient id="fl-band" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E7F0E1"/>'
            '<stop offset=".5" stop-color="#F6F0E4"/><stop offset="1" stop-color="#F8E0DB"/></linearGradient>',
            # a cirrhotic nodule: lit from the upper left, darker at its rim
            '<radialGradient id="fl-nod" cx=".4" cy=".36" r=".72"><stop offset="0" stop-color="#D9B994"/>'
            '<stop offset=".7" stop-color="#B48C66"/><stop offset="1" stop-color="#9C7652"/></radialGradient>']
    for i, (c1, c2) in enumerate(LIVER_FILL):
        defs.append(f'<linearGradient id="fl-lv{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/>'
                    f'<stop offset="1" stop-color="{c2}"/></linearGradient>')
    sev_grad, sev_row = _severity_row(18)
    defs.append(sev_grad)
    defs.append("</defs>")
    out = ["".join(defs), sev_row]
    for i, cx in enumerate(XS):
        out.append(_stage_label(i, cx))
    top, bot = BAND
    mid = (top + bot) / 2
    e = EDGE
    out.append(f'<path d="M{e + 12},{top} H{W - e - 60} L{W - e},{mid} L{W - e - 60},{bot} H{e + 12} '
               f'Q{e},{bot} {e},{bot - 12} V{top + 12} Q{e},{top} {e + 12},{top} Z" '
               'fill="url(#fl-band)" stroke="#E2D8D2" stroke-width="1"/>')
    for i, cx in enumerate(XS):
        out.append(liver(cx, LIVER_BOT, LIVER_S * STAGES[i][2], i))
    for cx in XS:
        out.append(_cone(cx))
        out.append(_lens(cx))
    out.append(_zoom_tag(XS[0], 188))
    for i, cx in enumerate(XS):
        out.append(tissue(cx, CY, R, i))
    for i, lines in enumerate(DRIVERS):
        gx = (XS[i] + XS[i + 1]) / 2
        out.append(T(gx, 174, lines, 10.2, 700, "#454C52", "middle", lh=1.22))
        out.append(f'<path d="M{gx - 14},211 H{gx + 7}" stroke="#8A9096" stroke-width="2.4" stroke-linecap="round"/>'
                   f'<path d="M{gx + 5},205.5 L{gx + 14},211 L{gx + 5},216.5 Z" fill="#8A9096"/>')
    for a, b in ((1, 0), (2, 1)):
        arc, low = _reverse_arc(a, b)
        out.append(arc)
        out.append(T(low[0], LABEL_Y, "OFTEN REVERSIBLE", 12.5, 800, GREEN_TX, "middle", ls=0.4))
    br, low = _hard_bracket(2, 3)
    out.append(br)
    out.append(T(low[0], LABEL_Y, "HARDEST TO REVERSE", 12.5, 800, RED_TX, "middle", ls=0.4))
    out.append(_key(KEY_Y))
    return svg(W, H, "".join(out), "How fatty liver disease progresses from a healthy liver to scarring, "
               "with magnified views of the liver tissue at each stage")


# ============================================================== blocks under the art
RISKS = [  # each factor is named in [AASLD23]
    ("soda", "Sugary drinks,<br>added sugar"),
    ("meter", "Insulin resistance<br>or diabetes"),            # T2DM: "the most impactful risk factor"
    ("waist", "Weight carried<br>at the belly"),
    ("heartpulse", "High blood<br>pressure"),
    ("tube", "High blood fats<br>(triglycerides)"),
    ("ovaries", "PCOS (polycystic<br>ovary syndrome)"),        # 2- to 4-fold higher MASLD prevalence
    ("dna", "Family history<br>and genes"),                     # PNPLA3; relatives of NASH cirrhosis
    ("intestine", "Gut imbalance<br>(being studied)"),          # [AASLD23]: gut microbiome products "may also contribute"
]

# The intestine, where the gut bacteria live (the kit's "gut" glyph is a stomach, the wrong organ here): the
# large intestine as a hollow tube framing the belly (cecum low on the viewer's left, rectum turning down at the
# bottom), the small intestine coiled inside and running into the cecum.  Kit line style: 64-unit grid, round
# caps and joins, the row's own stroke width; nudged up 2 units so it sits centred in its disc.
INTESTINE = ('<g transform="translate(0 -2)">'
             '<path d="M10.6 46V22A13.4 13.4 0 0 1 24 8.6H40A13.4 13.4 0 0 1 53.4 22V40A11.4 11.4 0 0 1 42 51.4H38'
             'A0.6 0.6 0 0 0 37.4 52V57A3.4 3.4 0 0 1 30.6 57V52A7.4 7.4 0 0 1 38 44.6H42A4.6 4.6 0 0 0 46.6 40V22'
             'A6.6 6.6 0 0 0 40 15.4H24A6.6 6.6 0 0 0 17.4 22V46A3.4 3.4 0 0 1 10.6 46Z"/>'
             '<path d="M24.5 21H39.75a3.25 3.25 0 0 1 0 6.5H25.25a3.25 3.25 0 0 0 0 6.5H39.75a3.25 3.25 0 0 1 0 6.5H25'
             'C21.6 40.5 19.6 41.7 17.6 43.6"/></g>')
# The back page's lifestyle discs only take kit icon names, so the glyph is also registered under a name no other
# sheet uses (the ibd and tendon-shoulder sheets register their own icons the same way).
kit.ICONS["flv-intestine"] = INTESTINE

# Glyphs drawn here in the kit's line style (64-unit grid, round caps, stroke 2.8 like the rest of the row)
_RISK_ICONS = {
    # a soda cup with a dome lid and a straw: "sugary drinks" at a glance (the kit's sugar cube read as a box)
    "soda": ('<path d="M18 25h28"/><path d="M21 25a11 6 0 0 1 22 0"/>'
             '<path d="M20 25l3.6 29.2a3 3 0 0 0 3 2.6h10.8a3 3 0 0 0 3-2.6L44 25"/>'
             '<path d="M34 19.2 37.6 7H45"/><path d="M21.5 37h21"/>'),
    # a uterus with its tubes and ovaries (PCOS), in place of the abstract calendar
    "ovaries": ('<path d="M25 21c0-4 14-4 14 0 0 9-3 15-4.6 19.5V50h-4.8V40.5C28 36 25 30 25 21z"/>'
                '<path d="M25.5 21.5C20 15 13 15 10 21"/><path d="M38.5 21.5C44 15 51 15 54 21"/>'
                '<ellipse cx="12.5" cy="29" rx="5.5" ry="4.3"/><ellipse cx="51.5" cy="29" rx="5.5" ry="4.3"/>'),
    "intestine": INTESTINE,
}


def _risk_icon(name, size="0.33in", sw=2.8):
    if name not in _RISK_ICONS:
        return icon(name, size, sw=sw)
    return (f'<svg class="ic" viewBox="0 0 64 64" style="width:{size};height:{size};color:currentColor" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{_RISK_ICONS[name]}</svg>')


_STEP_ICONS = {
    "vial": ('<g transform="rotate(20 32 32)"><path d="M22 7h20"/><path d="M26.5 7v39a5.5 5.5 0 0 0 11 0V7"/>'
             '<path d="M26.5 28h11v18a5.5 5.5 0 0 1-11 0z" fill="currentColor" fill-opacity=".3" stroke="none"/>'
             '<path d="M26.5 28h11"/></g>'),
    "gauge": ('<path d="M9 45a23 23 0 0 1 46 0"/><path d="M15.7 29.7l3.6 3M32 22v5M48.3 29.7l-3.6 3"/>'
              '<path d="M32 45 43.5 31.5"/><circle cx="32" cy="45" r="4" fill="currentColor" stroke="none"/><path d="M13 54h38"/>'),
    "probe": ('<path d="M26 6h12v20l-2.5 12h-7L26 26z"/><path d="M8 44h48"/>'
              '<path d="M22 50.5c6 3.6 14 3.6 20 0M16.5 57.5c9 5 22 5 31 0"/>'),
}


def _ico(name, px=24):
    return (f'<svg viewBox="0 0 64 64" style="width:{px}px;height:{px}px" fill="none" stroke="currentColor" '
            f'stroke-width="4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_STEP_ICONS[name]}</svg>')


_ARROW = ('<svg viewBox="0 0 12 22" style="width:9px;height:17px" aria-hidden="true"><path d="M2.5 2.5 9.5 11 2.5 19.5" '
          'fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')

# The three checks, in the order AASLD 2023 lays them out for primary care [AASLD23]:
#  - "Serum AST levels are often used clinically to identify patients with liver disease but can be normal
#    in patients with diabetes, NASH, and advanced hepatic fibrosis" (hence "normal levels do not rule out")
#  - "normal values provided by most laboratories are higher than what should be considered normal in
#    NAFLD, in which a true normal alanine aminotransferase (ALT) ranges from 29 to 33 U/L in men and
#    from 19 to 25 U/L in women": upper limits, so the dots give the top of each range ("about ... or less")
#  - FIB-4 is "based upon age, ALT, AST, and platelet count"; low risk is "FIB-4 <1.3"
#  - FIB-4 >= 1.3 -> VCTE (eg, FibroScan) favoured as the secondary test in primary care; it measures
#    liver stiffness, and its CAP reading "provides a point-of-care semiquantitative assessment of
#    hepatic steatosis but does not accurately quantify" liver fat (hence "estimates")
#  - VCTE "LSM <8 kPa can be used to rule out advanced fibrosis"; intermediate or high risk on the
#    secondary test -> "referred to specialty care" (red: the most serious result on the page)
CHECKS = [
    ("vial", "Liver enzymes (ALT, AST)",
     "A routine blood test. High levels can mean the liver is irritated, but normal levels do not rule out "
     "fatty liver.",
     # U/L, the unit lab reports print (some print IU/L, the same number) [AASLD23].  "Up to" gives the top of
     # each true-normal range (women 19-25, men 29-33 U/L) and keeps each dot on one line in the card.
     [(SEV[0], "Healthy ALT, women: up to 25 U/L"), (SEV[0], "Healthy ALT, men: up to 33 U/L")]),
    ("gauge", "FIB-4 score",
     "Worked out from your age and routine labs (ALT, AST, platelets) to estimate the risk of advanced scarring.",
     [(SEV[0], "Under 1.3: low risk"), (SEV[1], "1.3 or higher: a FibroScan is next")]),
    ("probe", "FibroScan (elastography)",
     "A no-needle scan that measures liver stiffness (scarring) and estimates liver fat. "
     "The next step if FIB-4 is 1.3 or higher.",
     [(SEV[0], "Under 8 kPa: low risk"), (SEV[3], "8 kPa or more: see a liver specialist")]),
]


def _ed(x, ed):
    return x.replace("{who}", ed["who"]).replace("{Who}", ed["Who"])


def risk_strip():
    cells = "".join(f'<div class="flv-rf"><span class="flv-disc">{_risk_icon(ic)}</span>'
                    f'<span class="flv-rl">{lab}</span></div>' for ic, lab in RISKS)
    return f'<div class="flv-risk">{cells}</div>'


def ask_panel(ed):
    cards = []
    for n, (ic, title, body, dots) in enumerate(CHECKS, 1):
        extra = ""
        if dots:
            extra = '<ul class="flv-dots">' + "".join(f'<li><i style="background:{c}"></i>{x}</li>' for c, x in dots) + "</ul>"
        cards.append(f'<div class="flv-step"><div class="flv-sh"><span class="flv-n">{n}</span>{_ico(ic)}<b>{title}</b></div>'
                     f'<p>{body}</p>{extra}</div>')
    steps = f'<div class="flv-arr">{_ARROW}</div>'.join(cards)
    # [AASLD23]: "In most patients, NAFLD is asymptomatic or associated with vague symptoms"
    lead = "You may feel fine. Ask {who} which checks fit you."
    if "pharmacist" in ed["who"]:    # a pharmacist can advise, but a doctor orders the labs and the scan
        lead = "You may feel fine. Ask {who} which checks fit you; your doctor can order them."
    # [AASLD23]: ">= 2 metabolic risk factors, particularly prediabetes or T2DM ... FIB-4 every 1-2 years"
    foot = "<b>Two or more metabolic risks, like prediabetes or belly fat?</b> Check FIB-4 every 1 to 2 years."
    return (f'<div class="flv-ask"><div class="flv-askhd"><b>Ask about liver checks</b><span>{_ed(lead, ed)}</span></div>'
            f'<div class="flv-steps">{steps}</div>'
            f'<div class="flv-foot"><span>{foot}</span><small>AASLD practice guidance, 2023</small></div></div>')


def front(t, ed):
    return ('<div class="flv">'
            '<h2 class="flv-h">How fatty liver progresses</h2>'
            f'<div class="art flv-art">{art_progression(t)}</div>'
            '<h2 class="flv-h">What raises your risk</h2>'
            f'{risk_strip()}{ask_panel(ed)}</div>')


CSS = r"""
.flv-h{display:flex;align-items:center;gap:0.1in;font:900 11pt/1.2 Merriweather,Georgia,serif;color:var(--c1);
  letter-spacing:.04em;text-transform:uppercase;margin:0.02in 0 0.06in}
.flv-h::after{content:"";flex:1;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--soft),rgba(246,228,225,0))}
.flv-art+.flv-h{margin-top:0.08in}
.flv-risk{display:grid;grid-template-columns:repeat(8,1fr);gap:0 0.04in}
.flv-rf{display:flex;flex-direction:column;align-items:center;text-align:center}
.flv-disc{width:0.52in;height:0.52in;border-radius:50%;background:var(--soft);color:var(--c1);display:flex;
  align-items:center;justify-content:center;box-shadow:inset 0 0 0 1.5px rgba(138,27,34,.10)}
.flv-rl{display:block;font-size:7.8pt;font-weight:600;line-height:1.22;color:#2F373C;margin-top:0.03in}
.flv-ask{margin-top:0.11in;background:var(--tint);border:1px solid #EBD3CE;border-radius:10px;padding:0.08in 0.12in 0.07in}
.flv-askhd{display:flex;align-items:baseline;gap:0.12in;margin:0 0 0.06in}
.flv-askhd b{flex:none;font:900 11pt/1.2 Merriweather,Georgia,serif;color:var(--c1);letter-spacing:.04em;text-transform:uppercase}
.flv-askhd span{font-size:8.4pt;line-height:1.3;color:#2B3236}
.flv-steps{display:grid;grid-template-columns:1fr 16px 1fr 16px 1fr;align-items:stretch}
.flv-step{background:#fff;border:1px solid #EDDDD9;border-radius:8px;padding:0.06in 0.08in 0.07in;box-shadow:0 1px 2px rgba(80,20,20,.06)}
.flv-sh{display:flex;align-items:center;gap:6px;margin:0 0 4px}
.flv-n{flex:none;width:17px;height:17px;border-radius:50%;background:var(--c1);color:#fff;font:800 8pt/1 Inter,sans-serif;
  display:flex;align-items:center;justify-content:center}
.flv-sh svg{flex:none;color:var(--c1)}
.flv-sh b{font:800 8.8pt/1.15 Inter,sans-serif;color:var(--deep)}
.flv-step p{margin:0;font-size:7.8pt;line-height:1.32;color:#2B3236}
.flv-dots{list-style:none;margin:4px 0 0;padding:0}
.flv-dots li{display:flex;align-items:center;gap:5px;font-size:7.6pt;font-weight:700;line-height:1.3;color:#2B3236;margin:1px 0}
.flv-dots i{flex:none;width:8px;height:8px;border-radius:50%}
.flv-arr{display:flex;align-items:center;justify-content:center;color:var(--c2)}
.flv-foot{display:flex;justify-content:space-between;align-items:baseline;gap:0.2in;margin-top:0.06in;font-size:7.4pt;color:#3F4A50}
.flv-foot b{color:var(--deep)}
.flv-foot small{font-size:7.2pt;color:#6A747B;white-space:nowrap}
/* back page, scoped by the marker span in the lifestyle title.  The check panel holds four checks (diabetes
   medicines; statins, warfarin and other medicines; pregnancy; gallstones and daisy-family allergy) and takes the
   wider part of the duo.  Nothing on this plan is taken at bedtime (asserted after COLS), so the kit's Bedtime box,
   which would only say "nothing to take", is hidden and the two meal boxes share the rhythm panel.  The notes box is
   the kit's own again (three writing lines 0.24 in apart): the two-line squeeze that made room for a fifth check
   left in the swap pass with the green tea check.  Each column's serving block sits at the bottom of its card, so
   all four "In each serving" rules line up as long as every serving line sets in four lines (polish round 2b: the
   two-unit servings read "2 tablets:" / "2 capsules:" instead of "Per 2 ...:", which brings Lipo-Flow's panel from
   five lines to four) and the dose bars stay level.  Measured in the build's Chromium, print media: see the polish
   round 2b note in the module docstring. */
.sheet.back:has(.flv-back) .col .what{display:flex;flex-direction:column}
.sheet.back:has(.flv-back) .col .key{margin-top:auto}
.sheet.back:has(.flv-back) .life .disc2{width:0.68in;height:0.68in}
.sheet.back:has(.flv-back) .life .disc2 svg{width:0.41in!important;height:0.41in!important}
.sheet.back:has(.flv-back) .band h2{margin-bottom:0.07in}
.sheet.back:has(.flv-back) .ns-title{margin-top:0.1in}
.sheet.back:has(.flv-back) .duo{grid-template-columns:1fr 1.4fr}
.sheet.back:has(.flv-back) .rhythm{grid-template-columns:1.2fr .8fr}
.sheet.back:has(.flv-back) .rhythm .slot:nth-child(3){display:none}
/* The kit's first box is "Morning", but on this plan it also holds the lunch doses (Berberine Pro and Lipo-Flow are
   taken 3 times a day and the kit has no midday box), so on this sheet only it reads "Breakfast and lunch": a patient
   filling a pill organizer by slot must not put the lunch pills in the morning.  font-size:0 hides the kit's text
   node; the sun icon keeps its CSS size.  The first box holds more lines (and says which meal for every product), so
   it gets the wider share of the panel; the shorter evening box still ends above it (measured). */
.flv-nw{white-space:nowrap}
.sheet.back:has(.flv-back) .rhythm .slot:nth-child(1) .when{font-size:0}
.sheet.back:has(.flv-back) .rhythm .slot:nth-child(1) .when::after{content:"Breakfast and lunch";font:800 7pt Inter,sans-serif}
"""

# ============================================================== back page
# Lifestyle: guideline steps [EASL24][AASLD23], plus the protocol's gut-liver angle [CSO26] (gut barrier,
# endotoxins; UltraBiotic Prebiotic on the fatty-liver list, Akkermansia in Asher's 2024 launch blast).
LIFE = [
    # [EASL24]: "improving diet quality (similar to the Mediterranean dietary pattern), limiting the consumption of
    # ultra-processed food (rich in sugars and saturated fat) and avoiding sugar-sweetened beverages"; [AASLD23]:
    # "dietary sugars (eg, fructose, sucrose, and glucose), drive the formation and accumulation of intrahepatic fat"
    ("plate", "Eat Mediterranean",
     "Vegetables, beans, olive oil, nuts and fish. Skip sugary drinks and sweets: sugar easily turns into liver fat."),
    # [EASL24X]: "In adults with MASLD and overweight", weight loss "should aim at a sustained reduction of >=5% to
    # reduce liver fat, 7-10% to improve liver inflammation and >=10% to improve fibrosis".  Lean MASLD is real
    # ([AASLD23]: "the prevalence of NAFLD in lean individuals varies from 4.1% in the United States to as high as
    # 19% in Asia") and EASL gives normal-weight adults diet and exercise instead, so the targets are asked as a
    # question ("Extra weight?") and never told to every reader.  ("Carrying extra weight?" ran this tile to five
    # lines and pushed the footer off the page; measured.)  Polish round 2: every figure carries its % sign, since a
    # bare "7 to 10" reads as pounds (7-10% of 250 lb is 17.5 to 25 lb).  Each clause is one unbreakable span (the
    # en dash is a break point otherwise), so the tile still sets one clause per line in four lines and the band
    # keeps its height (measured, both editions).
    ("scale", "Lose extra weight",
     'Extra weight? Losing <span class="flv-nw">5% cuts liver fat;</span> <span class="flv-nw">7&ndash;10% calms '
     'inflammation;</span> <span class="flv-nw">10% or more eases scarring.</span>'),
    # [EASL24]/[AASLD23]: ">150 min/week of moderate ... physical activity"; 2 strength days [HHS18];
    # 10-minute walks after meals lowered after-meal glucose more than one 30-minute walk [REYNOLDS16]
    ("walk", "Move every day",
     "150 minutes a week of brisk walking plus 2 strength days. A 10-minute walk after meals blunts the sugar spike."),
    # gut barrier and endotoxins [CSO26]; plant polyphenols and fiber as Akkermansia boosters [CSO24];
    # [AASLD23]: gut-microbiome products "may also contribute"
    ("flv-intestine", "Feed your gut",
     "Fiber and colorful plants feed helpful gut bacteria, like Akkermansia, that help keep the gut lining strong."),
    # [EASL24]: people with steatotic liver disease "should be discouraged from consuming alcohol"; "All alcohol
    # consumption should be stopped completely and permanently in individuals with advanced fibrosis or cirrhosis".
    # [AASLD23]: "Moderate alcohol use increases the probability of advanced fibrosis, particularly in patients with
    # obesity or T2DM"; [DELPHI23] names MetALD (MASLD plus greater drinking), so the tile never says alcohol played
    # no part: "even if" leaves room for the reader who drinks.  The title says "or none", matching the crossed-out
    # glass and EASL's "should be discouraged from consuming alcohol" [EASL24X]; "Skip alcohol if you can" wrapped
    # to two lines (measured).
    ("glass", "Less alcohol, or none",
     "Even if alcohol did not cause this, it adds to the liver&rsquo;s load. Less is better; none at all if there is "
     "scarring."),
]

def _claim(text, last):
    """A claim bullet that carries its own drawn FDA diamond (kit.DIAMOND), its last word and the diamond held
    together.  The diamond is an inline SVG and a line may always break before one, even after &nbsp;, so build.py's
    own mark wrapped onto a line by itself after "Supports healthy fat metabolism".  build.py adds no marks to a
    column whose bullets already carry one, so every bullet in such a column goes through here."""
    return f'{text} <span class="flv-nw">{last}&nbsp;<span class="mark">{kit.DIAMOND}</span></span>'


# Need headers say BLOOD sugar and BLOOD fats, liver and bile, and antioxidant support, so that on a page about liver
# fat and liver damage no header reads as "removes liver fat" or "protects against the disease" (implied disease
# claims).  Each fits the header bar on one line (measured), so all four bars stay 0.5 in and the photos line up.
COLS = [
    # [CSO26]; label [LABELS] ND1130 via products.d (fl_berberine).  The first driver on the front is insulin
    # resistance, and berberine is the competitor's first nutrient, so this is the one to start with.
    {"p": "fl_berberine", "need": "Steady blood sugar, blood fats", "needsub": "berberine (as dihydroberberine)",
     "start": True,
     "bullets": ["Supports healthy glucose&nbsp;metabolism", "Supports lipid levels already in a normal range"],
     "dose": "dose_from_db"},
    # NutriDyn science-team lipotropic; 400 mg artichoke + tangerine peel = the competitor's bergamot + artichoke.
    # On a page that defines the disease as fat stored in liver cells, "help the liver process fat" and "fat
    # metabolism in the liver" read as "clears the fat out of a fatty liver" (an implied disease claim, 21 CFR
    # 101.93(g)(2)), so the header names the liver and bile, and bullet 1 is ND606's own headline claim ("Support for
    # Healthy Fat Metabolism") without "in the liver".
    {"p": "fl_lipo_flow", "need": "Liver and bile support", "needsub": "artichoke, citrus peel, inositol",
     "bullets": [_claim("Supports healthy", "fat metabolism"), _claim("Supports healthy bile", "flow")],
     "dose": "dose_from_db"},
    # [CSO26]; antioxidant liver-cell support, the stand-in for the competitor's aged black garlic.
    # Claims stay structure/function: [AASLD23] calls silymarin's effect in NASH "inconclusive".  Both bullets are
    # the sell sheet's own claims ("Promote healthy liver function"; "promoting the liver's natural detoxification
    # processes") and start with a verb, so build.py ties each to the FDA line with the diamond.  The header carries
    # the antioxidant idea, so the first bullet does not repeat it.
    {"p": "fl_milk_thistle", "need": "Antioxidant liver support", "needsub": "milk thistle (silymarin), NAC",
     "bullets": ["Promotes healthy liver function", "Supports the liver&rsquo;s natural detox&nbsp;processes"],
     "dose": "dose_from_db"},
    # Cellular Energy (R145): 150 mg alpha-lipoic acid per 2 capsules = the competitor's ALA [ND325].  The GLC 2026
    # list's Mito Recharge [CSO26] sat here until the swap pass (2026-11-04): its 100 mg EGCG from green tea extract
    # meets USP's "Do not use if you have a liver problem" [USP20].  Both bullets are ND325's own claims ("Supports
    # energy production"; "Provides antioxidant support throughout the body", trimmed for space) and start with a
    # verb, so build.py ties each to the FDA line with the diamond.  The header keeps the cell-energy idea.  The sub
    # spells alpha-lipoic acid as the serving line and ND325 do; the no-break hyphen becomes a plain hyphen inside a
    # nowrap span (kit.print_safe), and the sub still sets on one line (measured, polish round 2b).
    {"p": "fl_cellular_energy", "need": "Help cells make energy", "needsub": "alpha&#8209;lipoic acid, CoQ10, NAC",
     "bullets": ["Supports energy production", "Provides antioxidant support"],
     "dose": "dose_from_db"},
]

# The CSS hides the rhythm's Bedtime box (the kit draws Morning, Evening meal, Bedtime in that order).  That is only
# right while no product on this page has a bedtime dose, so the build stops if one ever does.
_PRODUCTS_D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "products.d", "fatty-liver.json")
with open(_PRODUCTS_D) as _f:
    _OWN = json.load(_f)
assert all(slot != "bed" for c in COLS for slot, _n, _u in c.get("sched", _OWN[c["p"]]["sched"])), \
    "fatty-liver: a bedtime dose exists, so drop the .rhythm .slot:nth-child(3) rule in CSS"

# Medicine-and-nutrient checks for this page's own products.  Pharmacists check interactions and depletions;
# the doctor who prescribes a medicine is the one who adjusts it (a DC or ND handing out the practitioner edition
# usually does not manage diabetes medicines or warfarin, and a pharmacist does not either).  Four checks since the
# swap pass (2026-11-04): the green tea extract check, its written-yes gate and the rhythm note that repeated the
# gate left with Mito Recharge (Cellular Energy has no green tea [ND325]).
#  - berberine lowers blood sugar [ZHANG08]: a plain caution ("may lower blood sugar along with them"), never a
#    claim that the product boosts the drug.  Cellular Energy's 150 mg alpha-lipoic acid lowers it too, but less
#    [ALA], hence "(and, more mildly, the alpha-lipoic acid in Cellular Energy)" (polish round 2b).  Its CoQ10 has a
#    similar small effect [ALA]; "and CoQ10" ran the practitioner bullet to four lines and closed the gap above the
#    footer (measured), and both editions already send the reader to the prescriber before starting either product.
#  - berberine slowed CYP2D6, 2C9 and 3A4 in people (300 mg three times daily for 2 weeks) [GUO12]; "can slow"
#    because Berberine Pro gives 300 mg dihydroberberine a day, not the study's form and dose.  Warfarin is cleared
#    mainly by CYP2C9 (S-warfarin) and partly by CYP3A4 [KAMINSKY97], so the list names warfarin next to the statins
#    and both editions keep the INR (a clotting test) recheck.  Mito Recharge's vitamin K1 sentence left with it in
#    the swap pass, but the vitamin-K-type warfarin concern did not: Cellular Energy's 200 mg CoQ10 is chemically
#    similar to vitamin K, and CoQ10 has been tied to a weaker warfarin response and to more bleeding on warfarin
#    [COQ10], so the same bullet says "the CoQ10 in Cellular Energy may change how warfarin works" (polish round 2b).
#    CYP450 is never called "liver enzymes" on this sheet: here that phrase means the ALT/AST blood test, as on the
#    front.
#  - statins: simvastatin, lovastatin and atorvastatin are cleared by CYP3A4 [STATINS], which berberine can slow
#    [GUO12]; statins are first-line for blood fats in NAFLD [AASLD23].  (Polish round 1 cut a line about statins and
#    CoQ10: it had no action and read as a product making up for the drug.  The CoQ10 clause now in the medicines
#    check is the warfarin caution above, a different thing.)
#  - practitioner edition: both drug lines say "tell the doctor who prescribes them / who manages your warfarin before
#    you start" (polish round 2b), because that doctor can only adjust doses or recheck the INR if told.
#  - pregnancy: all four labels say "If you are pregnant, nursing, or taking medication, consult your healthcare
#    practitioner before use" [LABELS] (Cellular Energy too [ND325]); Berberine Pro is singled out to skip; PCOS is on
#    the front's risk list.
#  - gallstones, a blocked bile duct, or a daisy-family allergy (polish round 2): Lipo-Flow "provides choleretic and
#    cholagogue gastrointestinal agents", and "Cholagogue agents promote the healthy flow of bile from the liver and
#    gall bladder" [ND606]; "artichoke products should not be used by individuals with bile duct obstruction,
#    including those with gallstones" [SILVA25] (Lipo-Flow has 400 mg artichoke, Milk Thistle Complex 25 mg).
#    Milk thistle, artichoke and dandelion are daisy-family (Asteraceae) plants, and with milk thistle "caution is
#    advised in patients with a known sensitivity to plants in the Asteraceae/Compositae family (members of this
#    family include chrysanthemums, daisies, marigolds and ragweed)" [GILLESSEN20].  This reader is in the
#    high-gallstone group and is told to lose weight.  The guidance wants a doctor first with gallstones and a DC,
#    ND or pharmacist does not manage them, so both editions add "or your doctor", as the mold sheet's Lipo-Flow line
#    does.  Two lines in both editions (measured); "or allergic to ragweed or daisies" ran the pharmacy line to three.
# Fit since polish round 2b, measured in the build's Chromium (print media), both editions: the checks set in 3, 5, 2
# and 2 lines, no bullet ends on one word, and the page-2 footer keeps 12.2 px clear (13.5 before the two longer lines).
RX = {
    "pharmacy": [
        # &nbsp; joins keep each bullet from ending on a single word (checked in both editions).  [ZHANG08] [ALA]
        # "Cellular&nbsp;Energy" keeps the product name on one line here; the practitioner bullet cannot take that join
        # (it runs to four lines and closes the gap above the footer, measured).  alpha&#8209;lipoic: the kit turns the
        # no-break hyphen into a plain hyphen inside a nowrap span, so the word never splits at its hyphen.
        "<b>Diabetes medicines:</b> Berberine Pro (and, more mildly, the alpha&#8209;lipoic acid in Cellular&nbsp;Energy) "
        "may lower blood sugar along with them. Ask your doctor before you start, and check your blood sugar "
        "more&nbsp;often.",
        # One bullet for every enzyme interaction, statins first in the bold lead-in so a statin user finds it: a
        # separate "Statins:" bullet repeated "Berberine Pro can slow the enzyme" and pushed the footer off the page
        # (measured then: 6 lines for the two bullets against 5 for this one).  Polish round 2b adds Cellular Energy's
        # CoQ10, which may weaken warfarin or go with more bleeding on it [COQ10], so a warfarin user who takes Cellular
        # Energy without Berberine Pro is warned too: five lines in both editions.  "(a&nbsp;clotting" keeps "(a" off
        # the end of line four.  [GUO12] [STATINS] [KAMINSKY97] [COQ10]
        "<b>Statins, warfarin and other medicines:</b> Berberine Pro can slow the enzymes that clear some drugs "
        "(CYP2D6, 2C9, 3A4), including warfarin, simvastatin, lovastatin and atorvastatin, and the CoQ10 in Cellular "
        "Energy may change how warfarin works. Show {who} your full medicine list; your doctor may recheck your INR "
        "(a&nbsp;clotting test) after you&nbsp;start.",
        "<b>Pregnant, planning to be, or nursing?</b> Ask {who} before taking any of these, and skip Berberine Pro "
        "unless your doctor says&nbsp;otherwise.",
        # [ND606] [SILVA25] [GILLESSEN20]: see the gallstone note above the RX
        "<b>Gallstones, a blocked bile duct, or a ragweed or daisy allergy?</b> Ask {who} or your doctor before "
        "Lipo-Flow (it&nbsp;boosts bile flow) and Milk Thistle Complex.",
    ],
    "practitioner": [
        # A DC or ND handing out this edition does not manage diabetes medicines or warfarin, and the doctor who does
        # can only act if told, so both lines tell the reader to tell that doctor first (polish round 2b).  [ZHANG08]
        # [ALA]
        "<b>Diabetes medicines:</b> Berberine Pro (and, more mildly, the alpha&#8209;lipoic acid in Cellular Energy) "
        "may lower blood sugar along with them. Tell the doctor who prescribes them before you start; they may check "
        "your blood sugar more often and adjust&nbsp;doses.",
        # [GUO12] [STATINS] [KAMINSKY97] [COQ10]
        "<b>Statins, warfarin and other medicines:</b> Berberine Pro can slow the enzymes that clear some drugs "
        "(CYP2D6, 2C9, 3A4), including warfarin, simvastatin, lovastatin and atorvastatin, and the CoQ10 in Cellular "
        "Energy may change how warfarin works. Show {who} your full medicine list, and tell the doctor who manages "
        "your warfarin before you start; they may recheck your INR (a clotting&nbsp;test).",
        "<b>Pregnant, planning to be, or nursing?</b> Ask {who} before taking any of these, and skip Berberine Pro "
        "unless they say&nbsp;otherwise.",
        # [ND606] [SILVA25] [GILLESSEN20]: see the gallstone note above the RX
        "<b>Gallstones, a blocked bile duct, or a ragweed or daisy allergy?</b> Ask {who} or your doctor before "
        "Lipo-Flow (it&nbsp;boosts bile flow) and Milk Thistle Complex.",
    ],
}

SHEET = {
    "slug": "fatty-liver", "code": "ND-CM-201", "theme": "metab", "series": "Metabolic Health Series",
    "order": 4,
    "title": "Fatty Liver Disease", "sub": "MASLD, the condition formerly called NAFLD",
    # Renamed MASLD in June 2023 [DELPHI23].  "About 1 in 3 adults": US 31.9% [NHANES25], global 30%,
    # 38% in 2016-2019 [YOUNOSSI23] (AASLD 2023 gives 25-30% [AASLD23]).  Usually silent [AASLD23].
    # "Most common liver condition": "MASLD has become the most common chronic liver disease" [EASL24].
    # Often reversible: "weight loss of 3%-5% improves steatosis ... (>10%) ... NASH and fibrosis" [AASLD23].
    # "This kind": MASLD is the fatty liver that heavy drinking does not cause, but alcohol-related fatty liver and
    # MetALD (MASLD plus greater drinking) sit in the same 2023 scheme [DELPHI23], and moderate drinking raises the
    # odds of advanced fibrosis [AASLD23], so the intro never says alcohol plays no part.
    # MASLD is spelled out at its first use in the intro (the sub-head is a title line, the intro glosses it next).
    "intro": ("Fatty liver disease means extra fat is stored inside liver cells. In 2023, liver specialists named the "
              "most common kind <b>MASLD</b> (metabolic dysfunction-associated steatotic liver disease) because it goes "
              "hand in hand with insulin resistance, belly fat, high triglycerides and high blood pressure. This kind is "
              "<b>not caused by heavy drinking</b>. It is the most common liver condition in the world, affecting about "
              "<b>1 in 3 adults</b>, and most people feel nothing. Caught early, it is often reversible."),
    "front": front,
    "css": CSS,
    "back": {
        # the span marks this sheet's back page for the scoped CSS (.sheet.back:has(.flv-back))
        "life_title": 'Lifestyle Recommendations<span class="flv-back"></span>', "style": "circle",
        "life": LIFE,
        "cols": COLS,
        "rx": RX,
    },
}
