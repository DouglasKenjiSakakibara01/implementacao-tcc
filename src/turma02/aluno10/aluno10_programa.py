def tique_segundos(segundo):
        segundo=(segundo+1)%60
        return segundo == 0
    

def tique_minutos(minuto):
        minuto=(minuto+1)%60

        return minuto == 0
def tique(hora, minutos, segundos):
        mudou_segundos = tique_segundos(segundos)
        if mudou_segundos:
            mudou_minutos, minutos = tique_minutos(minutos)
            if mudou_minutos:
                hora=(hora+1)%24
            else:
                minutos+=1    
        else:
            segundos+=1
        return hora, minutos, segundos

    
   