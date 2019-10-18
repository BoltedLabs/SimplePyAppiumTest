import base64
import os
import unittest

from appium import webdriver
from random import randint


class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('builds/AppiumTest.app.zip')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.2',
                'deviceName': 'iPhone X',
                'automationName': 'XCUITest',
                'language': 'es',
                'locale': 'US'
            })
        
        # dump = os.popen('aapt dump badging myapp.apk').read()
        # defaults read /path/test.app/Info CFBundleShortVersionString
        # defaults read /path/test.app/Info CFBundleVersion

    def tearDown(self):
        self.driver.quit()

    def _generate_presses(self):
        pressCount = randint(1, 5)

        for i in range(0, pressCount):
            self.driver.find_element_by_accessibility_id('Button').click()
        
        self._expectedText = 'Button press count: {}'.format(pressCount)

    def test_button(self):
        self._generate_presses()

        countLabelText = self.driver.find_element_by_accessibility_id('ButtonCountLabel').text

        screenshotBase64 = self.driver.get_screenshot_as_base64()
        with open('screenshots/screenshot.png', 'wb') as f:
            f.write(base64.b64decode(screenshotBase64))

        self.assertEqual(countLabelText, self._expectedText)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)