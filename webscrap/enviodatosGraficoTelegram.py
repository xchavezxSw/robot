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
telegram=True

def enviomensaje(mensaje):
    if telegram:
        import requests
        api_id = 4679304
        api_hash = '1c1d636554bcbc5847c04dfc5cff96b0'
        #

        # Token del bot proporcionado por BotFather
        bot_token = '6856641360:AAGgxX5sh-UfC3tnudgLSU6mC5rh8-3XcWA'

        # ID del chat al que deseas enviar el mensaje
        chat_id = '-1002126842562'

        # Mensaje que deseas enviar

        # URL de la API de Telegram para enviar mensajes
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

        # Parámetros del mensaje
        params = {
            'chat_id': chat_id,
            'text': mensaje
        }

        # Envía la solicitud POST a la API de Telegram
        response = requests.post(url, json=params)

        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            print('Mensaje enviado exitosamente!')
        else:
            print('Error al enviar el mensaje:', response.text)
enviomensaje("asd")
time.sleep(20)

iframes = driver.find_elements(By.TAG_NAME, 'iframe')
currency=''
import socket
def enviar_datos(socket_envio, datos):
    # Envía cada dato en la lista
        print(datos.replace("x",""))
        socket_envio.sendall(str(datos).encode())

# Configura el socket
HOST = 'localhost'  # La dirección IP del servidor
PORT = 65432  # El puerto utilizado por el servidor

# Crea el socket y establece la conexión
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Llama a la función enviar_datos con el socket y los datos que deseas enviar

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
indice=0
entre=0
aposte=0
saldo_inicio=driver.find_element(By.XPATH, xpathsaldoActual).text
boton = driver.find_element(By.XPATH, "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[3]/div/div/div[1]")
boton.click()
#26,25,24,23,22,21,20,19,18,17
for i in [30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2]:
    try:
        xpathNuevo8 =  "/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-bubble-multiplier["+str(i)+"]/div"
        elemento9 = driver.find_element(By.XPATH, xpathNuevo8).text
        if elemento9 =='':
            xpathNuevo8="/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/app-stats-dropdown/div/div[2]/div["+str(i)+"]/div/app-bubble-multiplier/div"
        elemento9 = driver.find_element(By.XPATH, xpathNuevo8).text
        comparacion9 = elemento9.lower().replace("x", '').strip()+"|"
        if comparacion9 != '|':
            enviomensaje("el coeficiente que salio es:"+comparacion9.replace("x", '').replace("|", '').strip())
            enviar_datos(s, comparacion9)
    except:
        None
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
        enviar_datos(s, comparacion1)
        enviomensaje("el coeficiente que salio es:" + comparacion1.replace("x", '').replace("|", '').strip())
        comparacion2 = elemento1.lower().replace("x", '').strip()
        comparacion3 = elemento2.lower().replace("x", '').strip()
        comparacion4 = elemento3.lower().replace("x", '').strip()
        comparacion5 = elemento4.lower().replace("x", '').strip()
        comparacion6 = elemento5.lower().replace("x", '').strip()
    comparo = elemento + elemento1 + elemento2 + elemento3


s.close()