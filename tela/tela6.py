import tkinter as tk
from PIL import Image, ImageTk
 
window = tk.Tk()
window.title("Automação com Raspberry")
window.geometry("478x280")
window.columnconfigure(0, minsize=10)
window.rowconfigure([0, 1,2], minsize=10)

imagemDesligada = Image.open("lamp-ligada.png").resize((150,150))
 
imagem = ImageTk.PhotoImage(imagemDesligada) 

btnLigar = tk.Button(window, text = 'Click Me !',  image=imagem )
btnLigar.grid(row=1, column=0)
 
window.mainloop()