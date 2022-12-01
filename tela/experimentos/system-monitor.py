import psutil 
from tkinter import ttk
import tkinter as tk
from threading import Thread

# root window
root = tk.Tk()
root.geometry("478x280")
root.title('System Monitor')

def atuzalizaProgressbarCpu():
    porcentagemCpuUtilizada = psutil.cpu_percent(interval=1)    
    progressbarCPU['value'] = porcentagemCpuUtilizada
    labelCPU['text'] = f"CPU uso: {porcentagemCpuUtilizada} %"    

def atuzalizaProgressbarMemoria():
    porcentagemMemoriaUtilizada = psutil.virtual_memory().percent  
    progressbarMemoria['value'] = porcentagemMemoriaUtilizada
    labelMemoria['text'] = f"Memória uso: {porcentagemMemoriaUtilizada} %"  



# ------------------------ CPU
# label CPU
labelCPU = ttk.Label(root, text="CPU uso: 0.0%")
labelCPU.grid(column=0, row=0, columnspan=2, padx=2, pady=2)

# progressbar CPU
progressbarCPU = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=400
)
progressbarCPU.grid(column=0, row=1, columnspan=2, padx=20, pady=2)


# ------------------------ Memória
# label para memória
labelMemoria = ttk.Label(root, text="Memória uso: 0.0%")
labelMemoria.grid(column=0, row=3, columnspan=2)

# progressbar para memória
progressbarMemoria = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=400
)

progressbarMemoria.grid(column=0, row=4, columnspan=2, padx=20, pady=2)



def verificarStatusSistema():
    while True:
      atuzalizaProgressbarCpu()
      atuzalizaProgressbarMemoria()
      if stop_threads:
            break
      


# Cria  Thread
threadStatusSistema = Thread(target=verificarStatusSistema)
# Inicia a thread
threadStatusSistema.start()
stop_threads = False

try:
  root.mainloop()   
finally:
    print()
    stop_threads = True


