const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  fullyParallel: false,
  workers: 1,
  timeout: 45_000,
  expect: { timeout: 8_000 },
  reporter: [
    ['line'],
    ['html', { outputFolder: 'playwright-report', open: 'never' }],
  ],
  use: {
    baseURL: 'http://127.0.0.1:8765',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
    video: 'off',
  },
  webServer: {
    command: 'python3 -m http.server 8765 --bind 127.0.0.1 >/dev/null 2>&1',
    url: 'http://127.0.0.1:8765/2627-1/index.html',
    reuseExistingServer: !process.env.CI,
    timeout: 15_000,
  },
});
