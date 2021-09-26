from  dados import produtos, pessoas, lista

# MAP -> MAPEIA UMA FUNÇÃO QUE PASSA POR CADA ELEMENTO DO OBJETO QUE FOI ESCOLHIDO

# # USANDO MAP NA LISTA
# # nova_lista = map(lambda x: x * 2, lista) # com map
# # nova_lista = [x * 2 for x in lista] # com list_comprehension
# print(lista)
# print(list(nova_lista))

# # USANDO MAP NOS PRODUTOS
# def aumenta_preco(produto):
#     produto['preco'] = round(produto['preco'] * 1.05, 2)
#     return produto
#
# novos_produtos = map(aumenta_preco, produtos) # Mapeando produtos de acordo com a função aumenta_preco
#
# for produtos in novos_produtos:
#     print(produtos)

#USANDO MAP NAS PESSOAS
def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)

for pessoas in nomes:
    print(pessoas)
    