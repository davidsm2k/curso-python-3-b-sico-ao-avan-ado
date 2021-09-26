# lista = 1234 # Não iteravel
# print(hasattr(lista, '__iter__')) #Verificando se o objeto é iteravel
#
# lista = 'String' # Iteravel
# print(hasattr(lista, '__iter__')) #Verificando se o objeto é iteravel
#
# lista = [0,1,2,3,4,5] # Iteravel, mas não é iterador
# print(hasattr(lista, '__iter__')) #Verificando se o objeto é iteravel
# print(hasattr(lista, '__next__')) #Verificando se o objeto é iterador
#
# # for v in lista:# For transforma o objeto em um iterador e usa esse iterador para manipular ou exibir valores
# #     print(v)
#
# lista = iter(lista) # transformando o obj em um iterador
# print(hasattr(lista, '__next__')) #Verificando se o objeto é iterador
#
# #Utilizando o objeto iterador
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))

#************ ITERAVEL é um obj que vc pode iterar sobre ele, mas ele não é necessariamente um iterador
#************ ITERADOR é um obj que pode te dar os valores um de cada vez sempre que precisar
#************ ITERADORES podem ser usados com for ou tambem usando o next() pegando um valor de cada vez

# GERADORES
import time

# # Sem o usar a forma certa de gerador
# def gera():
#     r = []
#     for v in range(100):
#         r.append(v)
#         time.sleep(0.1) # Delay de 1 segundo
#     return r
#
# g = gera()
# for n in g:
#     print(n)

#Usando a forma certa de gerador(GERADOR É UM ITERADOR)
# def gera():
#      for v in range(100):
#         yield v
#         time.sleep(0.1) # Delay de 1 segundo
#
# g = gera()
# print(hasattr(g, '__iter__'))
# for n in g:
#     print(n)

# *** DIFERENÇA DE UMA SULUÇÃO PARA A OUTRA
# *** Com o GERADOR vc recebe a informação assim que ela é gerada sem ter q esperar concluir todoo o processo

# # Criando gerador manualmente sem o for
#
# def gera():
#     variavel = 'Valor 1'
#     yield variavel
#     variavel = 'Valor 2'
#     yield variavel
#     variavel = 'Valor 3'
#     yield variavel
#
# g = gera()
#
# next(g)
# print(next(g))
# print(next(g))

# Forma mais simplificada de criar GERADORES
import sys

# Mesmas lista com tipos diferentes
l1 = [x for x in range(1000)] # Criando compreensão de lista
print(f'Tipo da L1: {type(l1)}')
print(f'Tamanho da L1: {sys.getsizeof(l1)}')
    # Lista são seu valor inteiro na memória

l2 = (x for x in range(1000)) # Criando gerador
print(f'Tipo da L2: {type(l2)}')
print(f'Tamanho da L2: {sys.getsizeof(l2)}')
    # Gerador só puxa o valor e ocupa espaço na memoria quando vc pedi o valor

