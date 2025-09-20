import os
from pages.login import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.goto("http://3.8.242.61/")
    login_page.login(os.environ["USERNAME"], os.environ["PASSWORD"])
    assert page.get_by_role('heading', name ='Interest Calculator')
