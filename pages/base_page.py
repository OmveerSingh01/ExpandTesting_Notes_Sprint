from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)



    def click(self, locator):
        # Resolve the element once, scroll it into view and attempt a normal click.
        element = self.wait.until(EC.element_to_be_clickable(locator))

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element
        )

        # Clear overlays before clicking
        self.dismiss_ads()

        try:
            element.click()
        except Exception:
            # Final fallback: JavaScript click bypasses all overlay hit-testing
            self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def scroll(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(0, 275).perform()

    def validate_note(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def dismiss_ads(self):
        """Remove full-screen ad iframes (e.g. Google Ads) and grippy-host overlays
        that intercept clicks on the actual page elements."""
        self.driver.execute_script("""
               // Remove full-viewport ad iframes (aswift_*)
               document.querySelectorAll('iframe[id^="aswift_"]').forEach(el => el.remove());
               // Remove grippy-host overlay (Chrome DevTools panel handle)
               document.querySelectorAll('div.grippy-host').forEach(el => el.remove());
           """)

    def select_dropdown(self, locator, value):
        dropdown = self.wait.until(EC.visibility_of_element_located(locator))
        option = Select(dropdown)
        option.select_by_value(value)

    def refresh(self):
        self.driver.refresh()


