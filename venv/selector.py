#Usando xpath para coletar dados
from selenium import webdriver
from selenium.webdriver.common.by import By

#peguei um elemento muito especifico
driver = webdriver.Chrome()
driver.get('https://ge.globo.com/futebol/brasileirao-serie-a/')
table = driver.find_element(By.CSS_SELECTOR,'#classificacao__wrapper > article > section.tabela.tabela__pontos-corridos > div > table.tabela__equipes.tabela__equipes--com-borda > tbody > tr:nth-child(2)')
print(table.text)
    
    