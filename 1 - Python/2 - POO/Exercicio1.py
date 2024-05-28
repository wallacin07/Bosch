with open('clientes.txt', 'r') as f:
    caracter_especial =["!@$&*¨%+-#"]
    for linha in f:
        nome = linha.split()
        for nomes in nome:
          if "!@$&*¨%+-#" in nomes:
             print('tem')
            # formatado = []
            # formatadadin = nomes.strip()
            # formatado.append(formatadadin)
            # real = formatadadin.strip('!?')
            # if '#' in nomes:
            #     print('tem')
            # print(formatado)
            # print(real)

            