## 使用命令 playwright codegen https://hmshop-test.itheima.net/

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hmshop-test.itheima.net/")
    page.get_by_role("link", name="登录").click()
    page.get_by_role("textbox", name="手机号/邮箱").click()
    page.get_by_role("textbox", name="手机号/邮箱").fill("15937343985")
    page.get_by_role("textbox", name="手机号/邮箱").press("Tab")
    page.get_by_role("textbox", name="密码").fill("mjy5210...")
    page.get_by_role("textbox", name="密码").press("Tab")
    page.get_by_role("textbox", name="验证码").fill("8888")
    page.get_by_role("link", name="登    录").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
