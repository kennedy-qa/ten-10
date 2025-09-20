from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Welcome to Ten10 Technical")
        self.login_button = page.get_by_role("button", name="Login")
        self.email_field = page.get_by_role("textbox", name="Email")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.log_in_button = page.get_by_role("button", name="Log in")

    def goto(self, url):
        self.page.goto(url)    

    def login(self, username, password):
        assert self.heading.is_visible()
        self.login_button.click()
        self.email_field.fill(username)
        self.password_field.fill(password)
        self.log_in_button.click()
