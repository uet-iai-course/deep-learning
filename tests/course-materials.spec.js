const { test, expect } = require('@playwright/test');

const lectures = [
  ['01', 'lecture-01-gioi-thieu-hoc-sau-va-mlp.html'],
  ['02', 'lecture-02-lan-truyen-va-do-thi-tinh-toan.html'],
  ['03', 'lecture-03-toi-uu-hoa-mang-no-ron-da-lop.html'],
  ['04', 'lecture-04-mang-no-ron-tich-chap.html'],
  ['05', 'lecture-05-cac-kien-truc-cnn-hien-dai.html'],
  ['06', 'lecture-06-hoc-bieu-dien-va-autoencoders.html'],
  ['07', 'lecture-07-mang-no-ron-hoi-quy.html'],
  ['08', 'lecture-08-cac-kien-truc-rnn-hien-dai-lstm-gru.html'],
  ['10', 'lecture-10-co-che-chu-y.html'],
  ['11', 'lecture-11-kien-truc-transformer.html'],
  ['12', 'lecture-12-transformer-nang-cao.html'],
  ['13', 'lecture-13-hoc-tang-cuong-va-hoc-bat-chuoc.html'],
  ['14', 'lecture-14-sieu-hoc-tap.html'],
];

function collectRuntimeErrors(page) {
  const errors = [];
  page.on('pageerror', error => errors.push(`pageerror: ${error.message}`));
  page.on('console', message => {
    if (message.type() === 'error') errors.push(`console: ${message.text()}`);
  });
  page.on('requestfailed', request => {
    errors.push(`request: ${request.url()} (${request.failure()?.errorText || 'unknown'})`);
  });
  return errors;
}

async function inspectDeck(browser, deck, viewport) {
  const context = await browser.newContext({ viewport });
  const page = await context.newPage();
  const runtimeErrors = collectRuntimeErrors(page);
  const response = await page.goto(`/2627-1/${deck}`, { waitUntil: 'networkidle' });
  expect(response?.ok()).toBeTruthy();
  await page.waitForFunction(() => window.Reveal && Reveal.isReady());

  const result = await page.evaluate(async () => {
    const slides = Reveal.getSlides();
    const overflow = [];
    for (const slide of slides) {
      const indices = Reveal.getIndices(slide);
      Reveal.slide(indices.h, indices.v);
      slide.querySelectorAll('.fragment').forEach(fragment => fragment.classList.add('visible'));
      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      const slideBox = slide.getBoundingClientRect();
      const offenders = [];
      for (const element of slide.querySelectorAll(':scope > *:not(aside)')) {
        const style = getComputedStyle(element);
        if (style.display === 'none' || style.visibility === 'hidden') continue;
        const box = element.getBoundingClientRect();
        if (
          box.left < slideBox.left - 3 || box.right > slideBox.right + 3 ||
          box.top < slideBox.top - 3 || box.bottom > slideBox.bottom + 3
        ) {
          offenders.push(`${element.tagName}.${element.className || ''}`);
        }
      }
      if (offenders.length) overflow.push(`${slide.dataset.slideId}: ${offenders.join(', ')}`);
    }
    return {
      slideCount: slides.length,
      noteCount: document.querySelectorAll('aside.notes').length,
      ids: slides.map(slide => slide.dataset.slideId),
      katexCount: document.querySelectorAll('.katex').length,
      katexErrors: document.querySelectorAll('.katex-error').length,
      brokenImages: [...document.images]
        .filter(image => !image.complete || image.naturalWidth === 0)
        .map(image => image.getAttribute('src')),
      overflow,
    };
  });

  expect(result.slideCount).toBeGreaterThan(0);
  expect(result.noteCount).toBe(result.slideCount);
  expect(new Set(result.ids).size).toBe(result.ids.length);
  expect(result.katexCount).toBeGreaterThan(0);
  expect(result.katexErrors).toBe(0);
  expect(result.brokenImages).toEqual([]);
  expect(result.overflow).toEqual([]);
  expect(runtimeErrors).toEqual([]);

  const navigation = await page.evaluate(() => {
    const firstStack = document.querySelector('.slides > section');
    const firstSlide = firstStack?.querySelector(':scope > section');
    const verticalSlides = [...(firstStack?.querySelectorAll(':scope > section') || [])];
    const nextStackSlide = document.querySelector('.slides > section:nth-of-type(2) > section');
    return {
      first: firstSlide?.dataset.slideId,
      second: verticalSlides[1]?.dataset.slideId,
      lastVertical: verticalSlides.length - 1,
      nextStack: nextStackSlide?.dataset.slideId,
    };
  });
  expect(navigation.first).toBeTruthy();
  expect(navigation.second).toBeTruthy();
  expect(navigation.nextStack).toBeTruthy();
  await page.evaluate(() => Reveal.slide(0, 0));
  await page.keyboard.press('ArrowDown');
  await expect.poll(() => page.evaluate(() => Reveal.getCurrentSlide()?.dataset.slideId)).toBe(navigation.second);
  await page.evaluate(lastVertical => {
    Reveal.slide(0, lastVertical);
    Reveal.getCurrentSlide()?.querySelectorAll('.fragment').forEach(fragment => fragment.classList.add('visible'));
    Reveal.sync();
  }, navigation.lastVertical);
  await page.keyboard.press('ArrowRight');
  await expect.poll(() => page.evaluate(() => Reveal.getCurrentSlide()?.dataset.slideId)).toBe(navigation.nextStack);
  await context.close();
}

async function loadAllImages(page) {
  await page.evaluate(async () => {
    for (const image of document.images) {
      image.loading = 'eager';
      image.scrollIntoView({ block: 'center' });
      await new Promise(resolve => setTimeout(resolve, 20));
    }
    await new Promise(resolve => setTimeout(resolve, 250));
    window.scrollTo(0, 0);
  });
}

async function inspectNote(browser, number, deck, viewport, printCheck) {
  const context = await browser.newContext({ viewport });
  const page = await context.newPage();
  const runtimeErrors = collectRuntimeErrors(page);
  const query = new URLSearchParams({
    doc: `materials/lec-${number}/lecture-note.md`,
    deck,
  });
  const response = await page.goto(`/2627-1/material-viewer.html?${query}`, { waitUntil: 'networkidle' });
  expect(response?.ok()).toBeTruthy();
  await page.waitForFunction(() => {
    const layout = document.querySelector('#material-layout');
    return layout && !layout.hidden;
  });
  await loadAllImages(page);

  const result = await page.evaluate(() => ({
    title: document.querySelector('#material-title')?.textContent.trim(),
    statusHidden: document.querySelector('#material-status')?.hidden,
    katexCount: document.querySelectorAll('.katex').length,
    katexErrors: document.querySelectorAll('.katex-error').length,
    brokenImages: [...document.querySelectorAll('#material-content img')]
      .filter(image => !image.complete || image.naturalWidth === 0)
      .map(image => image.getAttribute('src')),
    horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 2,
  }));

  expect(result.title).toBeTruthy();
  expect(result.statusHidden).toBeTruthy();
  expect(result.katexCount).toBeGreaterThan(0);
  expect(result.katexErrors).toBe(0);
  expect(result.brokenImages).toEqual([]);
  expect(result.horizontalOverflow).toBeFalsy();
  expect(runtimeErrors).toEqual([]);

  const firstDetails = page.locator('#material-content details').first();
  if (await firstDetails.count()) {
    const summary = firstDetails.locator('summary');
    await summary.focus();
    await page.keyboard.press('Enter');
    await expect(firstDetails).toHaveAttribute('open', '');
    await page.keyboard.press('Enter');
    await expect(firstDetails).not.toHaveAttribute('open', '');
  }

  if (printCheck) {
    const closedDetails = await page.locator('#material-content details:not([open])').count();
    await page.evaluate(() => window.dispatchEvent(new Event('beforeprint')));
    await expect(page.locator('#material-content details:not([open])')).toHaveCount(0);
    await page.evaluate(() => window.dispatchEvent(new Event('afterprint')));
    await expect(page.locator('#material-content details:not([open])')).toHaveCount(closedDetails);
    const pdf = await page.pdf({ format: 'A4', printBackground: true });
    expect(pdf.byteLength).toBeGreaterThan(10_000);
  }
  await context.close();
}

test.describe('Bộ trang chiếu RevealJS', () => {
  for (const [number, deck] of lectures) {
    test(`Bài ${number} dựng đúng ở hai khung nhìn`, async ({ browser }) => {
      await inspectDeck(browser, deck, { width: 1280, height: 720 });
      await inspectDeck(browser, deck, { width: 800, height: 600 });
    });
  }
});

test.describe('Lecture-note viewer', () => {
  for (const [number, deck] of lectures) {
    test(`Bài ${number} đọc được, đáp ứng màn hình hẹp và in được`, async ({ browser }) => {
      await inspectNote(browser, number, deck, { width: 1280, height: 720 }, true);
      await inspectNote(browser, number, deck, { width: 390, height: 844 }, false);
    });
  }

  test('chặn đường dẫn ngoài allowlist và cặp note/deck lệch bài', async ({ page }) => {
    for (const query of [
      'doc=../.env&deck=lecture-01-gioi-thieu-hoc-sau-va-mlp.html',
      'doc=materials/lec-01/lecture-note.md&deck=lecture-02-lan-truyen-va-do-thi-tinh-toan.html',
    ]) {
      await page.goto(`/2627-1/material-viewer.html?${query}`);
      await expect(page.locator('#material-status')).toContainText('Không thể mở tài liệu');
      await expect(page.locator('#material-layout')).toBeHidden();
    }
  });
});
