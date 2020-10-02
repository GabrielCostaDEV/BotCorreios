import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Bot:
    def __init__(self, codigos):
        self.codigos = codigos
        self.driver = webdriver.Firefox(executable_path = '/home/garga/Projetos/Python/Correios/geckodriver')
        self.driver.get('https://www2.correios.com.br/sistemas/rastreamento/default.cfm')      
        time.sleep(2)

        try:
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/font/strong')
            self.Bot(self.codigos)
        except:
            time.sleep(0)

        campo = self.driver.find_element_by_xpath('//*[@id="objetos"]')
        campo.click()
        campo.clear()
        
        for i in range (1, len(codigos), 2):
            campo.send_keys(codigos[i] + '; ')
    
        btn_buscar = self.driver.find_element_by_xpath('//*[@id="btnPesq"]')
        btn_buscar.click()

        time.sleep(5)

        try:
            self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[1]/td/div/font/strong')
            self.Bot(self.codigos)
        except:
            time.sleep(0)

        result = []
        
        cods = 1
        for i in range(0, int(len(codigos)/2)):
            result.append(self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[4]/div[1]/form/table/tbody/tr[' + str(cods) + ']/td[3]'))
            cods += 1            

        cods = 0
        print('{:^30} {:^30} {:^30}'.format('ITEM', 'CODIGO', 'SITUAÇÃO'))

        for i in range(1, len(codigos), 2):
            print('{:^30} {:^30} {:^30}'.format(codigos[i-1], codigos[i], result[cods].text))
            cods += 1


codigos = []
try:
    arquivo = open('Códigos.txt', 'r')

    for i in arquivo:
        codigos.append(i[:-1])

finally:        
    arquivo.close()    

robo = Bot(codigos)
