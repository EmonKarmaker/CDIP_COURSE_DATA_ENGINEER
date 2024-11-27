\from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")
quotes = driver.find_element(By.CLASS_NAME, 'quote')
quotes