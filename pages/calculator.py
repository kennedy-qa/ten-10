import time
from playwright.sync_api import Page

class CalculatorPage:
    def __init__(self, page: Page):
        self.page = page
        self.logout_button = page.get_by_role("button", name="Logout")
        self.heading = page.get_by_role("heading", name="Interest Calculator")
        # Optimistic intention to create test to verify image didn't render
        self.image = page.get_by_role("img", name="Logo")
        self.principal_amount_slider = page.get_by_role("slider", name="Principal Amount:")
        self.interest_rate_dropdown = page.get_by_role("button", name="Select Interest Rate")
        # Refactor this to be dynamic to pass in multiple percentages - don't think I didn't notice that cheeky missing 13%
        self.interest_rate_one_percent = page.get_by_role("checkbox", name="1%", exact=True)
        self.duration_yearly = page.get_by_role("link", name="Yearly") # Thought this was a button for the longest time
        self.mandatory_checkbox = page.get_by_role("checkbox", name="Please accept this mandatory")
        self.calculate_button = page.get_by_role("button", name="Calculate")

    # Not pretty but no time - Needed to dismiss dropdown, attempted esc but didn't work, tabbing away from drop down manually seemed to do the trick
    def shift_tab(self, times=1):
        for _ in range(times):
            self.page.keyboard.press("Shift+Tab")
        
    def logout(self):
        self.logout_button.click()

    def calculate_one_percent_annually(self):
        assert self.heading.is_visible()
        self.principal_amount_slider.fill('1000')
        self.interest_rate_dropdown.click()
        self.interest_rate_one_percent.click()
        self.shift_tab(2)
        self.duration_yearly.click()
        self.mandatory_checkbox.check()
        self.calculate_button.click()