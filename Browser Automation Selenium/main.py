import re
import os
import time
from typing import Any

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_credentials() -> tuple[Any, Any]:
    with open(".env", "r") as env:
        env_data = env.read()
        username_pattern = re.compile("USERNAME =([^\n]+)")
        password_pattern = re.compile("PASSWORD =([^\n]+)")
        password_match = re.findall(password_pattern, env_data)[0]
        username_match = re.findall(username_pattern, env_data)[0]
        username_match = username_match.strip(" ")
        password_match = password_match.strip(" ")
        return username_match[0:],password_match[0:]

class WebAutomation:
    def __init__(self):
        # Define driver, options, service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        project_path = os.getcwd()
        prefs = {'download.default_directory': project_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service(project_path + "\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        pass

    def login(self, username, password):
        # Load the webpage
        self.driver.get("https://demoqa.com/login")

        # Locate username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_field = self.driver.find_element(By.ID, 'login')

        # Fill in username and password
        username, password = get_credentials()
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Pressing the login button
        self.driver.execute_script("arguments[0].click();", login_field)
        pass

    def fill_form(self, fullname, email, current_address, permanent_address):
        # locate the ELements dropdown and Text box
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements.click()

        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit button
        full_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))

        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        full_name_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)

        self.driver.execute_script('arguments[0].click();', submit_button)
        pass

    def download(self):
        # Locate the Upload and Download button and the Download button
        upload_download = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'item-7')))
        upload_download.click()

        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script('arguments[0].click();', download_button)
        time.sleep(1)
        pass

    def close(self):
        self.driver.quit()
        pass


if __name__ == "__main__":
    webautomation = WebAutomation()
    username, password = get_credentials()
    webautomation.login(username, password)
    webautomation.fill_form("John Smith", "John@gmail.com", "Street 1", "Street 2")
    webautomation.download()
    print("Finished, closing program...")
    webautomation.close()
