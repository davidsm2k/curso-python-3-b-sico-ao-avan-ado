try: # Esse trecho de código serve para adicionar o caminho das pastas de trás a esse arquivo
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise

# A importação sem techo acima da erro pq não é possivel importar arquivos atras da pasta de origem
from pacote1.modulo1 import variavel1

variavel2 = 'variavel2'

print(variavel1)
