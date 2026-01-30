import re

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
service = Service("C:\\Users\\matok\\PycharmProjects\\Python Mega Course\\Browser Automation Selenium\\chromedriver-win64"
                  "\\chromedriver.exe")
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


input("press enter to close")
driver.quit()