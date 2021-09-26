nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print(f'{nome} seu nome é muito curto.')
elif tamanho_nome <= 6:
    print(f'{nome} seu nome é normal.')
else:
    print(f'{nome} seu nome é muito grande.')

