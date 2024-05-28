'''for i in range(10,51):
    print(i)'''


'''exercicio 1
c = int(input('Digite o começo da contagem  -- '))
f = int(input('Digite o final da contagem  -- '))
f = f+1

for i in range(c,f):
    if i % 2 == 0:
        print(i)'''

'''exercicio 2 ( era pra fazer com 2 for, fiz com um)
p = int(input('Digite um numero inteiro positivo -- '))
if p < 0:
        for i in range(p):
            print(p*"x ")'''

'''exercicio 3 
n = int(input('Escolha um numero para fibonacci -- '))
c = 0
a = 1
b =0


for i in range (b,n):
    print(c)    
    b = c+a
    c=a
    a=b'''

'''exercicio 4
n = int(input('Digite um numero -- '))
lista = []

for i in range(1,n+1):
    if n%i == 0:
        lista.append(i)
ue:
print(lista)
if len(lista) == 2:
    print('Esse numero é primo')    
else:
    print('esse numero não é primo')'''

'''exercico 5(mais dificil)

import random
vitoria = 0
score = 0
while True:
    sair = input('Se deseja parar digite 0')
    if sair == "0":
        break
    while True:
        pergunta = input('Você quer impar ou par? ')
        num = int(input("Fale um numero de 0 a 5 -- \n"))
        aleatorio = random.randint(0,5)
        soma = num + aleatorio
            
        if num > 0 and num <=5:
            if pergunta == 'par' and soma % 2 == 0:
                print('numero da maquina foi', aleatorio)
                print('Você ganhou')
                vitoria +=1
            elif pergunta == 'par' and soma % 2 == 1:
                print('numero da maquina foi', aleatorio)
                print('Você perdeu \n')
                print("Vitorias:", vitoria)
                print('\n Record anterior:', score)
                break
            elif pergunta == 'impar' and soma % 2 == 1:
                print('numero da maquina foi', aleatorio)
                print('Você ganhou')
                vitoria +=1
            elif pergunta == 'impar' and soma % 2 == 0:
                print('numero da maquina foi', aleatorio)
                print('Você perdeu')
                print("Vitorias:", vitoria)
                print('\n Record anterior:', score)
                break
            else:
                break
        else:
            print('ta tonto?')    

    if vitoria > score:
        score = vitoria'''
