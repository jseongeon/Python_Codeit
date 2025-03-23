from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
options.binary_location = "./chromedriver"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


# 티켓 예매 페이지
driver.get('http://localhost:5500/0101_web_automation/ticket-site/index.html')
date_element = driver.find_element(
    By.CSS_SELECTOR, '[data-date="2025-08-18 (월)"]')
date_element.click()
time_element = driver.find_element(By.CSS_SELECTOR, '[data-time="19:30"]')
time_element.click()
submit_element = driver.find_element(By.CSS_SELECTOR, '#book-button')
submit_element.click()

# 로그인 페이지
wait.until(EC.url_matches('/login'))
username_element = driver.find_element(By.CSS_SELECTOR, '#username')
password_element = driver.find_element(By.CSS_SELECTOR, '#password')
username_element.send_keys('codeit')
password_element.send_keys('love2learn')
submit_element2 = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
submit_element2.click()

# 좌석 선택 페이지
wait.until(EC.url_matches('/seat'))
seat_element = driver.find_element(By.CSS_SELECTOR, '[data-seat="r"]')
seat_element.click()
submit_element3 = driver.find_element(By.CSS_SELECTOR, '#book-button')
submit_element3.click()

# 예매 완료 페이지
sleep(5)
