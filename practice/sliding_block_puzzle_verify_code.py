import base64
import random

import ddddocr

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel = 'chrome',headless = False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    # page = context.pages[0]  # 不会多出空白页
    page.goto("https://www.geetest.com/demo/slide-float.html")

    # 点击按钮进入滑块
    page.locator(".geetest_radar_tip").click()
    page.wait_for_timeout(1000)

    # 找到背景图（将图片转换成字符串）
    bj_base64 = page.evaluate("document.getElementsByClassName('geetest_canvas_bg geetest_absolute')[0].toDataURL('image/png')")
    # print(bj_base64)
    with open('picture/bj_p.png', 'wb') as fp:
        bj_b = bj_base64.split(',')[-1]
        fp.write(base64.b64decode(bj_b))    # 转换类型

    slice_base64 = page.evaluate("document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0].toDataURL('image/png')")
    # print(slice_base64)
    with open('picture/slice_p.png', 'wb') as fp:
        slice_b = slice_base64.split(',')[-1]
        fp.write(base64.b64decode(slice_b))  # 转换类型

    # 识别缺口位置
    ocr = ddddocr.DdddOcr(show_ad=False, det = False, ocr = False)

    with open('./picture/bj_p.png', 'rb') as fp:
        target_bytes = fp.read()
    with open('./picture/slice_p.png', 'rb') as fp:
        background_bytes = fp.read()

    res = ocr.slide_comparison(target_bytes, background_bytes)
    # print(res)
    x = res.get('target')[0]    # 缺口位置
    print(x)

    slide_button = page.locator(".geetest_slider_button")
    slider = slide_button.bounding_box()    # 滑块 的位置
    print(slider)

    # 拖动鼠标位置需要去调试，找到合适的等待时间以及移动距离
    page.mouse.move(x=int(slider['x']), y=slider['y'] + slider['height'] / 2)
    page.mouse.down(button="middle")
    page.wait_for_timeout(300)
    page.mouse.move(x=int(slider['x']) + x + random.randint(2, 8), y=slider['y'] +slider['height'] / 2)

    page.wait_for_timeout(500)
    page.mouse.move(x=int(slider['x']) + x - 2, y=slider['y'] + slider['height'] / 2)
    page.mouse.move(x=int(slider['x']) + x - 6, y=slider['y'] + slider['height'] / 2)
    page.wait_for_timeout(300)
    page.mouse.move(x=int(slider['x']) + x - 8, y=slider['y'] + slider['height'] / 2)
    page.mouse.up(button="middle")
    page.wait_for_timeout(6000)

    context.close()