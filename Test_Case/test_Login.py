from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_credkart_001:
    def test_credkart_login_001(self, setup):
        self.driver = setup
        self.driver.maximize_window()

        self.driver.get("https://automation.credence.in/login")

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("nikitasbarge@gmail.com")

        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("nikita123")

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            self.driver.save_screenshot(".\\Screenshots\\login_screenshot_Credkart_pass.PNG")
            print("login pass")
            self.driver.close()
            assert True

        except:
            print("login failed")
            self.driver.save_screenshot(".\\Screenshots\\login_screenshot_Credkart_failed.PNG")
            self.driver.close()
            assert False

