#Usando xpath para coletar dados
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://ge.globo.com/futebol/brasileirao-serie-a/")
table = driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div/section[1]/article/section[1]/div/table[1]')
table_lines = table.find_elements(By.CLASS_NAME,'classificacao__tabela--linha')
clubs = []

for line in table_lines:
    club_name = line.find_element(By.CLASS_NAME, 'classificacao__equipes.classificacao__equipes--nome').get_attribute('innerHTML')
    clubs.append(club_name)

print(clubs)
