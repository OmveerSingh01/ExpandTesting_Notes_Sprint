from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.base_page import BasePage

class NotesPage(BasePage):
    add_btn = (By.XPATH, '//button[@data-testid="add-new-note"]')
    category_btn = (By.ID, "category")
    work_btn = (By.XPATH, '//option[@value="Work"]')
    title_btn = (By.ID, 'title')
    description_btn = (By.ID,"description")
    create_btn = (By.XPATH, '//button[@data-testid="note-submit"]')
    title = (By.XPATH,'//div[@data-testid="note-card-title"]')
    desc = (By.XPATH,'//p[@data-testid="note-card-description"]')
    in_title = (By.XPATH,"//div[.='Title is required']")

    def __init__(self,driver):
        super().__init__(driver)

    def click_add_btn(self):
        self.click(self.add_btn)

    def click_category_btn(self):
        self.click(self.category_btn)

    def click_work_btn(self):
        self.click(self.work_btn)

    def click_title_btn(self):
        self.click(self.title_btn)

    def enter_title_btn(self,text):
        self.enter_text(self.title_btn,text)

    def click_description_btn(self):
        self.click(self.description_btn)

    def enter_description_btn(self,text):
        self.enter_text(self.description_btn,text)

    def click_create_btn(self):
        self.click(self.create_btn)

    def validate_title(self):
        return self.validate_note(self.title)

    def validate_description(self):
        return self.validate_note(self.desc)

    def invalid_title(self):
        return self.validate_note(self.in_title)

    def count_note_by_title_desc(self, title, description):
        """Count occurrences of (title, description) pair in the UI"""
        try:
            title_elements = self.wait.until(EC.visibility_of_all_elements_located(self.title))
            desc_elements = self.wait.until(EC.visibility_of_all_elements_located(self.desc))
            
            titles = [e.text for e in title_elements]
            descs = [e.text for e in desc_elements]
            
            count = 0
            for i in range(min(len(titles), len(descs))):
                if titles[i] == title and descs[i] == description:
                    count += 1
            return count
        except (TimeoutException, NoSuchElementException):
            return 0

