import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#sample test with fixture:
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    

def test_sample(driver):
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    name = "Rahul"
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
    driver.find_element(By.ID, "alertbtn").click()
    time.sleep(5)
    alert = driver.switch_to.alert
    alertText = alert.text
    print(alertText)
    assert name in alertText
    alert.accept()
    #alert.dismiss()



    