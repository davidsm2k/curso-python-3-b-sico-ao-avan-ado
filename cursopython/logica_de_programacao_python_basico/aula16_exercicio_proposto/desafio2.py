try:
    horas = input('Digite as horas:(Ex.: 11.30 = 11h30) ')
    horas = float(horas)

    if horas >= 0 and horas <= 11.59:
        print(f'Bom dia ! \nHora Informada: {horas}')
    elif horas <= 17.59:
        print(f'Boa Tarde ! \nHora Informada: {horas}')
    elif horas <= 23.59:
        print(f'Boa Noite ! \nHora Informada: {horas}')
    else:
        print('Informe um horário valido.')
except:
    print('ERROR: Formato de hora incorreto!')
