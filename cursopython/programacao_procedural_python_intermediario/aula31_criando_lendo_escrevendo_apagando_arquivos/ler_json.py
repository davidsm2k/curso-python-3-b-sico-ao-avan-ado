import json

with open('d1.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json) # Transformando json em dicionario

print(type(d1_json))

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(f'\t{k1}: {v1}')
