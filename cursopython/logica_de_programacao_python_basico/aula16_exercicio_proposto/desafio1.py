try:
    num1 = input('Digite um numero inteiro: ')
    num1 = int(num1)

    if num1%2 == 0:
        print(f'O numero {num1} é PAR')
    else:
        print(f'O numero {num1} é IMPAR')
except:
    print('ERROR: Você deve informar somente um numero inteiro.')
