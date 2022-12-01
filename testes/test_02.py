'''TODO
Desafio extra: valor mais longo
Escreva uma função chamada valor_longo que usa um dicionário
como um argumento e retorna o primeiro valor mais longo do
dicionário. Por exemplo, o seguinte dicionário deve retornar
– maçã como o valor mais longo.
frutas = {'fruta': 'maçã', 'cor': 'verde'}
'''
frutas = {'fruta':'maçã',
         'cor':'verde'}

def long_value():
    if len(frutas['cor']) > len(frutas['fruta']):
        return frutas['cor']
    else:
        return frutas['fruta']    

print(long_value())

def test_deve_retornar_item_com_valor_mais_longo():
    expected = 'verde'
    tested = long_value()
    assert  tested == expected        

       