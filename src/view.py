#import do tkinter
import time
import CPU
import RAM
import Disco
from tkinter import *
from tkinter import ttk
from colorama import Fore
import psutil
import random

#nova janela
janela = Tk()
#definir tamanho
janela.geometry("500x400")
#definir titulo
janela.title("Trabalho Tópicos especias em informática")
#adicionar uma label
lblbv = ttk.Label(janela, text="Bem-vindo! - Monitoramento de CPU, RAM, Disco e GPU")
#adicionar a label na janela em uma posição
lblbv.pack()
#posicionar label
lblNuvem = ttk.Label(janela, text="Nuvem")
lblNuvem.pack()
lblNuvem.place(x=10, y=10)

#cpu
lblCPU = ttk.Label(janela, text="CPU: " + CPU.monitorar_cpu(0) + "%")
lblCPU.pack()
lblCPU.place(x=10, y=30)


#ram
lblRAM = ttk.Label(janela, text="*****************************************************\n" +
                                 "RAM Used: " + RAM.mem_used() +
                                "MB" + ".......... RAM Livre: " + RAM.mem_free() +
                                "MB" + "\nRAM Total: " + RAM.mem_total() + "MB" +
                                "\n*****************************************************")
lblRAM.pack()
lblRAM.place(x=10, y=60)
#text box

#disco
lblDisco = ttk.Label(janela, text="Disco: " + Disco.monit_disco(0) + " GB")
lblDisco.pack()
lblDisco.place(x=10, y=130)
#criar textbox texto_disco
########################################################################################
#criar VM

def VM( ):
    xx = random.randint(10, 500)
    #random cpu
    novaCPU = random.randint(0, 100)
    novaCPU = str(novaCPU)
    novaRAM = random.randint(0, 100)
    novaRAM = str(novaRAM)
    novo_disco = random.randint(100, 120)
    novo_disco = str(novo_disco)
    lblCPU.configure(text="CPU: " + novaCPU + "%")
    lblVM = ttk.Label(janela, text="VM: Nova VM" + "\n" + "CPU: "
                                   + novaCPU + "%" + "\n" + "RAM: " + novaRAM +
                                   "MB" + "\n" + "Disco: " + novo_disco + " GB")
    lblVM.pack()
    lblVM.place(x=xx, y=200)


btnVM = ttk.Button(janela, text="VM", command=VM)
btnVM.pack()
btnVM.place(x=10, y=170)


########################################################################################

#botao sair!!!
botao4 = ttk.Button(janela, text="Sair")
botao4.pack()
botao4.place(x=300, y=60)
#sair
def sair():
    exit()
botao4.configure(command=sair)
#mantem a janela aberta
janela.mainloop()
