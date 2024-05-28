while True:
    class Aluno:
        def __init__(self, nome= input("Digite o nome do aluno\n--"),idade = int(input("Digite a idade do aluno\n--")),turma = input("Digite a turma do aluno\n--"),planta = input("Digite a planta do aluno\n--")):
            self.__nome = nome
            self.__idade = idade
            self.__turma = turma
            self.__planta = planta

        def mostrar_informações(self):
            print(self.__nome,self.__idade,self.__turma,self.__planta)

        def getnome(self):
            return self.__nome
        def getturma(self):
            return self.__turma
        def getidade(self):
            return self.__idade
        def getplanta(self):
            return self.__planta
        
    aluno1 = Aluno()
    aluno1.mostrar_informações()

    with open('alunos.txt', 'a', encoding='utf-8')as f:
            f.write(f'Nome:{aluno1.getnome()}, Idade: {aluno1.getidade()}, Turma:{aluno1.getturma()}, Planta: {aluno1.getplanta()}\n')
            if int(input("deseja escrever mais um aluno?\n1- Sim\n2-Não\n--")) == 2:
                break