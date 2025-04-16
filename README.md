# Shopping Cart UI Test Suite

Automated UI testing suite for an e-commerce website built using **Playwright**, **Pytest**, and **Allure Reports**.

## Features Covered

- Add 3 different products to cart:
  -  Virtual Gift Card
  -  14.1-inch Laptop
  -  Build your own (cheap/expensive) Computer
- Verify cart items and quantities
- Remove one item and verify removal
- Clear cart and verify it's empty

## Tech Stack

- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)
- [Allure](https://docs.qameta.io/allure/)
- [Jenkins](https://www.jenkins.io/) (CI/CD)

##  Project Structure
shopping-cart-ui-tests/
├── locators/                     # All element locators (selectors)
│   ├── cart_page_repo.py
│   ├── home_page_repo.py
│   └── product_page_repo.py
│
├── pages/                        # Page Object Models (POM)
│   ├── base_page.py
│   ├── cart_page.py
│   ├── home_page.py
│   └── product_page.py
│
├── tests/                        # Test cases
│   └── test_shopping_cart_flow.py
│
├── screenshots/                  # Screenshots taken on test failures
│
├── .gitignore                    # Git ignored files
├── Jenkinsfile                   # Jenkins pipeline configuration
├── pytest.ini                    # Pytest configuration (browser, headed, etc.)
├── requirements.txt              # All project dependencies



##Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install


## Run tests
pytest

## Generate Allure Reports
pytest --alluredir=allure-results
allure serve allure-results
