
class LoginScreen(object):
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def landingPage(self):
        # verify app is launched successfully
        emailField = self.driver.find_element_by_id("com.recsolu.newton:id/text_email")
        return emailField

    def submitButton(self):
        submitButton = self.driver.find_element_by_id("com.recsolu.newton:id/button_login")
        return submitButton

    def errorValidation(self):
        emailField = self.driver.find_element_by_id("com.recsolu.newton:id/text_email")
        submitButton = self.driver.find_element_by_id("com.recsolu.newton:id/button_login")
        emailField.send_keys("kashifali9829@gmail.com")
        submitButton.click()
        error = self.driver.find_element_by_id("android:id/message")
        return error
