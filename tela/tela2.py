from tkinter import *

def createDisplay():
    global janela 
    
    janela = Tk()
    janela.title("Cotação Atual de Moedas")
    texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
    texto.grid(column=0, row=0, padx=10, pady=10)

    botao = Button(janela, text="Buscar cotações", command=terminate)
    botao.grid(column=0, row=1, padx=10, pady=10)

    

    texto_resposta = Label(janela, text="")
    texto_resposta.grid(column=0, row=2, padx=10, pady=10)
    janela.mainloop()

def terminate():
 #Acao do botao SAIR
 global janela
 janela.destroy()


def main():
    createDisplay()
          
try:
  if __name__ == '__main__': 
      main()
   
finally:
    print("oi")