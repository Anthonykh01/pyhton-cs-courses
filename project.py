import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

def login_to_portal(username, password):
    LOGIN_URL = "https://myportal.lau.edu.lb/"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(LOGIN_URL)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(username)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    login_button.click()

    return driver

username = sys.argv[1]
password = sys.argv[2]

driver = login_to_portal(username, password)

