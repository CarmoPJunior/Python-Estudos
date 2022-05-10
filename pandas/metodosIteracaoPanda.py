# Importa a lib do Pandas
import pandas as pd
  
# Cria uma lista de dictionary, para realizar os testes
list_df = [{'nome':'Ana', 'idade': 25},
            {'nome':'Paulo', 'idade':40},
            {'nome':'Ivan', 'idade':32}]
  
# Cria um dataframe com a lista criada
df = pd.DataFrame(list_df)

# Imprimi o dataframe criado
print('DataFrame: \n', df)

 ## Iteração utilizando o método DataFrame.itertuples():  
print('\nLinhas Iteradas usando o método iterrows() : ')
for index, row in df.iterrows():
    print(row['nome'], row['idade'])
  

## Iteração utilizando o método DataFrame.itertuples(): 
print('\n Linhas Iteradas usando o metódo itertuples() : ')
for row in df.itertuples():
    print(getattr(row, 'nome'), getattr(row, 'idade'))
 