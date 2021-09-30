'''
Módulos padrão do Python:
Módulos são arquivos .py (que contém código python) e servem para expandir
as funcionalidades padrão da linguagem.
Veja todos os módulos padrão do Python em:
https://docs.python.org/3/py-modindex.html
'''

# Exemplos de importação
from random import randint as randint_original # Importando e dando um novo nome
for i in range(10):
    print(randint_original(0,10))

# import sys
#

# print(sys.platform) # Vendo qual plataforma o script esta sendo

from sys import platform
print(platform) # Vendo qual plataforma o script esta sendo usado
