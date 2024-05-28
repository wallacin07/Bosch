""" explicação


Manipulação de string :
#len
fruta ='banana'
letra = fruta[0]
print(letra)

#concatenção
parte_um = 'bana'
parte_dois = 'na'
print(parte_um + parte_dois)

#marcação de caracter especial
print('mcdonald\'s')

#quebra de linha
print('pão de batata \npeixe e atum') #tem como usar aspas triplas direto na string para a quebra de linha

#metodo split
s = ' s o u f o d a'
m = 'mama-mia'
print(s.split(' '))
print(m.split('-'))

#metodo join
list = ['Roberto', 'bosch', 'Curitiba']
list2 = ['We', 'are', 'Bosch']
print('-'.join(list))
print(' '.join(list2))

"""

#exercicios

#abreviação de nome
#nome = str(input('insira seu nome -- '))
#print('A abreviação do seu nome é ' + (nome[0:3]).upper())

#nome completo e tamanho do nome

nome = str(input('Insira seu nome completo em letras minusculas -- '))
nomeMaiusculo = nome.title()
nomeContagem = nome.strip()
print(nomeContagem, nomeMaiusculo)

#COMEEEEER
