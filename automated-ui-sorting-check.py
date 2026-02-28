import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)


import pytest
from playwright.async_api import async_playwright

BASE_URL = "https://news.ycombinator.com/"

# Utility function to launch the browser and page in headed mode
async def launch_page(headless=False):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=headless)
    page = await browser.new_page()
    await page.goto(BASE_URL)
    return playwright, browser, page

@pytest.mark.asyncio
async def test_page_title():
    playwright, browser, page = await launch_page(headless=False)
    try:
        assert "Hacker News" in await page.title()
        await page.wait_for_timeout(2000)  # pause 2 seconds to see result
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_new_tab_navigation():
    playwright, browser, page = await launch_page(headless=False)
    try:
        await page.get_by_role("link", name="new", exact=True).click()
        await page.wait_for_url("**/newest")
        assert "new links" in (await page.title()).lower()
        await page.wait_for_timeout(2000)
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_login_link():
    playwright, browser, page = await launch_page(headless=False)
    try:
        login_link = page.get_by_text("login")
        await login_link.click()
        await page.wait_for_timeout(2000)
        # Add assertions if needed
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_article_ranks_present():
    playwright, browser, page = await launch_page(headless=False)
    try:
        ranks = await page.locator(".rank").all()
        assert len(ranks) > 0
        await page.wait_for_timeout(2000)
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_article_scores():
    playwright, browser, page = await launch_page(headless=False)
    try:
        scores = await page.locator(".score").all()
        assert len(scores) > 0
        await page.wait_for_timeout(2000)
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_comment_links():
    playwright, browser, page = await launch_page(headless=False)
    try:
        comment_links = await page.locator("a:has-text('comments')").all()
        assert len(comment_links) > 0
        await page.wait_for_timeout(2000)
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_logo_visible():
    playwright, browser, page = await launch_page(headless=False)
    try:
        logo = page.get_by_role("link", name="Hacker News")
        visible = await logo.is_visible()
        assert visible
        await page.wait_for_timeout(2000)
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_past_link_navigation():
    playwright, browser, page = await launch_page(headless=False)
    try:
        await page.get_by_role("link", name="past").click()
        await page.wait_for_url("**/front")
        assert "Hacker News" in await page.title()
        await page.wait_for_timeout(2000)
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_article_rows():
    playwright, browser, page = await launch_page(headless=False)
    try:
        articles = await page.locator(".athing").all()
        assert len(articles) > 0, "No article rows found."
        # Optional: take screenshot for each article
        for idx, article in enumerate(articles, start=1):
            await article.screenshot(path=f"screenshots/article_{idx}.png")
        await page.wait_for_timeout(2000)
    finally:
        await browser.close()
        await playwright.stop()
