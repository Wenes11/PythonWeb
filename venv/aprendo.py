# Importa as bibliotecas necessárias:
# - selenium para automação do navegador
# - time para adicionar pausas no script
from selenium import webdriver
import time

# Inicializa o driver do Chrome (abre o navegador)
driver = webdriver.Chrome()

# Aguarda 10 segundos antes de prosseguir (útil para testes e depuração)
time.sleep(10)

# Acessa a página desejada (neste caso, o site de esportes da Globo)
driver.get("https://google.com/")

# Captura de titulo da pagina
print(driver.title)

# Captura de titulo da url da pagina
print(driver.current_url)
time.sleep(10)

#Coloca o navegador fullscreen, mas pode ser modificada
driver.fullscreen_window()

# Coleta a posição da pagina e tambem permite a modificação
print(driver.get_window_rect())

# Coleta todo contuedo html
print(driver.page_source)


# esse comando recarrega a pagina
driver.refresh() 

#Esse comando volta a pagina interior
driver.back()

#Esse comando avança a para a frente até a ultima pagina
driver.forward()

# Fecha o navegador e encerra a sessão do WebDriver
driver.quit()
 

