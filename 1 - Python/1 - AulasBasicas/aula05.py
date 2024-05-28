'''função'''

'''import time
def  contagem():
    for i in range (5,0, -1):
        print(i)
        time.sleep(1)

contagem()'''
'''exercicio 1
import time
def contador(a,b,c):
    for i in range (a,b,c):
        print(i)
        time.sleep(0.2)

contador(20,0,-2)
print("---------- fim contador ---------")
contador(0,106,5)
print("---------- fim contador ---------")
contador(96,51,-2)
print("---------- fim contador ---------")
contador(3,42,1)
print("---------- fim contador ---------")
contador(75,14,-5)
print("---------- fim contador ---------")
contador(390,39,-10)
print("---------- fim contador ---------")
contador(int(input("Fale um numero pra começar -- ")),int(input("Fale um numero pra terminar -- ")),int(input("Fale de quantos em quantos quer -- ")))'''


'''import math
while True:
    def operacoes(num = int(input('Digite um valor -- '))):
                return {"Raiz": num**0.5,"Quadrado":num**2, "Inverso": 1/num, "Fatorial" : math.factorial(num) }
    result = operacoes()
    for i in result:
        print(i,":", result[i])  
    if input("deseja continuar as operações? \n 1 - sim \n 2 - nao \n") == "2":
           break'''

'''import random
lista = []
def aleatorio(li = int(input('Digite o numero minimo ')),ls = int(input('Digite o numero maximo ')),tl = int(input('Digite o tamanho  '))):
    for i in range(tl):
        numale= random.randint(li,ls)
        lista.append(numale)
        if len((lista)) == tl:
            print(lista)
def ordenar(lista):
    for i in range(len(lista)):
        for x in range(i+1,len(lista)):
            if lista[x] < lista [i]:
                a = lista[i]
                lista[i]=lista[x]
                lista[x] = a
    print(lista)         
aleatorio()
ordenar(lista)'''
