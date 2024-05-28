import argparse

parser = argparse.ArgumentParser(description='Aula07')
parser.add_argument('--path', action='store',dest='file_path', required=True, help='nome do arquivo')
parser.add_argument('--file', action='store',dest='palavra', required=True, help='palavra a ser procurada')
arguments = parser.parse_args()
path = arguments.file_path
palavra = arguments.palavra


count = 0
f = open(path, 'r')
texto = f.readlines()
for linhas in texto:
    print(linhas)
    palavras = linhas.split()
    for limpas in palavras:
        print(limpas)
        palavra_formatada = limpas.strip(',.!?;')
        if palavra_formatada == palavra:
            print(palavra_formatada)
            count += 1 
print(f'A palavra {palavra} apareceu {count} vezes')
