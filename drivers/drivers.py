from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

from config.config import Configuration


class MobileDriver:

    def __init__(self):
        self.env_config, self.device_config = Configuration.get_config()

    """    
    # ==============================
    # ANDROID DRIVER
    # ==============================
    """

    def android_driver(self):
        options = UiAutomator2Options()

        # -------- Device Capabilities --------

        options.platform_name = "Android"
        options.platform_version = self.device_config.platformVersion
        options.device_name = self.device_config.deviceName
        options.automation_name = self.device_config.automationName

        # -------- App Capabilities --------

        if self.env_config.apk:
            options.app = self.env_config.apk
        else:
            options.app_package = self.env_config.appPackage
            options.app_activity = self.env_config.appActivity

        # Optional stability caps

        options.new_command_timeout = 300
        options.auto_grant_permissions = True

        driver = webdriver.Remote(
            command_executor=self.device_config.server_url, options=options
        )

        return driver

    """    
    # ==============================
    # IOS DRIVER
    # ==============================
    """

    def ios_driver(self):
        options = XCUITestOptions()

        # -------- Device Capabilities --------
        options.platform_name = "iOS"
        options.platform_version = self.device_config.platformVersion
        options.device_name = self.device_config.deviceName
        options.automation_name = self.device_config.automationName
        options.udid = getattr(self.device_config, "udid", None)

        # -------- App Capabilities --------
        if self.env_config.ipa:
            options.app = self.env_config.ipa
        else:
            options.bundle_id = self.env_config.bundleId

        options.new_command_timeout = 300

        driver = webdriver.Remote(
            command_executor=self.device_config.server_url, options=options
        )

        return driver

    """
    # ==============================
    # OPEN DRIVER (Like open_browser)
    # ==============================
    """

    def open_mobile(self):
        platform = self.device_config.__class__.__name__.lower()

        if "android" in platform:
            return self.android_driver()
        elif "ios" in platform:
            return self.ios_driver()
        else:
            raise ValueError("Unsupported Mobile Platform")
