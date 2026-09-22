import getpass

from playwright.sync_api import sync_playwright


USER_DIR_PATH = f"C:\\Users\\MJY\\AppData\\Local\\Google\\Chrome\\User Data\\Default"

with sync_playwright() as p:
    # browser = p.chromium.launch(channel = 'chrome',headless=False, args = ['--start-maximized'])  # 启动chromium浏览器
    browser = p.chromium.launch_persistent_context(
        user_data_dir = USER_DIR_PATH,
        channel = 'chrome',
        headless = False,
        args = ["--start-maximized"],   # 最大化
        slow_mo = 50
    )  # 启动chromium浏览器
    page = browser.new_page()  # 打开一个标签页
    page.goto("https://chatgpt.com/")
    print(page.title())
    page.pause()# 断点
    browser.close()