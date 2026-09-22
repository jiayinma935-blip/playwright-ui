from playwright.sync_api import Page


class AddModulePage:

    def __init__(self, page: Page):
        self.page = page
        self.locator_module_name = page.get_by_label("模块名称:")
        self.locator_module_project = page.get_by_label("所属项目:")
        self.locator_module_desc = page.get_by_label('模块描述:')
        self.locator_save_button = page.get_by_text('点击提交')
        # boot box
        self.locator_boot_box = page.locator('.bootbox-body')

    def navigate(self):
        self.page.goto("/add_module.html")

    def fill_module_name(self, name):
        self.locator_module_name.fill(name)

    def select_module_by_value(self, value):
        self.locator_module_project.select_option(value=value)

    def fill_module_desc(self, desc):
        self.locator_module_desc.fill(desc)

    def click_save_module(self):
        self.locator_save_button.click()
