import criando_modulos

print(criando_modulos.PI)

lista = [2, 4]
print(criando_modulos.multiplica(lista))

# OU

from criando_modulos import multiplica, PI, dobra_lista
from outro import fala_oi

print(PI)

lista = [2, 4]
print(multiplica(lista))
print(dobra_lista(lista))
fala_oi()