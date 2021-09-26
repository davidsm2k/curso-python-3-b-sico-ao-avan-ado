while True:
    numero_1 = input("Digite um numero inteiro: ")
    numero_2 = input("Digite outro numero inteiro: ")

    if not numero_1.isnumeric() or not numero_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    tipo_calc = input('Digite o tipo do calculo "+" "-" "*" "/": ')

    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    if tipo_calc == "+":
        print(f"{numero_1} {tipo_calc} {numero_2} = {numero_1 + numero_2}")
    elif tipo_calc == "-":
        print(f"{numero_1} {tipo_calc} {numero_2} = {numero_1 - numero_2}")
    elif tipo_calc == "*":
        print(f"{numero_1} {tipo_calc} {numero_2} = {numero_1 * numero_2}")
    elif tipo_calc == "/":
        print(f"{numero_1} {tipo_calc} {numero_2} = {(numero_1 / numero_2):.2f}")
    else:
        print("Tipo de calculo invalido!")

    sair = input('Deseja sair ? [s]im ou [n]ão ')
    if sair == 's':
        break
    print()
