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

    term_selector = Select(fetch_element(driver_instance, By.XPATH, '//*[@id="term_input_id"]'))
    term_selector.select_by_value("202410")
    fetch_element(driver_instance, By.XPATH, "/html/body/div[3]/form/input[2]").click()

    subject_selector = Select(fetch_element(driver_instance, By.XPATH, '//*[@id="subj_id"]'))
    subject_selector.select_by_value("CSC")

    campus_selector = Select(fetch_element(driver_instance, By.XPATH, '//*[@id="camp_id"]'))
    campus_selector.select_by_value("2")

    fetch_element(driver_instance, By.XPATH, '/html/body/div[3]/form/input[12]').click()

    course_details = {
        'titles': [element.text for element in driver_instance.find_elements(By.CSS_SELECTOR, ".ddtitle > a")],
        'instructors': [element.text for element in driver_instance.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(7)")],
        'hours': [element.text for element in driver_instance.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(2)")],
        'days': [element.text for element in driver_instance.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(3)")],
        'locations': [element.text for element in driver_instance.find_elements(By.CSS_SELECTOR, "tr > .dddefault:nth-child(4)")],
    }

    merged_data = list(zip(course_details['titles'], course_details['instructors'], course_details['locations'], course_details['hours'], course_details['days']))

    csv_output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'course_data.csv')

    with open(csv_output_path, 'w', newline='') as csv_output_file:
        csv_output_writer = csv.writer(csv_output_file)
        csv_output_writer.writerow(["Title", "Instructor", "Place", "Hour", "Day"])
        csv_output_writer.writerows(merged_data)

        print(f"CSV file saved at {csv_output_path}")

    driver_instance.quit()

if __name__ == "__main__":
    fetch_course_information()
