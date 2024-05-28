"""explicações

operadores aritmeticos = +, -, *, /, %, **
operadores de comparação = <,>,==,<=,>=, !=



dicionario
sala_de_aula = {"instrutor": "nycollas", "aluno01": "Wallace", "aluna02": "Marryana"}

print(sala_de_aula["aluna02"])


input
nome = input("insira seu nome -- ")
print('seu nome é ' + nome)

classificando variaveis
idade = int(input('Diga sua idade -- '))
print('Sua idade é ', idade)"""

#exercicios
pergunta = input('voce quer fazer o que \n 1-Celsius em fahrenheit \n 2-fahrenheit em celsius')
if pergunta == 1:
    temp_c = input('digite a temperatura em celsius')
    temp_f = temp_c * 1.8 + 32
    print('temperatura em fahrenheit é ',temp_f, 'ºF')
if pergunta == 2:
    temp_f = input('digite a temperatura em celsius')
    temp_c = temp_f / 1.8 - 32
    print('temperatura em Celsius é ', temp_c, 'ºC')
    
    #fiz a mais, incompleto pois deu errado, mas exercicio da aula resolvido