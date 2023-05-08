import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def login_to_portal(username, password):
    login_url = "https://myportal.lau.edu.lb/"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(login_url)

    time.sleep(2)

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys(username)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

    time.sleep(5)

    success = False
    if "cas/login" not in driver.current_url:
        success = True

    driver.quit()

    return success

def main():
    username = input("Enter your LAU username: ")
    password = input("Enter your LAU password: ")

    if login_to_portal(username, password):
        print("Logged in successfully!")
    else:
        print("Login failed. Please check your credentials.")

if __name__ == "__main__":
    main()
