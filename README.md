# 🧪 Test Automation Framework

A Python-based test automation framework covering both **API** and **UI** testing, built with **pytest** and **Playwright**. Designed for CI/CD integration and structured for clear separation between API and browser-based test suites.

---

## 📋 Overview

| Suite | Target | Tests | Status |
|---|---|---|---|
| API | [ReqRes](https://reqres.in) REST API | 8 | ✅ All Passed |
| UI | Web Application (Login, Checkout, Sorting) | 7 | ✅ All Passed |
| **Total** | | **15** | ✅ **15 / 15** |

---

## 📁 Project Structure

```
├── tests/
│   ├── api/
│   │   └── test_reqres.py        # API tests against ReqRes API
│   └── ui/
│       ├── test_login.py         # Login flow UI tests
│       ├── test_checkout.py      # Cart & checkout UI tests
│       └── test_sorting.py       # Product sorting UI tests
├── reports/
│   ├── api-report.html           # API test HTML report
│   └── ui-report.html            # UI test HTML report
├── conftest.py                   # Shared fixtures & configuration
├── pytest.ini / pyproject.toml   # Pytest configuration
└── requirements.txt              # Python dependencies
```

---

## 🧪 Test Coverage

### 🔌 API Tests — `tests/api/test_reqres.py`

Target: **[ReqRes API](https://reqres.in)**

| Test | Description | Duration |
|---|---|---|
| `test_get_list_users` | GET `/users` returns a list of users | 268 ms |
| `test_get_single_user` | GET `/users/{id}` returns a single user | 222 ms |
| `test_get_user_not_found` | GET non-existent user returns 404 | 226 ms |
| `test_create_user` | POST `/users` creates a new user | 232 ms |
| `test_register_successful` | POST `/register` with valid credentials | 256 ms |
| `test_register_missing_password` | POST `/register` without password returns error | 226 ms |
| `test_update_user` | PUT `/users/{id}` updates user data | 141 ms |
| `test_delete_user` | DELETE `/users/{id}` returns 204 | 141 ms |

---

### 🖥️ UI Tests — `tests/ui/`

Powered by **Playwright** for browser automation.

#### `test_login.py` — Login Flows

| Test | Description | Duration |
|---|---|---|
| `test_login_valid` | Login with correct credentials succeeds | 884 ms |
| `test_login_wrong_password` | Login with wrong password shows error | 841 ms |
| `test_login_wrong_username` | Login with wrong username shows error | 833 ms |
| `test_login_empty_fields` | Login with empty fields shows validation error | 882 ms |
| `test_login_long_input` | Login with excessively long input is handled | 854 ms |

#### `test_checkout.py` — Cart & Checkout

| Test | Description | Duration |
|---|---|---|
| `test_add_to_cart_and_checkout` | Add item to cart and complete checkout flow | ~2 s |

#### `test_sorting.py` — Product Sorting

| Test | Description | Duration |
|---|---|---|
| `test_sort_price_high_to_low` | Products correctly sort by price (high to low) | 931 ms |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.11 | Language |
| pytest | 8.3.5 | Test runner |
| pytest-playwright | 0.5.1 | Browser automation |
| pytest-html | 4.1.1 | HTML report generation |
| pytest-base-url | 2.1.0 | Base URL configuration |
| pytest-metadata | 3.1.1 | Report metadata |
| pluggy | 1.6.0 | pytest plugin system |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/reyhaiz/api-automation-framework.git
cd api-automation-framework

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

---

## ▶️ Running Tests

### Run all tests

```bash
pytest
```

### Run only API tests

```bash
pytest tests/api/ --html=reports/api-report.html --self-contained-html
```

### Run only UI tests

```bash
pytest tests/ui/ --html=reports/ui-report.html --self-contained-html
```

### Run both suites with separate reports

```bash
pytest tests/api/ --html=reports/api-report.html --self-contained-html
pytest tests/ui/ --html=reports/ui-report.html --self-contained-html
```

### Run with a custom base URL

```bash
pytest --base-url=https://your-app.example.com
```

### Run in headed mode (UI tests)

```bash
pytest tests/ui/ --headed
```

### Run with verbose output

```bash
pytest -v
```

---

## 📊 Reports

After running tests, open the HTML reports in your browser:

```bash
# API report
open reports/api-report.html

# UI report
open reports/ui-report.html

# On Windows
start reports/api-report.html
start reports/ui-report.html
```

Reports include sortable/filterable results, per-test durations, logs, and environment metadata.

---

## ⚙️ CI/CD

This framework is configured for CI and has been validated on **Linux (Azure)**. The `CI=true` environment flag is detected automatically by pytest.

Example GitHub Actions workflow:

```yaml
name: Test Automation

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Install Playwright browsers
        run: playwright install --with-deps

      - name: Run API tests
        run: pytest tests/api/ --html=reports/api-report.html --self-contained-html

      - name: Run UI tests
        run: pytest tests/ui/ --html=reports/ui-report.html --self-contained-html

      - name: Upload reports
        uses: actions/upload-artifact@v3
        with:
          name: test-reports
          path: reports/
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/add-new-tests`)
3. Commit your changes (`git commit -m 'Add tests for X'`)
4. Push to the branch (`git push origin feature/add-new-tests`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
