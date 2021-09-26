"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

contador1 = 0
contador2 = 10

for n in range(9):
    print(f'{contador1} {contador2}')
    contador1 += 1
    contador2 -= 1

print('\n')

# RESULTADO DO PROFESSOR
for p, r in enumerate(range(10,1,-1)):
    print(p, r)
