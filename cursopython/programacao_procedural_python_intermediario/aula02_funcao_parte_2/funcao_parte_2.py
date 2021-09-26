"""
Funções (def) em Python - return (Parte 2)
"""

# def divisao(n1, n2):
#     return n1 / n2
#
# divide = divisao(8, 2)
#
# print(divide)

# def divisao(n1, n2):
#     if n2 == 0:
#         return
#
#     return n1 / n2
#
# divide = divisao(8, 0)
#
# if divide:
#     print(divide)
# else:
#     print('Conta Inválida.')

# ***********COISA NOVA*********************
# def f(var):
#     print(var)
#
# def dumb():
#     return f # Informar a função sem os parenteses chama ela sem executar
#
# var = dumb()('E colocar o meu valor aqui') # Segundo parentese com valor é o parametro da função 'f'

def f(var):
    print(var)

def dumb():
    return f

var = dumb() # var agora é uma função igual a def 'f'
var('Pode imprimir algo na tela.')
