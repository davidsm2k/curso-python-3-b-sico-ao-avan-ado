import valida_cnpj as cnpj

cnpj1 = input("Digite o CNPJ: ")

validacao = cnpj.valida_cnpj(cnpj1)

print(f'{cnpj1} é valido') if validacao else print(f'{cnpj1} é invalido')

