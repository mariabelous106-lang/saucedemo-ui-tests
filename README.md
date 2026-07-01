# SauceDemo UI Tests

Автоматизированные UI-тесты интернет-магазина [SauceDemo](https://www.saucedemo.com/) на Playwright + Pytest.

## Стек
- Python 3.14
- Playwright
- Pytest

## Установка и запуск

```bash
git clone https://github.com/mariabelous106-lang/saucedemo-ui-tests.git
cd saucedemo-ui-tests
python -m venv venv
venv\Scripts\activate
pip install pytest-playwright
playwright install chromium
pytest -v