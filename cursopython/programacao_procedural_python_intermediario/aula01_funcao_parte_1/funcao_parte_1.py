"""
Funções - def em Python (Parte 1)
"""

# def saudacao(msg, nome):
#     print(msg, nome)
#
# saudacao('Olá', 'David')

# def saudacao(msg='Olá', nome='usuário'):
#     print(msg, nome)
#
# saudacao()
# saudacao(nome='David')
# saudacao(nome='Zezinho', msg='Hello')

# def saudacao(msg='Olá', nome='usuário'):
#     nome = nome.replace('e', '3')
#     msg = msg.replace('l', '1')
#     print(msg, nome)
#
# saudacao()
# saudacao(nome='David')
# saudacao(nome='Zezinho', msg='Hello')

def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('l', '1')
    return f'{msg} {nome}'

variavel = saudacao()

print(variavel)
