from select import select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(executable_path='drivers/geckodriver')
driver.get('https://docs.ozon.ru/global/commissions/ozon-fees/commissions/?country=OTHER')
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, "//article[@class='markdown markdown--article']/div[1]/p[1]").text
print(element)
driver.quit()