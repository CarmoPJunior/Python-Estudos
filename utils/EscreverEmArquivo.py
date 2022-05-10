
# r:   - abre o arquivo para leitura. O stream é posicionado no início do arquivo.
# w:   - abre o arquivo para leitura e escrita. 
#         O stream é posicionado no início do arquivo e o arquivo será criado caso não exista.
#         E sobre escreve toda as informações do arquivo  
# a:   - Abre o arquivo para leitura e escrita. O arquivo será criado caso não exista e 
#         o stream é posicionado no final do arquivo.

#Abre e sobreescreve as informações do arquivo
with open('arquivo.txt', 'w') as arq:
    arq.write('teste3')
    arq.write('\n')

# Abre e escreve a informação na ultima linha do arquivo.
with open('arquivo.txt', 'a') as arq:
    arq.write('teste2')
    arq.write('\n')
# Abre o arquivo para leitura
with open('arquivo.txt', 'r') as arq:
    print(arq.read)