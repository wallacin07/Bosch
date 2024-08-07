from machine import Pin
import time

# Configuration of LCD pins (assuming your connections match)
rs = Pin(14, Pin.OUT)
e = Pin(13, Pin.OUT)
d4 = Pin(12, Pin.OUT)
d5 = Pin(27, Pin.OUT)
d6 = Pin(26, Pin.OUT)
d7 = Pin(25, Pin.OUT) 
buttom = Pin(32,Pin.IN)
num = 0;
contador = 16
posicaoPlayer = [1,1]
posicaoMissil = [1,15]
pontuação = 0

Missil = [
  0b00000,
  0b00000,
  0b00100,
  0b01000,
  0b10111,
  0b01000,
  0b00100,
  0b00000
]


Cara_normal = [
  0b00100,
  0b01010,
  0b00100,
  0b00100,
  0b11111,
  0b00100,
  0b01010,
  0b10001]

Cara_pulando = [
  0b00100,
  0b01010,
  0b00101,
  0b01110,
  0b10100,
  0b00100,
  0b01010,
  0b10001
]

bolinhaPequena = [
  0b00000,
  0b00000,
  0b00000,
  0b00100,
  0b01110,
  0b00100,
  0b00000,
  0b00000
]

bolinhaGrande = [
  0b00000,
  0b00000,
  0b00100,
  0b01110,
  0b11111,
  0b01110,
  0b00100,
  0b00000
]

pequenaExplosao = [
  0b01000,
  0b11100,
  0b01000,
  0b00010,
  0b00111,
  0b00010,
  0b01000,
  0b11100
]



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


def explosao():
    
    create_char(7,bolinhaPequena)
    create_char(8,bolinhaGrande)
    create_char(9,pequenaExplosao)
    lcd_command(0x80 | (posicaoPlayer[0]*0x40)+posicaoPlayer[1])
    time.sleep_ms(500)
    send_byte(0x07,True)
    time.sleep_ms(500)
    lcd_command(0x80 | (posicaoPlayer[0]*0x40)+posicaoPlayer[1])
    time.sleep_ms(5)
    send_byte(0x08,True)
    lcd_command(0x80 | (posicaoPlayer[0]*0x40)+posicaoPlayer[1])
    time.sleep_ms(500)
    send_byte(0x09,True)
    time.sleep_ms(5)
    lcd_command(0x80 | ((posicaoPlayer[0]*0x40)+(posicaoPlayer[1]-1)))
    send_byte(0x09,True)
    time.sleep_ms(5)
    lcd_command(0x80 | (((posicaoPlayer[0]-1)*0x40)+posicaoPlayer[1]))
    send_byte(0x09,True)
    time.sleep_ms(5)
    lcd_command(0x80 | (((posicaoPlayer[0]-1)*0x40)+(posicaoPlayer[1]-1)))
    send_byte(0x09,True)
    time.sleep_ms(1000)
    lcd_command(0x01)
    time.sleep_ms(5)
# Initialize the LCD
lcd_init()

# Write to the display
create_char(0,Cara_normal)
create_char(5,Missil)
while True:
    buttom_state = buttom.value()
    if buttom_state == 1:
        create_char(0,Cara_pulando)
        posicaoPlayer[0] = 0
        lcd_command(0x01)
        time.sleep_ms(5)
        lcd_command(0x80 | (0*0x40)+7)
        lcd_puts("Score")
        lcd_command(0x80 | (0*0x40)+14)
        time.sleep_ms(5)
        lcd_puts(str(pontuação))
        time.sleep_ms(5)
        lcd_command(0x80 | (posicaoMissil[0]*0x40)+posicaoMissil[1])
        send_byte(0x05,True)
        time.sleep_ms(5)
        lcd_command(0x80 | (posicaoPlayer[0]*0x40)+posicaoPlayer[1])
        send_byte(0x00,True)
        time.sleep_ms(100)
        posicaoMissil[1] -=1
        if posicaoMissil[1] < 0:
            posicaoMissil[1] = 15
            pontuação += 1
    else:
        create_char(0,Cara_normal)
        posicaoPlayer[0] = 1
        lcd_command(0x01)
        time.sleep_ms(2)
        lcd_command(0x80 | (0*0x40)+7)
        lcd_puts("Score")
        lcd_command(0x80 | (0*0x40)+14)
        time.sleep_ms(2)
        lcd_puts(str(pontuação))
        time.sleep_ms(2)
        lcd_command(0x80 | (posicaoMissil[0]*0x40)+posicaoMissil[1])
        send_byte(0x05,True)
        time.sleep_ms(2)
        if posicaoMissil[1] == posicaoPlayer[1]:
            lcd_command(0x01)
            time.sleep_ms(50)
            explosao()
            lcd_command(0x80 | (1*0x40)+1)
            lcd_puts("Voce perdeu")
            break 
        lcd_command(0x80 | (posicaoPlayer[0]*0x40)+posicaoPlayer[1])
        send_byte(0x00,True)
        time.sleep_ms(125)
        posicaoMissil[1] -=1
        if posicaoMissil[1] < 0:
            posicaoMissil[1] = 15
            pontuação += 1
            
            
            
        
            


        