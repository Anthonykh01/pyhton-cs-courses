import os
import sys
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def fetch_element(driver_instance, search_by, value):
    return driver_instance.find_element(search_by, value)

def fetch_course_information():
    credentials = {
        'username': sys.argv[1],
        'password': sys.argv[2]
    }

    LAU_PORTAL = "https://myportal.lau.edu.lb/"
    COURSE_URL = "https://banweb.lau.edu.lb/prod/bwckschd.p_get_crse_unsec"

    chrome_config = webdriver.ChromeOptions()
    chrome_config.add_argument("--headless")
    driver_instance = webdriver.Chrome(options=chrome_config)

    driver_instance.get(LAU_PORTAL)

    fetch_element(driver_instance, By.NAME, "username").send_keys(credentials['username'])
    fetch_element(driver_instance, By.NAME, "password").send_keys(credentials['password'])
    fetch_element(driver_instance, By.XPATH, "//input[@type='submit']").click()

    fetch_element(driver_instance, By.XPATH, '//*[@id="zz4_TopNavigationMenuV4"]/div/ul/li/ul/li[3]/a').click()
    fetch_element(driver_instance, By.XPATH, '//*[@id="cbqwpctl00_m_g_df4e4cc9_291f_48af_90eb_524811091537"]/div/div[2]/a[4]').click()

    driver_instance.get("https://banweb.lau.edu.lb/prod/bwckschd.p_disp_dyn_sched")

    
    driver_instance.quit()

if __name__ == "__main__":
    fetch_course_information()
