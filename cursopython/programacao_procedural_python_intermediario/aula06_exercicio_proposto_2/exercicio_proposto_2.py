"""
1 - Crie uma funcão1 que recebe uma função2 como parametro e retorne o valor da função2 executada.
"""
# print('Resposta Exercicio 1')
# def func1(arg):
#     return arg
#
# def func2():
#     valor_func2 = 'Valor Função 2'
#     return valor_func2
#
# var = func2()
# print(func1(var))

'''
2 - Crie uma funcao1 que recebe uma função2 como parametro e retorne o valor da função2 executada. Faça a funcao1
executar duas funções que recebam um numero diferente de argumentos.
'''
print('Resposta Exercicio 2')
def func3(*arg):
    arg = list[arg]
    return arg

def func4():
    valor_func2 = 'Valor Função 2'
    return valor_func2

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

var = func4()
var2 = fala_oi('David Santos')
var3 = saudacao(saudacao='Olá', nome='Dave')
var4 = func3(var, var2, var3)
print(var4)
