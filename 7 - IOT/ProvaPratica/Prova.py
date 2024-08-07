from machine import ADC,Pin
import time
import dht
import urequests
import ujson
import network

nome = "Wallace"
senha = "ola12345"

FIREBASE_URL = "https://iiot-7276b-default-rtdb.firebaseio.com/"
SECRET_KEY = ""




dht_sensor = dht.DHT11(Pin(12))
ledVerde = Pin(13,Pin.OUT)
ledAmarelo = Pin(14,Pin.OUT)
ledVermelho = Pin(27,Pin.OUT)
ledDados = Pin(26,Pin.OUT)

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

def read_dht11():
    while True:
        try :
            dht_sensor.measure()
            temp = dht_sensor.temperature()
            hum = dht_sensor.humidity()
            print(f"Temperatura: {temp}\nUmidade: {hum}")
        except OSError as e:
                  print("falha na leitura do sensor:",e)
        time.sleep(2)
        
while True:
    try :
        ledDados.on()
        conectarWifi()
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        if temp < 25:
            ledVerde.on()
            ledAmarelo.off()
            ledVermelho.off()
        elif ((temp > 25) and (temp < 27)):
            ledAmarelo.on()
            ledVerde.off()
            ledVermelho.off()
        elif temp > 27 :
            ledVermelho.on()
            ledAmarelo.off()
            ledVerde.off()
        else:
            print("Erro de IO")
        informacao = {
            "Temperatura": temp,
            "Umidade": hum
        }
        enviarFire(informacao)
    except OSError as e:
        print("falha na leitura do sensor:",e)
    time.sleep(2)
    ledDados.off()
    time.sleep(28)
    