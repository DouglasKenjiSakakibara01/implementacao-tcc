import datetime


def tique(horas, minutos, segundos):
        
        if ((0 <= horas <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59)):

                x = datetime.time(horas, minutos, segundos);
                x = (datetime.datetime.combine(datetime.date.today(), x) + datetime.timedelta(seconds = 1)).time(); 

                horario = str(x).split(':')
                horas= int(horario[0])
                minutos= int(horario[1])
                segundos= int(horario[2])
        else:
            horas=-1
            minutos-1
            segundos= -1
          
        return horas, minutos, segundos