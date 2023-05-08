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

    return driver if success else None

def main():
    username = input("Enter your LAU username: ")
    password = input("Enter your LAU password: ")

    driver = login_to_portal(username, password)
    if driver:
        print("Logged in successfully!")
        driver.get("https://banweb.lau.edu.lb/")
        time.sleep(5)
        print("Navigated to Banner.")
    else:
        print("Login failed. Please check your credentials.")

if __name__ == "__main__":
    main()
