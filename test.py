import unittest
import os
from random import randint
from appium import webdriver

class SimpleIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = os.path.abspath('builds/AppiumTest.app.zip')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '13.1',
                'deviceName': 'iPhone 11',
                'automationName': 'XCUITest'
            })

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
        self.assertEqual(countLabelText, self._expectedText)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)