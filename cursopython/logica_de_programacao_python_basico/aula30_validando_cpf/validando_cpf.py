"""
CPF = 168.995.350-09
----------------------------------
1 * 10 = 10                 #   1 * 11 = 11
6 * 9 = 54                  #   6 * 10 = 60
8 * 8 = 64                  #   8 *  9 = 72
9 * 7 = 63                  #   9 *  8 = 72
9 * 6 = 54                  #   9 *  7 = 63
5 * 5 = 25                  #   5 *  6 = 30
3 * 4 = 12                  #   3 *  5 = 15
5 * 3 = 15                  #   5 *  4 = 20
0 * 2 = 0                   #   0 *  3 = 0
                            #   0 *  2 = 0
        297                 #               343
11 - (297 % 11) = 11        #   11 - (343 % 11) = 9
11 > 9 = 0                  #
                            #
Digito 1 = 0                #   Digito 2 = 9
"""

cpf = input('Digite seu CPF: ')

# Criando listas***********
cpf_original = []
for n in range(11):
    cpf_original.append(int(cpf[n]))

novo_cpf = []
for n in range(9):
    novo_cpf.append(int(cpf[n]))

# Calculando Valores********

#   DIGITO 1
total_result_mult = 0
for i, n in enumerate(range(10, 1, -1)):
    result_mult = novo_cpf[i] * n
    total_result_mult += result_mult

formula_d1 = 11 - (total_result_mult % 11)
digito_1 = 0 if formula_d1 > 9 else formula_d1
novo_cpf.append(digito_1)

#   DIGITO 2
total_result_mult_2 = 0
for i, n in enumerate(range(11, 1, -1)):
    result_mult = novo_cpf[i] * n
    total_result_mult_2 += result_mult

formula_d2 = 11 - (total_result_mult_2 % 11)
digito_2 = 0 if formula_d2 > 9 else formula_d2
novo_cpf.append(digito_2)

# VERIFICANDO CPF
validacao_cpf = 'CPF Válido' if (cpf_original == novo_cpf and not sequencia) else 'CPF Inválido'

print(validacao_cpf)
