'''
count - Itertools (Gera um contador que é um iterador)
'''
from itertools import count

contador = count() # lança numeros infinitamente
# contador = count(start=5) # Start inicio da contagem
# contador = count(step=2) # Condição que sera exibido no caso pulando de dois em dois
# contador = count(step=0.1) # Condição que sera exibido no caso colocando casa decimal
# contador = count(start= 5, step=2) # Os dois juntos
# contador = count(start= 9, step=-1) # Faz a contagem de traz pra frente

for valor in contador:
    print(round(valor,2)) #Round para arredondar o valor no caso com duas casa decimais

    if valor >= 10 or valor <= -10:
        break

nomes = 'David', 'May', 'Damo', 'Dama', 'Loló', 'DeQueijo', 'Sant'

print(list([(v1,v2) for v1, v2 in zip(contador, nomes)]))
