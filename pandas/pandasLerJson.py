
import pandas as pd
import json
import matplotlib.pyplot as plt
import datetime

def convertUtcToDateString(utcDate):
    return datetime.datetime.fromtimestamp(
            int(utcDate) ).strftime('%d-%m-%Y %H:%M:%S:%u')

def convertDateStringToUtc(stringDate):
    return datetime.datetime.strptime(stringDate, "%d-%m-%Y %H:%M:%S").timestamp()

# pd.Timestamp('2019-01-15 13:30:00').timestamp()

data_JSON =  """[
{
"jsonrpc": "2.0",
"result": [
{
"hostid": "10481",
"host": "SRV-TAMOIOS-33"
}
],
"id": 1
},
{
"jsonrpc": "2.0",
"result": [
{
"itemid": "48316",
"clock": "1655295196",
"value": "54.299801",
"ns": "418744817"
},
{
"itemid": "48316",
"clock": "1655295136",
"value": "38.020892",
"ns": "34845400"
}
],
"id": 1
},
{
"jsonrpc": "2.0",
"result": [
{
"itemid": "48329",
"clock": "1655295209",
"value": "7.468623982877497",
"ns": "777604832"
},
{
"itemid": "48329",
"clock": "1655295149",
"value": "7.612761910870046",
"ns": "472082855"
}
],
"id": 1
}
]
"""

dados = json.loads(data_JSON)


dataConvertida = convertDateStringToUtc('15-06-2022 09:13:36') 
print(dataConvertida)

print(convertUtcToDateString(1655295196))


# dados.append(requisicao_two)

host = dados[0]['result'][0]['host']

df = pd.json_normalize(dados[1:])

df = df.explode('result')

df = df['result'].apply(pd.Series)

df['host'] = dados[0]['result'][0]['host']



#dados
# convertendo para os values para float
df["value"] =df["value"].astype('float64')

# Formata a data para o padão 'dd-mm-yyyy HH:min'
df["clock"]  = pd.to_datetime(df["clock"] , unit='s', origin='unix') 
df['clock'] = df['clock'].dt.strftime('%d-%m-%Y %H:%M')


pivotTable =df.pivot(values = ['value'], index = 'clock', columns = 'itemid')

print(pivotTable)

# dados da memoria 
df_memoria = df[df['itemid'].isin(['48329'])]
memoria = df_memoria["value"]
clock_memoria = df_memoria["clock"] 


#dados do processador
df_cpu = df[df['itemid'].isin(['48316'])]
cpu = df_cpu["value"]
clock_cpu = df_cpu["clock"] 

#clock_memoria = pd.Timestamp.fromtimestamp(df["clock"])

plt.plot(clock_memoria,memoria, label='Memoria')
plt.plot(clock_cpu,cpu, label='Processador')
host = host
plt.title(host)
plt.ylabel('%')
plt.xlabel('Memoria X Processador')
plt.legend(loc= 2, fontsize = 9)

plt.savefig('grafico.pdf', dpi =120)
plt.show()