from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait(by,search_value):
    global driver
    if by=='class':
        if ' ' in search_value:
            search_value = search_value.replace(' ', '.')
        element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.CLASS_NAME, search_value)))
        elements=driver.find_elements(by=By.CLASS_NAME,value=search_value)
    elif by=='tag':
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.TAG_NAME, search_value)))
        elements = driver.find_elements(by=By.TAG_NAME, value=search_value)
    elif by=='css':
        element = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, search_value)))
        elements = driver.find_elements(by=By.CSS_SELECTOR, value=search_value)
    if len(elements)==1:
        return element
    else:
        print(f"The element {search_value} is not unique")

def open_whatsapp():
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=myflaskapp\userData")
    #options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    global driver
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")


def send_message(name,message):
    #driver.minimize_window()
    text_box=wait('class',"_2vDPL")
    elements=text_box.find_elements(by=By.TAG_NAME, value='div')
    goal=elements[1]
    goal.send_keys(name)
    sleep(3)
    element = wait('css', 'div[style*="transform: translateY(72px);"]')
    element.click()
    element=wait('css','div[title="Scrivi un messaggio"]')
    element.send_keys(message)
    element.send_keys(Keys.RETURN)
    sleep(10)

def close_driver():
    global driver
    driver.quit()