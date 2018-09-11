from Driver import AppiumDriverSetup
from YellowInterviewMainPage import LoginScreen
import unittest


class YellowInterviewTests(unittest.TestCase):

    def test_yellowInterview_loginscreen(self):

        driver = AppiumDriverSetup.setUp(self)

        loginPage = LoginScreen(driver)

        emailField = loginPage.landingPage()
        self.assertTrue(emailField.is_displayed(), "App has launched successfully and landing page is correct")

        submitButton = loginPage.submitButton()
        self.assertTrue(submitButton.is_displayed(), "Submit Button is visible")

        error = loginPage.errorValidation()
        self.assertEqual(error.get_attribute('name'),
                         "There seems to be a problem, please check your email address and try again.")

        AppiumDriverSetup.tearDown(self)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(YellowInterviewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

