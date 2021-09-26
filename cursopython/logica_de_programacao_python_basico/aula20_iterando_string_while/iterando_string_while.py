# indices
# 0123456789...............33

frase = 'O rato roeu a roupa do rei de roma'
tamanho_da_frase = len(frase)
contador = 0
nova_string = ''

# while contador < tamanho_da_frase:
#     print(frase[contador], contador)
#     contador += 1

# while contador < tamanho_da_frase:
#     nova_string += frase[contador]
#     print(nova_string)
#     contador += 1

# while contador < tamanho_da_frase:
#     letra = frase[contador]
#     if letra == 'r':
#         nova_string += 'R'
#     else:
#         nova_string += letra
#     contador += 1
#
# print(nova_string)

print(f'Frase: {frase}')
input_do_usuario = input('Qual letra deseja colocar maiuscula: ')

while contador < tamanho_da_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
