i = 0
dicionario = dict()
lista = list()
with open('data.txt', 'r')as f:
    for linha in f:
        linhas = linha.split(":")
        for palavra in linhas:
           palavras = palavra.split(',')
           if i == 0:
               dicionario[palavras[0]] = palavras[1],palavras[2],palavras[3]
           elif i == 1:
               dicionario[palavras[0]] =palavras[1],palavras[2],palavras[3]
           elif i == 2:
               dicionario[palavras[0]] = palavras[1],palavras[2],palavras[3]
           i +=1
           
resposta = input("Digite a palavra\n-- ")
escolha = int(input("Digite a lingua que deseja\n[1] Portugues\n[2] Ingles\n[3] Alemao "))

if resposta == "Oi" or resposta == "Hello" or resposta == "Oi em alemao" :
    if escolha == 1:
        print(dicionario["Portugues"][0])
    if escolha == 2:
        print(dicionario["Ingles"][0])    
    if escolha == 3:
        print(dicionario["Alemao"][0])
        
elif resposta == "Bom dia" or resposta == "Good Morning" or resposta == "Bom dia em alemao" :
    if escolha == 1:
        print(dicionario["Portugues"][1])
    if escolha == 2:
        print(dicionario["Ingles"][1])    
    if escolha == 3:
        print(dicionario["Alemao"][1])
        
elif resposta == "Boa noite" or resposta == "Good night" or resposta == "Boa noite em alemao" :
    if escolha == 1:
        print(dicionario["Portugues"][2])
    if escolha == 2:
        print(dicionario["Ingles"][2])    
    if escolha == 3:
        print(dicionario["Alemao"][2])
    # if escolha == 1:

else:
    print("Nao tem essa palavra no dicionario")       