times = ['1_palmeiras', '2_coritiba', '1_corintians', '3_juventude', '2_fluminense', '3_bahia', '1_cuiaba', '2_cascavel', '3_ponte preta', '2_parana clube', '3_volta redonda']
primeira = []
segunda = []
terceira = []

for i in times:
    time = i.split(',')
    timezin = time[0]
    if timezin[0] == "1": 
        primeira.append(timezin[2:].capitalize())
    elif timezin[0] == "2": 
        segunda.append(timezin[2:].capitalize())
    elif timezin[0] == "3": 
        terceira.append(timezin[2:].capitalize())
 
print (f'Primeira divisão: {primeira}\nSegunda divisão: {segunda}\nTerceira divisão: {terceira} ')      