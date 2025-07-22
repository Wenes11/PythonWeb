#Usando xpath para coletar dados
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://ge.globo.com/futebol/brasileirao-serie-a/")
driver.find_elements(By.XPATH,'//div[@id="menu-curtain"]')

print(driver)