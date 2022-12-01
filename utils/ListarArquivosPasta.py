import os

pasta = './imagens'

for diretorio, subpastas, arquivos in os.walk(pasta, topdown = False):
    # Lista os Arquivos
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))
    # Lista as Pastas
    for pasta in subpastas:
        print(os.path.join(diretorio, pasta))