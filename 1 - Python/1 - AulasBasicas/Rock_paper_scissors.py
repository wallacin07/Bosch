import random

def maquina():
    jogada_maquina = random.randint(1,3)
    match(jogada_maquina):
        case 1: opcao_maquina = "PEDRA"
        case 2: opcao_maquina = "PAPEL"
        case 3: opcao_maquina = "TESOURA"
    
    return jogada_maquina


def game(opcao_maquina):
    jogada = int(input("Deseja jogar\n1 - pedra\n2 - papel\n3 - tesoura"))
    match(jogada):
        case 1: opcao= "PEDRA"
        case 2: opcao= "PAPEL"
        case 3: opcao= "TESOURA"

    if jogada == 1 & opcao_maquina == 3:
        print("\nVocê venceuuuu\n")
    if jogada == 2 & opcao_maquina == 1:
        print("\nVocê venceuuuu\n")
    if jogada == 3 & opcao_maquina == 2:
        print("\nVocê venceuuuu\n")
print("Bem vindo ao pedra papel ou tesoura\n")
opcao_maquina = maquina()
print(opcao_maquina)
        

