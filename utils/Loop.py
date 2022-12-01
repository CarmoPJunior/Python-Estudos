pessoas = [({'nome': 'João', 'cidade': 'Belo Horizonte'}),
                     ({'nome': 'Maria', 'cidade': 'São Paulo'}),
                     ({'nome': 'Pedro', 'cidade': 'Curitiba'})]
contador = 0
for pessoa in pessoas:
    contador += 1
    teste = 'rererer'
    print(contador)
    if pessoa['nome'] == 'Maria':
        print(pessoa['nome'], "mora em", pessoa['cidade'])
        break

print(teste)

