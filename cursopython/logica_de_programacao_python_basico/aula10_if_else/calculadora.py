numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite outro numero: "))
tipo_calc = input('Digite o tipo do calculo "+" "-" "*" "/": ')

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
