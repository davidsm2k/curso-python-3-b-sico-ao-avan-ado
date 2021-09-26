acumulador = 0
contador = 0

while contador < 10:
    acumulador += contador
    print(f'Contador: {contador} / Acumulador {acumulador}')
    # if (contador > 5):
    #     break
    contador += 1
else:
    print('Entrou no else')
print('Acabou')