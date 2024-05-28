import math


data_nascimento = int(input('fale sua data de nascimento'))
idade = int(input('fale sua idade'))

idade_basedata = 2024-data_nascimento

if(idade_basedata == idade):
    print('você não mentiu')
else:
    print('VOCÊ MENTIU SUA IDADE')