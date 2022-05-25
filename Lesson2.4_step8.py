from selenium import webdriver
import time
from math import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def calc(x):
    return str(log(abs(12*sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    
    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    browser.find_element(By.ID, 'answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.find_element_by_id('solve').click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла