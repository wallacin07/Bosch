buttomBlue = Pin(13, Pin.IN)
buttomGreen = Pin(12, Pin.IN)
buttomYellow = Pin(14, Pin.IN)
buttomRed = Pin(27, Pin.IN)

ledBlue = Pin(26, Pin.OUT)
ledGreen = Pin(25, Pin.OUT)
ledYellow = Pin(33, Pin.OUT)
ledRed = Pin(32, Pin.OUT)
       
rodada = 1
ordem = []
gameOver = 0

while gameOver == 0:
    ordem.append(random.randint(1, 4))

    for i in range(qtd):
        if ordem[i] == 1:
            ledBlue.on()
            time.sleep(0.5)
            ledBlue.off()
            
        elif ordem[i] == 2:
            ledGreen.on()
            time.sleep(0.5)
            ledGreen.off()
            
        elif ordem[i] == 3:
            ledYellow.on()
            time.sleep(0.5)
            ledYellow.off()
            
        elif ordem[i] == 4:
            ledRed.on()
            time.sleep(0.5)
            ledRed.off()
        time.sleep(0.5)
    
    for i in range(qtd):
        while True:
            if buttomBlue.value() == 1:
                click = 1
                ledBlue.on()
                time.sleep(0.5)
                ledBlue.off()
                break

            elif buttomGreen.value() == 1:
                click = 2
                ledGreen.on()
                time.sleep(0.5)
                ledGreen.off()
                break

            elif buttomYellow.value() == 1:
                click = 3
                ledYellow.on()
                time.sleep(0.5)
                ledYellow.off()
                break

            elif buttomRed.value() == 1:
                click = 4
                ledRed.on()
                time.sleep(0.5)
                ledRed.off()
                break
            time.sleep(0.1)
        
        if click != ordem[i]:
            gameOver = 1
            pts = qtd - 1 
            break
    rodada += 1
    time.sleep(1)