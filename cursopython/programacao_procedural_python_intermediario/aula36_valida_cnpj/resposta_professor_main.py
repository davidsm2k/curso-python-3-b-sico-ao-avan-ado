import resposta_professor_cnpj as cnpj

cnpj1 = '1234567891111'

if cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')
