import { test, expect } from '@playwright/test';

const UI_URL = 'https://flights-app.pages.dev/'

test('Test if user can write the same value to From and To inputs', async ({ page }) => {
  await page.goto(UI_URL);

  await page.getByRole('combobox', { name: 'From:' }).fill('IST');
  await page.getByRole('option', { name: 'Istanbul IST' }).click();

  await page.getByRole('combobox', { name: 'To:' }).fill('IST');
  await expect(page.getByRole('option')).toHaveCount(0, {"timeout": 5});
});

test('Test that there are no flights between the two locations', async ({ page }) => {
  await page.goto(UI_URL);

  await page.getByRole('combobox', { name: 'From:' }).fill('IST');
  await page.getByRole('option', { name: 'Istanbul IST' }).click();

  await page.getByRole('combobox', { name: 'To:' }).fill('JFK');
  await page.getByRole('option', { name: 'New York JFK' }).click();

  await expect(page.getByText('Found')).toHaveCount(0, {"timeout": 5});
})

test('Test that the number X in "Found X items" is the same as the number of flights list', async ({ page }) => {
  await page.goto(UI_URL);

  await page.getByRole('combobox', { name: 'From:' }).fill('Istanbul');
  await page.getByRole('option', { name: 'Istanbul IST' }).click();

  await page.getByRole('combobox', { name: 'To:' }).fill('LAX');
  await page.getByRole('option', { name: 'Los Angeles LAX' }).click();

  page.getByText('Found').innerText().then((innerText) => {
    var arr = innerText.split(" ");
    var count = parseInt(arr[1]);
    expect(page.getByRole('listitem')).toHaveCount(count);
  });

});
