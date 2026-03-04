import os
import pytest
from drivers.drivers import MobileDriver

"""
    # ==============================
    # Pytest CLI Options
    # ==============================
"""


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")
    parser.addoption(
        "--platform", action="store", default="android", help="android or ios"
    )
    parser.addoption(
        "--device", action="store", default="local", help="device config name"
    )


"""
    # ==============================
    # Configure Environment
    # ==============================
"""


def pytest_configure(config):
    os.environ["env"] = config.getoption("env")
    os.environ["platform"] = config.getoption("platform")
    os.environ["device"] = config.getoption("device")


"""
    # ==============================
    # Mobile Driver Fixture
    # ==============================
"""


@pytest.fixture(scope="class")
def mobile():
    global driver

    mobile_driver = MobileDriver()

    platform = os.getenv("platform").lower()

    if platform == "android":
        driver = mobile_driver.android_driver()
    elif platform == "ios":
        driver = mobile_driver.ios_driver()
    else:
        raise ValueError("Unsupported platform. Use android or ios")

    yield driver

    driver.quit()


"""
    # ==============================
    # Cross Platform Execution
    # ==============================
"""


@pytest.fixture(params=["android", "ios"], scope="class")
def cross_mobile(request):
    global driver

    os.environ["platform"] = request.param

    mobile_driver = MobileDriver()

    if request.param == "android":
        driver = mobile_driver.android_driver()
    elif request.param == "ios":
        driver = mobile_driver.ios_driver()

    yield driver

    driver.quit()
