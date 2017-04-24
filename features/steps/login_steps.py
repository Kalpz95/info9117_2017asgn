from behave import *
import re

@when(u'a user visits the login page')
def visit_login(context):
    context.browser.get(context.home + "/login")

@then(u'she should see the username field')
def see_username_field(context):
    see_username_field_found = re.search("username", context.browser.page_source, re.IGNORECASE)
    assert see_username_field_found

@then(u'she should see the password field')
def see_password_field(context):
    see_password_field_found = re.search("password", context.browser.page_source, re.IGNORECASE)
    assert see_password_field_found

@then(u'she should see the login button')
def see_login_button(context):
    see_login_button_found = re.search("btn_login", context.browser.page_source, re.IGNORECASE)
    assert see_login_button_found

@when(u'she logs in with username "{username}" and password "{password}"')
def login(context, username='test', password='test123'):
    uname = context.browser.find_element_by_name('username')
    passwd = context.browser.find_element_by_name('password')
    login_button = context.browser.find_element_by_id('btn_login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()

@then(u'she should see a message of "{text}"')
def see_login_success(context, text):
    context.browser.get(context.home)
    assert str.encode(text)

@given(u'a user visits the login page')
def step_impl(context):
    context.browser.get(context.home + "/login")

@given(u'she sees the Logout link')
def see_logout_link(context):
    see_logout_link_found = re.search("log out", context.browser.page_source, re.IGNORECASE)
    assert see_logout_link_found

@when(u'she clicks on the Logout link')
def click_logout_link(context):
    logout_link =  context.browser.find_element_by_link_text('log out')
    logout_link.click()

@then(u'she returns to the site')
def visit_site(context):
    context.browser.get(context.home + "/logout")

@then(u'she sees a message telling "{msg}"')
def see_logout_success(context, msg):
    context.browser.get(context.home)
    assert str.encode(msg)

