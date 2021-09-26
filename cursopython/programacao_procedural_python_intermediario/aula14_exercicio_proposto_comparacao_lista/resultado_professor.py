string = '012345678901234567890123456789'

# PARA EXPLICAR ##############
contadores = [i for i in range(0, len(string), 10)]
print(contadores)
tuplas = [(i, i + 10) for i in range(0, len(string), 10)]
print(tuplas)
raw = [f'string[{i}:{i+10}]' for i in range(0, len(string), 10)]
print(raw)
##########################

#RESPOSTA #############
lista = [string[i: i + 10] for i in range(0, len(string), 10)]
retorno = ".".join(lista)

print(lista)
print(retorno)
