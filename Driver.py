from appium import webdriver
import os
from pathlib import Path, PureWindowsPath, PurePosixPath
import platform


class AppiumDriverSetup(object):

    driver = None
    apkPathWindow = None
    apkPathLinux = None

    def apkPath(self):
        try:
            if platform.system() == "Windows":
                print("Tests are being executed on WINDOW operating system")
                PATH = PureWindowsPath(os.path.abspath(os.getcwd()))
                apkPathWindow = str(PATH) + str("\YelloInterview.apk")
                print('Window path is ::', apkPathWindow)
                return apkPathWindow

            if platform.system() == "Linux":
                print("Tests are being executed on Linux operating system")
                PATH = PurePosixPath(os.path.abspath(os.getcwd()))
                apkPathLinux = str(PATH) + str("\YelloInterview.apk")
                print('Linux path is ::', apkPathLinux)
                return apkPathLinux
        except IOError:
            print("Unfortunately, apk file doesn't exist at that location")

    def setUp(self):
        desiredCapibilities = {}
        desiredCapibilities['platformName'] = 'Android'
        desiredCapibilities['platformVersion'] = '7.1.1'
        desiredCapibilities['deviceName'] = 'Android Emulator'
        desiredCapibilities['app'] = AppiumDriverSetup.apkPath(self)
        desiredCapibilities['appPackage'] = 'com.recsolu.newton'
        desiredCapibilities['appActivity'] = 'com.recsolu.newton.activities.LoginActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desiredCapibilities)
        self.driver.implicitly_wait(30)
        return self.driver

    def tearDown(self):
        self.driver.quit()
