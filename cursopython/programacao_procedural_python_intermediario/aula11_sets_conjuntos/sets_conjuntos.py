# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set na esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

set1 = {1,2,3,4,5,6} # Set não possui identificador igual dicionarios
print(type(set1))

#Criando set sem valor

# set2 = {} # Errado

set3 = set()# Certo

print(type(set3))

# Adicionando
set3.add(1)
set3.add(2)
set3.add(3)
print(f"Valores adicionados -> {set3}")

# Discard (Excluir)
set3.discard(2)
print(f'Descartando/Excluindo -> {set3}')

# Update (Adiciona cada elemento iterando por cada um) não respeita ordem
set3.update("Python")
print(f'Update 1 -> {set3}')
set3.update([1,2,3,4,5], {5,6,7,8})
print(f'Update 2 -> {set3}')

# Set remove itens duplicados
l1 = [1,2,1,1,3,4,5,6,6,6,6,7,8,9,'Luiz', 'Luiz']
print(f'Lista Original -> {l1}')
l1 = set(l1)
l1 = list(l1)

print(f'Lista sem duplicação -> {l1}')

# union | (une/união)
set4 = {1,2,3,4,5}
set5 = {5,6,7,8}
set6 = set4 | set5

print(f'Sets unidos -> {set6}')

# Intersection & (todos os elementos presentes nos dois sets)
set7 = {1,2,3,4,5}
set8 = {4,5,6,7,8}
set9 = set7 & set8

print(f'Sets Intersection -> {set9}')

# Difference - (elementos apenas/somente no set na esquerda)
set10 = {1,2,3,4,5}
set11 = {4,5,6,7,8}
set12 = set10 - set11

print(f'Sets Difference -> {set12}')

# Symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
set13 = {1,2,3,4,5}
set14 = {4,5,6,7,8}
set15 = set13 ^ set14

print(f'Sets Symmetric_difference -> {set15}')

