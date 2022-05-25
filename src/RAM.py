import os
import time
import psutil
from colorama import Fore

def mem_used():
    # enquanto for verdadeiro
    # monitorar memoria
    memoria = psutil.virtual_memory()
    memoria = str(memoria.used )
    # transformar em MB
    memoria = str(int(memoria) / 1000000)
    # eliminar casas decimais
    memoria = str(memoria.split('.')[0])

    return memoria
def mem_free():
    ram = psutil.virtual_memory()
    ram = str(ram.free)
    ram = str(int(ram) / 1000000)
    ram = str(ram.split('.')[0])
    return ram

def mem_total():
    ram = mem_free() + mem_used()
    ram = str(int(ram) / 1000000)
    ram = str(ram.split('.')[0])
    return ram