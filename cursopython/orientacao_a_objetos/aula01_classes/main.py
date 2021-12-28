from pessoa import Pessoa

p1 = Pessoa("David", idade=23)
p2 = Pessoa("Maya", idade=22)

p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer('uva')
p1.falar('Treinos')
p1.parar_comer()
p1.falar('Treinos')
p1.falar('Treinos')
p1.comer('laranja')
p1.parar_falar()
p1.parar_falar()

print("*************************")
p1.falar("Lua")
p2.falar("Sol")
p1.parar_falar()
p1.comer("Strogonof")
p2.comer("Hamburguer")

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
