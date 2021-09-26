"""
Funções (def) em Python -
*args -> argumentos sem valor
**kwargs -> argumentos com valor
"""

# # ISSO DARA ERRO o padrão é primeiro os argumentos sem valor e dps os com valor
# def func(a1, a2, a3, a4, a5, nome = None, a6):
#     print(a1, a2, a3, a4, a5, nome, a6)
#
# func(nome = 'David',1, 2, 3,4,5,)

# def func(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
# func(1,2,3,4,5)

# # Os valores das tuplas não podem ser alterados caso queira fazer isso é preciso criar uma lista
# def func(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#
# func(1,2,3,4,5)

# # Lista em tupla normal
# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# func(lista, '6')

# # Lista desempacotada
# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# func(*lista, '6') # Lista desempacotada

# # Lista desempacotada
# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2) # Lista desempacotada

# # **kwargs
# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(kwargs['nome'], kwargs['sobrenome'])
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2, nome = 'David', sobrenome = 'Santos')

# GET - Utilizar quando não tem certeza se o argumento ira ser criado mesmo
def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(f'Idade existe e ela é {idade}')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome = 'David', sobrenome = 'Santos', idade=22)
