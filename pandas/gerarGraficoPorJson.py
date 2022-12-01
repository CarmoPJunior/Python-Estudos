# Importar o módulo
import json
import matplotlib.pyplot as plt
import datetime

def convertUtcToDateString(utcDate):
    return datetime.datetime.fromtimestamp(
            int(utcDate) ).strftime('%d-%m-%Y %H:%M:%S:%u')

def convertDateStringToUtc(stringDate):
    return datetime.datetime.strptime(stringDate, "%d-%m-%Y %H:%M:%S").timestamp()

#from datetime import timezone
 # alternative to '.utcnow()'
#dt_now = datetime.datetime.now(datetime.timezone.utc)
# alternative to '.utcfromtimestamp()'
#Unix timestamp 
s= '15-06-2022 09:13:36'
dt_now = datetime.datetime.strptime(s, "%d-%m-%Y %H:%M:%S").timestamp()


1629989121
1617295943.17321

1655295216.0
print(dt_now)
print(convertUtcToDateString('1655295216'))
#print(convertUtcToDateString('1655245105'))

print(convertUtcToDateString('1655295196'))
print(convertUtcToDateString('1655295136'))
print(convertUtcToDateString('1655295209'))
print(convertUtcToDateString('1655295149'))

1655295196
1655295136
1655295209
1655295149




# String em formato JSON
data_JSON =  """
[
	[
		{
			"hostid": "10481",
			"host": "SRV-TAMOIOS-33"
		}
	],
	[
		{
			"itemid": "48325",
			"clock": "1655245216",
			"value": "15",
			"ns": "740506090"
		},
		{
			"itemid": "48325",
			"clock": "1655245105",
			"value": "35",
			"ns": "245404386"
		}
	],
	[
		{
			"itemid": "48316",
			"clock": "1655245216",
			"value": "67.096152",
			"ns": "354689327"
		},
		{
			"itemid": "48316",
			"clock": "1655245105",
			"value": "51.523859",
			"ns": "666694162"
		}
	]
]
"""




# Converter a string em JSON em um dicionário
data_dict = json.loads(data_JSON)

infoHost =  data_dict[0]
infoHostCPU = data_dict[1]
infoHostMemory = data_dict[2]


# print(infoHost)
# print(infoHostMemory)
# print(infoHostCPU)


# for dado in data_dict:
#     # imprimindo nome e idade formatados
#     print(dado)

hostName = infoHost[0]['host']

xMemory = []
yMemory = []
xCpu = []
yCpu = []

for dataMem in infoHostMemory:
    # print(dataMem['clock'], dataMem['value'])
    xMemory.append(convertUtcToDateString(dataMem['clock']))
    yMemory.append(float(dataMem['value']))

for dataCPU in infoHostCPU:
    # print(dataCPU['clock'], dataCPU['value'])
    xCpu.append(convertUtcToDateString(dataCPU['clock']) )
    yCpu.append(float(dataCPU['value']))



# x= [1,2,3,4]
# y= [2,3,4,3]

plt.plot(xMemory, yMemory, label="Memória")
plt.plot(xCpu, yCpu, label="Processador")

plt.ylabel('%')
plt.xlabel('Memória X Processador')
plt.title(hostName)
# plt.xticks([0,1,2,3,4,5,6])
plt.yticks([0,10,20,30, 40, 50, 60, 70, 80, 90, 100])
# plt.axis(ymin=0, ymax=100)
# plt.axis('auto')
# plt.axis('square')
plt.legend()
# plt.plot(x,y)
plt.show()








