import time
import os
os.system('cls')

from datetime import timedelta

def somar_horas(lista_horas):
    total = timedelta()
    for hora in lista_horas:
        partes = list(map(int, hora.split(':')))
        if len(partes) == 2:  # Formato HH:MM
            horas, minutos = partes
            segundos = 0
        elif len(partes) == 3:  # Formato HH:MM:SS
            horas, minutos, segundos = partes
        else:
            raise ValueError(f"Formato de hora inválido: {hora}")
        
        total += timedelta(hours=horas, minutes=minutos, seconds=segundos)
    
    return str(total)

# Lista de horas no formato HH:MM ou HH:MM:SS
# horas = ['0:16','0:01','0:16','0:17','0:10','0:31','0:09','0:30','0:18','0:22','0:16','0:12','0:19','0:14','0:25',]
horas = ['0:33','0:27','0:17','0:16','0:21',]

resultado = somar_horas(horas)
print(f"Total de horas somadas: {resultado}\n")


