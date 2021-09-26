lista1 = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista1}
print(f'Exemplo D1 -> {d1}')

lista2 = [
    ('chave', 2),
    ('chave2', 'valor2'),
]

d2 = {x: y*2 for x, y in lista2}
print(f'Exemplo D2 -> {d2}')

d3 = {x.upper(): y.upper() for x, y in lista1}
print(f'Exemplo D3 -> {d3}')

d4 = {x for x in range(5)}
print(f'Exemplo D4 (Criando um set) -> {d4}', type(d4))

d5 = {f'chave_{x}': x**2 for x in range(5)}
print(f'Exemplo D5 -> {d5}')
