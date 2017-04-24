def login(context, username='test', password='test123'):
    context.browser.get(context.server_address + "/login")
    uname = context.browser.find_element_by_name('username')
    passwd = context.browser.find_element_by_name('password')
    login_button = context.browser.find_element_by_id('btn_login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()

def logout(ctx):
    pass

