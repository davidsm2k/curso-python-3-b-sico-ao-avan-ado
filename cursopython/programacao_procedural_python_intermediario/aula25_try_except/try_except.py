try:
    a = 0
    # try:
    #     a = 1/0
    # except:
    #     print('Erro')
except NameError as erro:
    print(f'Erro do desentolvedor, fale com ele. Tipo de erro: {erro}')
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:
    pass
finally:
    a = ''

print(a)
