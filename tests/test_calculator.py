import os
from pages.login import LoginPage
from pages.calculator import CalculatorPage

def test_calculate_one_percent_annually(page):
    login_page = LoginPage(page)
    calulator_page = CalculatorPage(page)
    login_page.goto("http://3.8.242.61/")
    login_page.login(os.environ["USERNAME"], os.environ["PASSWORD"])
    assert page.get_by_role("heading", name ="Interest Calculator")
    # Meant to be a simple proof of concept but the drop down ate up my time, intended to branch out into more general function that would accept different values, percentages and durations.
    calulator_page.calculate_one_percent_annually()
    # make assertions class, pass in dynamic values based off interest calculations
    assert page.get_by_role('heading', name ="Interest Amount: 10.00").is_visible
    assert page.get_by_role('heading', name ="Total Amount with Interest: 1010").is_visible
