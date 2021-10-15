"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""
import re
from copy import deepcopy

def removendo_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def converte_int(cnpj):
    novo_cnpj = []
    for n in range(14):
        novo_cnpj.append(int(cnpj[n]))
    return novo_cnpj


def primeiro_digito(cnpj=None):
    sum_dig = 0

    if cnpj is None:
        cnpj = []

    mult = 5
    for n in range(4):
        sum_dig += cnpj[n] * mult
        mult -= 1

    mult = 9
    for n in range(4, 12, 1):
        sum_dig += cnpj[n] * mult
        mult -= 1

    digito = 11 - (sum_dig % 11)
    return 0 if digito > 9 else digito


def segundo_digito(cnpj=None):
    sum_dig = 0

    if cnpj is None:
        cnpj = []

    mult = 6
    for n in range(5):
        sum_dig += cnpj[n] * mult
        mult -= 1

    mult = 9
    for n in range(5, 13, 1):
        sum_dig += cnpj[n] * mult
        mult -= 1

    digito = 11 - (sum_dig % 11)
    return 0 if digito > 9 else digito


def valida_cnpj(cnpj):
    cnpj = removendo_caracteres(cnpj)
    cnpj = converte_int(cnpj)
    novo_cnpj = deepcopy(cnpj[:-2])

    d1 = primeiro_digito(novo_cnpj)
    novo_cnpj.append(d1)
    d2 = segundo_digito(novo_cnpj)
    novo_cnpj.append(d2)


    return "CNPJ VÁLIDO" if int(novo_cnpj == cnpj) else "CNPJ INVÁLIDO"

if __name__ == "__main__":

    cnpj = input("Digite o CNPJ: ")

    validado = valida_cnpj(cnpj)

    print(validado)
