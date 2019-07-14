from selenium import webdriver

browser = webdriver.Firefox()

browser.get('https://www.testmy.net')

buttons = browser.find_elements_by_class_name('btn')

buttons[0].click()

elems = browser.find_elements_by_class_name('highcharts-label')

for e in elems:
    print(e.text)
