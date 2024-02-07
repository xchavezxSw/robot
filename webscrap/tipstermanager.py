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
driver.get("https://app.tipmanager.net/casino-bot/aviator/last-results")
driver.add_cookie({"name":"supabase-auth-token","value": "%5B%22eyJhbGciOiJIUzI1NiIsImtpZCI6Imlrb0I1Ulc0VFlkREJrVkYiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzA3ODgzODcxLCJpYXQiOjE3MDcyODM4NzEsImlzcyI6Imh0dHBzOi8vam51cnhlenNwbGV1Zmlvb3lla3cuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6Ijg4YTBlYTk5LWZkMWQtNDY2Ni05NWY3LTFkYjhjOTcxMjdmMCIsImVtYWlsIjoiY2xhdWRpby54LnBjQGdtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsibmFtZSI6ImNsYXVkaW8gY29yZG9iYSJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6InBhc3N3b3JkIiwidGltZXN0YW1wIjoxNzA3MjgzODcxfV0sInNlc3Npb25faWQiOiIwMDNhMWFiMC00YjdjLTQyOTUtOTZiZi1lOTc1ZDQzMzQ5ZTMifQ.QOgn_5adnFiEKsj0NN_qkAaFQSJBY21gGdLHusHYWAo%22%2C%22oQONdnAYEYSv3VvC6eJJQw%22%2Cnull%2Cnull%5D","domain":"app.tipmanager.net"})
#driver.refresh()
iframes = driver.find_elements(By.TAG_NAME, 'iframe')

currency=''
# Cierra la conexión cuando ya no la necesites más
print(iframes)
# Uso del script para enviar datos
time.sleep(15)
try:
    while(True):
        for i in range(300):
            i=i+1
            saldo = driver.find_element(By.XPATH,                                """//*[@id="__next"]/div/main/div/div/div[2]/div[1]/div[2]/div[2]/div["""+str(i)+"""]/div/h6""")
            hora = driver.find_element(By.XPATH,"""//*[@id="__next"]/div/main/div/div/div[2]/div[1]/div[2]/div[2]/div[""" + str(i) + """]/h6""")
            print({"coeficiente": saldo.text, "hora": hora.text})
        botonProxima = driver.find_element(By.XPATH,"""//*[@id="__next"]/div/main/div/div/div[2]/div[1]/div[2]/div[3]/div/div/button[2]""")
        botonProxima.click()
        time.sleep(2)

except:
    print("fallo")


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

time.sleep(20000)
#driver.get("https://app.tipmanager.net/casino-bot/aviator/last-results")

#print(saldo.text)
