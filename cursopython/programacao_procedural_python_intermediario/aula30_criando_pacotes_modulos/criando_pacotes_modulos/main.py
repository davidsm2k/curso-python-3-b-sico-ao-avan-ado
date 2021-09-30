from vendas.calc_preco import aumento, reducao
from vendas.formata.preco import real

preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata= True)
preco_com_reducao = reducao(preco, 15)

print(f'{preco_com_aumento}')
print(f'{preco_com_reducao}')
