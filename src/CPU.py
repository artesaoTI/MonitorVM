
from colorama import Fore
import time
import psutil
#cpu
cpu = 0.0
#monitorar cpu
def monitorar_cpu(Adicional):
    cpu = psutil.cpu_percent(interval=1) - Adicional
    cpu = str(cpu)
    return cpu



