import math 

"""
'''TODO'''

f"Dia 1: Divisão e Raiz Quadrada

f"- Escreva uma função chamada divide_or_square que leva um
argumento (um número).

f"- retorna a raiz quadrada do número
se for divisível por 5, retorna seu resto se não for divisível por
5. 

f"-Por exemplo, se você passar 10 como argumento, sua função
deve retornar 3,16 como a raiz quadrada."
'''
"""

def sum_number_more_one(x):
    return x + 1

def divide_or_square(num):
    #num = float(input("enter a number:\n"))
    if float(num) % 5 == 0:
        print("teste")
        source = math.sqrt(num)
        #return (f'\nThe square root of {num} it is {source}\n')
        return source
    else:
        rest = float(num) % 5
        #return (f"\n the rest of the number: {num} it is {rest}")
        return rest
     
    
# test to return source or rest the number
def test_deve_retornar_square():
    num = 10
    expected = math.sqrt(num)  
    tested = divide_or_square(num)
    assert  tested == expected        

# test to return source or rest the number
def test_deve_retornar_resto_divisao():
    num = 1.50
    expected = float(num) % 5
    tested = divide_or_square(num)
    assert  tested == expected


def test_deve_somar_mais_um():
    tested = sum_number_more_one(3)
    expected = 4
    assert tested == expected 





