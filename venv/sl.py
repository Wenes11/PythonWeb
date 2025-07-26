from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://ge.globo.com/')

buton = driver.find_element(By.CSS_SELECTOR, '#header-produto > div.gui-color-primary-bg.header-principal.header-navegacao-color > div > div.menu-area > div > div')
buton.click()

select = Select(driver.find_element(By.CLASS_NAME, 'menu-container'))
print(select.select_by_visible_text)
#Arrumar esse codigo depois