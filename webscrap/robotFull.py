from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from xpathsfiles import *
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
for iframe in iframes:
    try:
        iframe_src = iframe.get_attribute('src')
        if 'https://launch.spribegaming.com/aviator?currency=ARS&lang=es&user=60437626_ARS' in iframe_src:
            print("cambio")
            driver.switch_to.frame(iframe)
    except:
        print("falla")
    #driver.switch_to.default_content()
# Localiza el elemento en la página (puedes utilizar otros métodos como find_element_by_id, find_element_by_name, etc.)
comparo=''
#seteo apuestas
cambio=True
while (cambio):
    try:
        #me voy a seleccionar automatico
        boton = driver.find_element(By.XPATH, xpathButtonAutomatico)
        boton.click()
        time.sleep(1)

        #tildo el retiro auto
        boton = driver.find_element(By.XPATH, retiroautoswitch)
        boton.click()
        time.sleep(1)

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
        time.sleep(1)
        boton = driver.find_element(By.XPATH, xpathButtonAutomatico2)
        boton.click()
        time.sleep(1)

        # tildo el retiro auto
        boton = driver.find_element(By.XPATH, retiroautoswitch2)
        boton.click()
        time.sleep(1)

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
        cambio=False
    except:
        cambio=True
time.sleep(1)
indice=0
entre=0
while (True):
    time.sleep(1)
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
        comparacion1 = elemento.lower().replace("x", '').strip()
        comparacion2 = elemento1.lower().replace("x", '').strip()
        comparacion3 = elemento2.lower().replace("x", '').strip()
        comparacion4 = elemento3.lower().replace("x", '').strip()
        comparacion5 = elemento4.lower().replace("x", '').strip()
        comparacion6 = elemento5.lower().replace("x", '').strip()
        if indice >=3:
            if comparacion1 !='':
                if float(comparacion1) >= float(2):
                    if float(comparacion2) >= float(2):
                        if float(comparacion3) <= float(2.00):
                            print("apuesto-"+str(comparacion1)+"-"+str(comparacion2))
                            boton = driver.find_element(By.XPATH, xpathButtonApuesta)
                            boton.click()
                            boton = driver.find_element(By.XPATH, xpathButtonApuesta2)
                            boton.click()
                            entre=0
                if float(comparacion1) >= float(2):
                    if float(comparacion2) >= float(2):
                        if float(comparacion3) < float(1.51):
                            if float(comparacion4) < float(1.51):
                                if float(comparacion5) < float(1.51):
                                    print("apuesto-"+str(comparacion1)+"-"+str(comparacion2))
                                    boton = driver.find_element(By.XPATH, xpathButtonApuesta)
                                    boton.click()
                                    boton = driver.find_element(By.XPATH, xpathButtonApuesta2)
                                    boton.click()
                                    entre=0
                if float(comparacion1) < float(1.90):
                    if float(comparacion2) < float(1.90):
                        if float(comparacion3) < float(1.90):
                            if float(comparacion4) < float(1.90):
                                if float(comparacion5) < float(1.90):
                                    if entre==0:
                                        print("apuesto")
                                        """boton = driver.find_element(By.XPATH, xpathButtonApuesta)
                                        boton.click()
                                        boton = driver.find_element(By.XPATH, xpathButtonApuesta2)
                                        boton.click()"""
                                        entre=1
        indice=indice+1

    comparo = elemento + elemento1 + elemento2 + elemento3


