while True:
    numeros = []
    try:
        num = 0
        soma = 0
        numero = int(input('Digite o numero para somar os algarismos\n-- '))
        if numero <=0:
           raise ValueError
        numero = str(numero)
        for i in numero:
         numeros.append(int(i))
        print('A soma dos algarismos é: ',sum(numeros))
        break
    except ValueError:
        print('Numero Invalido. Tente novamente')   