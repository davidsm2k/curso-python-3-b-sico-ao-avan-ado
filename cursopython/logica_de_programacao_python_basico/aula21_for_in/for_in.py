'''
For in em Python
Iterando string com for
Função range(start=0, stop, step=1)
Start = Argumento de inicio onde eu quero que inicie o laço (Por padrão é 0)
Stop = Argumento para informar quando ira parar
Step = Argumento para informar de quantas em quantas casas ele vai pular (Por padrão 1)
'''

# texto = 'Python'
#
# for letra in texto:
#     print(letra)

# texto = 'Python'
#
# for n, letra in enumerate(texto):
#     print(n, letra)

# texto = 'Python'
#
# for n in range(6):
#     print(texto[n])

# texto = 'Python'
#
# for letra in texto:
#     print(letra)

# multiplicador = 0
# for n in range(0,71,7):
#     print(f'7 x {multiplicador} = {n}')
#     multiplicador += 1

texto = 'Python'
novo_texto = ''

for letra in texto:
    if letra == 'h':
        # continue
        novo_texto += letra.upper()
    elif letra == 't':
        novo_texto += letra.upper()
        # break
    else:
        novo_texto += letra

print(novo_texto)
