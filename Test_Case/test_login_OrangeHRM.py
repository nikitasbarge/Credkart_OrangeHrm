from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_OranfeHRm_001:
    def test_OrangeHRm_login_001(self, setup):
        self.driver = setup
        self.driver.maximize_window()

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(60)

        # username
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # password
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.implicitly_wait(60)
        # login
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.implicitly_wait(120)

        try:
            self.driver.find_element(By.XPATH, "//img[@alt='client brand banner']")
            self.driver.save_screenshot(".\\Screenshots\\screenshot_login_OrangeHrm_pass.PNG")
            print("login pass")
            self.driver.close()
            assert True

        except:
            self.driver.save_screenshot(".\\Screenshots\\screenshot_login_OrangeHrm_fail.PNG")
            print("login fail")
            self.driver.close()
            assert False






