import os
import time
import psutil
from colorama import Fore

def monit_disco(Adicional):
    # monitorar disco
    disco = psutil.disk_usage('/')
    disco = str(disco.used + Adicional)
    #transformar em GB
    disco = str(int(disco) / 1000000000)
    #eliminar casas decimais
    disco = str(disco.split('.')[0])
    return disco

