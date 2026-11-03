// Render condition sheets to Letter PDFs + previews + thumbnails with the
// pre-installed Playwright Chromium.  Usage: node render.js <job.json>
// job = {items:[{html,pdf,preview,thumb}], bundles:[{html,pdf}]}
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

(async () => {
  const job = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  for (const it of job.items) {
    await page.goto('file://' + it.html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(250);
    fs.mkdirSync(path.dirname(it.preview), { recursive: true });
    const sheets = await page.$$('.sheet');
    for (let i = 0; i < sheets.length; i++) {
      const png = `${it.preview}-${i + 1}.png`;
      await sheets[i].screenshot({ path: png });
      if (it.thumb) execFileSync('convert', [png, '-resize', '360x', '-quality', '82', `${it.thumb}-${i + 1}.jpg`]);
    }
    await page.emulateMedia({ media: 'print' });
    await page.pdf({ path: it.pdf, preferCSSPageSize: true, printBackground: true });
    await page.emulateMedia({ media: 'screen' });
    console.log('rendered', path.basename(it.pdf), sheets.length, 'pages');
  }
  for (const b of job.bundles || []) {
    await page.goto('file://' + b.html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.emulateMedia({ media: 'print' });
    await page.pdf({ path: b.pdf, preferCSSPageSize: true, printBackground: true });
    console.log('rendered bundle', b.pdf);
  }
  await browser.close();
})();
