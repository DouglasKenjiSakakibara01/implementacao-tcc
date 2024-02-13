# Funções 
'''
def organiza(hora_string):
    horas, minutos, segundos = map(int, hora_string.split(':'))
    return horas, minutos, segundos

def volta_para_string(horas,minutos,segundos):
    horario = str(horas).zfill(2) + ":" + str(minutos).zfill(2) + ":" + str(segundos).zfill(2)
    return horario
'''
def tique(horas, minutos, segundos):

    segundos += 1 

    if segundos == 60:
        minutos += 1
        segundos = 00

    if minutos == 60:
        horas += 1
        minutos = 00

    if horas == 24:
        horas = 00

    return horas, minutos, segundos

