import pandas as pd

df = pd.DataFrame({'ano': [2017,2018,2017,2018,2017,2018],
                       'mes': [1,1,2,2,3,3],
                       'usuarios': [215,167,123,193,235,241]})
print(df)

# Utiliando o metodo pivot
print(50 * '-')
print('--- Pivot Table ---')
print(50 * '-')

pivotTable = df.pivot(values = 'usuarios', index = 'mes', columns = 'ano')
print(pivotTable)


print(50 * '-')
print('--- Utiliando o metodo pivot com a função de agregação ---')
print(50 * '-')

df = pd.DataFrame({'ano': [2017,2018,2017,2018,2017,2018],
                       'mes': [1,2,2,2,3,3],
                       'usuarios': [215,167,123,193,235,241]})
print(df)

# Utiliando o metodo pivot com a função de agregação
print(50 * '-')
print('--- Pivot Table Com Agregação ---')
print(50 * '-')


pivotTable = df.pivot_table(values = 'usuarios', index = 'mes', columns = 'ano', aggfunc = 'sum')
print(pivotTable)