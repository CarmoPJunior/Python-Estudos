# pip install python-docx
from docx import Document
from docx.shared import Inches
import os
from datetime import datetime

document = Document()

pasta = './imagens'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        file = os.path.join(diretorio, arquivo)
        print(file)
        document.add_picture(file, width=Inches(5.25))
        document.add_page_break()


hora_atual = datetime.now().strftime('%H-%M-%S')

arq = hora_atual  + '.docx'
print(arq)
document.save(arq)

pasta = './imagens' 

for diretorio, subpastas, arquivos in os.walk(pasta, topdown = False):
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))