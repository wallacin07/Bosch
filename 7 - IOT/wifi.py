import urequests
import ujson
import network
from machine import ADC,Pin
import time
import dht

dht_sensor = dht.DHT11(Pin(12))
#Credenciais do WIFI
nome = "Wallace"
senha = "ola12345"

# Endereço do firebase
FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"
SECRET_KEY = ""

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
    url = FIREBASE_URL + "/Wallace.json"  # Coloque o seu nome

    response = urequests.put(url, data=ujson.dumps(data), headers=headers)
    print("Firebase Response:", response.text)
    response.close()

informacao = {
    "Deu": "Certo"
}

conectarWifi()
while True:
    try :
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        informacao = {
            "Temperatura": temp,
            "Humidade": hum
        }
        enviarFire(informacao)
    except OSError as e:
        print("falha na leitura do sensor:",e)
    time.sleep(0.5)
