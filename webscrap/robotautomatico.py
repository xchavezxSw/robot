from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from xpathsfilesaltas import *
import datetime
#os.enviroment ("webdriver.chrome.driver", "D:\\BStackDemo\\chromedriver.exe");
os.environ['path'] = 'C:\\chromedriver\\chrome-win64\\chrome.exe'
ruta_del_controlador = "C:\\chromedriver\\chromedriver.exe"
# Crear una instancia del navegador Chrome con la ruta del controlador
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\claudio\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
chrome_options.binary_location = "C:\\chromedriver\\chrome-win64\\chrome.exe"
driver = webdriver.Chrome( chrome_options)
driver.get("https://1woqab.top/casino/play/aviator")
time.sleep(20)

iframes = driver.find_elements(By.TAG_NAME, 'iframe')
currency=''
# Cierra la conexión cuando ya no la necesites más

# Uso del script para enviar datos

for iframe in iframes:
    try:
        iframe_src = iframe.get_attribute('src')
        print(iframe.get_attribute('src'))
        if 'https://launch.spribegaming.com/aviator?currency=USD&lang=es&user=60437626_USD' in iframe_src:
            print("cambio")
            driver.switch_to.frame(iframe)
            currency='USD'
        if 'https://launch.spribegaming.com/aviator?currency=ARS&lang=es&user=60437626_ARS' in iframe_src:
            print("cambio")
            driver.switch_to.frame(iframe)
            currency = 'ARS'
    except:
        print("falla")
    #driver.switch_to.default_content()
# Localiza el elemento en la página (puedes utilizar otros métodos como find_element_by_id, find_element_by_name, etc.)
comparo=''
#seteo apuestas
cambio=True
while (cambio):
    try:
        if currency=='ARS':
        #me voy a seleccionar automatico
            boton = driver.find_element(By.XPATH, xpathButtonAutomatico)
            boton.click()

            #tildo el retiro auto
            boton = driver.find_element(By.XPATH, retiroautoswitch)
            boton.click()

            saldo = driver.find_element(By.XPATH, saldo)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(apuestoars)
            boton = driver.find_element(By.XPATH, xpathButtonAutomatico2)
            boton.click()

            # tildo el retiro auto
            boton = driver.find_element(By.XPATH, retiroautoswitch2)
            boton.click()

            saldo = driver.find_element(By.XPATH, saldo2)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(apuestoars2)

            retiroApuesta = driver.find_element(By.XPATH, xpathretiroApuesta)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(retiroApuestavalor)
            retiroApuesta2 = driver.find_element(By.XPATH, xpathretiroApuesta2)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(retiroApuestavalor2)
        if currency == 'USD':
            # me voy a seleccionar automatico
            boton = driver.find_element(By.XPATH, xpathButtonAutomaticoUsd)
            boton.click()

            # tildo el retiro auto
            boton = driver.find_element(By.XPATH, retiroautoswitchUsd)
            boton.click()

            saldo = driver.find_element(By.XPATH, saldoUsd)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(apuestoUsd)
            boton = driver.find_element(By.XPATH, xpathButtonAutomatico2Usd)
            boton.click()

            # tildo el retiro auto
            boton = driver.find_element(By.XPATH, retiroautoswitch2Usd)
            boton.click()

            saldo = driver.find_element(By.XPATH, saldo2Usd)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(Keys.BACK_SPACE)
            saldo.send_keys(apuestoars2Usd)

            retiroApuesta = driver.find_element(By.XPATH, xpathretiroApuestaUsd)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(Keys.BACK_SPACE)
            retiroApuesta.send_keys(retiroApuestavalorUsd)
            retiroApuesta2 = driver.find_element(By.XPATH, xpathretiroApuesta2Usd)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(Keys.BACK_SPACE)
            retiroApuesta2.send_keys(retiroApuestavalor2Usd)
        cambio=False
    except:
        cambio=True
time.sleep(1)
indice=0
entre=0
aposte=0
saldo_inicio=driver.find_element(By.XPATH, xpathsaldoActual).text

while (True):
    time.sleep(1)
    saldo_actual = driver.find_element(By.XPATH, xpathsaldoActual).text
    saldoahora=float(saldo_actual)-float(saldo_inicio)
    elemento =driver.find_element(By.XPATH, xpathNuevo).text
    elemento1 =driver.find_element(By.XPATH, xpathNuevo1).text
    elemento2 =driver.find_element(By.XPATH, xpathNuevo2).text
    elemento3 =driver.find_element(By.XPATH, xpathNuevo3).text
    elemento4 = driver.find_element(By.XPATH, xpathNuevo4).text
    elemento5 = driver.find_element(By.XPATH, xpathNuevo5).text
    # Imprime el XPath del elemento
    if comparo !=elemento+elemento1+elemento2+elemento3:
        print("XPath del elemento:", elemento)
        print("XPath del elemento:", elemento1)
        print("XPath del elemento:", elemento2)
        print("XPath del elemento:", elemento3)
        print("=========================================")
        hora_actual = datetime.datetime.now()
        comparacion1 = elemento.lower().replace("x", '').strip()+"|"
        comparacion2 = elemento1.lower().replace("x", '').strip()
        comparacion3 = elemento2.lower().replace("x", '').strip()
        comparacion4 = elemento3.lower().replace("x", '').strip()
        comparacion5 = elemento4.lower().replace("x", '').strip()
        comparacion6 = elemento5.lower().replace("x", '').strip()

        if  float(hora_actual.hour) not in (14.00,15.00,16.00,17.00,18.00):
            # Tu código a ejecutar
            if indice >=4:
                if aposte==1:
                    print("saldo Ganado:" + str(saldoahora))
                    aposte=0
                    indice = 0
                    if float(comparacion1) <= 1.50:
                        if float(comparacion1) > 1.20:
                            boton = driver.find_element(By.XPATH, xpathButtonApuesta2)
                            boton.click()
                    if float(comparacion1) >= 1.51:
                        print("se gano:"+str(comparacion1))
                    else:
                        print("se perdio:" + str(comparacion1))

                if comparacion1 !='':
                    """baja,alta,baja,alta,alta"""
                    if float(comparacion4) >= float(2):
                        if float(comparacion3) < float(2):
                            if float(comparacion2) >= float(2.00):
                                if float(comparacion1) < float(2):
                                    """if float(comparacion1) < float(30):
                                        if float(comparacion2) < float(30):
                                            if float(comparacion3) < float(30):
                                                if float(comparacion4) < float(30):"""
                                    print("apuesto-"+str(comparacion1)+"-"+str(comparacion2))
                                    aposte=1
                                    boton = driver.find_element(By.XPATH, xpathButtonApuesta)
                                    boton.click()
                                    boton = driver.find_element(By.XPATH, xpathButtonApuesta2)
                                    boton.click()
            indice=indice+1
        else:
            print("Fuera del intervalo de tiempo")
    comparo = elemento + elemento1 + elemento2 + elemento3


s.close()