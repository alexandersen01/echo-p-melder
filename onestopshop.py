import time 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

arrangement = input('Enter the url of the arrangement: ')
student_email = input('Enter your username: ')
password = input('Enter your password: ')

# arrangement = 'https://echo.uib.no/arrangement/genvors-2'

driver = webdriver.Chrome()

driver.get(arrangement)

try:
    button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/auth/logg-inn"]'))
    )
    button1.click()
    
    print('button1 clicked')
    
    time.sleep(1)
    button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,  '//button[@type="button"]'))
    )
    button2.click()
    time.sleep(1)
    print('button2 clicked')

    #type 'uni'
    input1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'org_selector_filter'))
    )
    input1.send_keys('university of bergen')

    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    
    print('feide login ready')

    microsoft_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,  'microsoft-signin-button'))
    )
    microsoft_login.click()
    print('microsoft login initiated')
    time.sleep(3)
    ActionChains(driver).send_keys(student_email).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    ActionChains(driver).send_keys(password).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    print('microsoft login done')
    time.sleep(2)

    driver.get(arrangement)

    one_click = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//span[text()="One-click påmelding"]'))
    )
    time.sleep(0.5)
    one_click.click()
    print('one click done\nggwp')
    time.sleep(5)
except:
    driver.quit()
