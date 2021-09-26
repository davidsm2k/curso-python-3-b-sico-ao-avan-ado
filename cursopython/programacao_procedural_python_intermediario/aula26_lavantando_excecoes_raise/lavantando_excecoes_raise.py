# https://docs.python.org/3/library/exceptions.html

# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print(f'Log: {error}')
#         raise # Retorna o log de erro
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:
#     print(error)

# LANÇANDO MINHA PRÓPRIA EXCEÇÃO
def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0")
    return n1 / n2

try:
    print(divide(2, 0))
except ValueError as error:
    print(f'ERRO: {error}')
