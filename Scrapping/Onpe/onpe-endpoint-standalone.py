import lxml.html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime
from bs4 import BeautifulSoup
import schedule

CHROME_DRIVER = "/usr/bin/chromedriver"
ENDPOINT_URL = "https://api.resultadossep.eleccionesgenerales2021.pe/results/10/000000?name=param"
#URL = 'https://www.resultadossep.eleccionesgenerales2021.pe/SEP2021/EleccionesPresidenciales/RePres/T'

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument("--window-size=1200,800")
#options.add_argument('--headless')

def go_onpe():
    driver = webdriver.Chrome(CHROME_DRIVER, options=options)
    driver.get(ENDPOINT_URL)
    time.sleep(4)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')

    porcentaje_actas = ''
    cantidad_castillo = 0
    cantidd_keiko = 0

    porcentaje_actas = driver.find_element_by_xpath('//*[@id="imprimelo2"]/div[1]/div/ul/li[2]').text

    print(soup)

    diferencia = (cantidad_castillo - cantidd_keiko)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    msg = "Siendo las " + current_time + " " + porcentaje_actas + " Diferencia: " + str(diferencia)

    os.system('telegram-cli -W -e "msg Wadas_Axcess_Sec ' + msg + '"')
    os.system('telegram-cli -W -e "msg @shecatli ' + msg + '"')
    os.system('telegram-cli -W -e "msg FISI_2005 ' + msg + '"')
    os.system('telegram-cli -W -e "msg Sergio_William_Mejia_Guadamur ' + msg + '"')

go_onpe()