# Import Module
from tkinter import *
from PIL import Image, ImageTk
 
# Create Tkinter Object
root = Tk()
root.title("Automação com Raspberry")
root.geometry("478x280")
# root.config(cursor="none")

# Variável que verifica o estado do led
isLigado = False
 
# Read the Image
imagemLigada = Image.open("lamp-ligada.png").resize((150,150))
imagemDesligada = Image.open("lamp-desligada.png").resize((150,150))

def alterarImagem(imagem):   
    imagem = ImageTk.PhotoImage(imagem)
    btnLigar.image = imagem           # save reference
    btnLigar.configure(image=imagem)  # configure the label
 

def verificarEstado():
    global isLigado
    isLigado = not isLigado
    
    if(isLigado):
        alterarImagem(imagemLigada)
    else:
        alterarImagem(imagemDesligada)
        

imagem = ImageTk.PhotoImage(imagemDesligada) 

btnLigar = Button(root, text = 'Click Me !',  image=imagem,
                    compound = CENTER, command=verificarEstado)
# btnLigar.pack(side = TOP) 

btnLigar.place(x=165, y=65)
 
# Execute Tkinter
root.mainloop()