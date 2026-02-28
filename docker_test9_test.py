import os
import pytest
from playwright.async_api import async_playwright

BASE_URL = "https://news.ycombinator.com/"

@pytest.fixture
async def page():
    import os
    playwright = await async_playwright().start()
    headless_mode = os.environ.get("DOCKER", "0") == "1"
    browser = await playwright.chromium.launch(headless=headless_mode)
    page = await browser.new_page()
    await page.goto(BASE_URL)
    yield page
    await browser.close()
    await playwright.stop()
    
# TC09 -  Final Test: Verify that Hacker News articles exist on the front page by checking for '.athing' elements (each article row)
@pytest.mark.asyncio
async def test_article_rows_screenshots(page):
    articles = await page.locator(".athing").all()
    print(f"Found {len(articles)} article rows")

    os.makedirs("screenshots", exist_ok=True)

    for idx, article in enumerate(articles, start=1):
        filename = f"screenshots/article_{idx}.png"
        await article.screenshot(path=filename)
        print(f"Saved screenshot: {filename}")


    assert len(articles) > 0
