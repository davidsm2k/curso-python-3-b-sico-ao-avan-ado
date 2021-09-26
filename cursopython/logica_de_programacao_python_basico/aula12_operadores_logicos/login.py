usuario = input('Digite seu usuario: ')
senha = input('Digite a sua senha: ')

usuario_bd = 'david'
senha_bd = '123456'

if usuario == usuario_bd and senha == senha_bd:
    print("Você esta logado no sistema !")
else:
    print('Usuario ou senha inválidos.')