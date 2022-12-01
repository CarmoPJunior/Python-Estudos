
"""
'''TODO'''

Day 2: Strings to Integers
Write a function called convert_add that takes a list of strings 
as an argument and converts it to integers and sums the list. For 
example ['1', '3', '5'] should be converted to [1, 3, 5] and
summed to 9.
'''
"""

x = ['1','3','5']

def convert_add(x):
    novo_x = []
    for i in x:
        novo_x.append(int(i))
        #print(i)
    soma = sum(novo_x)
    print(soma)
    return soma    

convert_add(x)    

'''
TODO

Extra Challenge: Duplicate Names
Write a function called check_duplicates that takes a list of 
strings as an argument. The function should check if the list has 
any duplicates. If there are duplicates, the function should return 
the duplicates. If there are no duplicates, the function should 
return "No duplicates". For example, the list of fruits below 
should return apple as a duplicate and list of names should 
return "no duplicates".
fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

'''
names = ['applee', 'orange','apple', 'banana','Yoda', 'Moses', 'Joshua', 'Mark']


def check_duplicates(names):
    dup = {x for x in names if names.count(x) > 1 }
    if dup:
        print(dup)
        return dup 
    else:
        return "No duplicates"
     
check_duplicates(names)    


# convert_add that takes a list of strings as an argument and converts it to integers and sums the list.
def test_converts_it_to_integers_and_sums_the_list():

    #Arrange (Preparar o teste) Mock
    x = ['1','3','5']
    novo_x = []
    for i in x:
        novo_x.append(int(i))
    resultExpected = sum(novo_x)

    #ACT (Rodar o teste)
    resultReceived = convert_add(x)

    #Assert (Verificar as asserções)
    assert resultReceived == resultExpected
   

def test_duplicate_names():

    #Arrange (Preparar o teste) Mock
    names = ['apple', 'orange','apple', 'banana','Yoda', 'Moses', 'Joshua', 'Mark']
    dup = {x for x in names if names.count(x) > 1 }
    if dup:
        resultExpected = dup
    else: resultExpected = "No duplicates"    

    #ACT (Rodar o teste)
    resultReceived = check_duplicates(names) or "No duplicates"

    #Assert (Verificar as asserções)
    assert resultReceived == resultExpected or "No duplicates"
