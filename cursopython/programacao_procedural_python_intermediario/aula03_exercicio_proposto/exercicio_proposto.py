"""
1 - Crie uma função que exibe uma saudação com os parametros saudação e nome.
"""
print('RESPOSTA 1')
def exibi_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

msg = exibi_saudacao(nome='David', saudacao="Boa Noite")
print(msg)


"""
2 - Crie uma função que recebe 3 numeros como parametros e exiba a soma entre eles.
"""
print('\nRESPOSTA 2')
def soma_3n(n1,n2,n3):
    return n1 + n2 + n3

soma = soma_3n(5,5,5)
print(soma)


"""
3 - Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo.
"""
print('\nRESPOSTA 3')
def calc_porc(valor, porc):
    porcentagem = (porc*valor)/100
    return valor + porcentagem

soma_porc = calc_porc(50, 10)
print(soma_porc)

"""
4 - Fizz Buzz - Se o parametro da função for divisivel por 3, retorne fizz, se o parametro da função 
dor divisivel por 5, retorne buzz. Se o parametro da função for divisivel por 5 e por 3, retorne 
FizzBuzz, caso contrário, retorne o numero enviado.
"""
print('\nRESPOSTA 4')
def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FuzzBuzz'
    if numero % 5 == 0:
        return 'buzz'
    if numero % 3 == 0:
        return 'fizz'
    return numero

print(fizz_buzz(9))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(2))


