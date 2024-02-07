"""Relógio digital"""

def tique(horas, minutos, segundos):
    '''
    if horario['horas'] > 23 or horario['minutos'] > 59 or horario['segundos'] > 59:
        return "Horário inválido"
    '''
    if segundos == 59:
        segundos = 0
        if minutos == 59:
            minutos = 0
            if horas == 23:
                horas = 0
            else:
                horas += 1
        else:
            minutos += 1
    else:
        segundos += 1

    return horas, minutos, segundos


"""Fim Relógio digital"""


