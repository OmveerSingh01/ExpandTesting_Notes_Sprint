from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DeletePage(BasePage):

    delete_btn = (By.XPATH, '(//button[@data-testid="note-delete"])[1]')
    confirm_delete = (By.XPATH,'//button[@data-testid="note-delete-confirm"]')
    note_titles = (By.XPATH, '//div[@data-testid="note-card-title"]')

    def __init__(self,driver):
        super().__init__(driver)

    def click_delete(self):
        self.click(self.delete_btn)

    def click_confirm(self):
        self.click(self.confirm_delete)

    def get_all_notes(self):
        return self.driver.find_elements(*self.note_titles)