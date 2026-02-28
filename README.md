# Playwright UI Tests – Hacker News

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Pytest](https://img.shields.io/badge/pytest-passing-brightgreen)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Project Overview
This project contains a set of automated UI tests for [Hacker News](https://news.ycombinator.com/) built using **Python** and **Playwright**.  

* Validates key page elements such as article rows, ranks, titles, and comment links.

* Includes Test 9, which verifies all .athing article rows and can generate visual screenshots for each row.

* Tests can run locally in headed mode for visual verification or in Docker in headless mode for CI/CD environments.

This project demonstrates professional QA practices including:

* Async test execution using `pytest-asyncio`

* Headless browser testing for CI/CD integration

* Screenshot capture for visual validation

* Dockerized test execution for reproducible environments

### Features / Tests
| Test #   | Description |
|----------|-------------|
| 1-8<br/> |Validate page title, navigation links, login link, article ranks, scores, comment links, logo visibility, past link navigation             |
| 9<br/>        |Verify all .athing rows exist, optionally capture screenshots of each article row             |

*Screenshots for Test 9 are saved in screenshots/ and automatically generated in Docker or local runs.*



### Requirements

* Python 3.10+

* Playwright

* Pytest

* Pytest-asyncio

Install dependencies: 

`pip install -r requirements.txt`

### Running Tests Locally

1. Navigate to project root:
`cd C:\Users\Yourusername\PycharmProjects\PlaywrightUITests`


2. Run all tests with visual browser (headed mode):
`pytest -s`


3. Run only Test 9:
`pytest -s docker_test9_test.py`

### Dockerized Test Execution
1. Build Docker Image

`docker build -t playwright-ui-tests .`

2. Run Test 9 in Docker:
`docker run --rm -e DOCKER=1 -v ${PWD}:/app playwright-ui-tests pytest -s docker_test9_test.py
`
* `-e DOCKER=1` → runs browser in headless mode

* `-v ${PWD}:/app `→ mounts project folder so screenshots are saved locally

3. Screenshots will be in:

`screenshots/article_1.png`

`screenshots/article_2.png`

`…`

Should be seen in generated directory with a folder structure as seen below.

````
screenshots/
├─ article_1.png
├─ article_2.png
├─ article_3.png
...
├─ article_30.png

````

### Example Screenshot
![Article 1 Screenshot](screenshots/article_1.png)

### Project Structure 

````
PlaywrightUITests/
├─ docker_test9_test.py       # Test 9 with screenshots
├─ automated-ui-sorting-check.py  # Main UI test suite (Tests 1–9)
├─ requirements.txt
├─ Dockerfile
├─ screenshots/               # Generated screenshots
└─ README.md
`````


### Notes / Best Practices

* Async Playwright tests require pytest-asyncio to run properly.

* PyCharm may not detect async tests automatically; running with a pytest run configuration or in Docker ensures full compatibility.

* Screenshots in Test 9 allow visual verification of each article row, useful for QA or regression testing.

* Docker provides reproducible environments for CI/CD or other users cloning this repo.

### Author

Byron McDowell – QA / Automation Portfolio Project

## License

This project is licensed under the [MIT License](LICENSE) – see the LICENSE file for details.









