print()
print('Texto explicativo')

perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '8',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 3 * 2 ?',
        'respostas': {
            'a': '6',
            'b': '2',
            'c': '9',
        },
        'resposta_certa': 'a',
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}\n\t {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'\t [{rk}]: {rv}')

    resposta_usuario = input("Sua Resposta: ")
    print()

    if resposta_usuario == pv['resposta_certa']:
        print("PARABENNS !! Voce acertou")
        respostas_certas += 1
    else:
        print(f"ERROU !! Voce não acertou a resposta. :(\nReposta certa é {pv['resposta_certa']}")

qtd_perguntas = len(perguntas)
porcentagem_acerto = (respostas_certas / qtd_perguntas) * 100

print(f'Você acertou {respostas_certas} resposta(s).')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')
