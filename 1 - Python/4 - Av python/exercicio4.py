telefone= {}

def incluirNovoNome():
        nome = input('digite o nome da pessoa que deseja adicionar\n-- ')
        numero = input('digite o numero da pessoa que deseja adicionar\n-- ')
        telefone[nome]= numero
        
def incluirTelefone():
        numero = input('digite o numero da pessoa que deseja adicionar\n-- ')
        nome = input('digite o nome da pessoa que para qual deseja adicionar esse numero\n-- ')
# telefone= {nome: numero}

while True:
    escolha = input('Você quer adicionar um novo nome ou um novo telefone\n1 - novo nome\n2 - novo telefone')
    if (escolha == '1') or (escolha == 'novo nome'.lower()):
       incluirNovoNome()
    elif (escolha == '2') or (escolha == 'novo telefone'.lower()):       
        incluirTelefone()
