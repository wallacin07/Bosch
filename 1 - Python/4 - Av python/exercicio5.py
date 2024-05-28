# o programa pede ao usuario numeros conforme o tamanho da lista(se o tamanho que vc quiser for 6, ele vai pedir por 6 valores) e depois os organiza

# Criação da lista e input para definir o tamanho dessa lista
lista = []
tam=int(input('Digite o tamanho da lista: '))

# Criação de um loop pra pedir os valores que voce quer organizar de acordo com o tamanho
for i in range (1,tam+1,1):
    x = int(input("VALOR {} :".format(i)))
    # aqui ele adiciona a lista do começo cada numero
    lista.append(x)
# aqui ele vai printar a lista na tela, mas fora de ordem
print("\nLISTA:")
print(lista)

# É criado um outro loop, para comparar e substituir de lugar se for menor que o numero anterior
for i in range(tam):
    for j in range(tam):
        # aqui é onde acontece a comparação, onde ele verifica se p numero no indice j é maior que no indice i. 
        # caso seja, ele armazena o antigo valor de do indice i, e o substitui pelo valor do indice j
        if lista[j] > lista[i]:
            lista [i], lista[j]=lista [j],lista[i]
# E por fim, ele printa a lista ordenada.            
print("\nLISTA ORDENADA: ")
print(lista)            