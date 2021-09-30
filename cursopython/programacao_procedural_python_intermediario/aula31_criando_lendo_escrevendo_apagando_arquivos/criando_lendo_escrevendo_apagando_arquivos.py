# http://docs.pythn.org/3/library/functions.html#open
# w -> leitura
# + -> add escrita
# r -> somente leitura
# a -> ativa o apeend mode (adiciona arquivos sem apagar jogando o cursos no final do arquivo e add coisas)
# import os -> apaga o arquivo
import json

file = open('abc.txt', 'w+') # criando arquivo com nome abc e dizendo que ele é para leitura e escrita
file.write('ABC\n')
file.write('Linha 1\n') # write serve para escrever no arquivo
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0,0) # seek informando as posiçoes serve para voltar o cursos para o inicio do arquivo e assim ler ele
print('Lendo as linhas: ')
print(file.read()) # read serve para ler todas as linhas do arquivo
print('######################')

file.seek(0, 0)
print(file.readline(), end='') # readLine serve para ler linha por linha / end com valor vazio serve para tirar a quebra de linha on final
print(file.readline(), end='') # readLine serve para ler linha por linha
print(file.readline(), end='') # readLine serve para ler linha por linha
print('######################')

file.seek(0, 0)
print(file.readlines()) # readLines retorna uma lista com as linhas
print('######################')

file.seek(0, 0)
# for linha in file.readlines():
#     print(linha, end='')
# OU
for linha in file.readlines():
    print(linha, end='')

file.close() # close serve para fechar o arquivo

print("\n################# OUTRO EXEMPLO ######################")

try:
    file2 = open('dfg.txt', 'w+')
    file2.write('DFG\n')
    file2.write('Linha')
    file2.seek(0)
    print(file2.read())
finally:
    file2.close()

print("\n################# FORMA MAIS PYTHONICA DE CRIAR ARQUIVOS (WITH) ######################")

with open('hij.txt', 'w+') as file3: # with -> trata o arquivo abrindo ele e após concluir tudo fecha ele automaticamnte
    file3.write('HIJ\n')
    file3.write('Linha 1\n')
    file3.write('Linha 2\n')
    file3.write('Linha 3\n')
    file3.seek(0)
    print(file3.read())

print("\n################# R - Leitura ######################")

with open('abc.txt', 'r') as file:
    print(file.read())

print("\n################# A - Adicionando coisas no arquivo ######################")

with open('abc.txt', 'a+') as file:
    file.write('Outra linhaa')
    file.seek(0)
    print(file.read())

print("\n################# REMOVENDO/EXCLUINDO ARQUIVO ######################")
# import os
# os.remove('abc.txt')
# os.remove('dfg.txt')
# os.remove('hij.txt')

print("\n################# CONVERTENDO PARA JSON ######################")

d1 = {
    'Pessoa 1':{
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
}

d1_json = json.dumps(d1)

with open('d1.json', 'w+') as file:
    file.write(d1_json)

    
