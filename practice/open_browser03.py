import getpass

from playwright.sync_api import sync_playwright


USER_DIR_PATH = f"C:\\Users\\MJY\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

with sync_playwright() as p:
    # browser = p.chromium.launch(channel = 'chrome',headless=False, args = ['--start-maximized'])  # 启动chromium浏览器
    browser = p.chromium.connect_over_cdp('http://localhost:12345/')
         # 启动chromium浏览器
    page = browser.contexts[0].pages[0]  # 打开一个标签页
    page.goto("https://chatgpt.com/")
    print(page.title())
    page.pause()# 断点
    browser.close()