import warnings
warnings.filterwarnings("ignore", category=ResourceWarning)

import re
import pytest
from playwright.async_api import async_playwright

BASE_URL = "https://news.ycombinator.com/"

# Utility function to launch the browser and page
async def launch_page():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch()
    page = await browser.new_page()
    await page.goto(BASE_URL)
    return playwright, browser, page

@pytest.mark.asyncio
async def test_page_title():
    playwright, browser, page = await launch_page()
    try:
        assert "Hacker News" in await page.title()
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_new_tab_navigation():
    playwright, browser, page = await launch_page()
    try:
        await page.get_by_role("link", name="new", exact=True).click()
        await page.wait_for_url("**/newest")
        assert "new links" in (await page.title()).lower()
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_login_link():
    playwright, browser, page = await launch_page()
    try:
        login_link = page.get_by_text("login")
        await login_link.click()
        # Add assertions if needed
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_article_ranks_present():
    playwright, browser, page = await launch_page()
    try:
        ranks = await page.locator(".rank").all()
        assert len(ranks) > 0
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_article_scores():
    playwright, browser, page = await launch_page()
    try:
        scores = await page.locator(".score").all()
        assert len(scores) > 0
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_comment_links():
    playwright, browser, page = await launch_page()
    try:
        comment_links = await page.locator("a:has-text('comments')").all()
        assert len(comment_links) > 0
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_logo_visible():
    playwright, browser, page = await launch_page()
    try:
        logo = page.get_by_role("link", name="Hacker News")
        visible = await logo.is_visible()
        assert visible
    finally:
        await browser.close()
        await playwright.stop()

@pytest.mark.asyncio
async def test_past_link_navigation():
    playwright, browser, page = await launch_page()
    try:
        await page.get_by_role("link", name="past").click()
        await page.wait_for_url("**/front")
        assert "Hacker News" in await page.title()
    finally:
        await browser.close()
        await playwright.stop()
