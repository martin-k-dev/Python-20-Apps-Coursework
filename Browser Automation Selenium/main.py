import re
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_credentials():
    with open(".env", "r") as env:
        env_data = env.read()
        username_pattern = re.compile("USERNAME =([^\n]+)")
        password_pattern = re.compile("PASSWORD =([^\n]+)")
        password_match = re.findall(password_pattern, env_data)[0]
        username_match = re.findall(username_pattern, env_data)[0]
        username_match = username_match.strip(" ")
        password_match = password_match.strip(" ")
        return username_match[0:],password_match[0:]


# Define driver, options, service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

project_path = os.getcwd()
prefs = {'download.default_directory': project_path}
chrome_options.add_experimental_option('prefs', prefs)

service = Service(project_path + "\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_field = driver.find_element(By.ID, 'login')

# Fill in username and password
username, password = get_credentials()
username_field.send_keys(username)
password_field.send_keys(password)
driver.execute_script("arguments[0].click();", login_field)

# locate the ELements dropdown and Text box
elements = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields and submit button
full_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'permanentAddress')))

submit_field = driver.find_element(By.ID, 'submit')

# Fill in the form fields
full_name_field.send_keys('John Smith')
email_field.send_keys('john.smith@gmail.com')
current_address_field.send_keys('John Street 100, New York, USA')
permanent_address_field.send_keys('John Street 100, New York, USA')

driver.execute_script('arguments[0].click();', submit_field)

# Locate the Upload and Download button and the Download button
upload_download = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'item-7')))
upload_download.click()

download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script('arguments[0].click();', download_button)


input("press enter to close")
driver.quit()