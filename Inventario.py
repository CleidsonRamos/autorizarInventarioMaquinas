from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
import time # biblioteca utilizada na função sleep
import random # biblioteca utiliza na função para gerar um numero aleatorio
from datetime import datetime # mostra data
import ctypes # biblioteca utilizada para mostrar um alerta

# abre o chrome
driver = webdriver.Chrome('C:\Python39\Scripts\chromedriver.exe')

# acessa o sistema de inventário
driver.get('https://arfacieg.acsoluti.com.br/inventario-maquina/autorizar-inventario')

# clica no botão Usar Certificado Digital
driver.find_element_by_id('precert').click()

# mostra uma mensagem de alerta informado para digitar a senha manualmente
print("Selecione o certificado e digite a senha", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
ctypes.windll.user32.MessageBoxW(0, "Selecione o certificado e digite a senha e aguarde 20 segundos", "Certificado", 1)

print("aguarde 20 segundos", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
time.sleep(20)

def buscar():
    print("estou no metodo buscar", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    buscar_filtrar = driver.find_element_by_id('formsubmit_label')
    buscar_filtrar.click()
    print("estou no metodo buscar e aguardando 10 seg.", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    time.sleep(10)
    autorizar()

def autorizar():
    try:
        # procura o botão autorizar
        autorizar = driver.find_element_by_xpath("//button[contains(text(),'Autorizar')]")

        #clica no botão autorizar
        autorizar.click()
        time.sleep(5)
        driver.find_element_by_id('check1').click() # marca o checkbox
        driver.find_element_by_id('check2').click() # marca o checkbox
        driver.find_element_by_id('check3').click() # marca o checkbox
        driver.find_element_by_id('check4').click() # marca o checkbox
        driver.find_element_by_id('check5').click() # marca o checkbox
        driver.find_element_by_id('check6').click() # marca o checkbox
        driver.find_element_by_id('check7').click() # marca o checkbox
        driver.find_element_by_id('check8').click() # marca o checkbox
        driver.find_element_by_id('check9').click() # marca o checkbox
        driver.find_element_by_id('check10').click() # marca o checkbox
        driver.find_element_by_id('check11').click() # marca o checkbox

        # clica no botão sim
        driver.find_element_by_xpath("//button[contains(text(),'SIM')]").click()
        
        time.sleep(10)
        buscar() #depois de aprovar volta a atualizar
    
    # caso não encontre o botão autorizar, volta para o metodo buscar
    except NoSuchElementException:
        print("Não foi encontrado o botão autorizar." ,datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

        # gera um numero aleatorio que vai de 2 minutos a 5 minutos
        aguarde = random.randrange(120, 300)

        print("estou dentro do exception e aguardando", str(aguarde)," segundos.", datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        time.sleep(aguarde) 
        buscar() # voltar para o metodo buscar

buscar()