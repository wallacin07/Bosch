'''arquivo = open('arquivo.txt', 'r')
palavra_user = input('Escolha uma palavra para ver se tem ela no roteiro -- ')
count = 0
for palavra in arquivo:
    palavra = palavra.strip()
    palavra = palavra.split(' ')
    print(palavra)
    for i in palavra:
        if i  == palavra_user:
            count +=1

print(f"A palavra {palavra_user} aparece {count} vezes")'''
'''r = open('dadosfinais.txt', 'w')
f = open('dados.txt', 'r')
preresultado = f.read()
infgeral = preresultado.split('\n')
print(infgeral)
infalunos = []
for i in infgeral:
    infalunos = i.split(', ')
    print(infalunos)
    media = 0
    soma = 0
    maiormedia = 0
    alunonotaalta = ""
    for i in infalunos:
        if i.isdigit():
            soma += int(i)  
            
    media = soma/3
     deu errado
     
       if maiormedia < media:
        maiormedia = media
        alunonotaalta = infalunos[0]
    if media > 6:
        resultado = 'Aprovado!'
        round(media, 2)
        r.write(f'Aluno {infalunos[0]} : Media {media:.2} Resultado : {resultado} \n') 
    else:
        resultado = 'Reprovado!'
        r.write(f'Aluno {infalunos[0]} : Media {media:.2} Resultado : {resultado} \n') 
r.write(f'A maior media foi de {maiormedia} de {alunonotaalta}') 
r.close()'''

def mostrarcardapio():
    with open('cardapio.txt', 'r') as f:
        for cardapio in f:
            itens = cardapio.strip('\n')
            print(itens)

mostrarcardapio()
combo1_valido = False
combo2_valido = False
comida_valida = False
bebida_valida = False
porção_valida = False
while True:
    modalidades = input(' \nDigite qual modalidade você quer \n1 - livre\n2 - combo\n--')
    while True:
        with open('listapedidos.txt', 'a')as p:
                while True:
                    nome = input('Como você gostaria de ser chamado\n-- ')
                    if not nome.isalpha():
                        print('Nome invalido')
                    else:
                        break
                if modalidades ==  '1':
                    comida = input('Digite a comida que voce quer\n-- ').lower()
                    if comida == 'hamburguer':
                        print('Você escolheu ', comida)
                        comida_valida = True
                        
                    elif comida == 'hot dog':
                        print('Você escolheu ', comida)
                        comida_valida = True
                                    
                    bebida = input('Digite a bebida que voce quer\n-- ').lower()
                    if bebida == 'coca cola':
                        print('Você escolheu ', bebida)
                        bebida_valida = True
                        
                    elif bebida ==  'guarana': 
                        print('Você escolheu ', bebida)
                        bebida_valida = True
                                
                    porção = input('Digite a porção que voce quer \n-- ').lower()    
                    if porção == 'frango':
                            print('Você escolheu ', porção)
                            porção_valida = True
                            break
                    elif porção == 'fritas': 
                        print('Você escolheu ', porção)
                        porção_valida = True
                            
                    if comida_valida and bebida_valida and porção_valida:
                        print(f'Voce escolheu {comida}, com refri {bebida}, e porção de {porção}')
                        p.write(f'\n{nome}, Comida: {comida}, bebida :{bebida}, porção {porção}')
                        break
                    else :
                        print('\nPedido invalido, pfv fazer novamente')
                if modalidades == '2':
                        combo = input('Você quer o combo um ou combo dois? \n--').lower()
                        if combo == '1':
                            print('Você escolheu o combo um')
                            combo1_valido = True
                            
                
                        elif combo == 'um':
                            print('Você escolheu o combo um')
                            combo1_valido = True
                            
                        elif combo == '2':
                            print('Você escolheu o combo dois')
                            combo2_valido = True
                        
                        elif combo == 'dois':
                            print('Você escolheu o combo dois')
                            combo2_valido = True
                        
                        else:
                            print('Combo invalido, pfv digite novamente\n')
                        if combo1_valido:
                            p.write(f'{nome}: Hamburguer, Refrigerante e Fritas\n')
                            break
                        elif combo2_valido:
                            p.write(f'{nome}: Hot Dog, Refrigerante e Frango\n') 
                            break   


    continuar_pedido = input('Voce quer fazer outro pedido?\n1 - Sim\n0 - não\n-- ')
    if continuar_pedido == '0':
            break


'''def contarpalavras():
    palavras_distintas = {}
    with open('texto_exemplo.txt', 'r') as f:
        for linhas in f:
            palavras = linhas.split()
            print(palavras)
            for palavra in palavras:
                palavra_formatada = palavra.strip(',.!?;')
                print(palavra_formatada)
                if not palavra_formatada in palavras_distintas:
                    palavras_distintas[palavra_formatada] = 0
                    palavras_distintas[palavra_formatada] += 1
        print(palavras_distintas)            
    with open('palavrasdistintas.txt', 'w') as d:
        convertidos = list(palavras_distintas.keys())
        for i in convertidos:
            todaspalavras = i.split()
            todaspalavras = i.strip(',.!?;')
            print(todaspalavras)
            d.write(f'{todaspalavras}\n')


contarpalavras()'''             