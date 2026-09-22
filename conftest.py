from pytest import Item
import allure
import pytest
from typing import Dict

# 本地插件注册
pytest_plugins = ['plugins.pytest_playwright', 'plugins.pytest_base_url_plugin']


def pytest_runtest_call(item: Item):

    # item为正在执行的测试项，由pytest自动传入，可以获取当前测试项的类名、类注释、测试方法名、测试方法注释

    # 动态添加测试类的allure.feature()
    if item.parent._obj.__doc__:
        # 获取测试类的文档字符串，将其添加到allure里，dynamic表示动态赋值
        allure.dynamic.feature(item.parent._obj.__doc__)
    # 动态添加测试用例的title标题allure.title()
    if item.function.__doc__:
        allure.dynamic.title(item.function.__doc__)


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args) -> Dict:
    """窗口最大化"""
    return {**browser_type_launch_args, "args": ['--start-maximized']}


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: Dict) -> Dict:
    context_args = {
        **browser_context_args,
        "ignore_https_errors": True,
    }

    if "viewport" not in browser_context_args:
        context_args["no_viewport"] = True

    return context_args
