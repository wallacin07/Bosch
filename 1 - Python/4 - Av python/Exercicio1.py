with open('clientes.txt', 'r') as f:
    for linha in f:
        nome = linha.split()
        for nomes in nome:
           if  nomes.isalpha:
               print('um')
           else:
               print('dois')
            # formatado = []
            # formatadadin = nomes.strip()
            # formatado.append(formatadadin)
            # real = formatadadin.strip('!?')
            # if '#' in nomes:
            #     print('tem')
            # print(formatado)
            # print(real)

            