# class Casa:
#     def __init__(self, area : int, cor, rua, nome = None) :
#         self._area= area
#         self._cor = cor
#         self._rua = rua
#         self._nome = nome
#         if input('Quer informar seu nome?\n1 - Sim\n2 - Não\n-- ') == '1':
#             pessoa = input('Digite seu nome\n-- ')
#             nome = pessoa
#             self._nome = nome

#     def mostrar(self):
#         print(f'Area:{self._area} m², Cor: {self._cor}, rua: {self._rua}, Inquilino: {self._nome} ')
        

# casinha = Casa(120, 'Azul', 'Matagal')
# casinha.mostrar()    

# class InstrumentodeEscrita:
#     def __init__(self, material):
#         self.material = material


#     def escrever(self):
#         print('...Escrevendo...')    
#     def Pintar(self):
#         print('...Pintando...')    
#     def Desenhar(self):
#         print('...Desenhando...')    


# class lapis(InstrumentodeEscrita):
#     def __init__(self):
#         super().__init__("grafite")



# canetinha = lapis()
# print(canetinha.material)
# while True:
#     try:
#         class Calculadora:
#             def __init__(self, num1 = int(input('Fale o numero 1\n-- ')), num2 = int(input('Fale o numero 2\n-- '))):
#                 self._num1 = num1
#                 self._num2 = num2
#                 self._soma = num1 + num2
#                 self._subtração = num1 - num2
#                 self._divisao = num1 / num2
#                 self._multiplicacao = num1 * num2

#             def somar(self):
#                 return self._soma   
#             def subtrair(self):
#                 return self._subtração   
#             def dividir(self):
#                 return self._divisao   
#             def multiplicar(self):
#                 return self._multiplicacao

#         class Calculadora_cientifica(Calculadora):
#             def __init__(self):
#                 super().__init__()   
#                 self.quadrado = self._num1 **2
#                 self.potencia = self._num1 ** self._num2
#                 self.raiz = self._num1**0.5

#             def aoquadrado(self):
#                     return self.quadrado
#             def exponenciacao(self):
#                     return self.potencia
#             def raizquadrada(self):
#                     return self.raiz

#         Calculadora1 = Calculadora()
#         Calculadoracientifica1 = Calculadora_cientifica()
#         calculadoras = int(input("\nDeseja qual calculadora?\n1 - Normal\n2 - Cientifica\n--"))
#         if calculadoras == 1:
#                     escolha = int(input('\nDigite qual calculo deseja\n1 - soma\n2 - subtração\n3 - divisao\n4 - multiplicação\n-- '))                   
#                     match escolha:
#                         case 1:
#                             print(f'\nResultado:{Calculadora1.somar()}')
#                         case 2:
#                             print(f'\nResultado:{Calculadora1.subtrair()}')
#                         case 3:
#                             print(f'\nResultado:{Calculadora1.dividir()}')
#                         case 4:
#                             print(f'\nResultado:{Calculadora1.multiplicar()}')
#         if calculadoras == 2:
#                     escolha = int(input('Digite qual calculo deseja\n1 - soma\n2 - subtração\n3 - divisao\n4 - multiplicação\n5 - quadrado\n6 - exponenciação\n7 - raiz quadrada\n\n--  '))
#                     match escolha:
#                         case 1:
#                                 print(f'\nResultado:{Calculadoracientifica1.somar()}')
#                         case 2:
#                                 print(f'\nResultado:{Calculadoracientifica1.subtrair()}')
#                         case 3:
#                                 print(f'\nResultado:{Calculadoracientifica1.dividir()}')
#                         case 4:
#                                 print(f'\nResultado:{Calculadoracientifica1.multiplicar()}')
#                         case 5:
#                                 print(f'\nResultado:{Calculadoracientifica1.aoquadrado()}')
#                         case 6:
#                                 print(f'\nResultado:{Calculadoracientifica1.exponenciacao()}')                
#                         case 7:
#                                 print(f'\nResultado:{Calculadoracientifica1.raizquadrada()}')

#         if input("\nDeseja continuar a calcular?\n1 - Sim\n2 - Não\n-- ") == '2':
#                     break
#     except ZeroDivisionError:
#             print("\nNão pode 0, seu cabaço\n")
#     except ValueError:
#             print("\ncoloca certo cabaço\n")                        

class Conta:
    def __init__(self,saldo : float,Agencia : int,Banco: str,conta: int):
        self._saldo = saldo
        self._agencia = Agencia
        self._banco = Banco
        self._conta = conta
        self._limitesaque = 0
    
    def verSaldo(self):
        print(self._saldo)
        return self._saldo
    
    def fecharConta(self):
        print("Conta Fechada") 

    def sacarDinheiro(self):
        while True:
            try:
                money = int(input("Digite o valor que deseja sacar\n-- "))
                if money > self._saldo:
                    raise ValueError
                print("Dinheiro sacado")
                self._saldo -= money
                self._limitesaque -=1
                try:
                    if self._limitesaque == 0:
                        raise ValueError
                except ValueError:
                    print('não pode mais sacar')
                break
            except ValueError:
                print("valor invalido, tente novamente")

    def emitirExtrato(self):
        print("Extrato emitido")

    def emitirCartãoDebito(self):
        print("cartão de debito emitido")    

class salario(Conta): 
    def __init__(self, salario : float):
        super().__init__(saldo=0, Agencia= "2295",Banco="bradesco", conta= 74450)
        self.salario =  salario 
        self._limitesaque = 5
        try:
            if self._limitesaque == 0:
                raise ValueError
        except ValueError:
            print('não pode mais sacar')    
    def informarSalario(self):
        inf = float(input("informe seu salario\n-- "))
        if inf < 0 :
            raise ValueError
        self.salario = inf
    def receberSalario(self):
        self._saldo += self.salario
        print('Salario caiu na conta\n')
    

class poupança(Conta):
    def __init__(self):
        super().__init__(saldo=0, Agencia= "2295",Banco="bradesco", conta= 74450)
        self._limitesaque = 2
        try:
            if self._limitesaque == 0:
                raise ValueError
        except ValueError:
            print('não pode mais sacar')  
    def depositarDinheiro(self):

        while True:
            try:
                money = int(input("Digite o valor que deseja depositar\n-- "))
                if money < 0 :
                    raise ValueError
                print("Dinheiro depositado")
                self._saldo += money
                break
            except ValueError:
                print("valor invalido, tente novamente") 

    def renderDinheiro(self):
        saldoAnterior = self._saldo
        self._saldo * 1.1
        rendimento = self._saldo - saldoAnterior
        print(f"Sua conta rendeu: R${rendimento}")            
class corrente(Conta):
    def __init__(self):
        super().__init__(saldo=0, Agencia= "2295",Banco="bradesco", conta= 74450)  

    def emitirCartãoCredito(self):
        print("cartão de credito emitido")
    
    def depositarDinheiro(self):
        while True:
            try:
                money = int(input("Digite o valor que deseja depositar\n-- "))
                if money < 0 :
                    raise ValueError
                print("Dinheiro depositado")
                self._saldo += money
                break
            except ValueError:
                print("valor invalido, tente novamente")          


try:
        account = int(input("Deseja visualizar qual conta?\n1 - Salario\n2 - Corrente\n3 - Poupança\n-- "))
        if account > 3:
            raise ValueError
        if account == 1:
            cs = salario(0)
            cs.informarSalario()
            while True:
                menu = int(input("Bem vindo! O que voce deseja fazer\n1 - Ver saldo\n2 - Sacar Dinheiro\n3- emitir extrato\n4 - Emitir cartão de Debito\n5 - Receber salario\n-- "))
                if menu > 5:
                    raise ValueError
                match menu:
                    case 1 : 
                        print(f"Seu saldo é: R${cs.verSaldo()}")
                    case 2 : 
                        cs.sacarDinheiro()
                    case 3 :
                        cs.emitirExtrato()   
                    case 4 :
                        cs.emitirCartãoDebito()         
                    case 5 :
                        cs.receberSalario()
                if int(input("Deseja fazer algo a mais na conta?\n1 - sim\n2 - não\n-- ")) == 2:
                    break     
        if account == 2:
            cc = corrente()
            while True:
                menu = int(input("Bem vindo! O que voce deseja fazer\n1 - Ver saldo\n2 - Sacar Dinheiro\n3- emitir extrato\n4 - Emitir cartão de Debito\n5 - Fazer depósito\n6 - Emitir cartão de Credito\n-- "))

                if menu > 5:
                    raise ValueError
                match menu:
                    case 1 : 
                        print(f"Seu saldo é: R${cc.verSaldo()}")
                    case 2 : 
                        cc.sacarDinheiro()
                    case 3 :
                        cc.emitirExtrato()   
                    case 4 :
                        cc.emitirCartãoDebito()         
                    case 5 :
                        cc.depositarDinheiro()
                    case 6 :
                        cc.emitirCartãoCredito()
                if int(input("Deseja fazer algo a mais na conta?\n1 - sim\n2 - não\n-- ")) == 2:
                    break  
        if account == 3:
            cp = poupança()
            while True:
                menu = int(input("Bem vindo! O que voce deseja fazer\n1 - Ver saldo\n2 - Sacar Dinheiro\n3- emitir extrato\n4 - Emitir cartão de Debito\n5 - Fazer depósito\n6 - Deixar render o dinheiro\n-- "))
                if menu > 5:
                    raise ValueError        
                match menu:
                    case 1 : 
                        print(f"Seu saldo é: R${cp.verSaldo()}")
                    case 2 : 
                        cp.sacarDinheiro()
                    case 3 :
                        cp.emitirExtrato()   
                    case 4 :
                        cp.emitirCartãoDebito()         
                    case 5 :
                        cp.depositarDinheiro()
                    case 6 :
                        cp.renderDinheiro()
                if int(input("Deseja fazer algo a mais na conta?\n1 - sim\n2 - não\n-- ")) == 2:
                    break         
except ValueError:
        print("Digite o numero correto")

