# ФИО: Абдыгапаров Санжар
# Дата: 11.11.2026
# Время: 16:50
# Описание: Автоматизированный тест с использованием библиотеки Playwright и pytest.
# Функция test_has_title проверяет, что заголовок главной страницы содержит нужное слово.
# Функция test_get_started_link имитирует клик по кнопке "Get started" и проверяет переход на страницу установки.

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev")
    # Проверяем, что в заголовке есть слово Playwright
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev")
    # Находим кнопку начала работы по её роли и кликаем
    page.get_by_role("link", name="Get started").click()
    # Проверяем, что появился заголовок Installation
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
