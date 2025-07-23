from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializa o driver
driver = webdriver.Chrome()

# Acessa o site do Brasileirão
driver.get("https://ge.globo.com/futebol/brasileirao-serie-a/")

# Aguarda carregamento da página (por segurança)

# Tenta encontrar o elemento com ID 'class'
table = driver.find_element(By.CLASS_NAME,'tabela tabela__pontos-corridos')
print(table.text)
# enta encontrar o elemento com ID name
# driver.find_element(By.NAME, '').get_property('')

# Verifica se encontrou algum elemento

# Espera 100 segundos antes de fechar
time.sleep(100)
