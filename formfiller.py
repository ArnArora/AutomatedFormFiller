from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = None
url = "https://docs.google.com/forms/d/e/1FAIpQLSd4-kKTcQzBTXlly-spsDSL_FKoPqK9ls-4HhgeZvTmGk7-LQ/viewform?gxids=7628"
##just fill out this information once
parent_name = "Put parent name"
parent_email = "Put parent email"
name = "Your name"
age = "Your age (as a string)"
sport = "Your sport"
phone_number = "your-phone-number"
##May 10, 2003-> "05102003"
birthday = "your birthday"
try:
    ##find path of chromedriver on your computer
    driver = webdriver.Chrome(executable_path="/Users/arnavarora/Downloads/chromedriver-4")
    driver.get(url)
    time.sleep(2)
    elem = driver.find_element_by_xpath("//input[@type='email']")
    
    elem.send_keys(email)
    elem = driver.find_element_by_xpath("//input[@type='text']")
    elem.send_keys(name)
    elem = driver.find_element_by_xpath("//div[@role='button']")
    elem.click()
    time.sleep(2)
    elems = driver.find_elements_by_xpath("//input[@type='text']")
    answers = [name, age, sport, phone_number]
    for i in range(4):
        elems[i].send_keys(answers[i])
    elem = driver.find_element_by_xpath("//input[@type='date']")
    elem.send_keys(birthday)
    ##put your birthday in the value below in the format shown
    driver.execute_script("""document.querySelector("input[type='date']").value="2005-08-18";""")
    driver.find_element_by_id("i16").click()
    driver.find_element_by_tag_name("textarea").send_keys("n/a")
    elems = driver.find_elements_by_xpath("//div[@role='radio'][@data-value='No']")
    for item in elems:
        item.click()
    time.sleep(1)
    ##elems = driver.find_elements_by_xpath("//div[@role='button']")
    ##elems[1].click()
    time.sleep(15)
finally:
        if driver is not None:
                driver.close()
                driver.quit()
    
