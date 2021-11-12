from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path=r'.\res\geckodriver.exe')
driver.get('https://www.mediamarkt.nl/nl/product/_legend-of-zelda-link-s-awakening-nintendo-switch-1623975.html')

WebDriverWait(driver, 3)

cookiePopup = driver.find_elements_by_css_selector('button.gdpr-cookie-layer__btn')

if (len(cookiePopup) > 0):
    cookiePopup[0].click()
    WebDriverWait(driver, 1)

productPrice = driver.find_elements_by_xpath('//meta[@itemprop="price"]')[0].get_attribute("content")

if (float(productPrice) > 50.0):
    print("Price is above 50!")

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.price-button"))
    ).click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a#basket-flyout-cart"))
    ).click()
