# Playwright Test Suite

Created by: **Oleksii Ivashchenko** [Linkedin](https://www.linkedin.com/in/oivashchenko/)

This project contains a test suite using [Playwright](https://playwright.dev/) and [pytest](https://docs.pytest.org/en/latest/) for end-to-end testing of a web application.

## Getting Started

### Prerequisites

- Python 3.7 or later
- A compatible browser (Chromium, Firefox, or WebKit)

### Installation

Clone the repository:

`git clone https://github.com/yourusername/playwright-test-suite.git`
`cd playwright-test-suite`


Install the required dependencies: `pip install -r requirements.txt`

Install the Playwright browser binaries: `playwright install`

## Running the Tests

To run the entire test suite, execute the following command: `pytest`

To run tests with the html report execute: `pytest tests/ --html-report=./report.html`

For more options and configurations, refer to the `pytest.ini` file in the project's root directory.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
