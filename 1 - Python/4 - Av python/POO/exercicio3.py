import random

class cliente:
    def __init__(self,saldo : float,Agencia : int,tipo_conta: str,conta: int, nome_cliente: str):
        self.__saldo = saldo
        self.__agencia = Agencia
        self.__nome_cliente = nome_cliente
        self.__conta = conta
        self.__tipo_conta = tipo_conta
    def getsaldo(self):
        print(self.__saldo)
        return self.__saldo 

    def getagencia(self):
        print(self.__agencia)
        return self.__agencia 
    def getnome_cliente(self):
        print(self.__nome_cliente)
        return self.__nome_cliente
    def getconta(self):
        print(self.__conta)
        return self.__conta
    def gettipo_conta(self):
        print(self.__tipo_conta)
        return self.__tipo_conta

    def gettotalcontas(cls):
        return
    @staticmethod
    def mostrarcontas():
        contas = 0
        contas += 1
        print(contas)
    def sacarDinheiro(self):
        while True:
            try:
                money = int(input("Digite o valor que deseja sacar\n-- "))
                if money > self.__saldo:
                    raise ValueError
                print("Dinheiro sacado")
                self.__saldo -= money
                break
            except ValueError:
                print("valor invalido, tente novamente")        

    def emitirExtrato(self):
        print("Extrato emitido")
    def emitirCartãoDebito(self):
        print("cartão de debito emitido")  

    def verinformações(self):
        return self.__nome_cliente,self.__agencia, self.__conta,self.__tipo_conta
    

    def depositarDinheiro(self):
         while True:
            try:
                money = int(input("Digite o valor que deseja depositar\n-- "))
                if money < 0 :
                    raise ValueError
                print("Dinheiro depositado")
                self.__saldo += money
                break
            except ValueError:
                print("valor invalido, tente novamente") 


    def get_depositardinheiro(self):
        return 




while True:
    if int(input("Deseja abrir uma conta?\n1- Sim\n2- não\n-- ")) == 1:
        tipoconta = input("Voce quer criar uma conta corrente ou poupança?(escreva somente o nome da conta)\n-- ")
        nome = input("Qual é seu nome?\n-- ")
        cliente.mostrarcontas()
        cc = cliente(0, 2596,tipoconta, random.randint(11111,99999),nome)
        while True:
            try:
                menu = int(input("Bem vindo! O que voce deseja fazer\n1 - Ver saldo\n2 - Sacar Dinheiro\n3- emitir extrato\n4 - Fazer depósito\n5 - Emitir cartão de Debito\n6 - ver suas informaçoes\n-- "))
                if menu > 6:
                    raise ValueError
                match menu:
                    case 1 : 
                        print(f"Seu saldo é: R${(cc.getsaldo())}")
                    case 2 : 
                        cc.sacarDinheiro()
                    case 3 :
                        cc.emitirExtrato()   
                    case 4 :
                        cc.depositarDinheiro()       
                    case 5 :
                        cc.emitirCartãoDebito()
                    case 6 :
                        print(cc.verinformações())
                if int(input("Deseja fazer algo a mais na conta?\n1 - sim\n2 - não\n-- ")) == 2:
                    break 
                 
            except ValueError:
                print("numero invalido")            