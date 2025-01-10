from selene import browser, be, have, query

def test_google_search(setup_browser):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_google_search_no_results(setup_browser):
        browser.open('https://google.com/ncr')
        browser.element('[name="q"]').should(be.blank).type('ertert34534tgdfgerg43t3').press_enter()
        browser.element('#center_col').should(have.text('did not match any documents'))
        print(browser.element('#center_col').get(query.text))