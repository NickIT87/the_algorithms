# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


TEST_DATA = {
    "page_title": "SEARCH",
    "Name":"Марія",
}


def test_first():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000")
    input = driver.find_element(by=By.NAME, value='s')
    input.send_keys(TEST_DATA['Name'])
    submit_btn = driver.find_element(by=By.CLASS_NAME, value='btn') 
    submit_btn.click()
    h1 = driver.find_element(by=By.XPATH, value='/html/body/div/h1')
    assert h1.text == TEST_DATA['page_title']
    h3 = driver.find_element(by=By.XPATH, value='/html/body/div/h3')
    assert h3.text == TEST_DATA['Name']
