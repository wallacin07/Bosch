from machine import ADC,Pin
import time
import dht
dht_sensor = dht.DHT11(Pin(12))


def pulse_enable():
    e.on()
    time.sleep_us(1)
    e.off()
    time.sleep_us(50)

def send_nibble(data):
    d4.value((data >> 0) & 1)
    d5.value((data >> 1) & 1)
    d6.value((data >> 2) & 1)
    d7.value((data >> 3) & 1)
    pulse_enable()

def send_byte(data, rs_value):
    rs.value(rs_value)
    send_nibble(data >> 4)  # Send upper nibble
    send_nibble(data & 0x0F)  # Send lower nibble

def lcd_command(cmd):
    send_byte(cmd, 0)

def lcd_data(data):
    send_byte(data, 1)

def lcd_init():
    time.sleep(0.05)
    rs.off()
    e.off()
    send_nibble(0x03)
    time.sleep_ms(5)
    send_nibble(0x03)
    time.sleep_us(150)
    send_nibble(0x03)
    send_nibble(0x02)
    lcd_command(0x28)  # Function set: 4 bits, 2 lines, 5x8 dots
    lcd_command(0x0C)  # Display on, cursor off, blink off
    lcd_command(0x06)  # Entry mode set: increment & no shift
    lcd_command(0x01)  # Clear display
    time.sleep_ms(2)

def lcd_puts(text):
    for char in text:
        lcd_data(ord(char))

def lcd_goto(linha, coluna):
    if (linha < 0 or linha > 1) or (coluna < 0):
        print("Invalid line or column. Ignoring goto command.")
        return

    if linha == 0:
        max_coluna = 14  
    else:
        max_coluna = 15  
    if coluna > max_coluna:
        coluna = max_coluna

    
    address = (linha * 0x40) + coluna  
    lcd_command(0x80 | address)  


def create_char(location,charmap):
    location &= 0x7
    send_byte(0x40|(location << 3),False)
    for i in range(8):
        send_byte(charmap[i],True)

def read_potentiometer():
    while True:
        port_value= adc.read()
        time.sleep(0.2)
        print("Valor do potenciometro: ", port_value)
        digital_Signal = ((port_value/4095)*10000)
        lugar_numero = int(digital_Signal/322)
        print("Valor do potenciometro digital: ", round(digital_Signal))
        print("numero: ", round(lugar_numero))
        if lugar_numero > 15:
            segunda_linha = lugar_numero-16
            lcd_command(0x01)
            time.sleep(0.02)
            lcd_command(0x80 | (0x40 * 1)+ segunda_linha)
            lcd_puts(str(1))
        else:
            lcd_command(0x01)
            time.sleep(0.02)
            lcd_command(0x80 | (0x40 * 0)+ lugar_numero)
            lcd_puts(str(1))

def read_lightSensor():
    while True :
        sensorLight = light.value()
        
        print("sensor:", sensorLight)
        time.sleep(0.15)
        
def read_dht11():
    while True:
        try :
            dht_sensor.measure()
            temp = dht_sensor.temperature()
            hum = dht_sensor.humidity()
        except OSError as e:
                  print("falha na leitura do sensor:",e)
        time.sleep(2)
        
# # read_potentiometer()
# read_lightSensor()
read_dht11()