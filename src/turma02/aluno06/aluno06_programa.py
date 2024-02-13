from datetime import datetime, timedelta



def tique(horas, minutos, segundos):
        tempo= datetime(horas, minutos, segundos)
        tempo += timedelta(seconds=1)
        horario_aux= str(tempo).split()
        horario= str(horario_aux[1]).split(':')
        horas = int(horario[0])
        minutos = int(horario[1])
        segundos = int(horario[2])
        return horas, minutos, segundos

    