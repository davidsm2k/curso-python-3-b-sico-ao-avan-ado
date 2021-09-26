from dados import produtos, pessoas, lista

# Filter é parecido com MAP, porém retorna os elementos que resultarem TRUE

# # FILTER na Lista
# nova_lista = filter(lambda x: x > 5, lista) # Com filter
# nova_lista = [x for x in lista if x > 5] # list_comprehension
# print(nova_lista)

# # FILTER nos Produtos
# # def filtra(produto):
# #     if produto['preco'] > 50:
# #         return True
# def filtra(produto):
#     if produto['preco'] > 50:
#         produto['e_caro'] = True
#     return True
# # nova_lista = filter(lambda p: p['preco'] > 50, produtos)
# nova_lista = filter(filtra, produtos)
# for produto in nova_lista:
#     print(produto)

# FILTER nas Pessoas
def filtra(pessoa):
    if pessoa['idade'] < 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)
for pessoa in nova_lista:
    print(pessoa)
