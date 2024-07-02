from pytest_bdd import scenarios, given, when, then, parsers
from ...page_object_model.login import LoginPage
from ...page_object_model.overview import OverviewPage

scenarios('../features/demo.feature')

@given('I am on the login page')
def i_am_on_the_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()

@when(parsers.parse('I login with {username} and {password}'))
def i_login_with_username_and_password(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

@then('I should be in the overview page with correct credentials')
def i_should_see_the_overview_page(driver):
    overview_page = OverviewPage(driver)
    overview_page.verify_url()
    overview_page.verify_element_displayed(overview_page.logged_user_name_div)
    overview_page.verify_element_displayed(overview_page.logged_user_role_div)
    overview_page.verify_element_displayed(overview_page.balance_value_div)

@then('I should see the available credit is 17800')
def i_should_see_the_available_credit(driver):
    overview_page = OverviewPage(driver)
    overview_page.verify_balance_value(17800)
    