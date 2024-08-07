from machine import Pin, PWM
import random
import time
import urequests
import ujson
import network
import dht
import _thread
dht_sensor = dht.DHT11(Pin(15))



#Credenciais do WIFI
nome = "Wallace"
senha = "ola12345"

# Endereço do firebase
FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"
SECRET_KEY = ""

proxies = {'https': "http://disrct:etsps2024401@10.224.200.26:8080"}
wallace = "https://iiot-7276b-default-rtdb.firebaseio.com/.json"
def conectarWifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando no WiFi...")
        wlan.connect(nome, senha)
        while not wlan.isconnected():
            pass
    print("Wifi conectado... IP: {}".format(wlan.ifconfig()[0]))

def enviarFire(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
    url = FIREBASE_URL + "/wallace.json"  # Coloque o seu nome

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()

def receberFire():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + SECRET_KEY
    }
    url = FIREBASE_URL + "/Wallace.json" 
    response = urequests.get(url, headers=headers)
    Json = ujson.loads(response.text)
    response.close()
    
    return Json



buttomBlue = Pin(13, Pin.IN)
buttomGreen = Pin(12, Pin.IN)
buttomYellow = Pin(14, Pin.IN)
buttomRed = Pin(27, Pin.IN)

ledBlue = Pin(26, Pin.OUT)
ledGreen = Pin(25, Pin.OUT)
ledYellow = Pin(33, Pin.OUT)
ledRed = Pin(32, Pin.OUT)

barulho = Pin(4,Pin.OUT)
rodada = 1
ordem = []
gameOver = 0
pts = 0

# while gameOver == 0:
#     ordem.append(random.randint(1, 4))
#     print(ordem)
#     for i in range(rodada):
#         if ordem[i] == 1:
#             ledBlue.on()
#             barulho.on()
#             time.sleep(0.5)
#             barulho.off()
#             ledBlue.off()
#             
#         elif ordem[i] == 2:
#             ledGreen.on()
#             barulho.on()
#             time.sleep(0.5)
#             ledGreen.off()
#             barulho.off()
#             
#         elif ordem[i] == 3:
#             ledYellow.on()
#             barulho.on()
#             time.sleep(0.5)
#             ledYellow.off()
#             barulho.off()
#             
#         elif ordem[i] == 4:
#             ledRed.on()
#             barulho.on()
#             time.sleep(0.5)
#             ledRed.off()
#             barulho.off()
#         time.sleep(0.5)
#     
#     for i in range(rodada):
#         while True:
#             if buttomBlue.value() == 1:
#                 click = 1
#                 ledBlue.on()
#                 time.sleep(0.5)
#                 ledBlue.off()
#                 break
# 
#             elif buttomGreen.value() == 1:
#                 click = 2
#                 ledGreen.on()
#                 time.sleep(0.5)
#                 ledGreen.off()
#                 break
# 
#             time.sleep(0.1)
#         
#         if click != ordem[i]:
#             gameOver = 1
#             pts = rodada - 1 
#             break
#     rodada += 1
#     time.sleep(1)
# print("Voce perdeu")  elif buttomYellow.value() == 1:
#                 click = 3
#                 ledYellow.on()
#                 time.sleep(0.5)
#                 ledYellow.off()
#                 break
# 
#             elif buttomRed.value() == 1:
#                 click = 4
#                 ledRed.on()
#                 time.sleep(0.5)
#                 ledRed.off()
#                 break
#             time.sleep(0.1)
#         
#         if click != ordem[i]:
#             gameOver = 1
#             pts = rodada - 1 
#             break
#     rodada += 1
#     time.sleep(1)
# print("Voce perdeu")


conectarWifi()
# try :
#     informacao = {
#             "jogador" : "Wallace",
#             "Pontuacao" : int(pts)
#     }
#     enviarFire(informacao)
# except OSError as e:
#     print("falha na leitura do sensor:",e)
#     time.sleep(0.5)
def FuncaoA():
    while True:
        lampada = receberFire()
        print(lampada)
#         lampadakey = list(lampada.keys())
#         lampadavalues = list(lampada.values())
#     #     print(lampadakey)
#     #     print(lampadavalues)
#     #     print(lampada)
#         if lampadakey[0] == 'RedStatus' and lampadavalues[0] == 1:
#              ledRed.on()
#         elif lampadakey[0] == 'RedStatus' and lampadavalues[0] == 0:
#              ledRed.off()
#         elif lampadakey[0] == 'GreenStatus' and lampadavalues[0] == 1:
#              ledGreen.on()
#         elif lampadakey[0] == 'GreenStatus' and lampadavalues[0] == 0:
#              ledGreen.off()
#         elif lampadakey[0] == 'YellowStatus' and lampadavalues[0] == 1:
#              ledYellow.on()
#         elif lampadakey[0] == 'YellowStatus' and lampadavalues[0] == 0:
#              ledYellow.off()
        time.sleep(1)

def FuncaoB():
    while True:
        try :
            dht_sensor.measure()
            temp = dht_sensor.temperature()
            hum = dht_sensor.humidity()
            inf = {
                "Temperatura" : temp,
                "Umidade" : hum
                }
            enviarFire(inf)
        except OSError as e:
            print("falha na leitura do sensor:",e)
        time.sleep(2)
 
 

while True:
    
    lampada = receberFire()
    print(lampada)
    lampadakey = list(lampada.keys())
    lampadavalues = list(lampada.values())
    if lampadakey[0] == 'RedStatus' and lampadavalues[0] == 1:
        ledRed.on()
    elif lampadakey[0] == 'RedStatus' and lampadavalues[0] == 0:
        ledRed.off()
    elif lampadakey[0] == 'GreenStatus' and lampadavalues[0] == 1:
        ledGreen.on()
    elif lampadakey[0] == 'GreenStatus' and lampadavalues[0] == 0:
        ledGreen.off()
    elif lampadakey[0] == 'YellowStatus' and lampadavalues[0] == 1:
        ledYellow.on()
    elif lampadakey[0] == 'YellowStatus' and lampadavalues[0] == 0:
        ledYellow.off()    
    time.sleep(0.1)
    try :
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        inf = {
            "Temperatura" : temp,
            "Umidade" : hum
            }
        enviarFire(inf)
    except OSError as e:
        print("falha na leitura do sensor:",e)
    time.sleep(0.1)
 


    
    
    