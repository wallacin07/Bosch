import random
jogo = [[6,0 ,0 ,0 ,9,0 ,0 ,0 ,0],
        [0 ,3,4,0 ,1,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,0 ,0 ,7,6,8],
        
        [5,7,0 ,0 ,0 ,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,1,4,0 ,0 ,0 ,0],
        [0 ,0 ,0 ,0 ,6,0 ,3,5,0],
        
        [1,0 ,0 ,8,0 ,0 ,5,0 ,0],
        [4,0 ,0 ,0 ,0 ,9,0 ,2,0],
        [9,0 ,0 ,0 ,1 ,0 ,0 ,0 ,6]]




def verify(jogo,x : int ,y : int,value):
    
    value = int(value)
    try:
#?             VERIFICAÇÃO SE A POSIÇÃO JA POSSUI O VALOR
        if jogo[x][y] != 0:
            return False

#TODO            VERIFICAÇÃO DE LINHAS E COLUNAS PARA A NAO REPETIÇÃO DOS NUMEROS
        for i in range(9):
            if jogo[i][y] == value:

                return False
            elif jogo[x][i] == value:

                return False
            else:
                return True
        
        
#!              VERIFICAÇÃO DAS GRADES(foi o jeito mais simples que achei, mas mais trabalhoso)

        if x == 0 or x == 1 or x == 2:
            if y == 0 or y == 1 or y == 2:
                for i in range(3):
                    for j in range(3):
                        if jogo[i][j] == value:
            
                            return False
                        
            elif y == 3 or y == 4 or y == 5:
                for i in range(3):
                    for j in range(3):
                        if jogo[i][3+j] == value:
            
                            return False
                    
            elif y == 6 or y == 7 or y == 8:
                for i in range(3):
                    for j in range(3):
                        if jogo[i][6+j] == value:
            
                            return False
                        
                        
        elif x == 3 or x == 4 or x == 5:
            if y == 0 or y == 1 or y == 2:
                for i in range(3):
                    for j in range(3):
                        if jogo[3+i][j] == value:
            
                            return False
                        
            elif y == 3 or y == 4 or y == 5:
                for i in range(3):
                    for j in range(3):
                        if jogo[3+i][3+j] == value:
            
                            return False
                    
            elif y == 6 or y == 7 or y == 8:
                for i in range(3):
                    for j in range(3):
                        if jogo[3+i][6+j] == value:
            
                            return False   
                        
                        
                        
        elif x == 6 or x == 7 or x == 8:
            if y == 0 or y == 1 or y == 2:
                for i in range(3):
                    for j in range(3):
                        if jogo[6+i][j] == value:
            
                            return False
                        
            elif y == 3 or y == 4 or y == 5:
                for i in range(3):
                    for j in range(3):
                        if jogo[6+i][3+j] == value:
            
                            return False
                    
            elif y == 6 or y == 7 or y == 8:
                for i in range(3):
                    for j in range(3):
                        if jogo[6+i][6+j] == value:
            
                            return False                    
        else:
            return True 
    except ValueError:
        print("Voce nao colocou um valor valido")  
    except IndexError:
        print("Indice da matriz errado")    
                 
def isValidGame(jogo):
    
    num = 1
    
    # for i in range(9):
    #     for j in range(9):
    #         if
    
            
def solve(jogo):
    num = 0
    for i in range(9):
        for j in range(9):
            antigo_number = num
            num = random.randint(1,9)
            if num == antigo_number:
                num -= 1
            if verify(jogo,i,j,num) == True:
                jogo[i][j] = num

    for i in range(9):
        print(jogo[i])
    
     
solve(jogo)
                
                

            
                
        
    