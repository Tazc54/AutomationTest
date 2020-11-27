import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://randomtodolistgenerator.herokuapp.com/library")
    items = driver.find_elements(By.CSS_SELECTOR, ".card-body")
    to_do_list = []
    for item in items:
        name = item.find_element(By.CSS_SELECTOR, ".task-title div")
        to_do_list.append(name.text)
    driver.get("https://todoist.com/users/showlogin")
    user_field = driver.find_element(By.ID, "email").send_keys("jidaca4117@questza.com")
    password_field = driver.find_element(By.ID, "password").send_keys("Test1234" + Keys.RETURN)
    wait.until(presence_of_element_located((By.CSS_SELECTOR, ".plus_add_button")))
    button = driver.find_element(By.CSS_SELECTOR, ".plus_add_button").click()
    for item in to_do_list:
        text_area = driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-ltr").send_keys(item)
        WebDriverWait(driver, timeout=5).until(element_to_be_clickable((By.CSS_SELECTOR, ".ist_button.ist_button_red")))
        submit_button = driver.find_element(By.CSS_SELECTOR, ".ist_button.ist_button_red").click()
    time.sleep(3)  # waiting for todist.com server to save the inputs before close.
