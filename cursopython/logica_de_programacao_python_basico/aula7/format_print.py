'''
Iniciar com letra, pode conter numeros, separar _, letras minúsculas
'''

nome = 'David Santos' #str
idade = 22 # int
altura = 1.80 # float
e_maior = idade > 18 # bool
peso = 75
imc = peso / (altura ** 2)

print(nome, "tem", idade, "anos de idade e seu IMC é ", imc)
print(F"{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}")
print("{2} tem {1} anos de idade e seu IMC é {0}".format(nome, idade, imc))
print("{n} tem {i} anos de idade e seu IMC é {im}".format(n=nome, i=idade, im=imc))
