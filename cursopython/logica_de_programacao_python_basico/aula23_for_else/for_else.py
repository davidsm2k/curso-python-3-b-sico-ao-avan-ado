'''
For / Else em Python
'''

variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        print('Existe uma palavra que começa com J')
        break
else:
    print('Não existe uma palavra que começa com J')