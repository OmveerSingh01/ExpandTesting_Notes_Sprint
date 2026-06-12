from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)

    def click(self,locator):
        self.wait.until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until((EC.visibility_of_element_located(locator))).send_keys(text)

    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def switch_to_main_page(self):
        self.driver.switch_to.default_content()

    def scroll(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 275).perform()

    def validate_note(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def refresh(self):
        self.driver.refresh()



