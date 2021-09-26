# Tuplas são similares a listas o que muda é que uma tupla não pode ser modificada
# Ao menos que vc converta ela para uma lista e modifique seu valor

# Tupla não pode ser modificada
# t1 = (1,2,3,4,5)
# t1[1] = 5

# Modificando tupla convertendo para lista e dps para tupla novamente
t1 = (1,2,3,4,5)
t1 = list(t1)
t1[3] = 3000
t1 = tuple(t1)

print(t1)
