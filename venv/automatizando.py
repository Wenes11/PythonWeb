from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://ge.globo.com/')

lupa = driver.find_element(By.CSS_SELECTOR, '#header-produto > div.gui-color-primary-bg.header-principal.header-navegacao-color > div > div > div.search-area.header-navegacao-color')
lupa.click()

time.sleep(2)

buscar = driver.find_element(By.NAME,'q')

enviar = driver.find_element(By.CSS_SELECTOR,'#frmBusca > fieldset > button')

buscar.send_keys(Keys.ENTER)
buscar.send_keys('flamengo')

buscar.click()
buscar.send_keys(Keys.ENTER)

time.sleep(200)
# Nesse codigo estou tentando automatizar preenchimento, quando eu rodo, ele vai na pagina do GE, depois que me informa um erro, mas quando eu clico no buscar ele simples não roda

