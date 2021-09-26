usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Vocé precisa digitar pelo menos 6 caracteres')
else:
    print('Cadastro realizado com sucesso.')
