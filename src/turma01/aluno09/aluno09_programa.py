# relogio_digital.py
from datetime import datetime, timedelta

def tique(horas, minutos, segundos):
        
        horario= f"{str(horas)}:{str(minutos)}:{str(segundos)}"
        horario = datetime.strptime(horario,"%H:%M:%S")
        novo_horario = horario + datetime.timedelta(seconds=1)
        novo_horario=str(novo_horario).split()
        novo_horario= novo_horario[1]
        novo_horario= novo_horario.split(":")

        return int(novo_horario[0]), int(novo_horario[1]), int(novo_horario[2])

    
