from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id("button")
    time.sleep(5)
    button = browser.find_element_by_css_selector("[type = 'submit']")
    button.click()       
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
  
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    ans = browser.find_element_by_id("answer")
    ans.send_keys(y)
    button = browser.find_element_by_css_selector("[type = 'submit']")
    button.click()
    
finally:
    
    time.sleep(10)
    
    browser.quit()