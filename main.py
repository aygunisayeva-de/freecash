from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import time

driver = webdriver.Chrome()

try:
    driver.get("https://freecash.com/de")

    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), \"Yes, I'm happy\")]"))
        )
        cookies_button.click()
    except (TimeoutException, ElementNotInteractableException):
        print("Cookies accept button not found or not interactable.")

    try:
        anmelden_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "chakra-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", anmelden_button)
        anmelden_button.click()

        modal = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "chakra-modal__body"))
        )

        email_field = WebDriverWait(modal, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "chakra-input"))
        )
        email_field.send_keys("test@email.com")

        password_field = WebDriverWait(modal, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password_field.send_keys("1234")

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'].chakra-button.css-1bkxg6o"))
        )

        submit_button.click()

    except TimeoutException:
        print("Email or password fields not found or modal did not appear.")
        driver.quit()
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
        exit()

    time.sleep(5)

finally:
    print("Test completed!")
    driver.quit()