from playwright.async_api import async_playwright, Page, expect


def test_login(page: Page):
    page.goto('http://47.116.12.183/login.html')
    page.get_by_label("用 户 名:").fill("py")
    page.get_by_label("密    码:").fill("123456")
    page.get_by_text("立即登录").click()
    page.wait_for_timeout(5000)
    print(page.title())
    expect(page).to_have_title('首页')