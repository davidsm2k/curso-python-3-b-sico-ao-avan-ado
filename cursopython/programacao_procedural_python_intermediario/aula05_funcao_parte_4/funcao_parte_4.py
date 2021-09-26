# variavel = 'valor'
#
# def func():
#     print(variavel)

# #Não é uma boa pratica
# def func2():
# # é preciso dizer que ela é global para se utilizar a variavel global e não uma nova variavel dentro do escopo dessa def
#
#     global variavel
#     variavel = 'Outro valor'
#     print(variavel)

# #Boa pratica
# def func2(**kwargs):
#     arg = kwargs.get('arg')
#     if arg is not None:
#         arg = arg.replace('v', 'c')
#     return arg
#
# func()
# outra_variavel = func2(arg=variavel)
#
# print(outra_variavel)

####### OUTROS EXEMPLO SEM VARIAVEL GLOBAL
def func():
    outra_variavel = 'David Santos'
    return outra_variavel

def func2(arg):
    print(arg)

var = func()
func2(var)
