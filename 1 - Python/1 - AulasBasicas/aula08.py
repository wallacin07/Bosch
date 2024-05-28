'''while True:
    try:
        num1 = int(input('Digite o primeiro numero -- '))
        num2 = int(input('Digite o segundo numero -- '))
        escolha = int(input('Digite a operação que quer fazer \n 1- Adição \n 2- Subtração \n 3-Multiplicação \n 4- Divisão\n 5- Potenciação  \n -- '))
        if escolha == 1:
            soma = num1 + num2
                        
        elif escolha == 2:
            soma = num1 - num2
                        
        elif escolha == 3:
            soma = num1 * num2
                    
        elif escolha == 4:
            soma = num1 / num2
                     
        elif escolha == 5:
            soma = num1 ** num2 
        elif escolha > 5:
              print('não é nenhuma opção')     
        if int(input('Digite 0 pra sair ou qualquer outro numero para continuar  -- ')) == 0:
            break
    except ZeroDivisionError:
                    print('Não se pode dividir um valor por zero \nTente novamente')
    except ValueError:
                    print('Isso não é um numero.\nPor favor, tente novamente')'''

import random
pontuação = 100
while True:
    palavra = []
    with open('palavras.txt', 'r') as f:
        linhas = f.read()
        linha = linhas.split('\n')
        while True:
            try:
                dificuldade =  int(input('Escolha a dificuldade\n1 - Facil\n2 - Medio\n3 - Dificil\n-- '))
                match dificuldade:
                    case 1 :
                        d =  linha[0].split(', ')
                    case 2 :
                        d = linha[1].split(', ')
                    case 3 :
                        d = linha[2].split(', ')
                if (dificuldade != 1) and (dificuldade != 2) and  (dificuldade != 3):
                    raise ValueError 
                else:
                    break 
            except ValueError:
                print('Só pode valores entre 1 a 3')


    palavra_aleatoria = random.choice(d)
    for i in palavra_aleatoria:
        palavra.append(i)          
    random.shuffle(palavra)
    palavra_embaralhada = "".join(palavra)

    while True:
        print(palavra_embaralhada)
        palpite = input('Digite qual é a palavra no anagrama\n-- ').lower()
        if palpite == palavra_aleatoria:
            print('Você acertou') 
            break
        else:
            print('ERROUUUUU')
            pontuação -= 20
            print(f'Você perdeu 20 pontos\nAgora vc tem {pontuação}')
            if pontuação == 0:
                print('Você perdeu :(\n')
                break
    if input('Quer continuar?\n1 - continuar\n0 - sair\n-- ')== '0':
        break


            


