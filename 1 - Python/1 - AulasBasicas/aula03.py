"""lista = [8,7,5,2]
lista.append(6)
print(min(lista) , max(lista),  sum(lista), lista)"""

""" Exercicio 1[Adição de valores a uma lista(com e sem loop)]

valores = [0,1,2,3,4,5,6,7,8,9]
#Input

valor1 = int(input('Digite o primeiro valor da lista  '))
valor2 = int(input('Digite o Segundo valor da lista  '))
valor3 = int(input('Digite o Terceiro valor da lista  '))
valor4 = int(input('Digite o Quarto valor da lista  '))
valor5 = int(input('Digite o Quinto valor da lista  '))
valor6 = int(input('Digite o Sexto valor da lista  '))
valor7 = int(input('Digite o Setimo valor da lista  '))
valor8 = int(input('Digite o Oitavo valor da lista  '))
valor9 = int(input('Digite o Nono valor da lista  '))
valor10 = int(input('Digite o Decimo valor da lista  '))

#Substituição

valores[0] = valor1

valores[1] = valor2

valores[2] = valor3

valores[3] = valor4

valores[4] = valor5

valores[5] = valor6

valores[6] = valor7

valores[7] = valor8

valores[8] = valor9

valores[9] = valor10

#Ordenação
valores.sort(   )

print(len(valores))
print(valores)
"""

"""valores = []


for i in range(1,11):
    print('Digite o valor ', i)
    valor = int(input())
    valores.append(valor)

valores.sort
print(valores)

    """

""" Exercicio 2(tupla)

ricos = ("Elon Musk","Bernard Arnault", "Jeff Bezos", 
         "Larry Ellison", "Warren Buffett", "Bill Gates", "Mark Zuckerberg",
          "Larry Page", "Steve Ballmer", "Sergey Brin")

print("Os mais ricos são ", ricos)
print("Os 3 mais ricos são ", ricos[0:3])
print("O mais rico é ", ricos[0])"""

"""Exercicio 3 (dicionario)

fastfood = {"Hamburguer" : 10, "Hotdog" : 6.5, "Salada" : 4,
             "Suco": 4, "Refrigerante": 4.5, "Agua": 2}

print(fastfood.keys())

comida = input("Digite a comida que você quer  ")
bebida = input("Digite a bebida que você quer ")

if comida in fastfood:
    valorcomida = fastfood[comida]
if bebida in fastfood:
    valorcomida = valorcomida + fastfood[bebida]

    print("O valor total é ", valorcomida)"""

'''exercicio 4(acertar o numero secreto)

numsecreto = "25"
print('tente acertar o numero')
palpite = 0
while palpite != numsecreto:
    palpite = input("Digite o numero ")
    if palpite.isdigit():
        if palpite == numsecreto:
            print('Você acertou!!')
            break
        else:
            print('Não foi dessa vez')    
    else:
        print('isso não é um numero')'''

'''exercicio 5 (votação)

nascimento = int(input('Digite o ano que você nasceu -- '))
idade = 2024 - nascimento
print(idade)

if idade <= 15:
    print('Você não pode votar.')
elif idade >= 16 and idade < 18 or idade >=70:
    print('Seu voto é facultativo')
else:
    print('Seu voto é obrigatorio')'''

'''exercicio 6 (mexendo com loop)

limite = int(input('Digite até que numero a soma vá -- '))
i=1
soma = 0
while i <= limite:
    soma = soma + i
    i = i + 1

print(soma)'''

'''exercicio 7(calculadora)

while True:
    num1 = int(input('Digite o primeiro numero -- '))
    num2 = int(input('Digite o segundo numero -- '))

    escolha = int(input('Digite a operação que quer fazer \n 1- Adição \n 2- Subtração \n 3-Multiplicação \n 4- Divisão \n 0- sair \n -- '))
    if escolha == 1:
        soma = num1 + num2
        
    elif escolha == 2:
        soma = num1 - num2
        
    elif escolha == 3:
        soma = num1 * num2
       
    elif escolha == 4:
        soma = num1 / num2
        
    elif escolha > 4: 
        print('não é nehuma opção')
        break
    elif escolha == 0:
        break
    print(soma)
    if int(input('Digite 0 pra sair ou qualquer outro numero para continuar  -- ')) == 0:
        break'''