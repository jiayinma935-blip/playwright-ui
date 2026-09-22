# 识别图片验证码

import ddddocr
from playwright.sync_api import sync_playwright



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://so.gushiwen.cn/user/login.aspx?from=http://so.qushiwen.cn/user/collect.aspx")

    img_loc = page.locator('#imgCode')
    img_loc.screenshot(path='./picture/yzm.png')

    ocr = ddddocr.DdddOcr(show_ad = False)

    with open('./picture/yzm.png', 'rb') as fp:
        yzm_img = fp.read()
    yzm = ocr.classification(yzm_img)
    page.locator('#code').fill(yzm)


print(yzm)
