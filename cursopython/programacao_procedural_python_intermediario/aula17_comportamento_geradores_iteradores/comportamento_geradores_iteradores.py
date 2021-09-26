# List, tuples, str -> Sequences (São sequencias) -> Iteravel

# #Normal
nome = 'David Santos'
#
# for valor in nome:
#     print(valor)
#
# print('#' * 80)
#
# for valor in nome:
#     print(valor)

# Geradores e Iteradores (Dps de mostrar os dados não tem mais dados para mostrar novamente)
iterador = iter(nome)

try:
    print(next(iterador)) # D
    print(next(iterador)) # A
    print(next(iterador)) # V
    print(next(iterador)) # I
    print(next(iterador)) # D
    print(next(iterador)) #
    print(next(iterador)) # S
    print(next(iterador)) # A
    # print(next(iterador)) # N
    # print(next(iterador)) # T
    # print(next(iterador)) # O
    # print(next(iterador)) # S
except:
    pass

print('Cade o resto dos valores ?')
for valor in iterador:
    print(valor)

gerador = (letra for letra in nome)
try:
    print(next(gerador)) # D
    print(next(gerador)) # A
    print(next(gerador)) # V
    print(next(gerador)) # I
    print(next(gerador)) # D
    print(next(gerador)) #
    # print(next(gerador)) # S
    # print(next(gerador)) # A
    # print(next(gerador)) # N
    # print(next(gerador)) # T
    # print(next(gerador)) # O
    # print(next(gerador)) # S
except:
    pass

print('Cade o resto dos valores ?')
for valor in gerador:
    print(valor)

'''
Geradores e iteradores foram feitos para consumir os seus valor
e só. 
Após todo o consumo de seus valores não se usa eles outra vez
'''
