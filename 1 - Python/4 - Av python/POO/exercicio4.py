class Bosch:

    def __init__(self,nome = "Robert Bosch LTDA.",CNPJ = '45.990.181/0001-89',Nacionalidade = "alemã",Nome_do_responsavel = 'Gastón Diaz Perez',Paises_Atuação = ['argentina', "alemanha", "brasil", 'chile', "portugal"],Produtos = {}):
        self.nome = nome
        self.CNPJ = CNPJ
        self.Nacionalidade = Nacionalidade
        self.NomeResponsavel = Nome_do_responsavel
        self.paisesdeatuação = Paises_Atuação
        self.produtos = Produtos
    
    def Presidente_Bosch(self):
        return self.NomeResponsavel
    
    def paisesAtuacao(self):
        return self.paisesdeatuação
    
    def pesquisarpais(self):
        Pesquisar = input("Digite o nome do pais que quer pesquisar").lower
        if Pesquisar in self.paisesdeatuação:
            print("Ele atua nesse pais")
        else:
            print("não atua nesse pais")

    def Adicionarproduto(self):
        Produto = input("Digite o produto que quer adicionar\n--").lower
        preço = float(input("Digite o preço do produto"))
        descricao = input("descreva o produto e o que ele faz breviamente")
        self.produtos [Produto] = preço,descricao
        produtos_str = str(self.produtos)
        print(produtos_str)
    def relatorioprodutos(self):
        return self.produtos
    
    def pesquisarprodutos(self):
        pesquisa = input("digite o produto que quer pesquisar").lower
        if pesquisa in self.produtos:
            print("Ela fabrica esse produto")



class Areas(Bosch):
    def __init__(self,nome_setor = "PT",sigla = "PT",função ="FAZ PEÇA", responsavel ="NAO SEI",lucro = 0,dia = 0 ,dfa = 0):
        super().__init__()            
        self.nome_setor = nome_setor
        self.sigla = sigla
        self.função = função
        self.responsavel = responsavel
        self.lucros = lucro
        self.dia = dia
        self.dfa = dfa

    def responsavel_area(self):
        return self.responsavel    
    
    def relatoriofinanceiro(self):
        faturamento = int(input("digite o valor faturado pela area\n--"))
        gastos = int(input("digite os gastos pela area\n--"))
        self.lucros = faturamento - gastos
        print(f"o fatruamento foi: {faturamento}, os gastos da area foi: {gastos}, e com isso, o lucro foi: {self.lucros()}")

    def  periodoauditoria(self):
        dia_inicio = int(input("Digite o dia que começa a auditoria"))
        dia_fim = int(input("Digite o dia que termina a auditoria"))
        mes_inicio = int(input("Digite o mes que começa a auditoria"))
        mes_fim = int(input("Digite o mes que termina a auditoria"))
        ano_inicio = int(input("Digite o ano que começa a auditoria"))
        ano_fim =    int(input("Digite o ano que termina a auditoria"))
        mesfinal = mes_fim - mes_inicio
        diafinal = dia_fim - dia_inicio
        anofinal = ano_fim - ano_inicio
        print(f'o periodo da auditoria é: {anofinal} ano(s), {mesfinal} mes(es) e {diafinal} dias')

class Departamentos(Areas):
    def __init__(self, nome_departamento = "mecanica", sigla_departamento = "nao sei ", responsavel_departamento = 'Menor ideia'):
        super().__init__(nome_setor="PT") 
        self.nome_departamento = nome_departamento
        self.sigla_departamento = sigla_departamento
        self.responsavel_departamento = responsavel_departamento      
        self.qtd_funcionarios = 0
    
    def responsavel_departamentos(self):
        return self.responsavel_departamento

    def contratarfuncionarios(self):
        self.qtd_funcionarios += 1
        print("Você contratou um funcionario")

    def realizarTreinamento(self):
        print("Você realizou um treinamento")    

Wallace = Departamentos()
Wallace.Adicionarproduto()