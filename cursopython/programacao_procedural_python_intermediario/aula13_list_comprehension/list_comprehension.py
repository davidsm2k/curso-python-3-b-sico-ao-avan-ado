l1 = [1,2,3,4,5,6,7,8,9,10]

ex1 = [variavel for variavel in l1] # Iterando sobre cada valor da l1 e jogando no ex1
print(f'Exemplo 1: {ex1}')

ex2 = [v * 2 for v in l1] # Iterando sobre cada valor da l1 multiplicando por 2 e jogando no ex2
print(f'Exemplo 2: {ex2}')

ex3 = [(v, v2) for v in l1 for v2 in range(3)]# O v está iterando na lista e o v2 iterando sobre cada elemento da lista
print(f'Exemplo 3: {ex3}')

l2 = ['Luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@') for v in l2] #Mudando letras 'a' por '@'
print(f'Exemplo 4: {ex4}')

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex5 = [(x, y) for y, x in tupla]
print(f'Exemplo 5: {ex5}')
ex5 = dict(ex5)
print(f'Exemplo 5.1: {ex5}')
print(f'Exemplo 5.2: {ex5["valor2"]}')

l3 = list(range(100))
ex6 = [v for v in l3 if v % 2 == 0] # Pegando só os valores divisiveis por 2
print(f'Exemplo 6: {ex6}')
# ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
ex6 = [v for v in l3 if v % 3 == 0 and v % 8 == 0] # Pegando só os valores divisiveis por 3 e 8
print(f'Exemplo 6.1: {ex6}')
ex6 = [v if v % 3 == 0 else -1 for v in l3]
print(f'Exemplo 6.2: {ex6}')
ex6 = [v if v % 3 == 0 and v % 8 == 0 else -1 for v in l3]
print(f'Exemplo 6.3: {ex6}')
