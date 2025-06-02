# Hacker News UI Test Automation

This project is a UI test suite for [Hacker News](https://news.ycombinator.com/) using Python, Pytest, and Playwright. It validates key functionality and UI elements such as article scores, login links, navigation tabs, and comments.

# Tech Stack

- Python 3.11+
- Playwright (async API)
- Pytest

#  Setup

1. **Clone the repository**

   git clone https://github.com/yourusername/hacker-news-ui-tests.git
   cd hacker-news-ui-tests
---

Install dependencies

pip install -r requirements.txt
playwright install
---
Run tests

python cli.py

#  Test Coverage - Test Number, Name, Description

Test #1. test_page_title	Checks if the page title contains "Hacker News"

Test #2. test_new_tab_navigation	Verifies the "new" tab navigates properly

Test #3. test_login_link	Asserts the login link is functional

Test #4. test_article_ranks_present	Validates that article ranks are visible

Test #5. test_article_scores	Confirms article scores are present

Test #6. test_comment_links	Ensures comment links exist

Test #7. test_logo_visible	Checks visibility of the Hacker News logo

Test #8. test_past_link_navigation	Tests that the "past" link works correctly

# Notes
Test warnings are suppressed using warnings.filterwarnings.

All browser instances are properly closed using try/finally blocks.

# License
MIT License
This project is released under the MIT License, which permits unrestricted use, modification, and distribution of the software, provided that the original copyright notice and permission notice are included in all copies or substantial portions of the software. For complete terms, refer to the LICENSE file.

---

#  3. Documentation
A docs/ directory has been added to organize extended documentation. The main file is:

## docs/
   └── usage.md   # Contains detailed usage instructions and test descriptions

# How to Use Project

## 1. Running Tests via CLI

Run all UI tests:

python cli.py

## 2. Adding a New Test
Open automated-ui-sorting-check.py.

Add a new @pytest.mark.asyncio function using the Playwright API.

Use try/finally to ensure proper browser shutdown.

## 3. Example Test

@pytest.mark.asyncio
async def test_example():
    playwright, browser, page = await launch_page()
    try:
        assert await page.title() == "Expected Title"
    finally:
        await browser.close()
        await playwright.stop()

---










