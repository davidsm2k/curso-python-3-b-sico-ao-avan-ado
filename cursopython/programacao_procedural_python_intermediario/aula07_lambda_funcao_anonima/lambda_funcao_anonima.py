def funcao(arg, arg2): #Funcao normal
    return arg * arg2

var = funcao(2,2)

print(f'Função Normal: {var}')

a = lambda x, y: x * y # funcao anonima

print(f'Função Lambda Anonima: {a(3,3)}')

# Porque usar funcao anonima ? Um exemplo é para usar dentro de outras funções
print('\n EXEMPLO ORDENANDO LISTA \n')
# Ordenando lista sem Lambda
print('SEM LAMBDA')
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

def func(item):
    return item[1]

lista.sort(key=func)
print(lista)

print('\nCOM LAMBDA')
lista2 = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]
#Esse modo altera a lista original
# lista2.sort(key=lambda item: item[1], reverse=True) # **reverse** -> caso queira inverter a ordem

# Esse modo não altera a lista original
print(sorted(lista2, key=lambda i: i[1], reverse=True))
print(lista2)
