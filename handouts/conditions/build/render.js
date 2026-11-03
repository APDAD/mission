// Render the condition sheets to Letter PDFs + preview images with the
// pre-installed Playwright Chromium.  Usage: node render.js <OUT> [<TMP>]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

(async () => {
  const OUT = process.argv[2];
  const TMP = process.argv[3] || path.join(__dirname);
  const slugs = fs.readdirSync(OUT).filter(f => f.endsWith('.html') && f !== 'index.html').map(f => f.replace('.html', ''));
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  fs.mkdirSync(path.join(TMP, 'preview'), { recursive: true });
  for (const slug of slugs) {
    await page.goto('file://' + path.join(OUT, slug + '.html'), { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    const sheets = await page.$$('.sheet');
    for (let i = 0; i < sheets.length; i++) {
      const png = path.join(TMP, 'preview', `${slug}-${i + 1}.png`);
      await sheets[i].screenshot({ path: png });
      execFileSync('convert', [png, '-resize', '360x', '-quality', '82', path.join(OUT, 'img', `thumb-${slug}-${i + 1}.jpg`)]);
    }
    await page.emulateMedia({ media: 'print' });
    await page.pdf({ path: path.join(OUT, slug + '.pdf'), preferCSSPageSize: true, printBackground: true });
    await page.emulateMedia({ media: 'screen' });
    console.log('rendered', slug, sheets.length, 'pages');
  }
  const all = path.join(TMP, '_all.html');
  if (fs.existsSync(all)) {
    await page.goto('file://' + all, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.emulateMedia({ media: 'print' });
    await page.pdf({ path: path.join(OUT, 'all-condition-sheets.pdf'), preferCSSPageSize: true, printBackground: true });
    console.log('rendered all-condition-sheets.pdf');
  }
  await browser.close();
})();
