class Livro():
    def __init__(self,titulo,autor,qtd_paginas, guardado=True):
        self.titulo = titulo
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.guardado = guardado
        self.paginas = 1
    def pegar_livro(self):
        if self.guardado:
            print("Você pegou o livro")
            self.guardado = False
        else:
            print("livro ja esta fora da estante")

    def devolver_livro(self):
            if not self.guardado:
                print("Você devolveu o livro")
                self.guardado = True
            else:
                print("Livro ja esta na estante")

    def virar_uma_pagina(self):
        if self.paginas > self.qtd_paginas:
            print("não tem mais paginas parar virar") 
        elif self.guardado:
            print('pegue o livro primeiro')                
        else:
            self.paginas += 1

    def virar_n_paginas(self):
        n_paginas = int(input("Quantas paginas deseja virar?\n--"))
        if n_paginas + self.paginas > self.qtd_paginas:
            print("não da para virar tantas paginas assim")
        elif self.guardado:
            print('pegue o livro primeiro')    
        else:
            self.paginas += n_paginas

    def voltar_uma_pagina(self):
        if self.paginas < 1:
            print("não tem como voltar mais")
        elif self.guardado:
            print('pegue o livro primeiro')                 
        else:
            self.paginas -= 1

    def voltar_n_paginas(self):
        n_paginas = int(input("Quantas paginas deseja virar?\n--"))
        if self.paginas - n_paginas < 1:
            print("não da pra voltar tantas paginas")
        elif self.guardado:
            print('pegue o livro primeiro')    
        else:
            self.paginas -= n_paginas

    def ler_livro(self):
        print(f"Nome: {self.titulo}, Autor: {self.autor}" )

    def mostrar_pagina(self):
        print(self.paginas)    

livro1 = Livro("bela adormecida", "eu", 290)            
while True:
    try:
        
            menu = int(input("Bem vindo! O que voce deseja fazer\n1- pegar livro\n2- devolver livro \n3- virar uma pagina\n4- virar n paginas\n5- voltar uma pagina\n6-voltar n paginas\n7- ler livro\n8- mostrar pagina\n--  "))
            if (menu > 8) or (menu < 1 ):
                    raise ValueError
            match menu:
                case 1 : 
                    livro1.pegar_livro()
                case 2 : 
                    livro1.devolver_livro()
                case 3 :
                    livro1.virar_uma_pagina()
                case 4 :
                    livro1.virar_n_paginas()
                case 5 :
                    livro1.voltar_uma_pagina()
                case 6:
                    livro1.voltar_n_paginas()
                case 7: 
                    livro1.ler_livro()
                case 8:
                    livro1.mostrar_pagina()    
            if int(input("Deseja fazer algo a mais?\n1 - sim\n2 - não\n-- ")) == 2:
                break
    except ValueError:
        print("\ninsira um numero correto\n")


